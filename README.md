# CP02 — NLP com spaCy  
## Analisador de Sentimentos com spaCy

### 📝 Descrição
Este projeto utiliza a biblioteca **spaCy** para identificar sentimentos (positivos, negativos, mistos ou neutros) em frases da língua portuguesa, por meio de **regras personalizadas com `Matcher`** e **extensões do objeto `Doc`**.

---

### ⚙️ Como funciona

- Utiliza o modelo pré-treinado `pt_core_news_sm` para processar frases em português.
- Define padrões com `Matcher` para identificar palavras associadas a sentimentos **positivos** e **negativos**.
- Cria uma extensão personalizada `.sentimento` no objeto `Doc` que:
  - Detecta a presença de palavras-chave na frase;
  - Classifica automaticamente o sentimento da seguinte forma:
    - `Positivo`: contém palavras positivas e nenhuma negativa;
    - `Negativo`: contém palavras negativas e nenhuma positiva;
    - `Misto`: contém ambas;
    - `Neutro`: não contém nenhuma palavra associada a sentimento.

---

### ✅ Exemplo de Saída

