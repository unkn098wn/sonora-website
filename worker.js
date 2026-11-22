export default {
  async fetch(request, env, ctx) {
    // Keep-alive ping to Render cloud bot so it never sleeps
    if (ctx && ctx.waitUntil) {
      ctx.waitUntil(fetch('https://sonora-bot.onrender.com/health').catch(() => {}));
    }
    return env.ASSETS.fetch(request);
  },
  async scheduled(event, env, ctx) {
    if (ctx && ctx.waitUntil) {
      ctx.waitUntil(fetch('https://sonora-bot.onrender.com/health').catch(() => {}));
    }
  }
};
