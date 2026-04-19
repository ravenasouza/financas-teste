# Pitch: Lumina – Sua Mentora Financeira Inteligente
 
## Roteiro Sugerido

### 1. O Problema (30 seg)
Muitos brasileiros, como o nosso cliente fictício João Silva, têm uma vida financeira organizada, mas "estacionada". O João ganha bem como Analista de Sistemas, mas o dinheiro da reserva de emergência não está rendendo o que poderia e o sonho do apartamento em 2027 parece distante porque ele não consegue enxergar onde estão os gargalos do seu orçamento diário. Chatbots comuns apenas respondem saldo; eles não ajudam a planejar.

### 2. A Solução (1 min)
Apresento a Lumina. Mais do que um chatbot, a Lumina é uma agente financeira proativa construída com IA Generativa.
Utilizando Python, modelos de linguagem de última geração e uma base de dados real (CSV/JSON), a Lumina faz o que um gerente de banco humano faria: ela analisa o perfil moderado do João, cruza com seus gastos de transporte e alimentação, e sugere atalhos. Se o João gastou demais com Uber, a Lumina não só avisa, ela calcula quanto aquele valor renderia se fosse aplicado hoje no Tesouro Selic para a meta do seu apartamento.

### 3. Demonstração (1 min)
A demonstração prática do agente Lumina foca em três fluxos principais de interação, evidenciando a capacidade de processamento de dados e personalização:

- **Fluxo de Boas-Vindas e Contextualização:** O sistema inicia a sessão reconhecendo o usuário (João Silva) e apresentando um resumo imediato do progresso de suas metas (Reserva de Emergência e Apartamento), estabelecendo uma conexão direta com os dados do arquivo perfil_investidor.json.
- **Análise de Transações em Tempo Real:** Ao ser questionada sobre gastos, a Lumina acessa o transacoes.csv, agrupa os dados por categoria e apresenta o total de gastos. O sistema identifica proativamente desvios (ex: gastos elevados com Uber) e sugere uma economia percentual calculada para acelerar o aporte mensal.
- **Simulação de Investimento Baseada em Perfil:** O usuário solicita uma sugestão para um valor extra. O sistema consulta o produtos_financeiros.json, filtra apenas produtos de baixo risco (devido ao perfil moderado e aceita_risco: false) e recomenda o Tesouro Selic, justificando a escolha com base na segurança e na meta de reserva de emergência incompleta.

### 4. Diferencial e Impacto (30 seg)

- **Inovação:** Diferente de assistentes genéricos, a Lumina utiliza uma camada de validação que impede a recomendação de produtos fora do perfil do cliente, eliminando alucinações financeiras perigosas.
- **Impacto Social:** A solução democratiza o acesso ao planejamento financeiro consultivo. Ao transformar dados complexos de planilhas em diálogos simples e motivadores, a Lumina reduz a carga cognitiva do usuário e aumenta as chances de sucesso no alcance de metas de longo prazo, como a aquisição da casa própria.

---

## Checklist do Pitch

- [ ] Duração máxima de 3 minutos
- [ ] Problema claramente definido (A inércia financeira do João)
- [ ] Solução demonstrada na prática (Interface Streamlit + IA)
- [ ] Diferencial explicado (Proatividade e Segurança/Anti-alucinação)
- [ ] Tom de voz alinhado à Persona Lumina
---

## Link do Vídeo

[Link do vídeo]
