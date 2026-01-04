@echo off
title Atualizar Site - GitHub
echo ===============================
echo   ATUALIZANDO O SITE ONLINE
echo ===============================
echo.

REM Garante que está na pasta do script
cd /d "%~dp0"

echo Verificando alteracoes...
git status
echo.

echo Adicionando arquivos...
git add .
echo.

echo Criando commit...
git commit -m "Atualizacao de produtos"
echo.

echo Enviando para o GitHub...
git push
echo.

echo ===============================
echo   SITE ATUALIZADO COM SUCESSO!
echo ===============================
pause
