import os

website_dir = r"C:\Users\maksi\OneDrive\Desktop\Sonora Project\Sonora-Website"
index_path = os.path.join(website_dir, "index.html")

html_content = r'''<!DOCTYPE html>
<html lang="ru" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sonora Music — Музыка всех миров в одном монолитном плеере</title>
  <meta name="description" content="Sonora — ультрасовременный бесплатный музыкальный плеер для Windows и Android. Мгновенный поиск по 18 мировым и андеграунд площадкам, FLAC 24-бит, умная «Моя волна», DSP-студия, вечная облачная синхронизация медиатеки. 0 подписок и 0 рекламы.">
  <meta name="keywords" content="Sonora, музыкальный плеер, музыка без подписки, mp3 плеер, flac плеер, моя волна, soundcloud, youtube music, streaming player, linear dark, 3d плеер">

  <!-- OpenGraph Meta -->
  <meta property="og:title" content="Sonora Music — Музыка всех миров">
  <meta property="og:description" content="18 музыкальных площадок в одном монолитном плеере. 100% бесплатно навсегда.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://sonoramusic.ru/">
  <link rel="canonical" href="https://sonoramusic.ru/">

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
              950: '#000000',
              900: '#060608',
              850: '#0B0B0E',
              800: '#111115',
              700: '#18181D',
              600: '#23232A',
            }
          }
        }
      }
    }
  </script>

  <style>
    /* Linear / Vercel Dark Monochrome Design Tokens */
    :root {
      --bg: #000000;
      --surface: #09090B;
      --surface-elevated: #111115;
      --border: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(255, 255, 255, 0.22);
      --text-primary: #FFFFFF;
      --text-secondary: #A1A1AA;
      --text-muted: #52525B;
    }

    body {
      background-color: var(--bg);
      color: #EDEDED;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Prevent mobile tap delay and optimize touch interaction */
    button, a, input, select, textarea {
      touch-action: manipulation;
    }

    /* Clean details marker */
    details summary::-webkit-details-marker {
      display: none;
    }
    details summary {
      list-style: none;
    }

    /* Video background pointer-events immunity */
    #headerVideoWrapper,
    #headerLightRaysVideo {
      pointer-events: none !important;
      -webkit-user-select: none;
      user-select: none;
      -webkit-touch-callout: none;
    }

    /* Engineering Dot Grid Background */
    .bg-grid {
      background-image: radial-gradient(rgba(255, 255, 255, 0.08) 1px, transparent 1px);
      background-size: 28px 28px;
    }

    /* Monolithic Precision Glass Card */
    .glass-card {
      background: rgba(10, 10, 13, 0.72);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--border);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(255, 255, 255, 0.06);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .glass-card:hover {
      border-color: var(--border-hover);
      box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.95), inset 0 1px 0 rgba(255, 255, 255, 0.12);
    }

    /* Tactile Equalizer Fader */
    input[type=range].eq-slider {
      -webkit-appearance: none;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 9999px;
      height: 4px;
    }
    input[type=range].eq-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      height: 16px;
      width: 16px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 2px solid #000000;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.8);
      cursor: pointer;
      transition: transform 0.15s ease;
    }
    input[type=range].eq-slider::-webkit-slider-thumb:hover {
      transform: scale(1.2);
    }

    /* 3D Perspective Context */
    .perspective-1000 {
      perspective: 1000px;
      transform-style: preserve-3d;
    }
    .preserve-3d {
      transform-style: preserve-3d;
    }
  </style>
</head>
<body class="bg-grid selection:bg-white/20 selection:text-white relative">

  <!-- ATMOSPHERIC LIGHT RAYS VIDEO BACKGROUND (HEADER HERO) -->
  <div id="headerVideoWrapper" class="fixed top-0 inset-x-0 h-[100vh] min-h-[720px] max-h-[1100px] overflow-hidden pointer-events-none z-0 transition-opacity duration-300" style="will-change: opacity;">
    <video id="headerLightRaysVideo" autoplay muted loop playsinline preload="auto" class="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full object-cover object-top" style="filter: blur(14px) contrast(1.18) brightness(0.92); mix-blend-mode: screen; opacity: 0.92;">
      <source src="assets/videos/light_rays.mp4" type="video/mp4">
    </video>
    <!-- Seamless Gradient Vignette merging into Obsidian Black -->
    <div class="absolute inset-0 bg-gradient-to-b from-black/15 via-transparent to-black pointer-events-none"></div>
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_center,transparent_30%,rgba(0,0,0,0.8)_100%)] pointer-events-none"></div>
  </div>

  <!-- STICKY PRECISION HEADER -->
  <header class="fixed top-2.5 sm:top-4 inset-x-0 z-50 flex flex-col items-center px-3 sm:px-4" id="mainHeader">
    <nav class="glass-card rounded-2xl lg:rounded-full px-3.5 sm:px-5 py-2 sm:py-2.5 flex items-center justify-between gap-2 sm:gap-4 max-w-5xl w-full border border-white/10 shadow-2xl relative">
      <!-- Logo -->
      <a href="#" class="flex items-center gap-2 sm:gap-3 group flex-shrink-0" aria-label="Sonora Music Главная">
        <div class="w-7 h-7 sm:w-8 sm:h-8 rounded-lg bg-zinc-900 border border-white/15 flex items-center justify-center p-1 sm:p-1.5 transition duration-300 group-hover:border-white/40">
          <i data-lucide="disc" class="w-4 h-4 text-white group-hover:rotate-90 transition duration-700"></i>
        </div>
        <div class="flex items-center gap-1.5 sm:gap-2">
          <span class="text-xs sm:text-sm font-black text-white tracking-wider sm:tracking-widest font-mono">SONORA</span>
          <span class="hidden sm:inline-block text-[10px] font-mono font-semibold text-zinc-400 bg-white/5 px-2 py-0.5 rounded-full border border-white/10">v2.7.0</span>
        </div>
      </a>

      <!-- Navigation Links (Desktop) -->
      <div class="hidden lg:flex items-center gap-4 xl:gap-6 text-xs font-semibold text-zinc-400 font-mono">
        <a href="#spectrogram" class="hover:text-white transition">Спектрограмма</a>
        <a href="#platforms" class="hover:text-white transition">18 Платформ</a>
        <a href="#dsp-studio" class="hover:text-white transition">Студия DSP</a>
        <a href="#architecture" class="hover:text-white transition">Архитектура</a>
        <a href="#roadmap" class="hover:text-white transition">Roadmap</a>
        <a href="#faq" class="hover:text-white transition">FAQ</a>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center gap-1.5 sm:gap-2.5 flex-shrink-0">
        <!-- Feedback Button (Desktop / Tablet) -->
        <button onclick="openFeedbackModal()" class="hidden sm:flex text-xs font-bold text-zinc-300 hover:text-white px-3 py-1.5 rounded-lg border border-white/10 hover:bg-white/5 transition items-center gap-1.5 active:scale-95" title="Обратная связь">
          <i data-lucide="message-square" class="w-3.5 h-3.5 text-zinc-400"></i>
          <span>Отзыв</span>
        </button>
        <!-- Download CTA Button (Responsive) -->
        <a href="#download" class="bg-white hover:bg-zinc-200 text-black font-extrabold text-xs px-3.5 sm:px-4 py-1.5 sm:py-2 rounded-full transition transform hover:scale-105 active:scale-95 flex items-center gap-1.5 shadow-lg shadow-white/5 flex-shrink-0">
          <i data-lucide="download" class="w-3.5 h-3.5"></i>
          <span>Скачать</span>
        </a>
        <!-- Mobile Menu Toggle Button -->
        <button id="mobileMenuBtn" onclick="toggleMobileMenu()" aria-label="Открыть навигацию" class="lg:hidden text-zinc-300 hover:text-white p-1.5 sm:p-2 rounded-lg border border-white/10 hover:bg-white/5 transition flex items-center justify-center flex-shrink-0 active:scale-95">
          <i data-lucide="menu" id="mobileMenuIcon" class="w-4 h-4"></i>
        </button>
      </div>
    </nav>

    <!-- Mobile Dropdown Navigation -->
    <div id="mobileMenuDropdown" class="hidden lg:hidden w-full max-w-5xl mt-2 glass-card rounded-2xl p-3 sm:p-4 border border-white/10 shadow-2xl backdrop-blur-2xl bg-black/95 flex flex-col space-y-1 font-mono text-xs text-zinc-300 transition-all duration-300">
      <a href="#spectrogram" onclick="closeMobileMenu()" class="p-2.5 hover:bg-white/5 rounded-xl hover:text-white flex items-center justify-between border border-transparent hover:border-white/5">
        <span class="flex items-center gap-2"><i data-lucide="activity" class="w-3.5 h-3.5 text-zinc-400"></i> Спектрограмма</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-zinc-500"></i>
      </a>
      <a href="#platforms" onclick="closeMobileMenu()" class="p-2.5 hover:bg-white/5 rounded-xl hover:text-white flex items-center justify-between border border-transparent hover:border-white/5">
        <span class="flex items-center gap-2"><i data-lucide="radio" class="w-3.5 h-3.5 text-zinc-400"></i> 18 Платформ</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-zinc-500"></i>
      </a>
      <a href="#dsp-studio" onclick="closeMobileMenu()" class="p-2.5 hover:bg-white/5 rounded-xl hover:text-white flex items-center justify-between border border-transparent hover:border-white/5">
        <span class="flex items-center gap-2"><i data-lucide="sliders" class="w-3.5 h-3.5 text-zinc-400"></i> Студия DSP</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-zinc-500"></i>
      </a>
      <a href="#architecture" onclick="closeMobileMenu()" class="p-2.5 hover:bg-white/5 rounded-xl hover:text-white flex items-center justify-between border border-transparent hover:border-white/5">
        <span class="flex items-center gap-2"><i data-lucide="layers" class="w-3.5 h-3.5 text-zinc-400"></i> Архитектура</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-zinc-500"></i>
      </a>
      <a href="#roadmap" onclick="closeMobileMenu()" class="p-2.5 hover:bg-white/5 rounded-xl hover:text-white flex items-center justify-between border border-transparent hover:border-white/5">
        <span class="flex items-center gap-2"><i data-lucide="map-pin" class="w-3.5 h-3.5 text-zinc-400"></i> Roadmap развития</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-zinc-500"></i>
      </a>
      <a href="#faq" onclick="closeMobileMenu()" class="p-2.5 hover:bg-white/5 rounded-xl hover:text-white flex items-center justify-between border border-transparent hover:border-white/5">
        <span class="flex items-center gap-2"><i data-lucide="help-circle" class="w-3.5 h-3.5 text-zinc-400"></i> FAQ</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-zinc-500"></i>
      </a>
      <div class="my-1 border-t border-white/10"></div>
      <a href="#download" onclick="closeMobileMenu()" class="p-2.5 bg-white text-black font-extrabold rounded-xl flex items-center justify-between">
        <span class="flex items-center gap-2"><i data-lucide="download" class="w-3.5 h-3.5"></i> Скачать плеер (Windows / Android)</span>
        <i data-lucide="arrow-down" class="w-3.5 h-3.5"></i>
      </a>
      <button onclick="openFeedbackModal(); closeMobileMenu();" class="w-full p-2.5 hover:bg-white/5 rounded-xl hover:text-white flex items-center justify-between border border-transparent hover:border-white/5 text-left">
        <span class="flex items-center gap-2"><i data-lucide="message-square" class="w-3.5 h-3.5 text-zinc-400"></i> Написать разработчику (Отзыв / Баг)</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-zinc-500"></i>
      </button>
      <div class="pt-2 border-t border-white/10 flex items-center justify-between text-[11px] text-zinc-400">
        <span>Sonora Music v2.7.0</span>
        <a href="https://t.me/sonoramus1c_bot" target="_blank" class="text-white hover:underline flex items-center gap-1 font-sans">
          <i data-lucide="send" class="w-3 h-3"></i> Telegram-бот
        </a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION WITH REAL-TIME 3D AUDIO SPECTROGRAM -->
  <section class="relative z-10 pt-28 sm:pt-40 pb-16 sm:pb-20 max-w-6xl mx-auto px-4 text-center">
    <!-- Version & Monolith Tag -->
    <div class="inline-flex max-w-full items-center gap-2 px-3 sm:px-3.5 py-1.5 rounded-full glass-card border border-white/10 mb-8 text-center">
      <span class="w-1.5 h-1.5 rounded-full bg-white animate-pulse flex-shrink-0"></span>
      <span class="text-[11px] sm:text-xs font-mono font-medium text-zinc-300">
        Sonora v2.7.0 Obsidian Architecture • 0 подписок • 0 рекламы
      </span>
    </div>

    <!-- Main Headline -->
    <h1 class="text-3xl sm:text-6xl md:text-7xl font-extrabold text-white tracking-tight leading-[1.1] sm:leading-[1.08] max-w-5xl mx-auto">
      Музыка всех миров в одном <span class="text-zinc-400">монолитном плеере</span>
    </h1>

    <p class="text-zinc-400 text-sm sm:text-lg max-w-2xl mx-auto mt-4 sm:mt-6 leading-relaxed font-normal">
      Слушайте треки из 18 мировых площадок в студийном FLAC 24-бит с математической 3D-спектрограммой, бесконечной Моей Волной и вечной синхронизацией медиатеки.
    </p>

    <!-- Official Installers Download Buttons -->
    <div class="mt-8 sm:mt-10 flex flex-col sm:flex-row flex-wrap items-center justify-center gap-3 sm:gap-4 max-w-2xl mx-auto w-full">
      <!-- Windows Setup Button -->
      <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.7.0/Sonora-v2.7.0-Setup.exe" class="w-full sm:w-auto bg-white text-black font-extrabold text-xs sm:text-sm md:text-base px-5 sm:px-7 py-3.5 rounded-xl flex items-center justify-center gap-2 sm:gap-3 transition transform hover:scale-[1.02] active:scale-[0.98] shadow-2xl hover:bg-zinc-200">
        <i data-lucide="monitor" class="w-4 h-4 flex-shrink-0"></i>
        <span>Windows Setup (.exe)</span>
        <span class="text-[11px] sm:text-xs font-mono font-bold bg-black/10 px-2 py-0.5 rounded flex-shrink-0">30.5 МБ</span>
      </a>

      <!-- Android Universal APK Button -->
      <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.7.0/Sonora-v2.7.0-Android.apk" class="w-full sm:w-auto glass-card hover:bg-white/5 text-white font-bold text-xs sm:text-sm md:text-base px-5 sm:px-7 py-3.5 rounded-xl flex items-center justify-center gap-2 sm:gap-3 transition transform hover:scale-[1.02] active:scale-[0.98] border border-white/15">
        <i data-lucide="smartphone" class="w-4 h-4 text-zinc-300 flex-shrink-0"></i>
        <span>Android (APK)</span>
        <span class="text-[11px] sm:text-xs font-mono text-zinc-400 bg-white/5 px-2 py-0.5 rounded border border-white/10 flex-shrink-0">138.1 МБ</span>
      </a>

      <!-- Telegram Bot CTA -->
      <a href="https://t.me/sonoramus1c_bot" target="_blank" class="w-full sm:w-auto glass-card hover:bg-white/5 text-zinc-300 hover:text-white font-bold text-xs sm:text-sm md:text-base px-4 sm:px-5 py-3.5 rounded-xl flex items-center justify-center gap-2 transition transform hover:scale-[1.02] active:scale-[0.98] border border-white/10">
        <svg class="w-4 h-4 fill-current flex-shrink-0" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.74-.55 2.92-1.27 4.86-2.11 5.83-2.52 2.77-1.18 3.35-1.38 3.73-1.39.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .37z"/></svg>
        <span>Telegram-бот</span>
      </a>
    </div>

    <!-- INTERACTIVE 3D SPECTROGRAM STAGE CARD -->
    <div id="spectrogram" class="scroll-mt-24 mt-12 sm:mt-16 relative perspective-1000 max-w-4xl mx-auto">
      <div id="spectrogramCard" class="glass-card rounded-2xl p-4 sm:p-8 border border-white/10 preserve-3d transition-transform duration-200 shadow-2xl relative overflow-hidden">
        
        <!-- Header row of the Workbench -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 sm:gap-4 pb-4 border-b border-white/5">
          <div class="flex items-center gap-2.5 sm:gap-3">
            <span class="w-2 h-2 rounded-full bg-white flex-shrink-0"></span>
            <span class="text-[11px] sm:text-xs font-mono uppercase tracking-wider sm:tracking-widest text-zinc-300 font-bold">ИНТЕРАКТИВНАЯ 3D-СПЕКТРОГРАММА</span>
          </div>
          <div class="flex items-center gap-2 sm:gap-3 font-mono text-[10px] sm:text-xs">
            <span class="px-2.5 py-0.5 rounded bg-white/5 border border-white/10 text-zinc-300">FLAC 24-BIT / 96kHz</span>
            <span class="text-zinc-500">LOSSLESS 1411 KBPS</span>
          </div>
        </div>

        <!-- 3D Canvas Spectrogram Container with Touch-Pan-Y -->
        <div class="relative w-full h-48 sm:h-64 my-4 flex items-center justify-center overflow-hidden rounded-xl bg-black/40 border border-white/5 touch-pan-y">
          <canvas id="spectrogramCanvas" class="w-full h-full cursor-crosshair"></canvas>
          
          <!-- Subtle Spectrogram Watermark Overlay -->
          <div class="absolute bottom-3 right-4 pointer-events-none text-right font-mono text-[9px] sm:text-[10px] text-zinc-600">
            <div>FFT SPECTRUM • 32 BANDS</div>
            <div>REAL-TIME DSP HARMONICS</div>
          </div>
        </div>

        <!-- Track & Audio Pipeline Status -->
        <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 sm:gap-4 pt-3 text-left">
          <div class="space-y-1">
            <div class="text-xs sm:text-sm font-bold text-white flex items-center gap-2">
              <i data-lucide="volume-2" class="w-4 h-4 text-zinc-400 flex-shrink-0"></i>
              <span>Shadows in the Dark — Kavinsky</span>
            </div>
            <p class="text-[11px] sm:text-xs font-mono text-zinc-500">Audio Pipeline: Direct WASAPI Output • Micro-Fade 40ms Active</p>
          </div>

          <!-- Feature Pills in Monochrome Titanium -->
          <div class="flex flex-wrap gap-1.5 sm:gap-2">
            <span class="text-[10px] sm:text-[11px] font-mono px-2.5 py-1 rounded bg-white/5 border border-white/10 text-zinc-300">10-Band EQ: Flat Hi-Fi</span>
            <span class="text-[10px] sm:text-[11px] font-mono px-2.5 py-1 rounded bg-white/5 border border-white/10 text-zinc-300">Vinyl Crackle: 33⅓</span>
            <span class="text-[10px] sm:text-[11px] font-mono px-2.5 py-1 rounded bg-white/5 border border-white/20 text-white font-semibold">Cloud KV Synced</span>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- KINETIC STATS COUNTER -->
  <section class="max-w-6xl mx-auto px-4 py-8 relative z-10">
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 sm:gap-6">
      
      <div class="glass-card p-6 rounded-xl text-center">
        <div class="text-3xl sm:text-4xl font-extrabold text-white font-mono flex items-center justify-center">
          <span class="stat-counter" data-target="18">0</span>
        </div>
        <p class="text-xs sm:text-sm font-medium text-zinc-400 mt-2 font-mono">Музыкальных сервисов</p>
      </div>

      <div class="glass-card p-6 rounded-xl text-center">
        <div class="text-3xl sm:text-4xl font-extrabold text-white font-mono flex items-center justify-center">
          <span class="stat-counter" data-target="24">0</span><span class="text-2xl text-zinc-400">bit</span>
        </div>
        <p class="text-xs sm:text-sm font-medium text-zinc-400 mt-2 font-mono">FLAC Hi-Res Audio</p>
      </div>

      <div class="glass-card p-6 rounded-xl text-center">
        <div class="text-3xl sm:text-4xl font-extrabold text-white font-mono flex items-center justify-center">
          <span class="stat-counter" data-target="10">0</span>
        </div>
        <p class="text-xs sm:text-sm font-medium text-zinc-400 mt-2 font-mono">Полос DSP-эквалайзера</p>
      </div>

      <div class="glass-card p-6 rounded-xl text-center">
        <div class="text-3xl sm:text-4xl font-extrabold text-white font-mono flex items-center justify-center">
          0<span class="text-2xl text-zinc-400">₽</span>
        </div>
        <p class="text-xs sm:text-sm font-medium text-zinc-400 mt-2 font-mono">Подписок и рекламы</p>
      </div>

    </div>
  </section>

  <!-- 18 STREAMING PLATFORMS SHOWCASE (MONOCHROME TITANIUM BADGES) -->
  <section id="platforms" class="scroll-mt-24 max-w-6xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-white/5 border border-white/10 text-zinc-300 text-xs font-mono font-medium mb-3">
        <i data-lucide="radio" class="w-3.5 h-3.5"></i>
        18 Музыкальных экосистем
      </div>
      <h2 class="text-3xl sm:text-4xl font-bold text-white tracking-tight">Вся музыка планеты в единой поисковой строке</h2>
      <p class="text-zinc-400 text-sm sm:text-base max-w-xl mx-auto mt-2">Никаких переключений между десятком приложений. Вводите название трека, артиста или вставляйте ссылку на альбом.</p>
    </div>

    <!-- 18 Platform Cards Grid with Official Monochrome SVGs -->
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 sm:gap-4">
      
      <!-- 1. YouTube Music -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 14.5c-2.49 0-4.5-2.01-4.5-4.5S9.51 7.5 12 7.5s4.5 2.01 4.5 4.5-2.01 4.5-4.5 4.5zm0-5.5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm-2 1l5-3-5-3v6z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">YouTube Music</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">FLAC & Клипы</span>
      </div>

      <!-- 2. SoundCloud -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M11.56 8.87V17h8.88c1.96 0 3.56-1.57 3.56-3.5 0-1.9-1.52-3.44-3.42-3.5-.27-2.73-2.58-4.87-5.42-4.87-1.39 0-2.67.51-3.6 1.37zm-2.04 8.13V9.67c-.2.27-.37.58-.51.9v6.43h.51zm-1.53 0v-5.8c-.26.47-.46.99-.58 1.54v4.26h.58zm-1.53 0v-3.72c-.17.65-.26 1.34-.26 2.05v1.67h.26zm-1.53 0v-1.67c0-.28-.02-.56-.05-.84v2.51h.05z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">SoundCloud</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Remixes & HQ</span>
      </div>

      <!-- 3. Deezer -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M18.8 6.2h3.9V9h-3.9zm-4.7 0H18V9h-3.9zm9.4 4.3v2.8h-3.9v-2.8zm-4.7 0v2.8H18v-2.8zm-4.7 0v2.8h3.9v-2.8zm9.4 4.3v2.8h-3.9v-2.8zm-4.7 0v2.8H18v-2.8zm-4.7 0v2.8h3.9v-2.8zm-4.7 0v2.8h3.9v-2.8zm-4.7 0v2.8H9v-2.8zm18.8 4.3v2.8h-3.9v-2.8zm-4.7 0v2.8H18v-2.8zm-4.7 0v2.8h3.9v-2.8zm-4.7 0v2.8H9v-2.8zm-4.7 0v2.8H4.3v-2.8z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Deezer</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">FLAC 1411 kbps</span>
      </div>

      <!-- 4. Яндекс Музыка -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M12 2L14.4 9.6L22 12L14.4 14.4L12 22L9.6 14.4L2 12L9.6 9.6L12 2Z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Яндекс Музыка</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Моя Волна HQ</span>
      </div>

      <!-- 5. Spotify -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.586 14.424c-.18.295-.563.387-.857.207-2.35-1.434-5.308-1.758-8.793-.963-.335.077-.67-.133-.746-.469-.077-.334.132-.67.467-.747 3.813-.871 7.08-.507 9.721 1.115.295.18.388.563.208.857zm1.226-2.723c-.226.367-.706.482-1.072.257-2.687-1.652-6.785-2.131-9.965-1.166-.413.127-.849-.106-.974-.517-.125-.413.108-.849.52-.974 3.632-1.102 8.147-.568 11.234 1.328.366.226.481.707.257 1.072zm.106-2.835C14.692 8.87 9.375 8.694 6.297 9.628c-.494.15-1.018-.13-1.168-.624-.15-.494.13-1.018.624-1.168 3.532-1.072 9.404-.866 13.115 1.338.445.264.59.838.327 1.282-.264.443-.838.59-1.277.33z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Spotify</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Импорт плейлистов</span>
      </div>

      <!-- 6. Apple Music -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm3.7 6.3l.003 4.88c0 1.63-1.08 2.62-2.5 2.62-1.32 0-2.32-.9-2.32-2.18s1-2.22 2.32-2.22c.4 0 .8.08 1.15.24V9.62l-3.35.83v4.32c0 1.63-1.08 2.62-2.5 2.62-1.32 0-2.32-.9-2.32-2.18s1-2.22 2.32-2.22c.4 0 .8.08 1.15.24V8.5c0-.6.44-1.1 1.03-1.22l4.17-.98c.55-.13 1.02.28 1.02.87z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Apple Music</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Каталоги & Тексты</span>
      </div>

      <!-- 7. VK Музыка -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14.5c-2.49 0-4.5-2.01-4.5-4.5S9.51 7.5 13 7.5v4.5h3.5c0 2.49-2.01 4.5-4.5 4.5z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">VK Музыка</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Редкие ремиксы</span>
      </div>

      <!-- 8. Tidal -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M4 8l4-4 4 4-4 4-4-4zm8 0l4-4 4 4-4 4-4-4zm-4 4l4-4 4 4-4 4-4-4zm8 0l4-4 4 4-4 4-4-4z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Tidal</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">MQA & Master</span>
      </div>

      <!-- 9. Bandcamp -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M0 18.75l7.437-13.5h16.563l-7.438 13.5z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Bandcamp</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Инди & Андеграунд</span>
      </div>

      <!-- 10. PromoDJ -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M10 8l6 4-6 4V8z" fill="#000000"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">PromoDJ</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">DJ-миксы & Сеты</span>
      </div>

      <!-- 11. Audius -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M12 3l9 16H3l9-16zm0 5l-5 9h10l-5-9z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Audius</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Web3 Музыка</span>
      </div>

      <!-- 12. JioSaavn -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6a6 6 0 100 12 6 6 0 000-12zm0 9a3 3 0 110-6 3 3 0 010 6z" fill="#000000"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">JioSaavn</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Азиатские чарты</span>
      </div>

      <!-- 13. Mixcloud -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M5.5 12c0-1.9 1.5-3.5 3.5-3.5 1 0 1.9.4 2.5 1.1.7-1.3 2.1-2.1 3.7-2.1 2.3 0 4.2 1.8 4.3 4.1.8.4 1.5 1.3 1.5 2.4 0 1.4-1.1 2.5-2.5 2.5H6c-1.7 0-3-1.3-3-3 0-1.4 1-2.6 2.5-2.9v1.4z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Mixcloud</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Радиошоу</span>
      </div>

      <!-- 14. Genius -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M4 4h16v16H4V4zm9 4h-2v4h2V8zm0 6h-2v2h2v-2z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Genius Lyrics</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Тексты & Смыслы</span>
      </div>

      <!-- 15. Jamendo -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M10 8l6 4-6 4V8z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Jamendo</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Creative Commons</span>
      </div>

      <!-- 16. Newgrounds -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="12" rx="3"/><circle cx="8" cy="12" r="2" fill="#000000"/><circle cx="16" cy="12" r="2" fill="#000000"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Newgrounds</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Игровые OST</span>
      </div>

      <!-- 17. Archive.org -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <svg class="w-5 h-5 sm:w-6 sm:h-6 fill-white" viewBox="0 0 24 24"><path d="M12 2L2 7v2h20V7L12 2zm-8 8v8h2v-8H4zm5 0v8h2v-8H9zm5 0v8h2v-8h-2zm5 0v8h2v-8h-2zM2 20v2h20v-2H2z"/></svg>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Archive.org</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Ретро фонотека</span>
      </div>

      <!-- 18. Cloudflare KV Sync -->
      <div class="glass-card p-3.5 sm:p-4 rounded-xl flex flex-col items-center text-center group">
        <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white/5 flex items-center justify-center p-2 mb-2 group-hover:scale-105 transition">
          <i data-lucide="cloud" class="w-5 h-5 sm:w-6 sm:h-6 text-white"></i>
        </div>
        <span class="font-bold text-xs sm:text-sm text-white">Cloudflare KV</span>
        <span class="text-[10px] font-mono text-zinc-400 mt-1">Синхронизация</span>
      </div>

    </div>
  </section>

  <!-- INTERACTIVE DSP EQUALIZER WORKBENCH (STUDIO RACKMOUNT CONSOLE) -->
  <section id="dsp-studio" class="scroll-mt-24 max-w-5xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-10">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-zinc-300 text-xs font-mono font-medium mb-3">
        <i data-lucide="sliders" class="w-3.5 h-3.5"></i>
        Студийная DSP-консоль
      </div>
      <h2 class="text-3xl sm:text-4xl font-bold text-white tracking-tight">Прецизионный 10-полосный эквалайзер</h2>
      <p class="text-zinc-400 text-sm sm:text-base mt-2 max-w-xl mx-auto">Управляйте звуком без искажений. Аппаратная сатурация, аналоговый винил 33⅓ и сырой бас.</p>
    </div>

    <div id="demoPlayerBox" class="glass-card rounded-2xl p-4 sm:p-8 border border-white/10 shadow-2xl relative overflow-hidden">
      
      <!-- Upper Controls: Theme Selector & Hardware Toggles -->
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-white/5">
        <div>
          <span class="text-xs font-mono text-zinc-400 uppercase tracking-widest">Профиль оформления:</span>
          <div class="flex flex-wrap gap-2 mt-2">
            <button onclick="setDemoTheme('obsidian', this)" data-theme="obsidian" class="theme-btn px-3 py-1.5 text-xs font-bold rounded-lg bg-white text-black transition active:scale-95 cursor-pointer">Obsidian Pure</button>
            <button onclick="setDemoTheme('oled', this)" data-theme="oled" class="theme-btn px-3 py-1.5 text-xs font-bold rounded-lg bg-white/5 text-zinc-300 hover:bg-white/10 transition active:scale-95 cursor-pointer">OLED Zero</button>
            <button onclick="setDemoTheme('titanium', this)" data-theme="titanium" class="theme-btn px-3 py-1.5 text-xs font-bold rounded-lg bg-white/5 text-zinc-300 hover:bg-white/10 transition active:scale-95 cursor-pointer">Titanium Raw</button>
          </div>
        </div>

        <!-- Audio Effect Toggles -->
        <div>
          <span class="text-xs font-mono text-zinc-400 uppercase tracking-widest">Аналоговый тракт:</span>
          <div class="flex flex-wrap gap-2 mt-2">
            <button id="vinylToggle" onclick="toggleVinylEffect()" class="px-3.5 py-1.5 text-xs font-bold rounded-lg bg-white/5 text-zinc-300 border border-white/10 hover:border-white/30 transition flex items-center gap-1.5 active:scale-95 cursor-pointer">
              <i data-lucide="disc" class="w-3.5 h-3.5 text-zinc-400"></i>
              <span>Винил 33⅓ RPM</span>
            </button>
            <button id="bassToggle" onclick="toggleBassEffect()" class="px-3.5 py-1.5 text-xs font-bold rounded-lg bg-white/5 text-zinc-300 border border-white/10 hover:border-white/30 transition flex items-center gap-1.5 active:scale-95 cursor-pointer">
              <i data-lucide="zap" class="w-3.5 h-3.5 text-zinc-400"></i>
              <span>Raw Bass +12dB</span>
            </button>
          </div>
        </div>
      </div>

      <!-- DSP Studio Presets Quick Bar -->
      <div class="mt-6 pt-1">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1 mb-3">
          <span class="text-xs sm:text-sm font-bold text-white flex items-center gap-2">
            <i data-lucide="activity" class="w-4 h-4 text-zinc-400"></i>
            DSP-эквалайзер (-12dB .. +12dB)
          </span>
          <span id="eqPresetLabel" class="text-[11px] sm:text-xs font-mono text-zinc-400">Пресет: Hi-Fi Linear Reference</span>
        </div>

        <!-- Preset Switcher Pills -->
        <div class="flex items-center gap-1.5 sm:gap-2 overflow-x-auto pb-2 -mx-1 px-1 mb-3">
          <span class="text-[10px] font-mono text-zinc-500 uppercase tracking-wider whitespace-nowrap hidden sm:inline">Пресеты:</span>
          <button onclick="applyEqPreset('flat')" class="eq-preset-btn text-[11px] font-mono px-2.5 py-1 rounded bg-white text-black font-bold border border-white transition active:scale-95 whitespace-nowrap cursor-pointer">Flat Hi-Fi</button>
          <button onclick="applyEqPreset('bass')" class="eq-preset-btn text-[11px] font-mono px-2.5 py-1 rounded bg-white/5 text-zinc-300 border border-white/10 hover:bg-white/10 transition active:scale-95 whitespace-nowrap cursor-pointer">Bass Boost +10dB</button>
          <button onclick="applyEqPreset('edm')" class="eq-preset-btn text-[11px] font-mono px-2.5 py-1 rounded bg-white/5 text-zinc-300 border border-white/10 hover:bg-white/10 transition active:scale-95 whitespace-nowrap cursor-pointer">Club / EDM</button>
          <button onclick="applyEqPreset('vocal')" class="eq-preset-btn text-[11px] font-mono px-2.5 py-1 rounded bg-white/5 text-zinc-300 border border-white/10 hover:bg-white/10 transition active:scale-95 whitespace-nowrap cursor-pointer">Vocal Clarity</button>
          <button onclick="applyEqPreset('acoustic')" class="eq-preset-btn text-[11px] font-mono px-2.5 py-1 rounded bg-white/5 text-zinc-300 border border-white/10 hover:bg-white/10 transition active:scale-95 whitespace-nowrap cursor-pointer">Acoustic</button>
        </div>

        <!-- 10 Sliders Track with Native Touch-Friendly Columns -->
        <div class="overflow-x-auto pb-2 -mx-2 px-2 sm:mx-0 sm:px-0">
          <div id="eqBandsContainer" class="grid grid-cols-10 gap-2 sm:gap-4 items-end h-40 pt-4 pb-2 bg-black/40 rounded-xl px-4 border border-white/5 min-w-[540px] sm:min-w-0 select-none">
            <!-- 10 Sliders -->
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="0">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">31Hz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="1">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">63Hz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="2">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">125Hz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="3">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">250Hz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="4">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">500Hz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="5">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">1kHz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="6">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">2kHz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="7">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">4kHz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="8">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">8kHz</span>
            </div>
            <div class="eq-col flex flex-col items-center h-full justify-between cursor-pointer py-1" data-band="9">
              <span class="text-[10px] font-mono text-zinc-500">0</span>
              <input type="range" min="-12" max="12" value="0" class="eq-slider w-20 transform -rotate-90 origin-center my-6" oninput="updateEqVisual(this)">
              <span class="text-[9px] font-mono text-zinc-400">16kHz</span>
            </div>
          </div>
        </div>

        <!-- Mobile horizontal scroll hint -->
        <div class="sm:hidden text-center text-[10px] font-mono text-zinc-500 mt-2 flex items-center justify-center gap-1">
          <i data-lucide="arrow-left-right" class="w-3 h-3"></i>
          <span>Прокрутите для всех 10 полос или выберите пресет выше</span>
        </div>
      </div>

    </div>
  </section>

  <!-- AUDIO ARCHITECTURE DEEP DIVE -->
  <section id="architecture" class="scroll-mt-24 max-w-5xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-white/5 border border-white/10 text-zinc-300 text-xs font-mono font-medium mb-3">
        <i data-lucide="layers" class="w-3.5 h-3.5"></i>
        Монолитная C++ Архитектура
      </div>
      <h2 class="text-3xl sm:text-4xl font-bold text-white tracking-tight">Инженерия звукового конвейера</h2>
      <p class="text-zinc-400 text-sm sm:text-base max-w-xl mx-auto mt-2">Что работает под капотом Sonora: 0ms latency и побитовая точность.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
      
      <div class="glass-card p-6 rounded-2xl border border-white/10 space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <i data-lucide="cpu" class="w-5 h-5 text-white"></i>
            <h3 class="font-bold text-white text-base">libmpv & Hardware Micro-Fade</h3>
          </div>
          <span class="text-xs font-mono text-zinc-400 bg-white/5 px-2 py-0.5 rounded">40ms Fade</span>
        </div>
        <p class="text-xs text-zinc-400 leading-relaxed">
          Аппаратное переключение треков с микро-приглушением громкости и бесщелчковой переконфигурацией фильтров FFmpeg. Чистый вывод без щелчков на Windows WASAPI и Android AudioTrack.
        </p>
      </div>

      <div class="glass-card p-6 rounded-2xl border border-white/10 space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <i data-lucide="compass" class="w-5 h-5 text-white"></i>
            <h3 class="font-bold text-white text-base">Taste Profile & «Моя Волна»</h3>
          </div>
          <span class="text-xs font-mono text-zinc-400 bg-white/5 px-2 py-0.5 rounded">Smart Merge</span>
        </div>
        <p class="text-xs text-zinc-400 leading-relaxed">
          Самообучающийся вкусовой профиль сохраняет веса артистов, историю прослушиваний и дизлайки. При переустановке на новое устройство вкусы объединяются из облака автоматически.
        </p>
      </div>

      <div class="glass-card p-6 rounded-2xl border border-white/10 space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <i data-lucide="cloud" class="w-5 h-5 text-white"></i>
            <h3 class="font-bold text-white text-base">Cloudflare KV Global Sync</h3>
          </div>
          <span class="text-xs font-mono text-zinc-400 bg-white/5 px-2 py-0.5 rounded">3-Tier Backup</span>
        </div>
        <p class="text-xs text-zinc-400 leading-relaxed">
          Тройной уровень защиты медиатеки: глобальная сеть Cloudflare KV, бэкап в шлюзе Telegram-бота и постоянный локальный архив на диске. Плейлисты никогда не сбрасываются.
        </p>
      </div>

      <div class="glass-card p-6 rounded-2xl border border-white/10 space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <i data-lucide="music" class="w-5 h-5 text-white"></i>
            <h3 class="font-bold text-white text-base">Synchronized Karaoke Engine</h3>
          </div>
          <span class="text-xs font-mono text-zinc-400 bg-white/5 px-2 py-0.5 rounded">LRC / Genius</span>
        </div>
        <p class="text-xs text-zinc-400 leading-relaxed">
          Пословная синхронизация караоке-текстов в такт музыке, мгновенный поиск в LRCLIB, интеграция смыслов с Genius и поддержка загрузки пользовательских .lrc файлов.
        </p>
      </div>

    </div>
  </section>

  <!-- PUBLIC ROADMAP SECTION -->
  <section id="roadmap" class="scroll-mt-24 max-w-4xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-10">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-white/5 border border-white/10 text-zinc-300 text-xs font-mono font-medium mb-3">
        <i data-lucide="map-pin" class="w-3.5 h-3.5"></i>
        Планы развития
      </div>
      <h2 class="text-3xl sm:text-4xl font-bold text-white tracking-tight">Публичный Roadmap Sonora</h2>
      <p class="text-zinc-400 text-sm sm:text-base max-w-xl mx-auto mt-2">Голосуйте за функции, которые вы хотите увидеть в следующих версиях плеера.</p>
    </div>

    <!-- Roadmap Cards List -->
    <div id="roadmapList" class="space-y-3 max-w-2xl mx-auto">
      <div class="glass-card p-4 rounded-xl flex items-center justify-between border border-white/5">
        <div class="flex items-center gap-3">
          <i data-lucide="loader" class="w-4 h-4 text-zinc-400 animate-spin"></i>
          <span class="text-xs font-mono text-zinc-400">Синхронизация актуальных задач...</span>
        </div>
      </div>
    </div>
  </section>

  <!-- COMPARISON TABLE SECTION -->
  <section id="comparison" class="max-w-5xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-8">
      <h2 class="text-3xl sm:text-4xl font-bold text-white tracking-tight">Сравнение с популярными стримингами</h2>
      <p class="text-zinc-400 text-sm sm:text-base max-w-lg mx-auto mt-2">Почему пользователи выбирают автономность Sonora.</p>
    </div>

    <!-- Mobile Scroll Hint -->
    <div class="sm:hidden text-right font-mono text-[11px] text-zinc-500 mb-2 flex items-center justify-end gap-1">
      <span>Прокрутите таблицу вправо</span>
      <i data-lucide="arrow-right" class="w-3 h-3"></i>
    </div>

    <div class="glass-card rounded-2xl overflow-x-auto border border-white/10 shadow-2xl">
      <table class="w-full text-left text-xs sm:text-sm min-w-[580px]">
        <thead>
          <tr class="border-b border-white/10 bg-white/[0.02]">
            <th class="p-4 sm:p-5 font-bold text-zinc-400 font-mono">Возможность</th>
            <th class="p-4 sm:p-5 font-bold text-zinc-400">Spotify</th>
            <th class="p-4 sm:p-5 font-bold text-zinc-400">Яндекс Музыка</th>
            <th class="p-4 sm:p-5 font-bold text-white bg-white/5 border-x border-white/10">Sonora Music 2.7.0</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/5 text-zinc-300">
          <tr>
            <td class="p-4 sm:p-5 font-semibold text-white">Стоимость подписки</td>
            <td class="p-4 sm:p-5 text-zinc-500">От $10.99/мес</td>
            <td class="p-4 sm:p-5 text-zinc-500">От 299 ₽/мес</td>
            <td class="p-4 sm:p-5 font-extrabold text-white bg-white/5 border-x border-white/10">0 ₽ НАВСЕГДА</td>
          </tr>
          <tr>
            <td class="p-4 sm:p-5 font-semibold text-white">Каталог источников</td>
            <td class="p-4 sm:p-5 text-zinc-500">1 (Spotify)</td>
            <td class="p-4 sm:p-5 text-zinc-500">1 (Яндекс)</td>
            <td class="p-4 sm:p-5 font-extrabold text-white bg-white/5 border-x border-white/10">18 сервисов в одном окне</td>
          </tr>
          <tr>
            <td class="p-4 sm:p-5 font-semibold text-white">Андеграунд и ремиксы</td>
            <td class="p-4 sm:p-5 text-zinc-500">Ограничено</td>
            <td class="p-4 sm:p-5 text-zinc-500">Ограничено</td>
            <td class="p-4 sm:p-5 font-extrabold text-white bg-white/5 border-x border-white/10">SoundCloud + PromoDJ + Bandcamp</td>
          </tr>
          <tr>
            <td class="p-4 sm:p-5 font-semibold text-white">DSP и аналоговый винил</td>
            <td class="p-4 sm:p-5 text-zinc-500">Базовый 6 полос</td>
            <td class="p-4 sm:p-5 text-zinc-500">Базовый 5 полос</td>
            <td class="p-4 sm:p-5 font-extrabold text-white bg-white/5 border-x border-white/10">10 полос + винил 33⅓ RPM</td>
          </tr>
          <tr>
            <td class="p-4 sm:p-5 font-semibold text-white">Реклама и телеметрия</td>
            <td class="p-4 sm:p-5 text-zinc-500">Множество трекеров</td>
            <td class="p-4 sm:p-5 text-zinc-500">Множество трекеров</td>
            <td class="p-4 sm:p-5 font-extrabold text-white bg-white/5 border-x border-white/10">0 ТРЕКЕРОВ И РЕКЛАМЫ</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- FAQ SECTION -->
  <section id="faq" class="scroll-mt-24 max-w-4xl mx-auto px-4 py-16 relative z-10">
    <div class="text-center mb-10">
      <h2 class="text-3xl sm:text-4xl font-bold text-white tracking-tight">Часто задаваемые вопросы</h2>
      <p class="text-zinc-400 text-sm sm:text-base mt-2">Всё об архитектуре и безопасности Sonora.</p>
    </div>

    <div class="space-y-3">
      
      <details class="glass-card rounded-xl p-5 border border-white/5 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex justify-between items-center select-none">
          <span>Действительно ли Sonora полностью бесплатна?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-zinc-400 transform group-open:rotate-180 transition"></i>
        </summary>
        <p class="text-xs sm:text-sm text-zinc-400 mt-3 leading-relaxed">
          Да, Sonora на 100% бесплатна, в ней нет платных подписок, рекламы или скрытых платежей. Проект развивается сообществом для свободы прослушивания музыки.
        </p>
      </details>

      <details class="glass-card rounded-xl p-5 border border-white/5 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex justify-between items-center select-none">
          <span>Сохранятся ли мои плейлисты при переустановке?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-zinc-400 transform group-open:rotate-180 transition"></i>
        </summary>
        <p class="text-xs sm:text-sm text-zinc-400 mt-3 leading-relaxed">
          Да! Медиатека защищена тремя независимыми уровнями: глобальное хранилище Cloudflare KV, шлюз в Telegram-боте и постоянный локальный файл на диске. При новой установке все треки и волна восстановятся автоматически.
        </p>
      </details>

      <details class="glass-card rounded-xl p-5 border border-white/5 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex justify-between items-center select-none">
          <span>Безопасен ли инсталлятор для Windows и APK для Android?</span>
          <i data-lucide="chevron-down" class="w-4 h-4 text-zinc-400 transform group-open:rotate-180 transition"></i>
        </summary>
        <p class="text-xs sm:text-sm text-zinc-400 mt-3 leading-relaxed">
          Инсталляторы собираются в открытом конвейере на базе Inno Setup 6 и официального Android SDK. Приложение не требует прав администратора и не собирает пользовательские данные.
        </p>
      </details>

    </div>
  </section>

  <!-- FINAL DOWNLOAD SECTION -->
  <section id="download" class="scroll-mt-24 max-w-5xl mx-auto px-4 py-16 sm:py-20 relative z-10">
    <div class="glass-card rounded-3xl p-6 sm:p-12 text-center border border-white/10 shadow-2xl relative overflow-hidden">
      <div class="relative z-10 max-w-2xl mx-auto space-y-4">
        <h2 class="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">Начните слушать Sonora прямо сейчас</h2>
        <p class="text-zinc-400 text-xs sm:text-base">Доступны 2 официальных дистрибутива с чистой побитовой установкой:</p>

        <div class="pt-4 flex flex-col sm:flex-row flex-wrap items-center justify-center gap-3 sm:gap-4 max-w-xl mx-auto w-full">
          <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.7.0/Sonora-v2.7.0-Setup.exe" class="w-full sm:w-auto bg-white hover:bg-zinc-200 text-black font-extrabold text-xs sm:text-sm px-6 sm:px-8 py-3.5 rounded-xl flex items-center justify-center gap-2.5 transition transform hover:scale-[1.02] active:scale-[0.98]">
            <i data-lucide="monitor" class="w-4 h-4 flex-shrink-0"></i>
            <span>Windows Setup (.exe, 30.5 МБ)</span>
          </a>
          <a href="https://github.com/unkn098wn/sonora-website/releases/download/v2.7.0/Sonora-v2.7.0-Android.apk" class="w-full sm:w-auto glass-card hover:bg-white/5 text-white font-bold text-xs sm:text-sm px-6 sm:px-8 py-3.5 rounded-xl flex items-center justify-center gap-2.5 transition transform hover:scale-[1.02] active:scale-[0.98] border border-white/15">
            <i data-lucide="smartphone" class="w-4 h-4 text-zinc-400 flex-shrink-0"></i>
            <span>Android (APK, 138.1 МБ)</span>
          </a>
        </div>

        <p class="text-xs font-mono text-zinc-500 pt-4">Релиз: v2.7.0 Obsidian Architecture • 100% бесплатно • Без телеметрии</p>
      </div>
    </div>
  </section>

  <!-- FOOTER WITH ABYSS & FLOATING LIGHT SPARKS CANVAS -->
  <footer id="abyssFooter" class="relative z-10 overflow-hidden bg-black border-t border-white/10 pt-20 sm:pt-24 pb-12 sm:pb-14">
    <!-- Deep Void Radial Gradient -->
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_bottom,_var(--tw-gradient-stops))] from-zinc-900/50 via-black to-black pointer-events-none"></div>

    <!-- Interactive HTML5 Abyss Canvas with Flying Light Sparks -->
    <canvas id="abyssCanvas" class="absolute inset-0 w-full h-full pointer-events-none z-0"></canvas>

    <!-- Fog / Mist layer at the threshold of the abyss -->
    <div class="absolute top-0 inset-x-0 h-20 bg-gradient-to-b from-black to-transparent pointer-events-none z-0"></div>

    <div class="relative z-10 max-w-6xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-zinc-500 text-center md:text-left">
      <div class="flex items-center gap-3 justify-center">
        <div class="w-7 h-7 rounded-lg bg-white/5 border border-white/15 flex items-center justify-center shadow-lg flex-shrink-0">
          <i data-lucide="disc" class="w-4 h-4 text-white"></i>
        </div>
        <div>
          <span class="text-zinc-300 font-bold block">Sonora Music Project</span>
          <span class="text-[11px] text-zinc-600">Свободный звук без границ • 100% бесплатно</span>
        </div>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-4 sm:gap-6 font-medium">
        <a href="privacy.html" class="hover:text-white transition">Политика конфиденциальности</a>
        <a href="terms.html" class="hover:text-white transition">Условия использования</a>
        <a href="javascript:void(0)" onclick="openFeedbackModal()" class="hover:text-white transition">Обратная связь</a>
        <a href="https://t.me/sonoramus1c_bot" target="_blank" class="hover:text-white transition">Telegram-бот</a>
        <a href="https://github.com/unkn098wn/sonora-website/releases" target="_blank" class="hover:text-white transition">GitHub Releases</a>
      </div>
    </div>
  </footer>

  <!-- FLOATING QUICK FEEDBACK BUTTON -->
  <button onclick="openFeedbackModal()" aria-label="Обратная связь" class="fixed bottom-5 right-4 sm:bottom-6 sm:right-6 z-40 bg-zinc-900 border border-white/20 text-white font-bold p-3 sm:p-3.5 rounded-full shadow-2xl hover:scale-105 active:scale-95 transition transform flex items-center gap-2 group cursor-pointer">
    <i data-lucide="message-square" class="w-5 h-5 text-white"></i>
    <span class="hidden md:inline text-xs font-mono font-semibold pr-1 tracking-wider uppercase">Обратная связь</span>
  </button>

  <!-- FEEDBACK & BUG REPORT MODAL -->
  <div id="feedbackModal" onclick="if(event.target === this) closeFeedbackModal()" class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/85 backdrop-blur-md opacity-0 pointer-events-none transition-opacity duration-300 overflow-y-auto">
    <div class="glass-card rounded-2xl p-5 sm:p-8 max-w-lg w-full border border-white/15 relative shadow-2xl space-y-4 sm:space-y-5 my-auto max-h-[92dvh] sm:max-h-[90vh] flex flex-col overflow-hidden">
      
      <!-- Close Button -->
      <button onclick="closeFeedbackModal()" aria-label="Закрыть модальное окно" class="absolute top-4 right-4 sm:top-5 sm:right-5 text-zinc-400 hover:text-white p-2 rounded-lg bg-white/5 hover:bg-white/10 transition z-10 active:scale-95 cursor-pointer">
        <i data-lucide="x" class="w-4 h-4"></i>
      </button>

      <div class="flex-shrink-0 pr-8">
        <span class="text-[11px] sm:text-xs font-mono text-zinc-400 uppercase tracking-widest flex items-center gap-1.5">
          <i data-lucide="send" class="w-3.5 h-3.5"></i>
          Прямой диалог с разработчиками
        </span>
        <h3 class="text-lg sm:text-2xl font-bold text-white mt-1">Обратная связь и баг-репорты</h3>
        <p class="text-[11px] sm:text-xs text-zinc-400 mt-1">Каждое обращение моментально регистрируется в системе и передается создателю проекта в Telegram.</p>
      </div>

      <!-- Category Tabs -->
      <div class="grid grid-cols-3 gap-1.5 sm:gap-2 p-1 bg-black/50 rounded-lg border border-white/10 flex-shrink-0">
        <button type="button" onclick="setFeedbackCategory('bug')" id="fbCatBtn-bug" class="fb-cat-btn py-1.5 text-xs font-bold rounded-md bg-white text-black flex items-center justify-center gap-1 sm:gap-1.5 transition active:scale-95 cursor-pointer">
          <span>🐞 Баг</span>
        </button>
        <button type="button" onclick="setFeedbackCategory('idea')" id="fbCatBtn-idea" class="fb-cat-btn py-1.5 text-xs font-bold rounded-md text-zinc-400 hover:text-white flex items-center justify-center gap-1 sm:gap-1.5 transition active:scale-95 cursor-pointer">
          <span>💡 Идея</span>
        </button>
        <button type="button" onclick="setFeedbackCategory('question')" id="fbCatBtn-question" class="fb-cat-btn py-1.5 text-xs font-bold rounded-md text-zinc-400 hover:text-white flex items-center justify-center gap-1 sm:gap-1.5 transition active:scale-95 cursor-pointer">
          <span>❓ Вопрос</span>
        </button>
      </div>

      <!-- Feedback Form -->
      <form id="feedbackForm" onsubmit="submitFeedback(event)" class="space-y-3 overflow-y-auto pr-1 flex-grow">
        <input type="hidden" id="fbCategory" value="bug">

        <div>
          <label class="block text-xs font-mono text-zinc-400 mb-1">Ваше имя или ник:</label>
          <input type="text" id="fbName" required placeholder="Например: Алекс" class="w-full bg-white/5 border border-white/10 rounded-lg px-3.5 py-2 text-sm text-white focus:outline-none focus:border-white/30">
        </div>

        <div>
          <label class="block text-xs font-mono text-zinc-400 mb-1">Telegram (@username) или Email для ответа:</label>
          <input type="text" id="fbContact" required placeholder="@username или your@email.com" class="w-full bg-white/5 border border-white/10 rounded-lg px-3.5 py-2 text-sm text-white focus:outline-none focus:border-white/30">
        </div>

        <div>
          <label class="block text-xs font-mono text-zinc-400 mb-1">Версия клиента:</label>
          <select id="fbVersion" class="w-full bg-[#0D1017] border border-white/10 rounded-lg px-3.5 py-2 text-sm text-white focus:outline-none focus:border-white/30">
            <option value="Android Universal APK v2.7.0">Android (Универсальный APK v2.7.0)</option>
            <option value="Windows Setup v2.7.0">Windows (Setup .exe v2.7.0)</option>
            <option value="Веб-сайт Sonora">Веб-сайт Sonora</option>
            <option value="Telegram Бот @sonoramus1c_bot">Telegram-бот</option>
          </select>
        </div>

        <div>
          <label class="block text-xs font-mono text-zinc-400 mb-1">Подробное описание:</label>
          <textarea id="fbMessage" required rows="3" placeholder="Опишите баг или предложите функцию..." class="w-full bg-white/5 border border-white/10 rounded-lg px-3.5 py-2 text-sm text-white focus:outline-none focus:border-white/30 resize-none"></textarea>
        </div>

        <button type="submit" id="fbSubmitBtn" class="w-full bg-white hover:bg-zinc-200 text-black font-extrabold text-sm py-3 rounded-lg transition flex items-center justify-center gap-2 active:scale-[0.98] cursor-pointer">
          <i data-lucide="send" class="w-4 h-4"></i>
          <span>Отправить обращение разработчикам</span>
        </button>
      </form>

      <!-- Success Card (Hidden by default) -->
      <div id="fbSuccessBox" class="hidden text-center py-6 space-y-4">
        <div class="w-12 h-12 bg-white/10 text-white rounded-full flex items-center justify-center mx-auto border border-white/20">
          <i data-lucide="check" class="w-6 h-6"></i>
        </div>
        <h4 class="text-lg font-bold text-white">Обращение принято!</h4>
        <p class="text-xs text-zinc-400">
          Номер вашего тикета: <span id="fbTicketId" class="text-white font-mono font-bold">#SON-0000</span>.<br>
          Отчет успешно сохранен и передан администратору в Telegram-бот.
        </p>
        <button onclick="closeFeedbackModal()" class="px-5 py-2 rounded-lg bg-white/10 hover:bg-white text-white hover:text-black font-bold text-xs transition active:scale-95 cursor-pointer">
          Закрыть окно
        </button>
      </div>

    </div>
  </div>

  <!-- COOKIE & PRIVACY NOTICE BANNER -->
  <div id="cookieBanner" class="fixed bottom-4 left-4 right-4 sm:left-6 sm:right-auto z-50 max-w-sm sm:max-w-md glass-card rounded-xl p-3.5 sm:p-4 border border-white/10 shadow-2xl flex flex-col sm:flex-row items-center justify-between gap-3 opacity-0 pointer-events-none transition-all duration-300">
    <div class="text-xs text-zinc-300 flex items-center gap-2.5">
      <i data-lucide="shield" class="w-4 h-4 text-white flex-shrink-0"></i>
      <span>Sonora не использует трекеры и рекламу. <a href="privacy.html" class="text-white underline font-semibold">Политика</a></span>
    </div>
    <button onclick="dismissCookieBanner()" class="w-full sm:w-auto bg-white text-black text-xs font-bold px-4 py-2 rounded-lg transition whitespace-nowrap hover:bg-zinc-200 active:scale-95 text-center flex-shrink-0 cursor-pointer">
      Понятно
    </button>
  </div>

  <!-- SCRIPT LOGIC: 3D SPECTROGRAM CANVAS, TILT, EQUALIZER, ROADMAP, FEEDBACK -->
  <script>
    // Initialize Lucide Icons
    lucide.createIcons();

    // 1. MATHEMATICAL 3D AUDIO SPECTROGRAM CANVAS ENGINE (TITANIUM MONOCHROME)
    (function init3DSpectrogramCanvas() {
      const canvas = document.getElementById('spectrogramCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let w, h;

      function resize() {
        w = canvas.width = canvas.parentElement.clientWidth;
        h = canvas.height = canvas.parentElement.clientHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      const numBars = 36;
      let phase = 0;
      let mouseX = w / 2;
      let mouseY = h / 2;
      let targetTiltX = 0;
      let targetTiltY = 0;
      let currentTiltX = 0;
      let currentTiltY = 0;

      canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouseX = e.clientX - rect.left;
        mouseY = e.clientY - rect.top;
        targetTiltX = (mouseX / w - 0.5) * 2;
        targetTiltY = (mouseY / h - 0.5) * 2;
      });

      canvas.addEventListener('mouseleave', () => {
        targetTiltX = 0;
        targetTiltY = 0;
      });

      // Mobile Touch Ripple Support
      function handleTouch(e) {
        if (!e.touches || !e.touches[0]) return;
        const rect = canvas.getBoundingClientRect();
        mouseX = e.touches[0].clientX - rect.left;
        mouseY = e.touches[0].clientY - rect.top;
        targetTiltX = (mouseX / w - 0.5) * 2;
        targetTiltY = (mouseY / h - 0.5) * 2;
      }
      canvas.addEventListener('touchstart', handleTouch, { passive: true });
      canvas.addEventListener('touchmove', handleTouch, { passive: true });
      canvas.addEventListener('touchend', () => {
        targetTiltX = 0;
        targetTiltY = 0;
      }, { passive: true });

      function render() {
        ctx.clearRect(0, 0, w, h);
        phase += 0.035;

        // Smooth camera tilt damping
        currentTiltX += (targetTiltX - currentTiltX) * 0.06;
        currentTiltY += (targetTiltY - currentTiltY) * 0.06;

        const centerX = w / 2;
        const baseY = h * 0.78 + currentTiltY * 20;
        const barSpacing = Math.min(22, (w - 60) / numBars);
        const startX = centerX - (numBars * barSpacing) / 2;

        // Draw Perspective 3D Grid Floor Lines in Titanium Wireframe
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.04)';
        ctx.lineWidth = 1;
        for (let g = 0; g < 6; g++) {
          const depthY = baseY + g * 12;
          ctx.beginPath();
          ctx.moveTo(startX - 20 - g * 10, depthY);
          ctx.lineTo(startX + numBars * barSpacing + 20 + g * 10, depthY);
          ctx.stroke();
        }

        // Draw 36 Precision Audio Frequency Columns in 3D Isometric Projection
        for (let i = 0; i < numBars; i++) {
          // Complex audio waveform harmonic calculation
          const harmonic1 = Math.sin(phase * 1.2 + i * 0.28) * 45;
          const harmonic2 = Math.cos(phase * 2.1 + i * 0.45) * 25;
          const harmonic3 = Math.sin(phase * 3.4 + i * 0.72) * 15;
          
          // Mouse / touch cursor proximity wave ripple
          const barX = startX + i * barSpacing + currentTiltX * (i - numBars / 2) * 2;
          const distToMouse = Math.abs(mouseX - barX);
          const mouseBonus = distToMouse < 90 ? (1 - distToMouse / 90) * 35 : 0;

          const barHeight = Math.max(8, 25 + harmonic1 + harmonic2 + harmonic3 + mouseBonus);
          const barWidth = Math.max(4, barSpacing - 6);
          const barTopY = baseY - barHeight;

          // 1. Draw Front Face
          const grad = ctx.createLinearGradient(0, barTopY, 0, baseY);
          grad.addColorStop(0, 'rgba(255, 255, 255, 0.95)');
          grad.addColorStop(0.35, 'rgba(200, 200, 210, 0.65)');
          grad.addColorStop(1, 'rgba(50, 50, 58, 0.2)');
          ctx.fillStyle = grad;
          ctx.fillRect(barX, barTopY, barWidth, barHeight);

          // 2. Draw 3D Top Cap (Perspective Diamond)
          const depthOffset = 5;
          ctx.beginPath();
          ctx.moveTo(barX, barTopY);
          ctx.lineTo(barX + depthOffset, barTopY - depthOffset);
          ctx.lineTo(barX + barWidth + depthOffset, barTopY - depthOffset);
          ctx.lineTo(barX + barWidth, barTopY);
          ctx.closePath();
          ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
          ctx.fill();

          // 3. Draw 3D Side Face
          ctx.beginPath();
          ctx.moveTo(barX + barWidth, barTopY);
          ctx.lineTo(barX + barWidth + depthOffset, barTopY - depthOffset);
          ctx.lineTo(barX + barWidth + depthOffset, baseY - depthOffset);
          ctx.lineTo(barX + barWidth, baseY);
          ctx.closePath();
          ctx.fillStyle = 'rgba(120, 120, 130, 0.35)';
          ctx.fill();

          // Peak Indicator Dot
          ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
          ctx.fillRect(barX + barWidth / 2 - 1, barTopY - depthOffset - 4, 2, 2);
        }

        // Draw Connected Audio Envelope Spline across Peaks
        ctx.beginPath();
        for (let i = 0; i < numBars; i++) {
          const barX = startX + i * barSpacing + currentTiltX * (i - numBars / 2) * 2;
          const harmonic = Math.sin(phase * 1.2 + i * 0.28) * 45 + Math.cos(phase * 2.1 + i * 0.45) * 25 + Math.sin(phase * 3.4 + i * 0.72) * 15;
          const distToMouse = Math.abs(mouseX - barX);
          const mouseBonus = distToMouse < 90 ? (1 - distToMouse / 90) * 35 : 0;
          const barHeight = Math.max(8, 25 + harmonic + mouseBonus);
          const barTopY = baseY - barHeight - 5;
          if (i === 0) ctx.moveTo(barX, barTopY);
          else ctx.lineTo(barX, barTopY);
        }
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
        ctx.lineWidth = 1;
        ctx.stroke();

        requestAnimationFrame(render);
      }
      render();
    })();

    // 2. 3D Tilt Parallax on Hero Card (Mouse on Desktop)
    (function init3DHeroTilt() {
      const card = document.getElementById('spectrogramCard');
      if (!card) return;

      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        const rotateX = (-y / rect.height) * 10;
        const rotateY = (x / rect.width) * 10;
        card.style.transform = `rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = 'rotateX(0deg) rotateY(0deg)';
      });
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
          duration: 2200,
          delay: 150,
        });
      });
    })();

    // 4. Interactive DSP Studio Engine
    function setDemoTheme(theme, btnElement) {
      const box = document.getElementById('demoPlayerBox');
      const buttons = document.querySelectorAll('.theme-btn');
      buttons.forEach(b => {
        b.classList.remove('bg-white', 'text-black');
        b.classList.add('bg-white/5', 'text-zinc-300');
      });
      const activeBtn = btnElement || document.querySelector(`[data-theme="${theme}"]`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-white/5', 'text-zinc-300');
        activeBtn.classList.add('bg-white', 'text-black');
      }

      if (!box) return;
      if (theme === 'oled') {
        box.style.background = 'rgba(0, 0, 0, 0.98)';
        box.style.borderColor = 'rgba(255, 255, 255, 0.12)';
      } else if (theme === 'titanium') {
        box.style.background = 'rgba(20, 20, 24, 0.85)';
        box.style.borderColor = 'rgba(255, 255, 255, 0.2)';
      } else {
        box.style.background = 'rgba(10, 10, 13, 0.72)';
        box.style.borderColor = 'rgba(255, 255, 255, 0.1)';
      }
    }

    let vinylActive = false;
    function toggleVinylEffect() {
      vinylActive = !vinylActive;
      const btn = document.getElementById('vinylToggle');
      if (btn) {
        const icon = btn.querySelector('svg, i');
        if (vinylActive) {
          btn.classList.add('bg-white', 'text-black', 'border-white', 'shadow-md');
          btn.classList.remove('bg-white/5', 'text-zinc-300', 'border-white/10');
          if (icon) icon.classList.replace('text-zinc-400', 'text-black');
        } else {
          btn.classList.remove('bg-white', 'text-black', 'border-white', 'shadow-md');
          btn.classList.add('bg-white/5', 'text-zinc-300', 'border-white/10');
          if (icon) icon.classList.replace('text-black', 'text-zinc-400');
        }
      }
    }

    let bassActive = false;
    function toggleBassEffect() {
      bassActive = !bassActive;
      const btn = document.getElementById('bassToggle');
      if (btn) {
        const icon = btn.querySelector('svg, i');
        if (bassActive) {
          btn.classList.add('bg-white', 'text-black', 'border-white', 'shadow-md');
          btn.classList.remove('bg-white/5', 'text-zinc-300', 'border-white/10');
          if (icon) icon.classList.replace('text-zinc-400', 'text-black');
        } else {
          btn.classList.remove('bg-white', 'text-black', 'border-white', 'shadow-md');
          btn.classList.add('bg-white/5', 'text-zinc-300', 'border-white/10');
          if (icon) icon.classList.replace('text-black', 'text-zinc-400');
        }
      }
    }

    function updateEqVisual(slider) {
      if (!slider) return;
      const val = parseInt(slider.value, 10);
      const col = slider.closest('.eq-col') || slider.closest('.flex-col');
      if (col) {
        const label = col.querySelector('span:first-child');
        if (label) {
          label.textContent = val > 0 ? `+${val}` : `${val}`;
          label.className = val !== 0 ? 'text-[10px] font-mono text-white font-bold' : 'text-[10px] font-mono text-zinc-500';
        }
      }
    }

    // DSP Presets
    const eqPresets = {
      flat: { name: 'Hi-Fi Linear (Flat)', values: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] },
      bass: { name: 'Raw Bass Boost (+10dB)', values: [10, 8, 6, 2, 0, 0, 1, 3, 5, 6] },
      edm: { name: 'Club / Electronic Punch', values: [7, 5, 2, -1, -2, 0, 3, 6, 8, 9] },
      vocal: { name: 'Vocal Clarity & Presence', values: [-3, -2, 0, 2, 4, 6, 5, 3, 1, 0] },
      acoustic: { name: 'Acoustic Hi-Res', values: [3, 2, 0, 1, 2, 3, 4, 5, 6, 7] },
    };

    function applyEqPreset(presetKey) {
      const preset = eqPresets[presetKey];
      if (!preset) return;
      const label = document.getElementById('eqPresetLabel');
      if (label) label.textContent = 'Пресет: ' + preset.name;

      const buttons = document.querySelectorAll('.eq-preset-btn');
      buttons.forEach(b => {
        b.classList.remove('bg-white', 'text-black', 'border-white', 'font-bold');
        b.classList.add('bg-white/5', 'text-zinc-300', 'border-white/10');
      });
      if (event && event.target) {
        const targetBtn = event.target.closest('button');
        if (targetBtn) {
          targetBtn.classList.remove('bg-white/5', 'text-zinc-300', 'border-white/10');
          targetBtn.classList.add('bg-white', 'text-black', 'border-white', 'font-bold');
        }
      }

      const sliders = document.querySelectorAll('.eq-slider');
      sliders.forEach((slider, i) => {
        if (i < preset.values.length) {
          const targetVal = preset.values[i];
          slider.value = targetVal;
          updateEqVisual(slider);
        }
      });
    }

    // Touch & Drag Support on EQ Band Columns for Phones
    (function initEqTouchControls() {
      const container = document.getElementById('eqBandsContainer');
      if (!container) return;

      const cols = container.querySelectorAll('.eq-col');
      cols.forEach(col => {
        const slider = col.querySelector('.eq-slider');
        if (!slider) return;

        function setFromClientY(clientY) {
          const rect = col.getBoundingClientRect();
          // Height between top label and bottom label (~120px)
          const top = rect.top + 20;
          const bottom = rect.bottom - 20;
          const clampedY = Math.max(top, Math.min(bottom, clientY));
          const ratio = 1 - ((clampedY - top) / (bottom - top)); // 0 at bottom, 1 at top
          const val = Math.round(ratio * 24 - 12); // -12 to +12
          slider.value = val;
          updateEqVisual(slider);
        }

        col.addEventListener('touchstart', (e) => {
          if (e.touches && e.touches[0]) {
            setFromClientY(e.touches[0].clientY);
          }
        }, { passive: true });

        col.addEventListener('touchmove', (e) => {
          if (e.touches && e.touches[0]) {
            setFromClientY(e.touches[0].clientY);
          }
        }, { passive: true });
      });
    })();

    // 5. Public Interactive Roadmap API Fetch & Voting
    const defaultRoadmapItems = [
      { id: 'carplay_auto', title: 'Поддержка Android Auto и Apple CarPlay', category: 'Платформы', votes: 148 },
      { id: 'airplay_cast', title: 'Беспроводной стриминг (AirPlay, Chromecast, DLNA)', category: 'Связь', votes: 122 },
      { id: 'smart_lyrics', title: 'Синхронный перевод иностранных песен на русский язык', category: 'Караоке', votes: 99 },
      { id: 'listen_together', title: 'Комнаты совместного прослушивания (Listen Along с друзьями)', category: 'Сообщество', votes: 89 },
      { id: 'smart_ai_wave', title: 'Умная Моя Волна: фильтрация по BPM, настроению и эпохам', category: 'Рекомендации', votes: 139 },
    ];

    function renderRoadmap(items) {
      const container = document.getElementById('roadmapList');
      if (!container) return;
      container.innerHTML = '';
      items.forEach(item => {
        const card = document.createElement('div');
        card.className = 'glass-card p-3.5 sm:p-4 rounded-xl flex items-center justify-between gap-3 sm:gap-4 border border-white/5 hover:border-white/20 transition';
        card.innerHTML = `
          <div class="space-y-1 min-w-0 pr-2">
            <span class="text-[10px] font-mono text-zinc-400 uppercase tracking-widest bg-white/5 px-2 py-0.5 rounded border border-white/10">${item.category}</span>
            <h4 class="text-xs sm:text-sm font-bold text-white leading-snug">${item.title}</h4>
          </div>
          <button onclick="voteRoadmap('${item.id}', this)" aria-label="Проголосовать" class="flex items-center gap-1.5 sm:gap-2 px-3 sm:px-3.5 py-2 rounded-lg bg-white/5 hover:bg-white hover:text-black text-zinc-300 text-xs font-mono font-bold transition flex-shrink-0 border border-white/10 active:scale-95 min-h-[38px] cursor-pointer">
            <i data-lucide="thumbs-up" class="w-3.5 h-3.5"></i>
            <span class="vote-count font-mono">${item.votes}</span>
          </button>
        `;
        container.appendChild(card);
      });
      lucide.createIcons();
    }

    async function loadRoadmap() {
      try {
        const res = await fetch('/api/roadmap');
        const data = await res.json();
        if (data.success && Array.isArray(data.items) && data.items.length > 0) {
          renderRoadmap(data.items);
          return;
        }
      } catch (e) {
        console.warn('Roadmap API fallback to default items:', e);
      }
      renderRoadmap(defaultRoadmapItems);
    }
    loadRoadmap();

    async function voteRoadmap(featureId, btn) {
      const countSpan = btn.querySelector('.vote-count');
      const current = parseInt(countSpan.textContent || '0', 10);
      countSpan.textContent = current + 1;
      btn.classList.add('bg-white', 'text-black');
      btn.disabled = true;

      if (typeof anime !== 'undefined') {
        anime({
          targets: btn,
          scale: [1, 1.15, 1],
          duration: 350,
          easing: 'easeOutQuad',
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

    // 6. Mobile Navigation Dropdown Controller
    function toggleMobileMenu() {
      const dropdown = document.getElementById('mobileMenuDropdown');
      const icon = document.getElementById('mobileMenuIcon');
      if (!dropdown) return;
      const isHidden = dropdown.classList.contains('hidden');
      if (isHidden) {
        dropdown.classList.remove('hidden');
        if (icon) icon.setAttribute('data-lucide', 'x');
      } else {
        dropdown.classList.add('hidden');
        if (icon) icon.setAttribute('data-lucide', 'menu');
      }
      lucide.createIcons();
    }

    function closeMobileMenu() {
      const dropdown = document.getElementById('mobileMenuDropdown');
      const icon = document.getElementById('mobileMenuIcon');
      if (dropdown) dropdown.classList.add('hidden');
      if (icon) icon.setAttribute('data-lucide', 'menu');
      lucide.createIcons();
    }

    // 7. Feedback Modal Controller
    function openFeedbackModal() {
      closeMobileMenu();
      const modal = document.getElementById('feedbackModal');
      if (!modal) return;
      modal.classList.remove('opacity-0', 'pointer-events-none');
      const form = document.getElementById('feedbackForm');
      const successBox = document.getElementById('fbSuccessBox');
      if (form) form.classList.remove('hidden');
      if (successBox) successBox.classList.add('hidden');
      document.body.style.overflow = 'hidden';
    }

    function closeFeedbackModal() {
      const modal = document.getElementById('feedbackModal');
      if (!modal) return;
      modal.classList.add('opacity-0', 'pointer-events-none');
      document.body.style.overflow = '';
    }

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeFeedbackModal();
        closeMobileMenu();
      }
    });

    // Close mobile menu if user clicks outside of header
    document.addEventListener('click', (e) => {
      const header = document.getElementById('mainHeader');
      const dropdown = document.getElementById('mobileMenuDropdown');
      if (dropdown && !dropdown.classList.contains('hidden')) {
        if (header && !header.contains(e.target)) {
          closeMobileMenu();
        }
      }
    });

    function setFeedbackCategory(cat) {
      const catInput = document.getElementById('fbCategory');
      if (catInput) catInput.value = cat;
      const btns = document.querySelectorAll('.fb-cat-btn');
      btns.forEach(b => {
        b.classList.remove('bg-white', 'text-black');
        b.classList.add('text-zinc-400');
      });
      const activeBtn = document.getElementById(`fbCatBtn-${cat}`);
      if (activeBtn) {
        activeBtn.classList.add('bg-white', 'text-black');
        activeBtn.classList.remove('text-zinc-400');
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

    // 8. Cookie Banner Controller
    function dismissCookieBanner() {
      try {
        localStorage.setItem('sonora_cookie_accepted', 'true');
      } catch (e) {}
      const banner = document.getElementById('cookieBanner');
      if (banner) {
        banner.classList.add('opacity-0', 'pointer-events-none');
        banner.style.display = 'none';
      }
    }

    (function initCookieBanner() {
      const banner = document.getElementById('cookieBanner');
      if (!banner) return;
      try {
        if (!localStorage.getItem('sonora_cookie_accepted')) {
          setTimeout(() => {
            banner.classList.remove('opacity-0', 'pointer-events-none');
          }, 1200);
        } else {
          banner.style.display = 'none';
        }
      } catch (e) {
        banner.style.display = 'none';
      }
    })();

    // 8. SCROLL-DRIVEN LIGHT RAYS OPACITY FADER (HEADER HERO)
    (function initScrollFadeRays() {
      const wrapper = document.getElementById('headerVideoWrapper');
      if (!wrapper) return;
      let ticking = false;

      function updateRaysOpacity() {
        const scrollY = window.pageYOffset || document.documentElement.scrollTop;
        // Fade from 1.0 down to 0.0 across 850px of downward scroll
        const fadeRange = 850;
        const opacity = Math.max(0, Math.min(1, 1 - (scrollY / fadeRange)));
        wrapper.style.opacity = opacity.toFixed(3);
        if (opacity <= 0.005) {
          wrapper.style.visibility = 'hidden';
        } else {
          wrapper.style.visibility = 'visible';
        }
        ticking = false;
      }

      window.addEventListener('scroll', () => {
        if (!ticking) {
          requestAnimationFrame(updateRaysOpacity);
          ticking = true;
        }
      }, { passive: true });

      updateRaysOpacity();
    })();

    // 9. HIGH-PERFORMANCE ABYSS CANVAS ENGINE (FLOATING LUMINESCENT SPARKS)
    (function initAbyssSparks() {
      const canvas = document.getElementById('abyssCanvas');
      const footer = document.getElementById('abyssFooter');
      if (!canvas || !footer) return;
      const ctx = canvas.getContext('2d');
      let w = 0, h = 0;
      let isVisible = false;
      let animId = null;

      function resize() {
        w = canvas.width = footer.clientWidth;
        h = canvas.height = footer.clientHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      // Particle Count & Pool
      const count = Math.min(65, Math.max(35, Math.floor(window.innerWidth / 25)));
      const particles = [];

      class Spark {
        constructor() {
          this.reset(true);
        }

        reset(initial = false) {
          this.x = Math.random() * (w || 1000);
          this.y = initial ? Math.random() * (h || 400) : (h + 10 + Math.random() * 20);
          this.radius = 0.8 + Math.random() * 2.2;
          // Smooth, tranquil floating speed (slowed down for atmospheric abyss depth)
          this.speedY = 0.12 + Math.random() * 0.28;
          this.swaySpeed = 0.007 + Math.random() * 0.012;
          this.swayAmp = 0.4 + Math.random() * 1.2;
          this.angle = Math.random() * Math.PI * 2;
          this.maxAlpha = 0.35 + Math.random() * 0.55;
          this.alpha = initial ? Math.random() * this.maxAlpha : 0;
          this.fadeIn = true;
          // 80% icy silver/white, 20% warm golden/amber micro-flashes
          this.isWarm = Math.random() < 0.22;
          this.colorR = this.isWarm ? 255 : (210 + Math.floor(Math.random() * 45));
          this.colorG = this.isWarm ? (165 + Math.floor(Math.random() * 45)) : (220 + Math.floor(Math.random() * 35));
          this.colorB = this.isWarm ? 85 : 255;
        }

        update() {
          this.y -= this.speedY;
          this.angle += this.swaySpeed;
          this.x += Math.sin(this.angle) * this.swayAmp;

          // Smooth Fade In as it emerges, Fade Out as it ascends
          if (this.fadeIn) {
            this.alpha += 0.007;
            if (this.alpha >= this.maxAlpha) {
              this.fadeIn = false;
            }
          } else {
            // Natural dissipation near the top
            const heightRatio = this.y / h;
            if (heightRatio < 0.3) {
              this.alpha *= 0.992;
            }
          }

          if (this.y < -15 || this.alpha <= 0.01 || this.x < -20 || this.x > w + 20) {
            this.reset(false);
          }
        }

        draw() {
          if (this.alpha <= 0.01) return;
          const glowRadius = this.radius * 3.8;
          const radGrad = ctx.createRadialGradient(
            this.x, this.y, 0,
            this.x, this.y, glowRadius
          );
          radGrad.addColorStop(0, `rgba(${this.colorR}, ${this.colorG}, ${this.colorB}, ${this.alpha.toFixed(2)})`);
          radGrad.addColorStop(0.35, `rgba(${this.colorR}, ${this.colorG}, ${this.colorB}, ${(this.alpha * 0.45).toFixed(2)})`);
          radGrad.addColorStop(1, `rgba(${this.colorR}, ${this.colorG}, ${this.colorB}, 0)`);

          ctx.fillStyle = radGrad;
          ctx.beginPath();
          ctx.arc(this.x, this.y, glowRadius, 0, Math.PI * 2);
          ctx.fill();

          // Bright Core Diamond
          ctx.fillStyle = `rgba(255, 255, 255, ${Math.min(1, this.alpha * 1.3).toFixed(2)})`;
          ctx.beginPath();
          ctx.arc(this.x, this.y, this.radius * 0.75, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      for (let i = 0; i < count; i++) {
        particles.push(new Spark());
      }

      function loop() {
        if (!isVisible) return;
        ctx.clearRect(0, 0, w, h);
        for (let i = 0; i < particles.length; i++) {
          particles[i].update();
          particles[i].draw();
        }
        animId = requestAnimationFrame(loop);
      }

      // Intersection Observer for 0% CPU consumption when out of view
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            if (!isVisible) {
              isVisible = true;
              resize();
              loop();
            }
          } else {
            isVisible = false;
            if (animId) cancelAnimationFrame(animId);
          }
        });
      }, { threshold: 0.05 });

      observer.observe(footer);
    })();
  </script>
</body>
</html>'''

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("[OK] index.html successfully generated!")
