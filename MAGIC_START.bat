@echo off
TITLE XTAL JURIS CORE - SETUP MAGICO
COLOR 0B
echo ======================================================
echo           XTAL JURIS CORE - SETUP MAGICO
echo     Banca de Advocacia Digital de Alta Performance
echo ======================================================
echo.

:: Verifica se o Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! Por favor, instale o Python 3.10+ para continuar.
    pause
    exit
)

:: Cria o ambiente virtual e instala dependencias leves
echo [*] Configurando ambiente inteligente...
if not exist "venv" (
    python -m venv venv
)
call venv\Scripts\activate
python -m pip install flask python-dotenv requests >nul

:: Configura o .env se nao existir
if not exist ".env" (
    echo [!] Arquivo de chaves (.env) nao encontrado.
    echo [*] Criando arquivo a partir do modelo...
    copy .env.example .env
    echo.
    echo [ATENCAO] Por favor, abra o arquivo .env e coloque suas chaves de IA.
    echo O sistema nao funcionara sem as chaves do SEU escritorio.
    pause
)

echo.
echo ======================================================
echo   SISTEMA PRONTO! ABRINDO DASHBOARD NO NAVEGADOR...
echo ======================================================
echo.

:: Inicia o servidor em background e abre o navegador
start "" "http://localhost:5000"
python server.py

pause
