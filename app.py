import streamlit as st
from openai import OpenAI

# Configuração da página
st.set_page_config(
    page_title="Terapeuta IA",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Terapeuta IA")
st.write("Olá, estou aqui para conversar com você. Como você está se sentindo hoje?")

# Inicializar cliente OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Personalidade da terapeuta
system_prompt = """
Você é uma terapeuta virtual empática, gentil e humana.

Seu objetivo é ouvir, acolher e ajudar emocionalmente.

Regras:
- Seja empática e acolhedora
- Faça perguntas para entender melhor
- Nunca seja fria ou robótica
- Use linguagem simples e humana
- Demonstre compreensão emocional
- Seja gentil e respeitosa
- Não dê conselhos médicos
- Não substitua um profissional humano

Exemplo:
Usuário: Estou triste
Você: Sinto muito que esteja se sentindo assim. Quer me contar o que aconteceu?
"""

# Memória da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
user_input = st.chat_input("Digite aqui...")

if user_input:
    # Salvar mensagem do usuário
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Mostrar mensagem do usuário
    with st.chat_message("user"):
        st.markdown(user_input)

    # Gerar resposta da IA
    response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {"role": "system", "content": system_prompt},
        *st.session_state.messages
    ]
)

resposta = response.output_text

st.session_state.messages.append({
    "role": "assistant",
    "content": resposta
})

with st.chat_message("assistant"):
    st.markdown(resposta)

    # Salvar resposta
    st.session_state.messages.append({
        "role": "assistant",
        "content": resposta
    })

    # Mostrar resposta
    with st.chat_message("assistant"):
        st.markdown(resposta)
