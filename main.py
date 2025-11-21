from fastapi import FastAPI
import uvicorn
from fastapi.responses import StreamingResponse, HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/ottaviadaracollection/static", StaticFiles(directory="./static"), name="static")

@app.get("/")
async def read_root():
    # return index page mounted at static files
    return FileResponse("index.html")

if __name__ == "__main__":
    # Run uvicorn
    uvicorn.run(app)