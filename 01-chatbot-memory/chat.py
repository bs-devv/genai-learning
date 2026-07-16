from config import MAX_LENGTH_MESSAGES, MODEL_NAME, TEMPERATURE


def trim_history(chat_messages):
    if len(chat_messages) > MAX_LENGTH_MESSAGES:
            del chat_messages[1:3]

def send_message(client, chat_messages):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=chat_messages,
            temperature=TEMPERATURE
        )
    except Exception:
        chat_messages.pop()
        return None
    else:
        chat_messages.append({"role": "assistant", "content" : response.choices[0].message.content})
        
        trim_history(chat_messages)
        
        return response.choices[0].message.content