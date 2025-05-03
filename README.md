# CP02---NLP-SpaCy-

# Analisador de Sentimentos com spaCy

## Descrição

Este projeto utiliza a biblioteca `spaCy` para identificar sentimentos (positivos, negativos ou mistos) em frases da língua portuguesa, usando regras personalizadas com `Matcher` e extensões do objeto `txt`.

## Como funciona

1. Utiliza o modelo `pt_core_news_sm` para processar frases em português.
2. Define regras com `Matcher` para identificar palavras associadas a sentimentos positivos e negativos.
3. Cria uma extensão personalizada `.sentimento` para o objeto `txt`, que analisa se a frase contém palavras de sentimento e classifica como:
   - **Positivo**
   - **Negativo**
   - **Misto**
   - **Neutro**

## Exemplo de saída

