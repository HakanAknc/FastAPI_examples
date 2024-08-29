from fastapi import FastAPI, Query

app = FastAPI()

@app.post("/submit-text/")
async def submit_text(text: str = Query(...)):
    return {"received_text": text}
