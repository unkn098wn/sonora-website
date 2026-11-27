export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // Keep-alive ping to Render cloud bot so it never sleeps
    if (ctx && ctx.waitUntil) {
      ctx.waitUntil(fetch('https://sonora-bot.onrender.com/health').catch(() => {}));
    }

    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        status: 204,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization',
        },
      });
    }

    // Cloud Library Sync Endpoints
    if (url.pathname === '/api/library/sync') {
      const headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      };

      if (!env.SONORA_KV) {
        return new Response(
          JSON.stringify({ success: false, error: 'KV storage binding unavailable' }),
          { status: 503, headers }
        );
      }

      if (request.method === 'GET') {
        const accountId = (url.searchParams.get('account_id') || '').trim();
        if (!accountId) {
          return new Response(
            JSON.stringify({ success: false, error: 'Missing account_id parameter' }),
            { status: 400, headers }
          );
        }

        try {
          const raw = await env.SONORA_KV.get(`library:${accountId.toLowerCase()}`);
          if (!raw) {
            return new Response(
              JSON.stringify({ success: true, account_id: accountId, library: null }),
              { status: 200, headers }
            );
          }
          const parsed = JSON.parse(raw);
          return new Response(
            JSON.stringify({
              success: true,
              account_id: accountId,
              library: parsed.library || parsed,
              updated_at: parsed.updated_at || null,
            }),
            { status: 200, headers }
          );
        } catch (err) {
          return new Response(
            JSON.stringify({ success: false, error: String(err) }),
            { status: 500, headers }
          );
        }
      }

      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const accountId = (body.account_id || '').trim();
          const library = body.library;

          if (!accountId || !library) {
            return new Response(
              JSON.stringify({ success: false, error: 'Missing account_id or library payload' }),
              { status: 400, headers }
            );
          }

          const record = {
            account_id: accountId,
            library: library,
            updated_at: new Date().toISOString(),
          };

          await env.SONORA_KV.put(
            `library:${accountId.toLowerCase()}`,
            JSON.stringify(record)
          );

          return new Response(
            JSON.stringify({
              success: true,
              account_id: accountId,
              saved_at: record.updated_at,
              playlist_count: Array.isArray(library.playlists) ? library.playlists.length : 0,
              favorite_count: Array.isArray(library.favorites) ? library.favorites.length : 0,
            }),
            { status: 200, headers }
          );
        } catch (err) {
          return new Response(
            JSON.stringify({ success: false, error: String(err) }),
            { status: 400, headers }
          );
        }
      }

      return new Response(
        JSON.stringify({ success: false, error: 'Method not allowed' }),
        { status: 405, headers }
      );
    }

    // Feedback & Bug Reports API
    if (url.pathname === '/api/feedback') {
      const headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      };

      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const category = (body.category || 'bug').trim().toLowerCase();
          const name = (body.name || 'Слушатель Sonora').trim();
          const contact = (body.contact || '').trim();
          const message = (body.message || '').trim();
          const version = (body.version || 'v2.7.0').trim();

          if (!message) {
            return new Response(
              JSON.stringify({ success: false, error: 'Текст обращения не может быть пустым' }),
              { status: 400, headers }
            );
          }

          const ticketId = `SON-${Math.floor(1000 + Math.random() * 9000)}`;
          const report = {
            ticket_id: ticketId,
            timestamp: new Date().toISOString(),
            category,
            name,
            contact,
            message,
            version,
            source: 'website',
            status: 'new',
          };

          if (env.SONORA_KV) {
            await env.SONORA_KV.put(
              `feedback:${Date.now()}:${ticketId}`,
              JSON.stringify(report)
            );
          }

          // Forward to Render cloud bot so Admin (@wezreg, ID: 960674720) receives instant Telegram alert
          if (ctx && ctx.waitUntil) {
            ctx.waitUntil(
              fetch('https://sonora-bot.onrender.com/api/feedback', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(report),
              }).catch(() => {})
            );
          }

          return new Response(
            JSON.stringify({
              success: true,
              ticket_id: ticketId,
              message: 'Обращение успешно принято и передано разработчикам',
            }),
            { status: 200, headers }
          );
        } catch (err) {
          return new Response(
            JSON.stringify({ success: false, error: String(err) }),
            { status: 400, headers }
          );
        }
      }

      return new Response(
        JSON.stringify({ success: false, error: 'Method not allowed' }),
        { status: 405, headers }
      );
    }

    // Public Interactive Roadmap API
    if (url.pathname === '/api/roadmap') {
      const headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      };

      const defaultRoadmap = [
        { id: 'carplay_auto', title: 'Поддержка Android Auto и Apple CarPlay', category: 'Платформы', votes: 148 },
        { id: 'airplay_cast', title: 'Беспроводной стриминг (AirPlay, Chromecast, DLNA)', category: 'Связь', votes: 122 },
        { id: 'smart_lyrics', title: 'Синхронный перевод иностранных песен на русский язык', category: 'Караоке', votes: 99 },
        { id: 'listen_together', title: 'Комнаты совместного прослушивания (Listen Along с друзьями)', category: 'Сообщество', votes: 89 },
        { id: 'smart_ai_wave', title: 'Умная Моя Волна: фильтрация по BPM, настроению и эпохам', category: 'Рекомендации', votes: 139 },
      ];

      if (request.method === 'GET') {
        let items = defaultRoadmap;
        if (env.SONORA_KV) {
          try {
            const stored = await env.SONORA_KV.get('roadmap_votes');
            if (stored) {
              const voteMap = JSON.parse(stored);
              items = defaultRoadmap.map(item => ({
                ...item,
                votes: (item.votes || 0) + (voteMap[item.id] || 0),
              }));
            }
          } catch (e) {}
        }
        return new Response(JSON.stringify({ success: true, items }), { status: 200, headers });
      }

      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const featureId = body.feature_id;
          if (!featureId) {
            return new Response(
              JSON.stringify({ success: false, error: 'feature_id required' }),
              { status: 400, headers }
            );
          }
          if (env.SONORA_KV) {
            let voteMap = {};
            try {
              const stored = await env.SONORA_KV.get('roadmap_votes');
              if (stored) voteMap = JSON.parse(stored);
            } catch (e) {}
            voteMap[featureId] = (voteMap[featureId] || 0) + 1;
            await env.SONORA_KV.put('roadmap_votes', JSON.stringify(voteMap));
          }
          return new Response(JSON.stringify({ success: true }), { status: 200, headers });
        } catch (e) {
          return new Response(JSON.stringify({ success: false, error: String(e) }), { status: 400, headers });
        }
      }
    }

    // Downloads redirect to official GitHub Releases (2 official installers)
    if (url.pathname.startsWith('/downloads/')) {
      const fileName = url.pathname.replace('/downloads/', '');
      let targetFile = fileName;
      if (fileName.toLowerCase().includes('android') || fileName.toLowerCase().endsWith('.apk')) {
        targetFile = 'Sonora-v2.7.0-Android.apk';
      } else if (fileName.toLowerCase().includes('setup') || fileName.toLowerCase().includes('windows') || fileName.toLowerCase().endsWith('.exe')) {
        targetFile = 'Sonora-v2.7.0-Setup.exe';
      }
      return Response.redirect(
        `https://github.com/unkn098wn/sonora-website/releases/download/v2.7.0/${targetFile}`,
        302
      );
    }

    // Telegram and Bot shortcuts
    if (url.pathname === '/telegram' || url.pathname === '/bot') {
      return Response.redirect('https://t.me/sonoramus1c_bot', 302);
    }

    // Dynamic Edge Page Serving via SONORA_KV
    if (env.SONORA_KV) {
      if (url.pathname === '/' || url.pathname === '/index.html') {
        const page = await env.SONORA_KV.get('page:index');
        if (page) {
          return new Response(page, {
            headers: {
              'Content-Type': 'text/html; charset=utf-8',
              'Access-Control-Allow-Origin': '*',
              'Cache-Control': 'public, max-age=0, must-revalidate',
            },
          });
        }
      }
      if (url.pathname === '/privacy' || url.pathname === '/privacy.html') {
        const page = await env.SONORA_KV.get('page:privacy');
        if (page) {
          return new Response(page, {
            headers: {
              'Content-Type': 'text/html; charset=utf-8',
              'Access-Control-Allow-Origin': '*',
              'Cache-Control': 'public, max-age=0, must-revalidate',
            },
          });
        }
      }
      if (url.pathname === '/terms' || url.pathname === '/terms.html') {
        const page = await env.SONORA_KV.get('page:terms');
        if (page) {
          return new Response(page, {
            headers: {
              'Content-Type': 'text/html; charset=utf-8',
              'Access-Control-Allow-Origin': '*',
              'Cache-Control': 'public, max-age=0, must-revalidate',
            },
          });
        }
      }
      if (url.pathname === '/version.json') {
        const page = await env.SONORA_KV.get('page:version');
        if (page) {
          return new Response(page, {
            headers: {
              'Content-Type': 'application/json; charset=utf-8',
              'Access-Control-Allow-Origin': '*',
            },
          });
        }
      }
    }

    return env.ASSETS.fetch(request);
  },

  async scheduled(event, env, ctx) {
    if (ctx && ctx.waitUntil) {
      ctx.waitUntil(fetch('https://sonora-bot.onrender.com/health').catch(() => {}));
    }
  },
};
