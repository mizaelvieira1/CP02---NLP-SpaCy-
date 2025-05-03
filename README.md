# 📘 CP02 — NLP com spaCy  
## 💬 Analisador de Sentimentos baseado em Regras

### 👥 Integrantes

| Nome completo                 | RM       |
|-------------------------------|----------|
| Mizael Vieira Bezerra         | RM555796 |
| Santiago Nascimento Bernardes | RM557447 |

### 📄 Descrição
Este projeto utiliza a biblioteca **spaCy** para realizar a análise de sentimentos em frases escritas em português.  
A detecção é feita com **regras manuais usando o Matcher**, que busca palavras positivas e negativas no texto.

🎯 **Objetivo:** classificar cada frase como:
- ✅ Positivo  
- ❌ Negativo  
- ⚖️  Misto  
- ➖ Neutro  

---

### ⚙️ Funcionamento

1. 📥 Carrega o modelo de linguagem pré-treinado: `pt_core_news_sm`.
2. 🧠 Define padrões com `Matcher` para detectar palavras positivas e negativas.
3. 🧩 Adiciona uma extensão personalizada ao objeto `Doc`, chamada `.sentimento`.
4. 📊 Analisa uma lista de frases e imprime o sentimento classificado.

---

### 🧾 Classificações possíveis

- ✅ **Positivo**: contém palavras positivas e nenhuma negativa.  
- ❌ **Negativo**: contém palavras negativas e nenhuma positiva.  
- ⚖️  **Misto**: contém palavras positivas e negativas.  
- ➖ **Neutro**: não contém nenhuma palavra associada a sentimentos.

---

### 🧪 Exemplo de Saída

- Frase: Hoje o dia está maravilhoso e me sinto ótimo!
Sentimento detectado: Positivo
- Frase: Estou muito triste com os acontecimentos recentes.
Sentimento detectado: Negativo
- Frase: Foi uma experiência incrível, mas o final foi horrível.
Sentimento detectado: Misto
- Frase: Nada de especial aconteceu hoje.
Sentimento detectado: Neutro
- Frase: Estou feliz, mas também um pouco chateado.
Sentimento detectado: Misto
