import pprint

import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.post("/")
def read_root(data):
    pprint.pprint(data)

if __name__ == '__main__':
    uvicorn.run(app='server:app', host="0.0.0.0", port=8000, reload=True)