"""API del motor multimodal — owner: Alejandro Marcelo.

Correr en local:
    uvicorn backend.main:app --reload
"""
from fastapi import FastAPI

app = FastAPI(title="Motor Multimodal — BD2 Proyecto 2")


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO App1: POST /buscar/audio   -> subir un fragmento, devolver top-k tracks similares.
# TODO App2: GET  /buscar/texto   -> query en lenguaje natural, devolver tracks por género/tags.
