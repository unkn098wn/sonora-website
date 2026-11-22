@echo off
chcp 65001 > nul
title Push Sonora-Website to GitHub
cls
echo ===================================================
echo   PUSHING SONORA-WEBSITE TO GITHUB
echo ===================================================
echo.
cd /d "%~dp0"
git add .
git commit -m "update website"
git push -u origin main
echo.
pause
