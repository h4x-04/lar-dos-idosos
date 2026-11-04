@echo off
title Servidor Lar dos Idosos WB - Python e SQL
echo ========================================================
echo   Iniciando Portal Web e Backend (Python Flask + SQL)
echo   Centro Universitario Internacional UNINTER
echo ========================================================
echo.
cd /d "%~dp0"
echo Acessando no navegador:
echo   - Portal Publico:  http://127.0.0.1:5000
echo   - Painel Admin:    http://127.0.0.1:5000/admin
echo.
python app.py
pause
