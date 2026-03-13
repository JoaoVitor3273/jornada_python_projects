#titulo
#campo do chat
#a cada mensagem que o usuário enviar
    #mostrar a mensagem que o usuário enviou no chat
    #pegar a pergyunta e enviar para uma IA responder
    #exibir a resposta da IA na tela

#para iniciar o teste abra o terminal e digite "streamlit run chatbot.py"


#ia utilizada no projeto: OpenAI
#pip install openia streamlit
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="sk-proj-JeR0roZge_Wq8AH7LlIgy0tYiyd0Ybm8hEte35im-uRbKbGMclEkma9ROstaZxpN9f4t_k2EyT3BlbkFJKfGnm5Jl-WLN36jgANE6BcaT4c9AXhS63DpgGyBwdznsELF7AgQlaQOmEMWWTecIFseb3Io5AA")

#criando estruturas do site utilizando streallit
st.write("# Chatbot IA") #formatação markdown

#cria a a lista/histórico de mensagens que vai ser mostrado durante a conversa com a IA
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []


#cria o campo para escrever mensagem
texto_usuario = st.chat_input("digite sua mensagem")
#arquivo = st.file_uploader("selecione um arquivo") (adiciona a opção de fazer udpload de arquivo)

#imprime as mensagens armazenadas na lista de msg e mostra na tela
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)


if texto_usuario:
    st.chat_message("user").write(texto_usuario) #retorna a mensagem no chat
    mensagem_usuario = {"role": "user", "content": texto_usuario}#configura o dicionário do usuario
    st.session_state["lista_mensagens"].append(mensagem_usuario)#adiciona a lista de msg

    #ia responde
    #utiliza a função OpenIA
    resporta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    #pega a resposta da IA, localiza a mensagem que queremos retornar e aloca a variavel para poder printar depois
    texto_resposta_ia = resporta_ia.choices[0].message.content

    #printa a respostab da IA no chat e adiciona a resposta a lista de mensagens
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistent", "content": texto_resposta_ia}#configura o dicionário para a mensagem da ia
    st.session_state["lista_mensagens"].append(mensagem_ia)#adiciona a mensagem a lista de msg

