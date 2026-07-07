# ⚽ Análise Estatística de Pênaltis da Seleção Brasileira (Copa do Mundo)

Uma análise exploratória em **Python** sobre os principais cobradores de pênaltis do ciclo da Seleção Brasileira de **2026**, motivada pela eliminação do Brasil para a Noruega após um pênalti desperdiçado.

O objetivo do projeto foi responder uma pergunta simples:

> **Os dados realmente indicavam que Bruno Guimarães era uma escolha melhor do que Vinícius Júnior para cobrar o pênalti decisivo?**

Ao invés de utilizar apenas a taxa de conversão (% de aproveitamento), foi aplicada uma abordagem estatística mais robusta utilizando o **Intervalo de Confiança de Wilson (95%)**, reduzindo o efeito de amostras muito pequenas.

---

## 📌 Objetivos

- Coletar o histórico de pênaltis dos principais jogadores da Seleção Brasileira.
- Comparar desempenho entre clube e seleção.
- Demonstrar como pequenas amostras podem gerar interpretações equivocadas.
- Aplicar conceitos estatísticos em um problema esportivo real.
- Produzir visualizações para facilitar a interpretação dos resultados.

---

## 📊 Jogadores analisados

- Neymar
- Raphinha
- Vinícius Júnior
- Bruno Guimarães
- Igor Thiago
- Gabriel Martinelli
- Rayan
- Matheus Cunha
- Danilo

---

## 📂 Dados utilizados

Para cada cobrança foram registrados:

- Jogador
- Clube/Seleção
- Competição
- Temporada
- Fase da competição
- Cobrança convertida ou perdida
- Tipo da partida (fase normal ou mata-mata)

As informações foram obtidas a partir de fontes esportivas públicas e do **Transfermarkt**.

---

## 🧠 Metodologia

Após a coleta dos dados, foi realizada toda a análise utilizando **Python**.

Etapas do projeto:

1. Coleta dos dados
2. Organização em DataFrame com Pandas
3. Tratamento e limpeza dos registros
4. Cálculo do aproveitamento bruto
5. Aplicação do **Wilson Score Interval (95%)**
6. Construção de gráficos comparativos
7. Interpretação estatística dos resultados

---

## 📈 Por que utilizar o Wilson Score?

Um jogador com:

- ✅ 1 acerto em 1 cobrança possui **100%** de aproveitamento.
- ✅ 2 acertos em 2 cobranças também possui **100%**.

Mas isso **não significa** que ele seja estatisticamente mais confiável do que outro jogador que converteu:

- 13 de 18 cobranças (72,2%).

O Intervalo de Wilson reduz esse problema ao considerar o tamanho da amostra, produzindo estimativas muito mais realistas.

---

## 📊 Principais resultados

A análise mostrou que:

- Jogadores com 100% de aproveitamento possuíam apenas 1 ou 2 cobranças registradas.
- Bruno Guimarães possuía 3 cobranças convertidas antes do jogo contra a Noruega.
- Após o ajuste pelo Wilson Score, sua estimativa caiu para aproximadamente **80%**, mostrando que a confiança estatística ainda era limitada.
- Vinícius Júnior, apesar do aproveitamento bruto menor (**72,2%**), possuía uma amostra muito maior (**18 cobranças**), tornando sua estimativa muito mais consistente.

Em outras palavras:

> Pequenas amostras podem criar uma falsa sensação de superioridade.

---

## 💡 Conclusão

Diferente do que a comissão técnica da CBF avaliou:
Neymar > Igor Thiago > Raphinha > Bruno Guimarães > Martinelli > Vini Jr.

No final, levando tudo em consideração, meu top 3 batedores de pênalti seriam:
Neymar > Raphinha > Vini Jr.

Observação: A análise não pretende afirmar quem deveria cobrar o pênalti.

O objetivo foi mostrar que:

- porcentagens isoladas podem ser enganosas;
- tamanho da amostra importa;
- decisões baseadas em dados precisam considerar a incerteza estatística.

Além disso, fatores como liderança, confiança, momento psicológico e contexto da partida continuam sendo elementos importantes que não podem ser capturados apenas pelos números.

---

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib

---

## 📚 Conceitos aplicados

- Data Cleaning
- Data Analysis
- Estatística Descritiva
- Intervalo de Confiança
- Wilson Score Interval
- Visualização de Dados
- Análise Exploratória (EDA)

---

## 📷 Exemplos de visualizações

O projeto gera gráficos comparando:

- Aproveitamento bruto
- Wilson Score
- Número de cobranças
- Comparação entre jogadores

---

## 📖 Aprendizados

Este projeto reforçou a importância de não interpretar dados apenas pela superfície.

Um simples "100% de aproveitamento" pode parecer uma evidência forte, mas, quando analisado com ferramentas estatísticas adequadas, muitas vezes revela apenas uma amostra pequena demais para sustentar uma conclusão.

Foi uma oportunidade de aplicar conceitos de Ciência de Dados em um contexto esportivo real, mostrando como estatística e programação podem contribuir para discussões que normalmente ficam apenas no campo da opinião.

---

## 👨‍💻 Autor

**Bruno Tubino Franco**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://linkedin.com/in/brunotubino)
