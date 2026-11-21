@echo off
chcp 65001 >nul
echo ==============================================================================
echo   SONORA WEBSITE — 1-CLICK DEPLOY ПОДГОТОВКА (Cloudflare Pages / GitHub)
echo ==============================================================================
echo.

cd /d "%~dp0"

if not exist ".git" (
    echo [*] Инициализация локального Git-репозитория...
    git init -b main
)

echo [*] Добавление файлов в Git (тяжелые Universal APK исключены по .gitignore)...
git add .

git status --short

echo.
set /p COMMIT_MSG="[?] Введите описание коммита (Enter для стандартного): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=feat: update Sonora landing website and release links

git commit -m "%COMMIT_MSG%"

echo.
echo ==============================================================================
echo   РЕПОЗИТОРИЙ САЙТА ГОТОВ К ОТПРАВКЕ!
echo ==============================================================================
echo.
echo Для бесплатной публикации на Cloudflare Pages:
echo 1. Создайте пустой репозиторий на github.com (например: sonora-website)
echo 2. Выполните (один раз):
echo      git remote add origin https://github.com/ВАШ_ЛОГИН/sonora-website.git
echo      git push -u origin main
echo 3. В панели dash.cloudflare.com -> Workers & Pages -> Create application -> Pages:
echo      Выберите ваш репозиторий sonora-website.
echo      Build command: Оставить пустым!
echo      Build output directory: Оставить пустым (или /)!
echo 4. Добавьте свой домен: Custom Domains -> mpthree.fun
echo.
echo Для отправки последующих обновлений просто запускайте этот скрипт и делайте:
echo      git push
echo.
pause
