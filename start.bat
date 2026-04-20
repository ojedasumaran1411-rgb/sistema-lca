@echo off
title Iniciando Sistema LCA_PRO
echo Cargando base de datos y sistema...
cd /d "%~dp0"
python -m streamlit run "LCA_PRO (1).py" --server.address 0.0.0.0 --server.headless true --server.port 8501
echo.
echo ============================================
echo  Abre en el celular: http://TU_IP:8501
echo  Para ver tu IP ejecuta: ipconfig
echo ============================================
pause