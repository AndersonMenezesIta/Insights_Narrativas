from pathlib import Path
import json

from pipeline.extractor import obter_dados_completos_clientes
from pipeline.transformer import transformar_em_perfil_narrativo
from pipeline.generator import gerar_mensagem_personalizada

def main():
    """
    Função principal que executa o pipeline do Motor de Insights e Narrativas.
    """
    print("🚀 Iniciando o Motor de Insights e Narrativas (MIN)...")
    
    # Define o caminho para a pasta de dados
    caminho_dados = Path(__file__).parent / "data"

    # 1. Extração
    print("\n[FASE 1: EXTRAÇÃO] Lendo dados dos clientes...")
    clientes_com_dados = obter_dados_completos_clientes(caminho_dados)
    print(f"✅ {len(clientes_com_dados)} clientes encontrados.")

    # Loop principal para processar cada cliente
    for cliente in clientes_com_dados:
        print("\n" + "="*50)
        print(f"👤 Processando cliente: {cliente['nome']} (ID: {cliente['id']})")
        print("="*50)

        # 2. Transformação
        print("\n[FASE 2: TRANSFORMAÇÃO] Gerando perfil narrativo...")
        perfil_narrativo = transformar_em_perfil_narrativo(cliente)
        
        # Usamos json.dumps para uma visualização bonita do dicionário
        print("✅ Perfil gerado com sucesso:")
        print(json.dumps(perfil_narrativo, indent=2, ensure_ascii=False))

        # 3. Geração (Carregamento)
        print("\n[FASE 3: GERAÇÃO] Criando mensagem personalizada com IA (simulada)...")
        mensagem = gerar_mensagem_personalizada(perfil_narrativo)
        print("✅ Mensagem criada com sucesso!")
        
        # Exibição final
        print("\n" + "-"*50)
        print("💡 MENSAGEM FINAL PARA O CLIENTE:")
        print(f"➡️   {mensagem}")
        print("-"*50)

    print("\n🏁 Processo finalizado com sucesso!")


if __name__ == "__main__":
    main()
