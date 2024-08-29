from fastapi import FastAPI
import json

app = FastAPI()

# JSON dosyasını okuyalım ve içeriği bir Python sözlüğüne yükleyelim
with open("main4_Json.json", "r", encoding="utf-8") as dosya:
    muzik_verisi = json.load(dosya)

@app.get("/muzik/")
async def muzik_koleksiyonunu_getir():
    return muzik_verisi
