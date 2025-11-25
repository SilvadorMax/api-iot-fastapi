from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()

POWERBI_URL = "https://api.powerbi.com/beta/1eba443f-23e5-4534-90d1-0976aabe86ac/datasets/9a7cf147-9106-47ed-9700-8f58cd7aa86a/rows?experience=power-bi&key=EsEmk55IZgh9aG7Pni%2BFz%2FBdhm9S4UAnzjaGAvqVdoPxwzcuWOv3BY8Uk3UIX6s8E5cn4pAqMgdwezbx5yv4qA%3D%3D"

@app.get("/")
def root():
    return {"status": "API funcionando en Render"}

@app.post("/sensor")
def sensor_data(data: dict):

    # Aquí puedes hacer suavizado matemático si quieres
    # Por ahora lo dejamos sin suavizar

    # Enviar a Power BI (opcional mientras pruebas)
    # requests.post(POWERBI_URL, json=[data])

    return {"status": "ok", "received": data}
