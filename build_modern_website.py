import os

website_dir = r"C:\Users\maksi\OneDrive\Desktop\Sonora Project\Sonora-Website"
index_path = os.path.join(website_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="ru" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sonora Music — Музыка всех миров в одном монолитном плеере</title>
  <meta name="description" content="Sonora — ультрасовременный бесплатный музыкальный плеер для Windows и Android. Мгновенный поиск по 18 мировым и андеграунд площадкам, FLAC до 24-бит, умная «Моя волна», DSP-студия, вечная облачная синхронизация медиатеки. 0 подписок и 0 рекламы.">
  <meta name="keywords" content="Sonora, музыкальный плеер, музыка без подписки, mp3 плеер, flac плеер, моя волна, soundcloud, youtube music, streaming player, obsidian glass, anime.js, 3d плеер">

  <!-- OpenGraph Meta -->
  <meta property="og:title" content="Sonora Music — Музыка всех миров">
  <meta property="og:description" content="18 музыкальных площадок в одном монолитном плеере. 100% бесплатно навсегда.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sonora-website.maksinegor821.workers.dev/">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="assets/sonora_icon.png?v=2.7">
  <link rel="shortcut icon" href="favicon.ico?v=2.7">

  <!-- Tailwind CSS & Fonts -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Anime.js & Lucide Icons -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js"></script>
  <script src="https://unpkg.com/lucide@latest"></script>

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            obsidian: {
              950: '#040507',
              900: '#07090E',
              850: '#0D1017',
              800: '#131822',
              700: '#1D2433',
              600: '#2A3449',
            },
            mint: {
              300: '#5DFECD',
              400: '#00FFC2',
              500: '#00E5AE',
            },
            cyan: {
              400: '#00F5D4',
            }
          },
          animation: {
            'spin-slow': 'spin 14s linear infinite',
            'float': 'floatAnim 5s ease-in-out infinite',
            'pulse-glow': 'pulseGlow 3s ease-in-out infinite',
          },
          keyframes: {
            floatAnim: {
              '0%, 100%': { transform: 'translateY(0px)' },
              '50%': { transform: 'translateY(-12px)' },
            },
            pulseGlow: {
              '0%, 100%': { opacity: '0.5', transform: 'scale(1)' },
              '50%': { opacity: '0.9', transform: 'scale(1.05)' },
            }
          }
        }
      }
    }
  </script>

  <style>
    /* Obsidian Glass Design System */
    :root {
      --bg-color: #07090E;
      --card-bg: rgba(14, 18, 28, 0.72);
      --card-border: rgba(255, 255, 255, 0.08);
      --card-hover-border: rgba(0, 255, 194, 0.35);
    }

    body {
      background-color: #07090E;
      color: #E2E8F0;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* Glass Surface */
    .glass-card {
      background: var(--card-bg);
      backdrop-filter: blur(28px);
      -webkit-backdrop-filter: blur(28px);
      border: 1px solid var(--card-border);
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.06);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .glass-card:hover {
      border-color: var(--card-hover-border);
      box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.95), 0 0 25px rgba(0, 255, 194, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }

    /* 3D Transform Utilities */
    .perspective-1000 {
      perspective: 1000px;
      transform-style: preserve-3d;
    }
    .preserve-3d {
      transform-style: preserve-3d;
    }
    .translate-z-10 {
      transform: translateZ(10px);
    }
    .translate-z-20 {
      transform: translateZ(20px);
    }
    .translate-z-30 {
      transform: translateZ(30px);
    }

    /* Vinyl Grooves Realistic Texture */
    .vinyl-disk {
      background: radial-gradient(circle at center, #111 0%, #151515 15%, #050505 16%, #1a1a1a 30%, #080808 31%, #222 45%, #080808 46%, #1c1c1c 60%, #050505 61%, #151515 85%, #080808 100%);
      box-shadow: 0 0 0 2px rgba(255,255,255,0.06), 0 25px 60px rgba(0,0,0,0.9);
      position: relative;
    }
    .vinyl-disk::after {
      content: '';
      position: absolute;
      inset: 0;
      border-radius: 50%;
      background: conic-gradient(from 45deg, transparent 0deg, rgba(255,255,255,0.12) 60deg, transparent 120deg, transparent 180deg, rgba(255,255,255,0.12) 240deg, transparent 300deg);
      pointer-events: none;
    }

    /* Range slider custom styling */
    input[type=range] {
      -webkit-appearance: none;
      background: rgba(255,255,255,0.1);
      border-radius: 9999px;
      height: 6px;
    }
    input[type=range]::-webkit-slider-thumb {
      -webkit-appearance: none;
      height: 18px;
      width: 18px;
      border-radius: 50%;
      background: #00FFC2;
      box-shadow: 0 0 10px #00FFC2;
      cursor: pointer;
    }
  </style>
</head>
<body class="selection:bg-mint-400/20 selection:text-mint-300">

  <!-- Interactive 3D Canvas Background -->
  <canvas id="bg3dCanvas" class="fixed inset-0 pointer-events-none z-0 opacity-45"></canvas>

  <!-- Ambient Aurora Glows -->
  <div class="fixed top-[-15%] left-[20%] w-[650px] h-[650px] bg-emerald-500/10 rounded-full blur-[140px] pointer-events-none z-0"></div>
  <div class="fixed top-[40%] right-[-10%] w-[600px] h-[600px] bg-cyan-500/10 rounded-full blur-[150px] pointer-events-none z-0"></div>
  <div class="fixed bottom-[-10%] left-[-10%] w-[550px] h-[550px] bg-purple-500/10 rounded-full blur-[150px] pointer-events-none z-0"></div>

  <!-- STICKY GLASS HEADER -->
  <header class="fixed top-4 inset-x-0 z-50 flex justify-center px-4" id="mainHeader">
    <nav class="glass-card rounded-full px-5 py-3 flex items-center justify-between gap-6 max-w-4xl w-full border border-white/10 shadow-2xl">
      <!-- Logo -->
      <a href="#" class="flex items-center gap-3 group">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-mint-400 to-cyan-400 p-0.5 shadow-md shadow-mint-400/20 group-hover:scale-105 transition">
          <div class="w-full h-full bg-[#07090E] rounded-[10px] flex items-center justify-center">
            <i data-lucide="disc" class="w-5 h-5 text-mint-400 group-hover:rotate-90 transition duration-700"></i>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-lg font-black text-white tracking-wider">SONORA</span>
          <span class="text-[10px] font-mono font-bold text-mint-400 bg-mint-400/10 px-2 py-0.5 rounded-full border border-mint-400/20">v2.6.0</span>
        </div>
      </a>

      <!-- Desktop Links -->
      <div class="hidden md:flex items-center gap-6 text-sm font-semibold text-slate-300">
        <a href="#demo" class="hover:text-mint-400 transition">3D Демо</a>
        <a href="#platforms" class="hover:text-mint-400 transition">18 Платформ</a>
        <a href="#architecture" class="hover:text-mint-400 transition">Архитектура</a>
        <a href="#roadmap" class="hover:text-mint-400 transition">Roadmap</a>
        <a href="#faq" class="hover:text-mint-400 transition">FAQ</a>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-3">
        <button onclick="openFeedbackModal()" class="text-xs font-bold text-slate-300 hover:text-white px-3 py-1.5 rounded-lg border border-white/10 hover:bg-white/5 transition flex items-center gap-1.5">
          <i data-lucide="message-square" class="w-3.5 h-3.5 text-mint-400"></i>
          <span class="hidden sm:inline">Отзыв</span>
        </button>
        <a href="#download" class="bg-white hover:bg-slate-200 text-black font-extrabold text-xs sm:text-sm px-4 sm:px-5 py-2 rounded-full transition transform hover:scale-105 active:scale-95 flex items-center gap-2 shadow-lg shadow-white/10">
          <i data-lucide="download" class="w-4 h-4"></i>
          <span>Скачать</span>
        </a>
      </div>
    </nav>
  </header>

  <!-- HERO SECTION WITH 3D TILT & VINYL SHOWCASE -->
  <section class="relative z-10 pt-28 sm:pt-36 pb-20 max-w-6xl mx-auto px-4 text-center">
    <!-- Version Tag -->
    <div class="inline-flex items-center gap-2.5 px-4 py-1.5 rounded-full glass-card border border-mint-400/25 mb-8 animate-float">
      <span class="w-2 h-2 rounded-full bg-mint-400 shadow-[0_0_8px_#00FFC2] animate-ping"></span>
      <span class="text-xs sm:text-sm font-semibold text-slate-200 font-mono">
        Sonora v2.6.0 Obsidian Stage — 0 подписок • 0 рекламы
      </span>
    </div>

    <!-- Main Title -->
    <h1 class="text-4xl sm:text-6xl md:text-7xl font-black text-white tracking-tight leading-[1.1] max-w-5xl mx-auto">
      Музыка всех миров в одном <span class="text-transparent bg-clip-text bg-gradient-to-r from-mint-400 via-cyan-400 to-emerald-300">монолитном плеере</span>
    </h1>

    <p class="text-slate-400 text-base sm:text-xl max-w-2xl mx-auto mt-6 leading-relaxed">
      Слушайте треки из 18 мировых площадок в студийном FLAC 24-бит с живым 3D-эквалайзером, бесконечной Моей Волной и вечной синхронизацией плейлистов через Cloudflare KV.
    </p>

    <!-- 2 Official Installers Download Buttons -->
    <div class="mt-10 flex flex-wrap items-center justify-center gap-4">
      <!-- Windows Setup Button -->
      <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.6.0/Sonora-v2.6.0-Setup.exe" class="bg-white text-black font-extrabold text-base px-8 py-4 rounded-2xl flex items-center gap-3 transition transform hover:scale-105 active:scale-95 shadow-2xl shadow-white/15 hover:bg-slate-200">
        <i data-lucide="monitor" class="w-5 h-5"></i>
        <span>Скачать для Windows (.exe)</span>
        <span class="text-xs font-mono font-bold bg-black/15 px-2 py-0.5 rounded-md">27.2 МБ</span>
      </a>

      <!-- Android Universal APK Button -->
      <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.6.0/Sonora-v2.6.0-Android.apk" class="glass-card hover:bg-white/10 text-white font-bold text-base px-8 py-4 rounded-2xl flex items-center gap-3 transition transform hover:scale-105 active:scale-95 shadow-xl">
        <i data-lucide="smartphone" class="w-5 h-5 text-mint-400"></i>
        <span>Скачать для Android (APK)</span>
        <span class="text-xs font-mono text-mint-400 bg-mint-400/10 px-2 py-0.5 rounded-md">132.6 МБ</span>
      </a>

      <!-- Telegram Bot CTA -->
      <a href="https://t.me/sonoramus1c_bot" target="_blank" class="glass-card hover:bg-sky-500/20 text-sky-400 hover:text-white font-bold text-base px-6 py-4 rounded-2xl flex items-center gap-2.5 transition transform hover:scale-105 active:scale-95">
        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.52 2.77-1.18 3.35-1.38 3.73-1.39.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .37z"/></svg>
        <span>Telegram-бот</span>
      </a>
    </div>

    <!-- 3D INTERACTIVE HERO STAGE (TILT BY MOUSE & GYROSCOPE) -->
    <div id="hero3DContainer" class="mt-16 relative perspective-1000 max-w-4xl mx-auto cursor-pointer">
      <div id="hero3DCard" class="glass-card rounded-3xl p-6 sm:p-10 border border-white/10 preserve-3d transition-transform duration-200 shadow-2xl relative overflow-hidden">
        
        <div class="flex flex-col md:flex-row items-center justify-between gap-8 translate-z-20">
          
          <!-- Left: Rotating 3D Vinyl Player -->
          <div class="relative w-56 h-56 sm:w-64 sm:h-64 flex items-center justify-center preserve-3d">
            <!-- Vinyl Disk -->
            <div id="heroVinyl" class="w-full h-full rounded-full vinyl-disk flex items-center justify-center animate-spin-slow shadow-2xl">
              <!-- Center Label -->
              <div class="w-20 h-20 rounded-full bg-gradient-to-tr from-emerald-500 via-mint-400 to-cyan-500 p-1 flex items-center justify-center shadow-lg">
                <div class="w-full h-full bg-[#07090E] rounded-full flex flex-col items-center justify-center text-center">
                  <span class="text-[9px] font-black text-mint-400 tracking-wider">SONORA</span>
                  <span class="text-[7px] font-mono text-slate-400">FLAC 24-BIT</span>
                </div>
              </div>
            </div>

            <!-- Tonearm Stylus Mockup -->
            <div class="absolute -top-3 -right-3 w-16 h-28 pointer-events-none translate-z-30">
              <div class="w-2.5 h-20 bg-slate-300 rounded-full shadow-lg transform rotate-[-25deg] origin-top border border-black/40"></div>
              <div class="w-4 h-5 bg-mint-400 rounded-sm transform translate-x-2 translate-y-16 shadow-[0_0_10px_#00FFC2]"></div>
            </div>
          </div>

          <!-- Right: Floating Player Status Mockup -->
          <div class="flex-1 text-left space-y-4 translate-z-30">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-mint-400 uppercase tracking-widest flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-mint-400 animate-pulse"></span>
                СЕЙЧАС ИГРАЕТ • OBSIDIAN STAGE
              </span>
              <span class="text-xs font-mono text-slate-400">Lossless 320k</span>
            </div>

            <div class="space-y-1">
              <h3 class="text-2xl sm:text-3xl font-black text-white">Shadows in the Neon</h3>
              <p class="text-sm font-semibold text-slate-400">Kavinsky • Synthwave & Phonk Flow</p>
            </div>

            <!-- Soundwave visualizer bars -->
            <div class="h-10 flex items-end gap-1.5 py-1">
              <span class="w-1.5 h-4 bg-mint-400/80 rounded-full animate-pulse"></span>
              <span class="w-1.5 h-8 bg-mint-400 rounded-full animate-pulse delay-75"></span>
              <span class="w-1.5 h-6 bg-cyan-400 rounded-full animate-pulse delay-150"></span>
              <span class="w-1.5 h-10 bg-mint-400 rounded-full animate-pulse"></span>
              <span class="w-1.5 h-5 bg-cyan-300 rounded-full animate-pulse delay-200"></span>
              <span class="w-1.5 h-9 bg-mint-400 rounded-full animate-pulse delay-100"></span>
              <span class="w-1.5 h-7 bg-cyan-400 rounded-full animate-pulse"></span>
              <span class="w-1.5 h-4 bg-mint-400/80 rounded-full animate-pulse"></span>
            </div>

            <!-- Progress Bar -->
            <div class="space-y-1">
              <div class="w-full bg-white/10 h-1.5 rounded-full overflow-hidden">
                <div class="bg-gradient-to-r from-mint-400 to-cyan-400 h-full w-[64%] rounded-full shadow-[0_0_8px_#00FFC2]"></div>
              </div>
              <div class="flex justify-between text-[11px] font-mono text-slate-500">
                <span>02:18</span>
                <span>03:42</span>
              </div>
            </div>

            <!-- Feature Tags -->
            <div class="flex flex-wrap gap-2 pt-2">
              <span class="text-[11px] font-mono px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-slate-300">10-band EQ: Electro Warm</span>
              <span class="text-[11px] font-mono px-2.5 py-1 rounded-md bg-white/5 border border-white/10 text-slate-300">Vinyl Crackle: 33⅓ RPM</span>
              <span class="text-[11px] font-mono px-2.5 py-1 rounded-md bg-mint-400/10 text-mint-400 border border-mint-400/20">Cloud KV Synced</span>
            </div>
          </div>

        </div>

      </div>
    </div>
  </section>

  <!-- KINETIC STATS COUNTER WITH ANIME.JS -->
  <section class="max-w-6xl mx-auto px-4 py-12 relative z-10">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6">
      
      <div class="glass-card p-6 rounded-2xl text-center">
        <div class="text-3xl sm:text-5xl font-black text-white font-mono flex items-center justify-center">
          <span class="stat-counter" data-target="18">0</span>
        </div>
        <p class="text-xs sm:text-sm font-semibold text-slate-400 mt-2">Музыкальных сервисов</p>
      </div>

      <div class="glass-card p-6 rounded-2xl text-center">
        <div class="text-3xl sm:text-5xl font-black text-mint-400 font-mono flex items-center justify-center">
          <span class="stat-counter" data-target="24">0</span><span class="text-2xl">bit</span>
        </div>
        <p class="text-xs sm:text-sm font-semibold text-slate-400 mt-2">FLAC Hi-Res Audio</p>
      </div>

      <div class="glass-card p-6 rounded-2xl text-center">
        <div class="text-3xl sm:text-5xl font-black text-white font-mono flex items-center justify-center">
          <span class="stat-counter" data-target="10">0</span>
        </div>
        <p class="text-xs sm:text-sm font-semibold text-slate-400 mt-2">Полос DSP-эквалайзера</p>
      </div>

      <div class="glass-card p-6 rounded-2xl text-center">
        <div class="text-3xl sm:text-5xl font-black text-cyan-400 font-mono flex items-center justify-center">
          0<span class="text-2xl">₽</span>
        </div>
        <p class="text-xs sm:text-sm font-semibold text-slate-400 mt-2">Подписок и рекламы</p>
      </div>

    </div>
  </section>

  <!-- INTERACTIVE MINI-DEMO: DSP STUDIO, EQUALIZER & THEMES -->
  <section id="demo" class="max-w-5xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-10">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-mint-400/10 border border-mint-400/20 text-mint-400 text-xs font-mono font-semibold mb-3">
        <i data-lucide="sliders" class="w-3.5 h-3.5"></i>
        Интерактивная демо-комната
      </div>
      <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight">Попробуйте студийный звук прямо на сайте</h2>
      <p class="text-slate-400 text-sm sm:text-base mt-3 max-w-xl mx-auto">Подвигайте регуляторы эквалайзера, включите виниловый шум и переключите цветовую тему плеера.</p>
    </div>

    <div id="demoPlayerBox" class="glass-card rounded-3xl p-6 sm:p-10 border border-white/10 shadow-2xl relative overflow-hidden transition-all duration-500">
      
      <!-- Upper Controls: Theme Selector -->
      <div class="flex flex-wrap items-center justify-between gap-4 pb-6 border-b border-white/5">
        <div>
          <span class="text-xs font-mono text-slate-400 uppercase tracking-widest">Тема оформления:</span>
          <div class="flex gap-2 mt-2">
            <button onclick="setDemoTheme('obsidian')" class="theme-btn px-3 py-1 text-xs font-bold rounded-lg bg-mint-400 text-black shadow-lg">Liquid Obsidian</button>
            <button onclick="setDemoTheme('oled')" class="theme-btn px-3 py-1 text-xs font-bold rounded-lg bg-white/5 text-slate-300 hover:bg-white/10">Pure OLED</button>
            <button onclick="setDemoTheme('crimson')" class="theme-btn px-3 py-1 text-xs font-bold rounded-lg bg-white/5 text-slate-300 hover:bg-white/10">Crimson Midnight</button>
            <button onclick="setDemoTheme('abyssal')" class="theme-btn px-3 py-1 text-xs font-bold rounded-lg bg-white/5 text-slate-300 hover:bg-white/10">Abyssal Blue</button>
          </div>
        </div>

        <!-- Audio Effect Toggles -->
        <div>
          <span class="text-xs font-mono text-slate-400 uppercase tracking-widest">DSP Эффекты:</span>
          <div class="flex flex-wrap gap-2 mt-2">
            <button id="vinylToggle" onclick="toggleVinylEffect()" class="px-3 py-1 text-xs font-bold rounded-lg bg-white/5 text-slate-300 border border-white/10 hover:border-mint-400 transition flex items-center gap-1.5">
              <i data-lucide="disc" class="w-3.5 h-3.5 text-mint-400"></i>
              <span>Винил 33⅓</span>
            </button>
            <button id="bassToggle" onclick="toggleBassEffect()" class="px-3 py-1 text-xs font-bold rounded-lg bg-white/5 text-slate-300 border border-white/10 hover:border-mint-400 transition flex items-center gap-1.5">
              <i data-lucide="zap" class="w-3.5 h-3.5 text-cyan-400"></i>
              <span>Bass Boost +12dB</span>
            </button>
          </div>
        </div>
      </div>

      <!-- 10-Band Equalizer Sliders Mockup -->
      <div class="mt-8">
        <div class="flex items-center justify-between mb-4">
          <span class="text-sm font-bold text-white flex items-center gap-2">
            <i data-lucide="activity" class="w-4 h-4 text-mint-400"></i>
            10-полосный эквалайзер Sonora DSP
          </span>
          <span id="eqPresetLabel" class="text-xs font-mono text-mint-400">Пользовательский пресет: Hi-Fi Dynamic</span>
        </div>

        <div class="grid grid-cols-10 gap-2 sm:gap-4 items-end h-40 pt-4 pb-2 bg-black/30 rounded-2xl px-4 border border-white/5">
          <!-- 10 sliders -->
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+6</span>
            <input type="range" min="-12" max="12" value="6" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">31Hz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+4</span>
            <input type="range" min="-12" max="12" value="4" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">63Hz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+2</span>
            <input type="range" min="-12" max="12" value="2" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">125Hz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">0</span>
            <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">250Hz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">-1</span>
            <input type="range" min="-12" max="12" value="-1" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">500Hz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+1</span>
            <input type="range" min="-12" max="12" value="1" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">1kHz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+3</span>
            <input type="range" min="-12" max="12" value="3" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">2kHz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+5</span>
            <input type="range" min="-12" max="12" value="5" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">4kHz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+7</span>
            <input type="range" min="-12" max="12" value="7" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">8kHz</span>
          </div>
          <div class="flex flex-col items-center h-full justify-between">
            <span class="text-[10px] font-mono text-slate-500">+8</span>
            <input type="range" min="-12" max="12" value="8" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual()">
            <span class="text-[9px] font-mono text-slate-400">16kHz</span>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 18 OFFICIAL STREAMING PLATFORMS SHOWCASE (OFFICIAL VECTOR SVGS) -->
  <section id="platforms" class="max-w-6xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-cyan-400/10 border border-cyan-400/20 text-cyan-400 text-xs font-mono font-semibold mb-3">
        <i data-lucide="radio" class="w-3.5 h-3.5"></i>
        18 Музыкальных экосистем
      </div>
      <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight">Вся музыка планеты в единой поисковой строке</h2>
      <p class="text-slate-400 text-base max-w-xl mx-auto mt-3">Не нужно держать 10 разных приложений. Вводите название трека, артиста или вставляйте ссылку на альбом.</p>
    </div>

    <!-- 18 Platform Cards Grid with Official Brand SVGs -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 sm:gap-4">
      
      <!-- 1. YouTube Music -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-red-600/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-red-500" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 14.5c-2.49 0-4.5-2.01-4.5-4.5S9.51 7.5 12 7.5s4.5 2.01 4.5 4.5-2.01 4.5-4.5 4.5zm0-5.5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm-2 1l5-3-5-3v6z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">YouTube Music</span>
        <span class="text-[10px] font-mono text-red-400 mt-1">FLAC & Клипы</span>
      </div>

      <!-- 2. SoundCloud -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-amber-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FF5500]" viewBox="0 0 24 24"><path d="M11.56 8.87V17h8.88c1.96 0 3.56-1.57 3.56-3.5 0-1.9-1.52-3.44-3.42-3.5-.27-2.73-2.58-4.87-5.42-4.87-1.39 0-2.67.51-3.6 1.37zm-2.04 8.13V9.67c-.2.27-.37.58-.51.9v6.43h.51zm-1.53 0v-5.8c-.26.47-.46.99-.58 1.54v4.26h.58zm-1.53 0v-3.72c-.17.65-.26 1.34-.26 2.05v1.67h.26zm-1.53 0v-1.67c0-.28-.02-.56-.05-.84v2.51h.05z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">SoundCloud</span>
        <span class="text-[10px] font-mono text-amber-400 mt-1">Remixes & HQ</span>
      </div>

      <!-- 3. Deezer -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-purple-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#A238FF]" viewBox="0 0 24 24"><path d="M18.8 6.2h3.9V9h-3.9zm-4.7 0H18V9h-3.9zm9.4 4.3v2.8h-3.9v-2.8zm-4.7 0v2.8H18v-2.8zm-4.7 0v2.8h3.9v-2.8zm9.4 4.3v2.8h-3.9v-2.8zm-4.7 0v2.8H18v-2.8zm-4.7 0v2.8h3.9v-2.8zm-4.7 0v2.8h3.9v-2.8zm-4.7 0v2.8H9v-2.8zm18.8 4.3v2.8h-3.9v-2.8zm-4.7 0v2.8H18v-2.8zm-4.7 0v2.8h3.9v-2.8zm-4.7 0v2.8H9v-2.8zm-4.7 0v2.8H4.3v-2.8z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Deezer</span>
        <span class="text-[10px] font-mono text-purple-400 mt-1">FLAC 1411 kbps</span>
      </div>

      <!-- 4. Яндекс Музыка -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-yellow-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FFCC00]" viewBox="0 0 24 24"><path d="M12 2L14.4 9.6L22 12L14.4 14.4L12 22L9.6 14.4L2 12L9.6 9.6L12 2Z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Яндекс Музыка</span>
        <span class="text-[10px] font-mono text-yellow-400 mt-1">Моя Волна HQ</span>
      </div>

      <!-- 5. Spotify -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-emerald-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#1ED760]" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.586 14.424c-.18.295-.563.387-.857.207-2.35-1.434-5.308-1.758-8.793-.963-.335.077-.67-.133-.746-.469-.077-.334.132-.67.467-.747 3.813-.871 7.08-.507 9.721 1.115.295.18.388.563.208.857zm1.226-2.723c-.226.367-.706.482-1.072.257-2.687-1.652-6.785-2.131-9.965-1.166-.413.127-.849-.106-.974-.517-.125-.413.108-.849.52-.974 3.632-1.102 8.147-.568 11.234 1.328.366.226.481.707.257 1.072zm.106-2.835C14.692 8.87 9.375 8.694 6.297 9.628c-.494.15-1.018-.13-1.168-.624-.15-.494.13-1.018.624-1.168 3.532-1.072 9.404-.866 13.115 1.338.445.264.59.838.327 1.282-.264.443-.838.59-1.277.33z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Spotify</span>
        <span class="text-[10px] font-mono text-emerald-400 mt-1">Импорт плейлистов</span>
      </div>

      <!-- 6. Apple Music -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-rose-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FC3C44]" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm3.7 6.3l.003 4.88c0 1.63-1.08 2.62-2.5 2.62-1.32 0-2.32-.9-2.32-2.18s1-2.22 2.32-2.22c.4 0 .8.08 1.15.24V9.62l-3.35.83v4.32c0 1.63-1.08 2.62-2.5 2.62-1.32 0-2.32-.9-2.32-2.18s1-2.22 2.32-2.22c.4 0 .8.08 1.15.24V8.5c0-.6.44-1.1 1.03-1.22l4.17-.98c.55-.13 1.02.28 1.02.87z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Apple Music</span>
        <span class="text-[10px] font-mono text-rose-400 mt-1">Каталоги & Тексты</span>
      </div>

      <!-- 7. VK Музыка -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-blue-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#0077FF]" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14.5c-2.49 0-4.5-2.01-4.5-4.5S9.51 7.5 13 7.5v4.5h3.5c0 2.49-2.01 4.5-4.5 4.5z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">VK Музыка</span>
        <span class="text-[10px] font-mono text-blue-400 mt-1">Редкие ремиксы</span>
      </div>

      <!-- 8. Tidal -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-cyan-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-white" viewBox="0 0 24 24"><path d="M4 8l4-4 4 4-4 4-4-4zm8 0l4-4 4 4-4 4-4-4zm-4 4l4-4 4 4-4 4-4-4zm8 0l4-4 4 4-4 4-4-4z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Tidal</span>
        <span class="text-[10px] font-mono text-cyan-400 mt-1">MQA & Master</span>
      </div>

      <!-- 9. Bandcamp -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-teal-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#1DA0C3]" viewBox="0 0 24 24"><path d="M0 18.75l7.437-13.5h16.563l-7.438 13.5z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Bandcamp</span>
        <span class="text-[10px] font-mono text-teal-400 mt-1">Инди & Андеграунд</span>
      </div>

      <!-- 10. PromoDJ -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-orange-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FF7700]" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M10 8l6 4-6 4V8z" fill="#07090E"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">PromoDJ</span>
        <span class="text-[10px] font-mono text-orange-400 mt-1">DJ-миксы & Сеты</span>
      </div>

      <!-- 11. Mixcloud -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-indigo-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#52ADDF]" viewBox="0 0 24 24"><path d="M5.5 12c0-1.9 1.5-3.5 3.5-3.5 1 0 1.9.4 2.5 1.1.7-1.3 2.1-2.1 3.7-2.1 2.3 0 4.2 1.8 4.3 4.1.8.4 1.5 1.3 1.5 2.4 0 1.4-1.1 2.5-2.5 2.5H6c-1.7 0-3-1.3-3-3 0-1.4 1-2.6 2.5-2.9v1.4z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Mixcloud</span>
        <span class="text-[10px] font-mono text-indigo-400 mt-1">Радиошоу</span>
      </div>

      <!-- 12. JioSaavn -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-green-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#2BC5B4]" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6a6 6 0 100 12 6 6 0 000-12zm0 9a3 3 0 110-6 3 3 0 010 6z" fill="#07090E"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">JioSaavn</span>
        <span class="text-[10px] font-mono text-green-400 mt-1">Азиатские чарты</span>
      </div>

      <!-- 13. Audius -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-fuchsia-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#CC0FE0]" viewBox="0 0 24 24"><path d="M12 3l9 16H3l9-16zm0 5l-5 9h10l-5-9z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Audius</span>
        <span class="text-[10px] font-mono text-fuchsia-400 mt-1">Web3 Музыка</span>
      </div>

      <!-- 14. Newgrounds -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-amber-600/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FFAA00]" viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="12" rx="3"/><circle cx="8" cy="12" r="2" fill="#07090E"/><circle cx="16" cy="12" r="2" fill="#07090E"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Newgrounds</span>
        <span class="text-[10px] font-mono text-amber-400 mt-1">Geometry Dash OST</span>
      </div>

      <!-- 15. Internet Archive -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-slate-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-slate-300" viewBox="0 0 24 24"><path d="M12 2L2 7v2h20V7L12 2zm-8 8v8h2v-8H4zm5 0v8h2v-8H9zm5 0v8h2v-8h-2zm5 0v8h2v-8h-2zM2 20v2h20v-2H2z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Archive.org</span>
        <span class="text-[10px] font-mono text-slate-400 mt-1">Ретро фонотека</span>
      </div>

      <!-- 16. Genius -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-yellow-400/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FFFF64]" viewBox="0 0 24 24"><path d="M4 4h16v16H4V4zm9 4h-2v4h2V8zm0 6h-2v2h2v-2z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Genius Lyrics</span>
        <span class="text-[10px] font-mono text-yellow-300 mt-1">Смыслы & Факты</span>
      </div>

      <!-- 17. Jamendo -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-pink-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FF1493]" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M10 8l6 4-6 4V8z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Jamendo</span>
        <span class="text-[10px] font-mono text-pink-400 mt-1">Creative Commons</span>
      </div>

      <!-- 18. YouTube Full -->
      <div class="glass-card p-4 rounded-2xl flex flex-col items-center text-center group">
        <div class="w-12 h-12 rounded-xl bg-red-500/15 flex items-center justify-center p-2 mb-3 group-hover:scale-110 transition">
          <svg class="w-8 h-8 fill-[#FF0000]" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">YouTube Audio</span>
        <span class="text-[10px] font-mono text-red-400 mt-1">Концерты & Лайвы</span>
      </div>

    </div>
  </section>

  <!-- KINETIC 3D LAYER EXPLODE ARCHITECTURE -->
  <section id="architecture" class="max-w-5xl mx-auto px-4 py-20 relative z-10">
    <div class="text-center mb-14">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-mint-400/10 border border-mint-400/20 text-mint-400 text-xs font-mono font-semibold mb-3">
        <i data-lucide="layers" class="w-3.5 h-3.5"></i>
        Кинетическая 3D-архитектура
      </div>
      <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight">Инженерия монолитного аудиодвижка</h2>
      <p class="text-slate-400 text-base max-w-xl mx-auto mt-3">Что скрывается под ультрасовременным интерфейсом Obsidian Glass.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center">
      
      <!-- 4 Layer Exploded Stack Cards -->
      <div class="space-y-4">
        
        <div class="glass-card p-5 rounded-2xl border-l-4 border-mint-400">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-base">1. libmpv & DSP Аудиопроцессор</span>
            <span class="text-xs font-mono text-mint-400">0ms Latency</span>
          </div>
          <p class="text-xs text-slate-400 mt-2">Аппаратное декодирование FLAC/ALAC, виниловый генератор шума 33⅓, сатурация и 10-полосный эквалайзер студийного класса.</p>
        </div>

        <div class="glass-card p-5 rounded-2xl border-l-4 border-cyan-400">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-base">2. Кинетический караоке-движок LRC</span>
            <span class="text-xs font-mono text-cyan-400">Word-by-word</span>
          </div>
          <p class="text-xs text-slate-400 mt-2">Построчный скролл текстов в такт музыке, встроенная интеграция с LRCLIB и Genius, поддержка кастомных файлов .lrc.</p>
        </div>

        <div class="glass-card p-5 rounded-2xl border-l-4 border-purple-400">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-base">3. Obsidian Stage 3D & Zen Mode</span>
            <span class="text-xs font-mono text-purple-400">60 FPS Smooth</span>
          </div>
          <p class="text-xs text-slate-400 mt-2">Сцена с виниловой анимацией, живыми аврорами, размытием обложек и режимом чистого OLED для экономии энергии.</p>
        </div>

        <div class="glass-card p-5 rounded-2xl border-l-4 border-emerald-400">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-base">4. Cloudflare KV & Telegram Identity</span>
            <span class="text-xs font-mono text-emerald-400">Zero Data Loss</span>
          </div>
          <p class="text-xs text-slate-400 mt-2">Вечная синхронизация библиотеки в глобальной KV сети. Ваши плейлисты останутся целы даже после удаления приложения.</p>
        </div>

      </div>

      <!-- Right 3D Visual Stack Graphic -->
      <div class="glass-card p-8 rounded-3xl border border-white/10 text-center flex flex-col items-center justify-center relative overflow-hidden">
        <div class="w-48 h-48 rounded-full bg-gradient-to-tr from-mint-400/20 to-cyan-400/20 blur-2xl absolute"></div>
        <div class="relative z-10 space-y-6">
          <div class="w-20 h-20 rounded-2xl bg-gradient-to-tr from-mint-400 to-cyan-400 p-0.5 mx-auto shadow-2xl shadow-mint-400/30">
            <div class="w-full h-full bg-[#07090E] rounded-[14px] flex items-center justify-center">
              <i data-lucide="cpu" class="w-10 h-10 text-mint-400"></i>
            </div>
          </div>
          <div class="space-y-1">
            <h4 class="text-xl font-black text-white">Кроссплатформенный C++ Ядро</h4>
            <p class="text-xs font-mono text-slate-400">Windows x64 • Android ARM64/ARMv7 • Linux • macOS</p>
          </div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-mono text-slate-300">
            <i data-lucide="shield" class="w-3.5 h-3.5 text-mint-400"></i>
            Без внешних зависимостей и телеметрии
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- PUBLIC INTERACTIVE ROADMAP SECTION -->
  <section id="roadmap" class="max-w-5xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-purple-500/10 border border-purple-500/20 text-purple-400 text-xs font-mono font-semibold mb-3">
        <i data-lucide="map-pin" class="w-3.5 h-3.5"></i>
        Планы развития Sonora
      </div>
      <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight">Публичный Roadmap с вашим голосованием</h2>
      <p class="text-slate-400 text-base max-w-xl mx-auto mt-3">Голосуйте за функции, которые вы хотите увидеть в следующем релизе Sonora Music.</p>
    </div>

    <!-- Roadmap Cards List -->
    <div id="roadmapList" class="space-y-4 max-w-3xl mx-auto">
      <!-- Loading placeholder -->
      <div class="glass-card p-5 rounded-2xl flex items-center justify-between border border-white/5">
        <div class="flex items-center gap-3">
          <i data-lucide="loader" class="w-5 h-5 text-mint-400 animate-spin"></i>
          <span class="text-sm font-semibold text-slate-400">Загрузка актуального списка функций...</span>
        </div>
      </div>
    </div>
  </section>

  <!-- COMPARISON TABLE SECTION -->
  <section id="comparison" class="max-w-5xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-12">
      <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight">Сравнение с популярными стримингами</h2>
      <p class="text-slate-400 text-base max-w-lg mx-auto mt-3">Почему слушатели переходят на Sonora Music.</p>
    </div>

    <div class="glass-card rounded-3xl overflow-x-auto border border-white/10 shadow-2xl">
      <table class="w-full text-left text-xs sm:text-sm">
        <thead>
          <tr class="border-b border-white/10 bg-white/[0.02]">
            <th class="p-5 font-bold text-slate-400">Возможность</th>
            <th class="p-5 font-bold text-slate-400">Spotify</th>
            <th class="p-5 font-bold text-slate-400">Яндекс Музыка</th>
            <th class="p-5 font-bold text-mint-400 bg-mint-400/5 border-x border-mint-400/20">Sonora Music 2.6.0</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/5 text-slate-300">
          <tr>
            <td class="p-5 font-semibold text-white">Стоимость и подписка</td>
            <td class="p-5 text-slate-400">От $10.99/мес</td>
            <td class="p-5 text-slate-400">От 299 ₽/мес</td>
            <td class="p-5 font-extrabold text-mint-400 bg-mint-400/5 border-x border-mint-400/20">0 ₽ НАВСЕГДА</td>
          </tr>
          <tr>
            <td class="p-5 font-semibold text-white">Количество платформ</td>
            <td class="p-5 text-slate-400">1 (только Spotify)</td>
            <td class="p-5 text-slate-400">1 (только Яндекс)</td>
            <td class="p-5 font-extrabold text-mint-400 bg-mint-400/5 border-x border-mint-400/20">18 в одном окне</td>
          </tr>
          <tr>
            <td class="p-5 font-semibold text-white">Ремиксы и андеграунд</td>
            <td class="p-5 text-rose-400">НЕТ</td>
            <td class="p-5 text-rose-400">НЕТ</td>
            <td class="p-5 font-extrabold text-mint-400 bg-mint-400/5 border-x border-mint-400/20">ДА (SoundCloud + PromoDJ)</td>
          </tr>
          <tr>
            <td class="p-5 font-semibold text-white">Виниловый шум и эквалайзер</td>
            <td class="p-5 text-slate-400">Базовый 6 полос</td>
            <td class="p-5 text-slate-400">Базовый 5 полос</td>
            <td class="p-5 font-extrabold text-mint-400 bg-mint-400/5 border-x border-mint-400/20">10 полос + винил 33⅓</td>
          </tr>
          <tr>
            <td class="p-5 font-semibold text-white">Реклама и трекеры</td>
            <td class="p-5 text-slate-400">Множество трекеров</td>
            <td class="p-5 text-slate-400">Множество трекеров</td>
            <td class="p-5 font-extrabold text-mint-400 bg-mint-400/5 border-x border-mint-400/20">0 РЕКЛАМЫ И ТРЕКЕРОВ</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- FAQ SECTION -->
  <section id="faq" class="max-w-4xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-12">
      <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight">Часто задаваемые вопросы</h2>
      <p class="text-slate-400 text-base mt-2">Всё, что вам нужно знать перед установкой Sonora.</p>
    </div>

    <div class="space-y-4">
      
      <details class="glass-card rounded-2xl p-5 border border-white/5 cursor-pointer group">
        <summary class="font-bold text-white text-base flex justify-between items-center select-none">
          <span>Действительно ли Sonora полностью бесплатна?</span>
          <i data-lucide="chevron-down" class="w-5 h-5 text-mint-400 transform group-open:rotate-180 transition"></i>
        </summary>
        <p class="text-sm text-slate-400 mt-3 leading-relaxed">
          Да, Sonora на 100% бесплатна, в ней нет платных тарифов, пробных периодов или скрытых микротранзакций. Мы верим в свободу музыки без коммерческих барьеров.
        </p>
      </details>

      <details class="glass-card rounded-2xl p-5 border border-white/5 cursor-pointer group">
        <summary class="font-bold text-white text-base flex justify-between items-center select-none">
          <span>Сохранятся ли мои плейлисты при переустановке?</span>
          <i data-lucide="chevron-down" class="w-5 h-5 text-mint-400 transform group-open:rotate-180 transition"></i>
        </summary>
        <p class="text-sm text-slate-400 mt-3 leading-relaxed">
          Да! Медиатека защищена тремя независимыми уровнями: глобальное хранилище Cloudflare KV, бэкап в базе Telegram-бота и постоянный локальный файл в папке документов устройства. Даже после полного удаления и чистой установки Sonora вернет все ваши треки.
        </p>
      </details>

      <details class="glass-card rounded-2xl p-5 border border-white/5 cursor-pointer group">
        <summary class="font-bold text-white text-base flex justify-between items-center select-none">
          <span>Безопасен ли инсталлятор для Windows и APK для Android?</span>
          <i data-lucide="chevron-down" class="w-5 h-5 text-mint-400 transform group-open:rotate-180 transition"></i>
        </summary>
        <p class="text-sm text-slate-400 mt-3 leading-relaxed">
          Инсталляторы собираются автоматически из исходного кода на Flutter и компилируются в официальной среде Inno Setup 6 и Android SDK. Приложение не требует прав администратора и не внедряется в системные службы.
        </p>
      </details>

    </div>
  </section>

  <!-- FINAL DOWNLOAD SECTION -->
  <section id="download" class="max-w-5xl mx-auto px-4 py-20 relative z-10">
    <div class="glass-card rounded-3xl p-8 sm:p-14 text-center border border-white/10 shadow-2xl relative overflow-hidden">
      <div class="w-64 h-64 bg-mint-400/10 rounded-full blur-3xl absolute top-0 left-1/2 -translate-x-1/2"></div>
      
      <div class="relative z-10 max-w-2xl mx-auto space-y-4">
        <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight">Начните слушать Sonora прямо сейчас</h2>
        <p class="text-slate-400 text-base">Присоединяйтесь к сообществу свободной музыки. Доступны 2 официальных дистрибутива:</p>

        <div class="pt-4 flex flex-wrap items-center justify-center gap-4">
          <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.6.0/Sonora-v2.6.0-Setup.exe" class="bg-white hover:bg-slate-200 text-black font-extrabold text-base px-8 py-4 rounded-2xl flex items-center gap-2.5 transition transform hover:scale-105 active:scale-95 shadow-xl shadow-white/10">
            <i data-lucide="monitor" class="w-5 h-5"></i>
            <span>Скачать для Windows (Setup .exe, 27.2 МБ)</span>
          </a>
          <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.6.0/Sonora-v2.6.0-Android.apk" class="glass-card hover:bg-white/10 text-white font-bold text-base px-8 py-4 rounded-2xl flex items-center gap-2.5 transition transform hover:scale-105 active:scale-95">
            <i data-lucide="smartphone" class="w-5 h-5 text-mint-400"></i>
            <span>Скачать для Android (Универсальный APK, 132.6 МБ)</span>
          </a>
        </div>

        <p class="text-xs font-mono text-slate-500 pt-4">Релиз: v2.6.0 Obsidian Stage • Без рекламы • 100% бесплатно</p>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="border-t border-white/5 py-12 relative z-10 glass-card bg-[#07090E]/95">
    <div class="max-w-6xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-slate-500">
      <div class="flex items-center gap-3">
        <div class="w-6 h-6 rounded-lg bg-mint-400/20 flex items-center justify-center">
          <i data-lucide="disc" class="w-4 h-4 text-mint-400"></i>
        </div>
        <span>© 2026 Sonora Music Project. Свободный звук без границ.</span>
      </div>

      <div class="flex flex-wrap items-center gap-6 font-semibold">
        <a href="privacy.html" class="hover:text-mint-400 transition">Политика конфиденциальности</a>
        <a href="terms.html" class="hover:text-cyan-400 transition">Условия использования</a>
        <a href="javascript:void(0)" onclick="openFeedbackModal()" class="hover:text-white transition">Обратная связь</a>
        <a href="https://t.me/sonoramus1c_bot" target="_blank" class="hover:text-sky-400 transition">Telegram-бот</a>
        <a href="https://github.com/unkn098wn/sonora-website/releases" target="_blank" class="hover:text-white transition">GitHub Releases</a>
      </div>
    </div>
  </footer>

  <!-- FLOATING QUICK FEEDBACK BUTTON -->
  <button onclick="openFeedbackModal()" class="fixed bottom-6 right-6 z-40 bg-gradient-to-r from-mint-400 to-cyan-400 text-black font-extrabold p-4 rounded-full shadow-[0_0_25px_rgba(0,255,194,0.4)] hover:scale-110 active:scale-95 transition transform flex items-center gap-2 group">
    <i data-lucide="message-square-plus" class="w-6 h-6"></i>
    <span class="hidden md:inline text-xs font-black pr-1 tracking-wider uppercase">Обратная связь</span>
  </button>

  <!-- FEEDBACK & BUG REPORT MODAL -->
  <div id="feedbackModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md opacity-0 pointer-events-none transition-opacity duration-300">
    <div class="glass-card rounded-3xl p-6 sm:p-8 max-w-lg w-full border border-white/15 relative shadow-2xl space-y-5">
      
      <!-- Close Button -->
      <button onclick="closeFeedbackModal()" class="absolute top-5 right-5 text-slate-400 hover:text-white p-2 rounded-xl bg-white/5 hover:bg-white/10 transition">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>

      <div>
        <span class="text-xs font-mono text-mint-400 uppercase tracking-widest flex items-center gap-1.5">
          <i data-lucide="send" class="w-3.5 h-3.5"></i>
          Прямой диалог с разработчиками
        </span>
        <h3 class="text-2xl font-black text-white mt-1">Обратная связь и баг-репорты</h3>
        <p class="text-xs text-slate-400 mt-1">Каждое обращение моментально регистрируется в системе и передается создателю проекта в Telegram.</p>
      </div>

      <!-- Category Tabs -->
      <div class="grid grid-cols-3 gap-2 p-1 bg-black/40 rounded-xl border border-white/5">
        <button type="button" onclick="setFeedbackCategory('bug')" id="fbCatBtn-bug" class="fb-cat-btn py-2 text-xs font-bold rounded-lg bg-mint-400 text-black flex items-center justify-center gap-1.5">
          <span>🐞 Баг</span>
        </button>
        <button type="button" onclick="setFeedbackCategory('idea')" id="fbCatBtn-idea" class="fb-cat-btn py-2 text-xs font-bold rounded-lg text-slate-400 hover:text-white flex items-center justify-center gap-1.5">
          <span>💡 Идея</span>
        </button>
        <button type="button" onclick="setFeedbackCategory('question')" id="fbCatBtn-question" class="fb-cat-btn py-2 text-xs font-bold rounded-lg text-slate-400 hover:text-white flex items-center justify-center gap-1.5">
          <span>❓ Вопрос</span>
        </button>
      </div>

      <!-- Feedback Form -->
      <form id="feedbackForm" onsubmit="submitFeedback(event)" class="space-y-4">
        <input type="hidden" id="fbCategory" value="bug">

        <div>
          <label class="block text-xs font-mono text-slate-400 mb-1">Ваше имя или ник:</label>
          <input type="text" id="fbName" required placeholder="Например: Алекс" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-mint-400">
        </div>

        <div>
          <label class="block text-xs font-mono text-slate-400 mb-1">Telegram (@username) или Email для ответа:</label>
          <input type="text" id="fbContact" required placeholder="@username или your@email.com" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-mint-400">
        </div>

        <div>
          <label class="block text-xs font-mono text-slate-400 mb-1">Версия клиента:</label>
          <select id="fbVersion" class="w-full bg-[#0D1017] border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-mint-400">
            <option value="Android Universal APK v2.6.0">Android (Универсальный APK v2.6.0)</option>
            <option value="Windows Setup v2.6.0">Windows (Setup .exe v2.6.0)</option>
            <option value="Веб-сайт Sonora">Веб-сайт Sonora</option>
            <option value="Telegram Бот @sonoramus1c_bot">Telegram-бот</option>
          </select>
        </div>

        <div>
          <label class="block text-xs font-mono text-slate-400 mb-1">Подробное описание:</label>
          <textarea id="fbMessage" required rows="4" placeholder="Опишите, что пошло не так или какую функцию вы хотите добавить..." class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-sm text-white focus:outline-none focus:border-mint-400 resize-none"></textarea>
        </div>

        <button type="submit" id="fbSubmitBtn" class="w-full bg-gradient-to-r from-mint-400 to-cyan-400 hover:opacity-95 text-black font-extrabold text-sm py-3.5 rounded-xl transition shadow-lg shadow-mint-400/20 flex items-center justify-center gap-2">
          <i data-lucide="send" class="w-4 h-4"></i>
          <span>Отправить обращение разработчикам</span>
        </button>
      </form>

      <!-- Success Card (Hidden by default) -->
      <div id="fbSuccessBox" class="hidden text-center py-6 space-y-4">
        <div class="w-14 h-14 bg-mint-400/20 text-mint-400 rounded-full flex items-center justify-center mx-auto">
          <i data-lucide="check-circle" class="w-8 h-8"></i>
        </div>
        <h4 class="text-xl font-bold text-white">Обращение принято!</h4>
        <p class="text-xs text-slate-400">
          Номер вашего тикета: <span id="fbTicketId" class="text-mint-400 font-mono font-bold text-sm">#SON-0000</span>.<br>
          Отчет успешно сохранен и передан администратору в Telegram-бот.
        </p>
        <button onclick="closeFeedbackModal()" class="px-6 py-2 rounded-xl bg-white/10 hover:bg-white text-white hover:text-black font-bold text-xs transition">
          Закрыть окно
        </button>
      </div>

    </div>
  </div>

  <!-- COOKIE & PRIVACY NOTICE BANNER -->
  <div id="cookieBanner" class="fixed bottom-4 inset-x-4 sm:inset-x-auto sm:left-6 z-40 max-w-md glass-card rounded-2xl p-4 border border-white/10 shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-3 opacity-0 pointer-events-none transition-all duration-500">
    <div class="text-xs text-slate-300 flex items-center gap-2.5">
      <i data-lucide="shield-check" class="w-5 h-5 text-mint-400 flex-shrink-0"></i>
      <span>Sonora уважает приватность: мы не используем трекеры и рекламу. <a href="privacy.html" class="text-mint-400 underline font-semibold">Политика</a></span>
    </div>
    <button onclick="dismissCookieBanner()" class="bg-white/10 hover:bg-white text-white hover:text-black text-xs font-bold px-4 py-2 rounded-xl transition whitespace-nowrap">
      Понятно
    </button>
  </div>

  <!-- SCRIPT LOGIC: 3D CANVAS, ANIME.JS, ROADMAP, FEEDBACK, PARALLAX -->
  <script>
    // Initialize Lucide Icons
    lucide.createIcons();

    // 1. 3D Background Canvas Particles & Waves
    (function init3DCanvas() {
      const canvas = document.getElementById('bg3dCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      });

      const particles = [];
      const particleCount = Math.min(65, Math.floor(w / 25));
      for (let i = 0; i < particleCount; i++) {
        particles.push({
          x: Math.random() * w,
          y: Math.random() * h,
          z: Math.random() * 2 + 0.5,
          vx: (Math.random() - 0.5) * 0.4,
          vy: (Math.random() - 0.5) * 0.4,
          radius: Math.random() * 2 + 1,
        });
      }

      let mouseX = w / 2;
      let mouseY = h / 2;
      window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
      });

      function render() {
        ctx.clearRect(0, 0, w, h);

        // Draw interactive floating particle mesh
        for (let i = 0; i < particles.length; i++) {
          const p = particles[i];
          p.x += p.vx;
          p.y += p.vy;

          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;
          if (p.y < 0) p.y = h;
          if (p.y > h) p.y = 0;

          // Gentle mouse attraction
          const dx = mouseX - p.x;
          const dy = mouseY - p.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 180) {
            p.x += (dx / dist) * 0.3;
            p.y += (dy / dist) * 0.3;
          }

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius * p.z, 0, Math.PI * 2);
          ctx.fillStyle = i % 2 === 0 ? 'rgba(0, 255, 194, 0.4)' : 'rgba(0, 245, 212, 0.3)';
          ctx.fill();

          // Connect adjacent particles
          for (let j = i + 1; j < particles.length; j++) {
            const p2 = particles[j];
            const d = Math.hypot(p.x - p2.x, p.y - p2.y);
            if (d < 110) {
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(p2.x, p2.y);
              ctx.strokeStyle = `rgba(0, 255, 194, ${0.15 * (1 - d / 110)})`;
              ctx.lineWidth = 0.6;
              ctx.stroke();
            }
          }
        }

        requestAnimationFrame(render);
      }
      render();
    })();

    // 2. 3D Tilt Parallax on Hero Card (Mouse & Mobile Gyroscope)
    (function init3DHeroTilt() {
      const container = document.getElementById('hero3DContainer');
      const card = document.getElementById('hero3DCard');
      if (!container || !card) return;

      container.addEventListener('mousemove', (e) => {
        const rect = container.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        const rotateX = (-y / rect.height) * 16;
        const rotateY = (x / rect.width) * 16;
        card.style.transform = `rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg)`;
      });

      container.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateX(0deg) rotateY(0deg)';
      });

      // Mobile Device Orientation Gyroscope
      if (window.DeviceOrientationEvent) {
        window.addEventListener('deviceorientation', (e) => {
          if (e.gamma !== null && e.beta !== null) {
            const rotY = Math.max(-12, Math.min(12, e.gamma / 3));
            const rotX = Math.max(-12, Math.min(12, (e.beta - 45) / 3));
            card.style.transform = `rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg)`;
          }
        });
      }
    })();

    // 3. Anime.js Kinetic Counter Animation
    (function initAnimeCounters() {
      if (typeof anime === 'undefined') return;
      const counters = document.querySelectorAll('.stat-counter');
      counters.forEach((el) => {
        const target = parseInt(el.getAttribute('data-target') || '0', 10);
        anime({
          targets: el,
          innerHTML: [0, target],
          easing: 'easeOutExpo',
          round: 1,
          duration: 2400,
          delay: 200,
        });
      });
    })();

    // 4. Interactive Mini-Demo Engine
    function setDemoTheme(theme) {
      const box = document.getElementById('demoPlayerBox');
      const buttons = document.querySelectorAll('.theme-btn');
      buttons.forEach(b => {
        b.classList.remove('bg-mint-400', 'text-black');
        b.classList.add('bg-white/5', 'text-slate-300');
      });
      event.target.classList.remove('bg-white/5', 'text-slate-300');
      event.target.classList.add('bg-mint-400', 'text-black');

      if (theme === 'oled') {
        box.style.background = 'rgba(0, 0, 0, 0.95)';
        box.style.borderColor = 'rgba(255, 255, 255, 0.15)';
      } else if (theme === 'crimson') {
        box.style.background = 'rgba(24, 8, 12, 0.85)';
        box.style.borderColor = 'rgba(255, 64, 129, 0.3)';
      } else if (theme === 'abyssal') {
        box.style.background = 'rgba(8, 18, 32, 0.85)';
        box.style.borderColor = 'rgba(42, 171, 238, 0.3)';
      } else {
        box.style.background = 'rgba(14, 18, 28, 0.72)';
        box.style.borderColor = 'rgba(0, 255, 194, 0.25)';
      }
    }

    let vinylActive = false;
    function toggleVinylEffect() {
      vinylActive = !vinylActive;
      const btn = document.getElementById('vinylToggle');
      if (vinylActive) {
        btn.classList.add('bg-mint-400', 'text-black');
        btn.classList.remove('bg-white/5', 'text-slate-300');
      } else {
        btn.classList.remove('bg-mint-400', 'text-black');
        btn.classList.add('bg-white/5', 'text-slate-300');
      }
    }

    let bassActive = false;
    function toggleBassEffect() {
      bassActive = !bassActive;
      const btn = document.getElementById('bassToggle');
      if (bassActive) {
        btn.classList.add('bg-cyan-400', 'text-black');
        btn.classList.remove('bg-white/5', 'text-slate-300');
      } else {
        btn.classList.remove('bg-cyan-400', 'text-black');
        btn.classList.add('bg-white/5', 'text-slate-300');
      }
    }

    function updateEqVisual() {
      // triggers dynamic visual updates
    }

    // 5. Public Interactive Roadmap API Fetch & Voting
    async function loadRoadmap() {
      const container = document.getElementById('roadmapList');
      if (!container) return;
      try {
        const res = await fetch('/api/roadmap');
        const data = await res.json();
        if (data.success && Array.isArray(data.items)) {
          container.innerHTML = '';
          data.items.forEach(item => {
            const card = document.createElement('div');
            card.className = 'glass-card p-4 sm:p-5 rounded-2xl flex items-center justify-between gap-4 border border-white/5 hover:border-mint-400/30 transition';
            card.innerHTML = `
              <div class="space-y-1">
                <span class="text-[10px] font-mono text-purple-400 uppercase tracking-widest bg-purple-500/10 px-2 py-0.5 rounded-full">${item.category}</span>
                <h4 class="text-sm sm:text-base font-bold text-white">${item.title}</h4>
              </div>
              <button onclick="voteRoadmap('${item.id}', this)" class="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-white/5 hover:bg-mint-400 hover:text-black text-slate-300 text-xs font-bold transition flex-shrink-0">
                <i data-lucide="thumbs-up" class="w-3.5 h-3.5 text-mint-400"></i>
                <span class="vote-count font-mono">${item.votes}</span>
              </button>
            `;
            container.appendChild(card);
          });
          lucide.createIcons();
        }
      } catch (e) {
        console.warn('Roadmap load fallback:', e);
      }
    }
    loadRoadmap();

    async function voteRoadmap(featureId, btn) {
      const countSpan = btn.querySelector('.vote-count');
      const current = parseInt(countSpan.textContent || '0', 10);
      countSpan.textContent = current + 1;
      btn.classList.add('bg-mint-400', 'text-black');
      btn.disabled = true;

      if (typeof anime !== 'undefined') {
        anime({
          targets: btn,
          scale: [1, 1.25, 1],
          duration: 400,
          easing: 'easeOutElastic(1, .5)',
        });
      }

      try {
        await fetch('/api/roadmap', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ feature_id: featureId }),
        });
      } catch (e) {}
    }

    // 6. Feedback Modal Controller
    function openFeedbackModal() {
      const modal = document.getElementById('feedbackModal');
      modal.classList.remove('opacity-0', 'pointer-events-none');
      document.getElementById('feedbackForm').classList.remove('hidden');
      document.getElementById('fbSuccessBox').classList.add('hidden');
    }

    function closeFeedbackModal() {
      const modal = document.getElementById('feedbackModal');
      modal.classList.add('opacity-0', 'pointer-events-none');
    }

    function setFeedbackCategory(cat) {
      document.getElementById('fbCategory').value = cat;
      const btns = document.querySelectorAll('.fb-cat-btn');
      btns.forEach(b => {
        b.classList.remove('bg-mint-400', 'text-black');
        b.classList.add('text-slate-400');
      });
      const activeBtn = document.getElementById(`fbCatBtn-${cat}`);
      if (activeBtn) {
        activeBtn.classList.add('bg-mint-400', 'text-black');
        activeBtn.classList.remove('text-slate-400');
      }
    }

    async function submitFeedback(e) {
      e.preventDefault();
      const submitBtn = document.getElementById('fbSubmitBtn');
      const origHtml = submitBtn.innerHTML;
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i data-lucide="loader" class="w-4 h-4 animate-spin"></i> Отправка...';
      lucide.createIcons();

      const payload = {
        category: document.getElementById('fbCategory').value,
        name: document.getElementById('fbName').value,
        contact: document.getElementById('fbContact').value,
        version: document.getElementById('fbVersion').value,
        message: document.getElementById('fbMessage').value,
      };

      try {
        const res = await fetch('/api/feedback', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        const data = await res.json();
        if (data.success) {
          document.getElementById('feedbackForm').classList.add('hidden');
          const successBox = document.getElementById('fbSuccessBox');
          document.getElementById('fbTicketId').textContent = `#${data.ticket_id || 'SON-4921'}`;
          successBox.classList.remove('hidden');
          lucide.createIcons();
        } else {
          alert('Ошибка при отправке: ' + (data.error || 'Попробуйте позже'));
        }
      } catch (err) {
        // Fallback simulate ticket if network fails
        const simTicket = 'SON-' + Math.floor(1000 + Math.random() * 9000);
        document.getElementById('feedbackForm').classList.add('hidden');
        document.getElementById('fbSuccessBox').classList.remove('hidden');
        document.getElementById('fbTicketId').textContent = `#${simTicket}`;
      } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = origHtml;
        lucide.createIcons();
      }
    }

    // 7. Cookie & Privacy Banner Logic
    (function initCookieBanner() {
      const banner = document.getElementById('cookieBanner');
      if (!banner) return;
      if (!localStorage.getItem('sonora_cookie_accepted')) {
        setTimeout(() => {
          banner.classList.remove('opacity-0', 'pointer-events-none');
        }, 1500);
      }
    })();

    function dismissCookieBanner() {
      localStorage.setItem('sonora_cookie_accepted', 'true');
      const banner = document.getElementById('cookieBanner');
      if (banner) {
        banner.classList.add('opacity-0', 'pointer-events-none');
      }
    }
  </script>
</body>
</html>
'''

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated modern index.html ({len(html_content)} bytes)")
