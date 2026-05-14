# COWORK_MAESTRO.py - Orquestrador de Colaboração Multi-Agente XTAL
import json
import os
import time
from HIVE_CORE.ROTEADOR_IA import ask_ai

class CoworkMaestro:
    def __init__(self):
        self.context_vault = "OFFICE_JURIS/SHARED_CONTEXT_VAULT.json"
        self._ensure_vault()

    def _ensure_vault(self):
        if not os.path.exists(self.context_vault):
            with open(self.context_vault, 'w', encoding='utf-8') as f:
                json.dump({"session_id": time.time(), "insights": [], "artifacts": []}, f)

    def log_insight(self, agent_name, insight):
        with open(self.context_vault, 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data["insights"].append({
                "timestamp": time.strftime('%H:%M:%S'),
                "agent": agent_name,
                "data": insight
            })
            f.seek(0)
            json.dump(data, f, indent=4)
        print(f"🧠 [COWORK]: Insight de {agent_name} registrado no Cofre.")

    def elaborar_documento_colaborativo(self, tema, demanda):
        print(f"🏛️ [XTAL COWORK]: Iniciando Elaboração de Documento sobre '{tema}'")
        
        # 1. ACIONA O PERITO (Conhecimento Técnico)
        perito_prompt = f"Analise tecnicamente a seguinte demanda: {demanda}. Foque em normas (NR, CONAMA, NHO) e geotecnia se aplicável."
        analise_tecnica = ask_ai(perito_prompt, context="PERITO_TECNICO")
        self.log_insight("PERITO", analise_tecnica)
        
        # 2. ACIONA O ADVOGADO (Estratégia Jurídica usando o insight do perito)
        advogado_prompt = f"""
        Com base na análise técnica do perito:
        ---
        {analise_tecnica}
        ---
        Elabore uma petição/parecer jurídico para a demanda: {demanda}.
        Utilize jurisprudência brasileira e argumentação de elite.
        """
        parecer_juridico = ask_ai(advogado_prompt, context="ADVOGADO_LEGAL")
        self.log_insight("ADVOGADO", parecer_juridico)
        
        # 3. REVISOR (O 'Contraditório' da Anthropic)
        revisor_prompt = f"""
        Revise o parecer abaixo buscando falhas lógicas ou falta de fundamentação técnica:
        {parecer_juridico}
        
        Aponte melhorias para tornar a peça imbatível.
        """
        revisao = ask_ai(revisor_prompt, context="REVISOR_FORENSE")
        self.log_insight("REVISOR", revisao)
        
        # 4. CONSOLIDAÇÃO FINAL
        documento_final = f"""
        # DOCUMENTO TÉCNICO-JURÍDICO XTAL JURIS
        TEMA: {tema}
        DATA: {time.strftime('%d/%m/%Y')}
        
        ## 1. FUNDAMENTAÇÃO TÉCNICA (PERÍCIA)
        {analise_tecnica}
        
        ## 2. PARECER JURÍDICO
        {parecer_juridico}
        
        ## 3. NOTAS DE REVISÃO E MELHORIAS
        {revisao}
        
        ---
        Gerado automaticamente pelo XTAL COWORK OS.
        """
        
        filename = f"OFFICE_JURIS/DOCS/DOC_{int(time.time())}.md"
        os.makedirs("OFFICE_JURIS/DOCS", exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(documento_final)
            
        print(f"✅ [COWORK]: Documento consolidado e salvo em {filename}")
        return filename

if __name__ == "__main__":
    maestro = CoworkMaestro()
    maestro.elaborar_documento_colaborativo("Defesa de Auto de Infração Ambiental", "Usinagem com emissão de ruído acima de 85dB próximo a área residencial.")
