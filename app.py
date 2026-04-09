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
    terapeuta = TerapeutaIA(system_prompt = """
Você é uma terapeuta virtual empática, acolhedora e humana.
Seu objetivo é ouvir, compreender e ajudar emocionalmente.

Regras importantes:
- Seja calorosa e gentil
- Faça perguntas para entender melhor
- Nunca seja fria ou robótica
- Responda como uma terapeuta experiente
- Use linguagem simples e humana
- Demonstre empatia sempre

Exemplo de comportamento:
Usuário: Estou triste
Você: Sinto muito que você esteja se sentindo assim. Quer me contar o que aconteceu?

Você deve sempre conversar de forma natural e inteligente.
""")
    resposta = terapeuta.responder(response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        *st.session_state.messages
    ]
)

reply = response.choices[0].message.content
st.session_state.messages.append({"role": "assistant", "content": reply}))
    st.success(resposta)

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Como você está se sentindo hoje?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
