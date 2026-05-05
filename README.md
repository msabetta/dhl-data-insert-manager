# 🚚 DHL / BlueDart Middleware API (FastAPI)

API REST per la gestione delle spedizioni e tracking integrata con **BlueDart / DHL API Gateway**.

Questo progetto funge da middleware tra sistemi aziendali (es. SAP ERP) e DHL/BlueDart, permettendo di generare Waybill, aggiornare eWaybill, annullare spedizioni e importare dati logistici in tempo reale.

---

## ⚙️ Stack tecnologico

* Python 3.10+
* FastAPI
* Requests
* Pydantic
* DHL / BlueDart REST API (Gateway)
* Autenticazione basata su JWT Token

---

## 📦 Funzionalità

* **Generazione Waybill**: Creazione di documenti di trasporto via BlueDart API.
* **Annullamento Waybill**: Cancellazione di spedizioni esistenti.
* **Aggiornamento eWaybill**: Integrazione e aggiornamento dei dati fiscali per le spedizioni.
* **Importazione Dati**: Caricamento massivo di informazioni logistiche (Consignee, Shipper, Services).
* **Autenticazione JWT**: Gestione automatica del token di sessione per le chiamate al Gateway.

---

## 🧱 Architettura

```
SAP / ERP System
        ↓
   FastAPI Middleware
        ↓
  DHL / BlueDart API Gateway
```

---

## 🚀 Avvio progetto

### 1. Installazione dipendenze

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2. Configurazione environment

Crea un file `.env` basato sulle tue credenziali BlueDart:

```env
DHL_API_KEY=vostro_client_id
DHL_API_SECRET=vostro_client_secret
BASE_URL="https://apigateway-sandbox.bluedart.com/"
```

---

### 3. Avvio server

```bash
uvicorn main:app --reload
```

---

### 4. Documentazione API

Dopo l’avvio, la documentazione interattiva (Swagger UI) è disponibile su:

```
http://127.0.0.1:8000/docs
```

---

## 📡 Endpoint API

### 🔹 Generare Waybill
`POST /waybill/GenerateWayBill`
Genera una nuova Waybill BlueDart.

### 🔹 Annullare Waybill
`POST /waybill/CancelWayBill`
Annulla una Waybill esistente tramite AWB Number.

### 🔹 Aggiornare eWaybill
`POST /waybill/UpdateEwayBill`
Aggiorna i dettagli della fattura e della eWaybill per una spedizione.

### 🔹 Importare Dati
`POST /importData`
Importazione completa di dati consignee, shipper e service.

### 🔹 Health check
`GET /health`
Verifica lo stato del middleware.

---

## 🔐 Sicurezza

* Autenticazione dinamica via JWT (token generato automaticamente).
* Credenziali sensibili gestite via variabili d'ambiente (`.env`).
* Validazione rigorosa degli schemi dati tramite Pydantic.

---

## 📁 Struttura progetto

```
dhl-data-insert-manager/
│
├── main.py          # Entry point FastAPI e rotte
├── dhl_service.py   # Logica di integrazione API BlueDart/DHL
├── schemas.py       # Modelli dati Pydantic
├── config.py        # Gestione configurazione env
├── .env             # Variabili d'ambiente (non versionate)
└── README.md        # Documentazione
```

## 📌 Note

Questo progetto è un middleware tecnico per integrazione logistica specifico per i servizi BlueDart/DHL Gateway.


## 📜 Licenza

MIT License
