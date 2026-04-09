import streamlit as st
import random

class TerapeutaIA:

    def detectar_emocao(self, texto):
        texto = texto.lower()

        emocoes = {
            "tristeza": ["triste", "sozinho", "desanimado"],
            "ansiedade": ["ansioso", "preocupado", "medo"],
            "raiva": ["raiva", "irritado", "frustrado"],
            "cansaço": ["cansado", "sobrecarregado"]
        }

        for emocao, palavras in emocoes.items():
            if any(p in texto for p in palavras):
                return emocao

        return "reflexão"

    def responder(self, texto):

        emocao = self.detectar_emocao(texto)

        respostas = {
            "tristeza": "Sinto que existe tristeza no que você está dizendo.",
            "ansiedade": "Percebo preocupação nessa situação.",
            "raiva": "Entendo que isso pode ser frustrante.",
            "cansaço": "Parece que você está sobrecarregado.",
            "reflexão": "Entendo que isso é importante para você."
        }

        perguntas = [
            "O que mais está te incomodando?",
            "O que você gostaria que fosse diferente?",
            "Quando isso começou?",
            "Como isso afeta você?"
        ]

        sugestoes = [
            "Respire fundo por alguns minutos.",
            "Escreva seus pensamentos.",
            "Dê um pequeno passo.",
            "Seja gentil consigo mesmo."
        ]

        return f"""
💙 {respostas[emocao]}

🧠 {random.choice(perguntas)}

🌱 {random.choice(sugestoes)}

Estou aqui com você.
"""


st.title("🌿 Terapeuta IA")
st.write("Um espaço seguro para conversar sem julgamentos")

texto = st.text_area("Como você está se sentindo?")

if st.button("Conversar"):
    terapeuta = TerapeutaIA()
    resposta = terapeuta.responder(texto)
    st.success(resposta)
