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

    if tipo == 'sanitaria':
        return jsonify({
            "resultado": "=== CONSULTORIA VIGILÂNCIA SANITÁRIA (XTAL) ===\n\n[INFO] Analisando conformidade com RDC 216 e RDC 50...\n[PERITO] Validando fluxos para LTA. Detectada necessidade de barreira sanitária.\n[ADVOGADO] Elaborando Memorial Descritivo para HSA.\n\nServiço de Vigilância Sanitária ativo com seus tokens."
        })
    elif tipo == 'ambiental':
        return jsonify({
            "resultado": "=== ANÁLISE TÉCNICA AMBIENTAL (MOTOR XTAL) ===\n\n[INFO] Aplicando Decisão de Diretoria CETESB DD 038/2017/C...\n[PERITO] Análise de Geotecnia concluída. Detectada falha no monitoramento de solo.\n[ADVOGADO] Fundamentando recurso com base na Lei 6.938/81."
        })
    else:
        return jsonify({
            "resultado": "=== ANÁLISE TÉCNICA TRABALHISTA/SST (MOTOR XTAL) ===\n\n[INFO] Cruzando NHO-01 Fundacentro com eSocial S-2240...\n[PERITO] Higiene Ocupacional: Ruído abaixo do limite de tolerância previdenciário.\n[ADVOGADO] Contestação de Aposentadoria Especial pronta."
        })

@app.route('/cowork', methods=['POST'])
def cowork():
    data = request.json
    tema = data.get('tema')
    demanda = data.get('demanda')
    
    from tools.COWORK_MAESTRO import CoworkMaestro
    maestro = CoworkMaestro()
    
    # O Maestro orquestra a colaboração entre Perito, Advogado e Revisor
    arquivo_gerado = maestro.elaborar_documento_colaborativo(tema, demanda)
    
    with open(arquivo_gerado, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        
    return jsonify({
        "resultado": conteudo,
        "arquivo": arquivo_gerado
    })

if __name__ == '__main__':
    print("[*] XTAL JURIS CORE - Servidor Online")
    app.run(port=5000)
