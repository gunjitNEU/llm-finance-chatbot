import streamlit as st
import ollama

# Define the model creation script
modelfile = '''
FROM llama3
SYSTEM You are an expert in the field of Canadian finance
'''

# Create the model (assuming the 'ollama.create' function works synchronously)
ollama.create(model='finance_chat_bot', modelfile=modelfile)

# Title of the app
st.title("Finance Help Chatbot")

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Input for user query
query = st.text_input("Ask your finance-related question:")

# Display response if query is entered
if query:
    response = ollama.chat(model='finance_chat_bot', messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])
    # Update conversation history
    st.session_state.history.append({'role': 'user', 'content': query})
    st.session_state.history.append({'role': 'bot', 'content': response['message']['content']})

# Display the conversation history
for message in st.session_state.history:
    if message['role'] == 'user':
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")
    

# Button to clear the chat history
if st.button("Clear Chat"):
    st.session_state.history = [
        {"role": "system", "content": "Hello! I'm Finance bot. How can I assist you with your finance questions?"}
    ]