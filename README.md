# 🚚 DHL Middleware API (FastAPI)

API REST per la gestione delle spedizioni e tracking integrata con DHL MyDHL API.

Questo progetto funge da middleware tra sistemi aziendali (es. SAP ERP) e DHL, permettendo di creare spedizioni, generare etichette e tracciare pacchi in tempo reale.

---

## ⚙️ Stack tecnologico

* Python 3.10+
* FastAPI
* Requests
* Pydantic
* DHL MyDHL API (Sandbox/Production)

---

## 📦 Funzionalità

* Creazione spedizioni via DHL API
* Generazione automatica etichette PDF
* Tracking spedizioni in tempo reale
* Validazione dati strutturata
* Middleware pronto per integrazione SAP / ERP

---

## 🧱 Architettura

```
SAP / ERP System
        ↓
   FastAPI Middleware
        ↓
  DHL MyDHL API
```

---

## 🚀 Avvio progetto

### 1. Installazione dipendenze

```bash
pip install fastapi uvicorn requests python-dotenv
```

---

### 2. Configurazione environment

Crea un file `.env`:

```
DHL_API_KEY=your_api_key
BASE_URL=https://api-mydhl-qa.dhl.com
```

---

### 3. Avvio server

```bash
uvicorn main:app --reload
```

---

### 4. Documentazione API

Dopo l’avvio:

```
http://127.0.0.1:8000/docs
```

---

## 📡 Endpoint API

### 🔹 Creare spedizione

`POST /shipments`

```json
{
  "shipper": {
    "name": "Company SRL",
    "address": "Via Roma 1",
    "city": "Napoli",
    "postal_code": "80100",
    "country": "IT",
    "phone": "+390000000"
  },
  "receiver": {
    "name": "Mario Rossi",
    "address": "Via Milano 10",
    "city": "Milano",
    "postal_code": "20100",
    "country": "IT",
    "phone": "+390000000"
  },
  "package": {
    "weight": 5,
    "length": 30,
    "width": 20,
    "height": 10
  },
  "service": "P"
}
```

---

### 🔹 Tracking spedizione

`GET /track/{tracking_number}`

---

### 🔹 Health check

`GET /health`

---

## 📄 Output

* Tracking number DHL
* File etichetta PDF
* Stato spedizione

---

## 🔌 Integrazione SAP

Il sistema può essere integrato con:

* SAP CPI (Cloud Platform Integration)
* IDoc / RFC
* REST API via ABAP

Flusso tipico:

```
Sales Order → Delivery → Middleware → DHL → Tracking → SAP Update
```

---

## 🧪 Sandbox DHL

Per test usare:

```
https://api-mydhl-qa.dhl.com
```

---

## 📁 Struttura progetto

```
project/
│
├── main.py
├── dhl_service.py
├── schemas.py
├── config.py
├── .env
└── README.md
```

---

## 🔐 Sicurezza

* API Key in `.env`
* Nessun dato sensibile nel repository
* Logging errori abilitato

---

## 🚀 Possibili estensioni

* Autenticazione JWT
* Database PostgreSQL
* Dashboard tracking spedizioni
* Webhook DHL
* Container Docker

---

## 📌 Note

Questo progetto è un middleware tecnico per integrazione logistica e non sostituisce le API ufficiali DHL.

---

## 📜 Licenza

MIT License
