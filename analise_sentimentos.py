import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc

# Carrega o modelo de linguagem em português
nlp = spacy.load("pt_core_news_sm")

# Define listas de palavras positivas e negativas
palavras_positivas = ["feliz", "ótimo", "maravilhoso", "excelente", "incrível", "bom"]
palavras_negativas = ["triste", "horrível", "péssimo", "terrível", "ruim", "chateado"]

# Inicializa o Matcher com o vocabulário do modelo
matcher = Matcher(nlp.vocab)

# Adiciona os padrões positivos ao matcher
for palavra in palavras_positivas:
    matcher.add("POSITIVO", [[{"LOWER": palavra}]])

# Adiciona os padrões negativos ao matcher
for palavra in palavras_negativas:
    matcher.add("NEGATIVO", [[{"LOWER": palavra}]])

# Função para identificar o sentimento com base nos matches
def identificar_sentimento(doc):
    matches = matcher(doc)
    positivo = False
    negativo = False

    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        if string_id == "POSITIVO":
            positivo = True
        elif string_id == "NEGATIVO":
            negativo = True

    if positivo and not negativo:
        return "Positivo"
    elif negativo and not positivo:
        return "Negativo"
    elif positivo and negativo:
        return "Misto"
    else:
        return "Neutro"

# Registra a extensão personalizada no objeto Doc
if not Doc.has_extension("sentimento"):
    Doc.set_extension("sentimento", getter=identificar_sentimento)

# Lista de frases para análise
frases = [
    "Hoje o dia está maravilhoso e me sinto ótimo!",
    "Estou muito triste com os acontecimentos recentes.",
    "Foi uma experiência incrível, mas o final foi horrível.",
    "Nada de especial aconteceu hoje.",
    "Estou feliz, mas também um pouco chateado."
]

# Processa cada frase e imprime o sentimento detectado
for frase in frases:
    doc = nlp(frase)
    print(f"Frase: {frase}")
    print(f"Sentimento detectado: {doc._.sentimento}")
    print("-" * 50)
