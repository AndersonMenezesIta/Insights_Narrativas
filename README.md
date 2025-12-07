# Protótipo: Motor de Insights e Narrativas (MIN)

Este projeto é uma demonstração do conceito de um pipeline de dados reimaginado, o **Motor de Insights e Narrativas (MIN)**, para criar mensagens de marketing personalizadas e proativas para clientes de um banco, atuando como um "Conselheiro Financeiro de Bolso".

O objetivo é transformar dados brutos de clientes em insights acionáveis e, em seguida, em uma mensagem hiper-personalizada, sem o uso de APIs externas para a geração de conteúdo, garantindo a privacidade e segurança dos dados.

---

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
santander/
│
├── data/
│   ├── customers.json      # Arquivo com dados fictícios dos clientes
│   └── transactions.json   # Arquivo com transações fictícias
│
├── pipeline/
│   ├── __init__.py
│   ├── extractor.py        # Módulo para extrair e combinar os dados
│   ├── transformer.py      # Módulo para transformar dados em um perfil narrativo
│   └── generator.py        # Módulo que simula a IA para gerar a mensagem
│
├── main.py                 # Script principal para orquestrar o pipeline
└── README.md               # Este arquivo
```

---

## Como Executar o Projeto

Este projeto foi construído com Python e não requer nenhuma biblioteca externa para a sua execução básica.

1.  **Pré-requisitos:**
    *   Ter o Python 3.6 ou superior instalado.

2.  **Execução:**
    *   Abra um terminal na raiz do projeto (`santander/`).
    *   Execute o script principal com o seguinte comando:

    ```bash
    python main.py
    ```

3.  **O que esperar:**
    *   O script será executado e processará os clientes definidos nos arquivos `.json`.
    *   Para cada cliente, ele imprimirá as três fases do pipeline:
        1.  **Extração:** Confirmação da leitura dos dados.
        2.  **Transformação:** O "Perfil Narrativo" gerado em formato JSON.
        3.  **Geração:** A mensagem final personalizada para o cliente.

---

## Próximos Passos

Este protótipo pode ser expandido de várias maneiras:
*   **Substituir o Simulador de IA:** O `generator.py` pode ser conectado a um modelo de linguagem real (open-source ou proprietário) hospedado localmente.
*   **Integração de Dados Reais:** O `extractor.py` pode ser modificado para se conectar a um banco de dados real.
*   **Interface Gráfica:** Construir uma interface web (usando frameworks como Flask ou FastAPI) para visualizar os resultados.
