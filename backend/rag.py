from backend.embeddings import embedding_model
from backend.pinecone_db import search_embeddings


def retrieve_context(
    question
):

    query_embedding=embedding_model.embed_query(
        question
    )

    results=search_embeddings(
        query_embedding
    )

    context=""

    for match in results["matches"]:

        if "text" in match["metadata"]:

            context+=(
                match["metadata"]["text"]
                + "\n"
            )

    return context