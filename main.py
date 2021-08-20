from fastapi import FastAPI, HTTPException
import random
import os
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/rand")
async def rand_Image():
    images = os.listdir("images/")

    imageID = random.randint(0, len(images)-1)
    path = "images/"+images[imageID]
    return FileResponse(path)


@app.get("/index")
async def index_of_archives():
    images = os.listdir("images/")
    
    return images


@app.get("/{query}")
async def specific_Image(query: str):
    query = query.lower()
    images = os.listdir("images/")

    if query+".png" in images:
        query += ".png"
        path = "images/"+query
    elif query.isdigit():
        path = "images/"+images[int(query) % len(images)]
    else:
        raise HTTPException(status_code=404, detail="404: Item not found")
    return FileResponse(path)
