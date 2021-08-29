from fastapi import FastAPI, HTTPException
import random
import os
from fastapi.responses import FileResponse

app = FastAPI()

directories = [
    "images/monster/",
]


@app.get("/")
async def index_of_images():
    files = {}

    for i in directories:
        dirFiles = os.listdir(i)
        dirFiles = [j[:-4] for j in dirFiles] #without file format

        files[i[7:-1]] = dirFiles #without images folder

    return files


@app.get("/{query}")
async def return_image(query: str):
    found = False
    query = query.lower()
    query += ".png"

    for i in directories:
        folderFiles = os.listdir(i)

        if query in folderFiles:
            path = i+query
            found = True
            break

    if found:
        return FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail="404: Item not found")


@app.get("/{directory}/id:{id_value}")
async def return_by_id(directory: str, id_value: int):
    path = "images/"+directory+"/"
    try:
        images = os.listdir(path)
    except:
        raise HTTPException(status_code=404, detail="404: Item not found")

    if(id_value < len(images)):
        path += images[id_value]
        return FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail="404: Item not found")