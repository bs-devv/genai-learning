from config import MAX_LENGTH_MESSAGES, MODEL_NAME, TEMPERATURE

# Quando la conversazione si allunga, elimina la coppia user/assistant più vecchia
# (in posizione 0 ci sono le istruzioni per il LLM da NON eliminare) 
def trim_history(chat_messages):
    if len(chat_messages) > MAX_LENGTH_MESSAGES:
            del chat_messages[1:3]


# Per l'elaborazione del messaggio dell'utente da parte del LLM
def send_message(client, chat_messages):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=chat_messages,
            temperature=TEMPERATURE
        )
    # In caso di errore, il messaggio è rimosso dalla memoria, altrimenti in chat_messages
    # si accumulerebbero richieste dell'utente in fila. L'errore è gestito visivamente nel main
    except Exception:
        chat_messages.pop()
        return None
    else:
        chat_messages.append({"role": "assistant", "content" : response.choices[0].message.content})
        
        # Valutazione superamento soglia messaggi in memoria
        trim_history(chat_messages)
        
        return response.choices[0].message.content