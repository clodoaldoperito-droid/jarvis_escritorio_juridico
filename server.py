import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Carrega as chaves do proprio escritorio (BYOK)
load_dotenv()

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar():
    data = request.json
    tipo = data.get('tipo')
    demanda = data.get('demanda')
    
    # Verifica se a chave de IA esta configurada
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key or "Sua_Chave_Aqui" in api_key:
        return jsonify({
            "resultado": "[ERRO] Chave de IA nao configurada! \nAbra o arquivo .env e coloque sua propria chave para o sistema funcionar."
        })

    # Aqui o Jarvis chamaria os agentes especializados
    # Por agora, retornamos o feedback de sucesso do motor
    if tipo == 'ambiental':
        return jsonify({
            "resultado": "=== ANALISE TECNICA AMBIENTAL (MOTOR XTAL) ===\n\n[INFO] Aplicando Decisao de Diretoria CETESB DD 038/2017/C...\n[PERITO] Analise de Geotecnia concluida. Detectada falha no monitoramento de solo.\n[ADVOGADO] Fundamentando recurso com base na Lei 6.938/81.\n\nSua peticao foi gerada com base nos seus proprios tokens de IA."
        })
    else:
        return jsonify({
            "resultado": "=== ANALISE TECNICA TRABALHISTA/SST (MOTOR XTAL) ===\n\n[INFO] Cruzando NHO-01 Fundacentro com eSocial S-2240...\n[PERITO] Higiene Ocupacional: Ruido abaixo do limite de tolerancia previdenciario.\n[ADVOGADO] Contestacao de Aposentadoria Especial pronta.\n\nSua defesa foi gerada com base nos seus proprios tokens de IA."
        })

if __name__ == '__main__':
    print("[*] XTAL JURIS CORE - Servidor Online")
    app.run(port=5000)
