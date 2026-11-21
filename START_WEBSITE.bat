@echo off
chcp 65001 > nul
title Sonora Music Website
color 0B

echo ============================================================
echo               SONORA MUSIC - OFFICIAL WEBSITE
echo ============================================================
echo.
echo [*] Запуск локального сервера веб-сайта Sonora на порту 8080 ...
echo [i] Адрес в браузере: http://localhost:8080
echo.

cd /d "%~dp0"
start http://localhost:8080
python -m http.server 8080
pause
