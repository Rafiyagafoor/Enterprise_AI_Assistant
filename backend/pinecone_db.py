from pinecone import Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv()

pc=Pinecone(
    api_key=os.getenv(
        "PINECONE_API_KEY"
    )
)

index_name="enterprise-ai"

existing=[
    i["name"]
    for i in pc.list_indexes()
]

if index_name not in existing:

    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

index=pc.Index(
    index_name
)


def store_embeddings(
    chunks,
    embeddings
):

    vectors=[]

    for i,(chunk,embedding) in enumerate(
        zip(
            chunks,
            embeddings
        )
    ):

        vectors.append(
            {
                "id":str(i),
                "values":embedding,
                "metadata":{
                    "text":chunk
                }
            }
        )

    index.upsert(
        vectors=vectors
    )


def search_embeddings(
    query_embedding
):

    result=index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True
    )

    return result