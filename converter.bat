@echo off
echo ===============================
echo  CONVERTENDO EXCEL PARA JSON
echo ===============================
echo.

py -m pip install --quiet pandas openpyxl

py converter.py

if exist produtos.json (
    echo.
    echo ✔ Conversao concluida com sucesso!
    echo Arquivo produtos.json gerado.
) else (
    echo.
    echo ❌ Erro ao gerar o JSON.
)

echo.
pause