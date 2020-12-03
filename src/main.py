from typing import Optional
from fastapi import FastAPI
import uvicorn as uvicorn
from server import *
import webbrowser
import time

tags_metadata = [
    {
        "name": "Get Similar Words",
        "description": "Returns all words in the dictionary that has the same permutation as the word.",
        "externalDocs": {
        "description":"example",
            "url": "http://localhost:8000/api/v1/similar/?word=destain",
        },
    },
    {
        "name": "Get Statistics",
        "description": "Return statistics about api",
        "externalDocs": {
            "description": "example",
            "url": "http://localhost:8000/api/v1/stats/",
        },
    },
    {
            "name": "Docs Api",
            "description": "Return all function in API",
            "externalDocs": {
                "description": "example",
                "url": "http://localhost:8000/docs",
            },
        },
]

app = FastAPI( title="Api Similar Words",openapi_tags=tags_metadata)


@app.get("/",tags=["Docs Api"])
def docs_api():
    webbrowser.open('http://localhost:8000/docs')




@app.get("/api/v1/similar/",tags=["Get Similar Words"])
async def get_words (word: Optional[str] = None):
    start_time = time.time_ns()
    if word:
        response= Server().similar_words(word.lower(),start_time)
        return response
    else:
        return {"word":[""]}



@app.get("/api/v1/stats/",tags=["Get Statistics"])
async def get_stat():
        response = Server().metrics()
        return response




if __name__ == "__main__":
    try:
        #sort data for new dictionary
        data = Data()
        data.read_words()
        data.save_sorted_words()
        # run API server
        uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True, workers=20)
    except Exception as error:
        print(error)



















