from fastapi import FastAPI, Request

app = FastAPI()

resim = "https://i.dr.com.tr/cache/500x400-0/originals/0000000669765-1.jpg"
resim2 = "https://m.media-amazon.com/images/I/81XdUdc3sVL._AC_UF894,1000_QL80_.jpg"  # url yokken de ekrana geliyor.

@app.get("/get_resim_url")
async def get_resim_url():
        return "index.html", { "image_url": resim, "img": resim2}

