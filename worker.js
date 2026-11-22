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

    return env.ASSETS.fetch(request);
  },

  async scheduled(event, env, ctx) {
    if (ctx && ctx.waitUntil) {
      ctx.waitUntil(fetch('https://sonora-bot.onrender.com/health').catch(() => {}));
    }
  },
};
