
from qdrant_client import QdrantClient
from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel

app = FastAPI()


qdrant_client = QdrantClient(
    url="https://f575a6c0-4880-4ba1-bac4-ce3febd5e83a.us-east4-0.gcp.cloud.qdrant.io",
    api_key="P9qpgcryuCBF8c78hYU4QwImfJIkZimHXZSIBqfax6W3rGi-LNwN4g",
)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class UserCreate(BaseModel):
    query: str

@app.post("/food&lifestyle_changes")
async def read_root(query_data: UserCreate):
    query = query_data.query
    #query = "Harry was admitted on 18/04/2013 in xyz hospital due to suddent chest pain and was treated for sudden heart attack."
    ques_vector = model.encode(query)

    result = qdrant_client.search(
        collection_name="food_lifestyle_data",
        query_vector=ques_vector,
        limit=1,

    )
    return {"food":result[0].payload["food"],"lifestyle":result[0].payload["lifestyle"]}


# print(result[0])
