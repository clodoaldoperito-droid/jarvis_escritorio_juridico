# XTAL_MCP_SERVER.py - Servidor Model Context Protocol para Direito Brasileiro
import json
import os
import sys

# Simulação de servidor MCP via stdio
def mcp_server():
    print("📡 [XTAL MCP]: Servidor de Contexto Jurídico Iniciado.", file=sys.stderr)
    
    knowledge_base = "BRAZILIAN_LEGAL_ADAPTER.json"
    
    while True:
        try:
            line = sys.stdin.readline()
            if not line: break
            
            request = json.loads(line)
            method = request.get("method")
            params = request.get("params", {})
            
            if method == "query_law":
                term = params.get("term", "").lower()
                with open(knowledge_base, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Busca simplificada na base
                    results = [v for k, v in data.items() if term in k.lower() or term in str(v).lower()]
                
                response = {"jsonrpc": "2.0", "id": request.get("id"), "result": results}
                print(json.dumps(response), flush=True)
                
            elif method == "get_skills":
                skills_dir = "OFFICE_JURIS/SKILLS"
                skills = os.listdir(skills_dir)
                response = {"jsonrpc": "2.0", "id": request.get("id"), "result": skills}
                print(json.dumps(response), flush=True)
            
        except Exception as e:
            error = {"jsonrpc": "2.0", "id": request.get("id", 0), "error": {"code": -32603, "message": str(e)}}
            print(json.dumps(error), flush=True)

if __name__ == "__main__":
    mcp_server()
