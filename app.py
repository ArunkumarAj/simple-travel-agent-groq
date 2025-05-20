import streamlit as st
import os
import time
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()
# Set your Groq API Key
groq_api_key = os.getenv("GROQ_API_KEY")  # Ensure this is set in your environment

if not groq_api_key:
    raise EnvironmentError("GROQ_API_KEY environment variable not set.")

chat = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma2-9b-It")
# System prompt / context 
context = '''
You are a virtual travel assistant for a travel agency. You help customers plan and book trips including flights, hotels, and activities.

Ask for the destination, travel dates, number of travelers, and preferences (budget, luxury, sightseeing, adventure, etc.). Suggest itinerary ideas based on their input and give general travel tips.

You don’t handle real-time bookings, but simulate helpful planning suggestions like a knowledgeable agent.

*note:
- Every time if you printing Travel Agency Name. Generate your own Agency name 

'''
print("🔥 App has restarted!")
# Add system message at start
system_message = AIMessage(content=context)

def response_generator(prompt, messages):
    # Prepare full chat history with system message
    full_chat = [system_message] + messages + [HumanMessage(content=prompt)]
    
    response = chat.invoke(full_chat)
    reply = response.content

    for word in reply.split():
        yield word + " "
        time.sleep(0.05)

def reset_chat():
    st.session_state.messages = []

def main():
    st.title("Travel Agent Assistant")
    st.write("Hello and welcome! I'm here to help you plan your perfect trip. Whether you need flights, hotels, or travel tips, I’ve got you covered. Let’s start your adventure!")


    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        role = "Human" if isinstance(message, HumanMessage) else "AI"
        with st.chat_message(role):
            st.markdown(message.content)

    if prompt := st.chat_input("Hello, how can I help you?"):
        st.session_state.messages.append(HumanMessage(prompt))
        with st.chat_message("Human"):
            st.markdown(prompt)

        with st.chat_message("AI"):
            placeholder = st.empty()
            response_words = []
            for word in response_generator(prompt, st.session_state.messages):
                response_words.append(word)
                placeholder.markdown("".join(response_words))
            response_text = ''.join(response_words)

        st.session_state.messages.append(AIMessage(response_text))

    st.button("Reset Chat", on_click=reset_chat)
    st.cache_data.clear()

if __name__ == "__main__":
    main()
