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

    # ... (lógica anterior) ...
    return jsonify({"resultado": "Processamento concluído."})

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
