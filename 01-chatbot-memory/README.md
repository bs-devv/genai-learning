# 01 - Chatbot conversazionale con memoria

Chatbot da terminale in Python che mantiene il contesto della conversazione, scritto per imparare i meccanismi di base di interazione con un LLM via API (senza framework).

## Funzionalità

- Conversazione continua con memoria: ogni messaggio tiene conto dei precedenti
- Il comando `reset` azzera la conversazione senza riavviare il programma, mentre il comando `exit` termina il programma
- Gestione automatica della lunghezza della memoria: superata una soglia, i messaggi più vecchi vengono rimossi per restare nei limiti di contesto del modello
- Gestione errori: se la chiamata all'API fallisce, il programma non crasha e il messaggio non riuscito viene rimosso dalla cronologia

## Struttura del progetto

01-chatbot-memory/
├── main.py # ciclo principale della conversazione
├── chat.py # logica di invio messaggi e gestione della memoria
└── config.py # impostazioni (modello, temperature, limiti)

## Cosa ho imparato

- Un LLM è **stateless**: la "memoria" della conversazione è simulata inviando l'intera cronologia dei messaggi ad ogni chiamata
- Il ruolo dei messaggi (`system`, `user`, `assistant`) e come costruire correttamente una cronologia coerente
- Gestione del **context window**: la memoria non può crescere all'infinito, va troncata mantenendo il system prompt
- Separazione della logica in moduli per un codice più leggibile e testabile
- Gestione degli errori di rete/API senza rompere lo stato della conversazione