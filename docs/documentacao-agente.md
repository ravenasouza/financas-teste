# Documentação do Agente

## Caso de Uso

### Problema

João Silva é um profissional de tecnologia com renda estável, mas que lida com a fragmentação de suas informações financeiras. Ele possui dados de gastos, perfil de risco e metas espalhados, o que dificulta a tomada de decisão proativa para seu grande objetivo: a entrada de um apartamento em 2027.

### Solução

A Lumina é uma agente financeira inteligente que consolida o histórico de transações, o perfil psicográfico do investidor e o catálogo de produtos bancários em uma interface de conversação fluida. Ela atua de forma consultiva, identificando padrões de gastos (como o alto volume em transporte e lazer) e cruzando-os com oportunidades de investimento de baixo risco, adequadas ao perfil moderado do João.

### Público-Alvo

Profissionais da área de tecnologia e jovens adultos que buscam autonomia financeira através de dados, mas que valorizam uma interface intuitiva e um tom de voz humano.

---

## Persona e Tom de Voz

### Nome do Agente
Lumina

### Personalidade

Estrategista e Acolhedora. A Lumina se comporta como uma mentora que entende de números, mas também entende de gente. Ela é direta quando precisa alertar sobre o orçamento, mas sempre oferece uma saída positiva e prática.

### Tom de Comunicação

Acessível, elegante e transparente. Ela evita o "financês" agressivo, preferindo explicar o "porquê" de cada sugestão.

### Exemplos de Linguagem
- Saudação: "Olá, João! Analisei suas movimentações recentes e tenho algumas luzes para trazer para o seu plano do novo apartamento. Vamos conversar?"
- Confirmação: "Perfeito, entendi seu objetivo. Deixa eu cruzar esses dados com nosso catálogo de produtos."
- Erro/Limitação: "Ainda não consigo processar investimentos em criptoativos, mas posso te mostrar como está sua reserva de emergência no Tesouro Selic hoje."

---

## Arquitetura

### Diagrama

**1. Cliente**
- João Silva interage com o sistema
- Envia perguntas ou informações de gastos

⬇️

**2. Interface (Streamlit)**
- Recebe a entrada do usuário
- Exibe respostas de forma interativa

⬇️

**3. LLM (GPT-4o / Gemini)**
- Processa a pergunta do usuário
- Interpreta contexto e intenção

⬇️

**4. Base de Conhecimento (CSV / JSON)**
- Consulta os arquivos `transacoes.csv` e `perfil_investidor.json`
- Retorna dados relevantes ao modelo

⬇️

**5. Validação de Perfil**
- Verifica o nível de risco (ex: Moderado)
- Filtra recomendações incompatíveis

⬇️

**6. Resposta Final (Lumina)**
- Gera resposta personalizada
- Baseada em dados + regras de segurança

### Componentes

| Componente                | Descrição |
|--------------------------|----------|
| **Interface**            | Chatbot interativo desenvolvido em Streamlit com foco em UX. |
| **LLM**                  | Utilização de modelos de larga escala (OpenAI/Google) via API para processamento. |
| **Base de Conhecimento** | Integração de dados de `transacoes.csv` e `perfil_investidor.json`. |
| **Validação**            | Camada de lógica que garante que o conselho respeite o perfil de risco do João. |

---

### Segurança e Anti-Alucinação

**Estratégias Adotadas:**

- [x] **Grounding de Dados:** O agente responde exclusivamente com base nos arquivos da pasta `data/`.
- [x] **Citação de Fontes:** Respostas sobre investimentos citam diretamente o nome do produto do arquivo JSON.
- [x] **Admissão de Falha:** Se a informação não constar nos arquivos fornecidos, a Lumina admite o desconhecimento.
- [x] **Filtro de Perfil:** O agente bloqueia recomendações de alto risco se `aceita_risco` for `false`.

---

### Limitações Declaradas

- Não realiza transações bancárias reais (é apenas um protótipo consultivo).
- Não fornece previsões de mercado de ações em tempo real.
- Não substitui a consultoria de um profissional de investimentos certificado para grandes patrimônios.
