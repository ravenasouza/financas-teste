# Base de Conhecimento

## Dados Utilizados

| Arquivo                         | Formato | Utilização no Agente |
|--------------------------------|---------|----------------------|
| `historico_atendimento.csv`    | CSV     | Consultar interações passadas (ex: dúvidas sobre CDB) para evitar repetições e dar continuidade ao suporte. |
| `perfil_investidor.json`       | JSON    | Identificar o perfil (Moderado), metas (Apartamento) e reserva de emergência atual. |
| `produtos_financeiros.json`    | JSON    | Catálogo oficial de investimentos permitidos para recomendação. |
| `transacoes.csv`               | CSV     | Análise de fluxo de caixa, identificação de gastos excessivos e cálculo de capacidade de aporte. |

---

## Adaptações nos Dados

Para este projeto, os dados mockados foram mantidos em sua estrutura original para garantir a integridade dos testes, mas foram interpretados da seguinte forma:

- **Metas Financeiras:** O campo `metas` no JSON foi utilizado para criar senso de urgência e proatividade no discurso da Lumina.  
- **Categorização de Gastos:** Os dados do CSV foram agrupados por categoria para gerar insights de economia em transporte e lazer.  

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos são carregados em memória no início da execução da aplicação (via **Pandas** para os CSVs e biblioteca `json` para os arquivos JSON).  
Eles são transformados em dicionários e tabelas que o sistema consulta antes de enviar o prompt final para a LLM.

### Como os dados são usados no prompt?

A Lumina utiliza uma abordagem de **RAG (Retrieval-Augmented Generation) simplificada**:

1. O sistema identifica o contexto da pergunta do usuário.  
2. Recupera as informações relevantes nos arquivos (ex: perguntas sobre gastos → `transacoes.csv`).  
3. Insere os dados filtrados no contexto enviado à IA, garantindo respostas baseadas na realidade do cliente.  

---

## Exemplo de Contexto Montado

```plaintext
### CONTEXTO DO CLIENTE ATUAL ###
- Nome: João Silva
- Perfil: Moderado (Aceita Risco: Falso)
- Reserva Atual: R$ 10.000,00 (Meta: R$ 15.000,00)
- Próxima Meta: Entrada Apartamento (R$ 50.000,00 até Dez/2027)

### DADOS RECENTES (Últimos 30 dias) ###
- Total de Entradas: R$ 5.000,00
- Principais Gastos: Moradia (R$ 1.380,00), Transporte (R$ 295,00)

### PRODUTOS DISPONÍVEIS ###
[Tesouro Selic, CDB Liquidez Diária, Fundo Multimercado...]

