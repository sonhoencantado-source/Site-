@echo off
cd /d "%~dp0"

echo ===============================
echo ENVIANDO ATUALIZACOES AO GITHUB
echo ===============================

git status
git add .
git commit -m "Atualizacao automatica do catalogo"
git push

echo.
echo ✔ Atualizacao enviada com sucesso!
pause
