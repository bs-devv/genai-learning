import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

from config import LLM_INSTRUCTIONS
from chat import send_message

# Lettura .env
current_dir = Path(__file__).parent
env_path = current_dir.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Client per parlare con l'API (chiave letta da .env, base_url = server Groq)
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

chat_messages = [{"role": "system", "content": LLM_INSTRUCTIONS}]

activated = True

print("LLM: Ciao, come posso esserti utile? Digita exit per terminare e reset per una nuova conversazione.")

while activated:
    
    message = input("User: ")
    
    if message == "exit":
        activated = False
        break
    
    if message == "reset":
        chat_messages = [{"role": "system", "content": LLM_INSTRUCTIONS}]
        print("LLM: Conversazione resettata. Come posso esserti utile?")
        continue
    
    while message == "":
        message = input("User:")
        
    chat_messages.append({"role": "user", "content": message})
    
    resp = send_message(client, chat_messages)
    if resp is None:
        print("Errore nella generazione della risposta, riprova.")
    else:
        print("LLM:", resp)

