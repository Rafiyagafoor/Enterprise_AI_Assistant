from fastapi import FastAPI, UploadFile, File
import os

from backend.pdf_handler import extract_text
from backend.splitter import split_text
from backend.embeddings import create_embeddings
from backend.pinecone_db import store_embeddings
from backend.rag import retrieve_context
from backend.llm import generate_answer

app = FastAPI()


# ---------------- PDF Upload ---------------- #

@app.post("/upload")
async def upload_pdf(
    files: list[UploadFile] = File(...)
):

    print("Upload API called")

    try:

        os.makedirs(
            "documents",
            exist_ok=True
        )

        for file in files:

            print(
                "Processing:",
                file.filename
            )

            file_path=f"documents/{file.filename}"

            with open(
                file_path,
                "wb"
            ) as f:

                content=await file.read()
                f.write(content)

            print("File saved")

            text=extract_text(
                file_path
            )

            print(
                "Text extracted"
            )

            chunks=split_text(
                text
            )

            print(
                "Total chunks:",
                len(chunks)
            )

            if not chunks:

                return {

                    "error":
                    "No chunks created"

                }

            embeddings=create_embeddings(
                chunks
            )

            print(
                "Embeddings created"
            )

            print(
                "Embedding size:",
                len(embeddings[0])
            )

            store_embeddings(
                chunks,
                embeddings
            )

            print(
                "Stored in Pinecone"
            )


        return {

            "message":
            "PDF uploaded successfully"

        }

    except Exception as e:

        print(
            "ERROR:",
            e
        )

        return {

            "error":
            str(e)

        }


# ---------------- Chat ---------------- #

@app.post("/chat")
def chat(
    question:str
):

    try:

        greetings=[

            "hi",
            "hello",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
            "how are you"

        ]


        question_clean=question.lower().strip()


        # Greeting responses

        if question_clean in greetings:

            return {

                "answer":
                """
Hello 👋

I'm EnterpriseGPT.

I can help you with:

• Answering questions from uploaded PDFs

• Summarizing documents

• Extracting important information

• Retrieving document content

Upload a document and ask anything.
                """
            }


        print(
            "Question:",
            question
        )


        context=retrieve_context(
            question
        )


        print(
            "Retrieved Context:"
        )

        print(
            context[:500]
        )


        # Nothing found

        if not context.strip():

            return {

                "answer":
                """
I could not find this information in the uploaded documents.

Please ask a question related to the uploaded document.
                """

            }


        answer=generate_answer(
            question,
            context
        )


        return {

            "answer":
            answer

        }

    except Exception as e:

        print(
            "Chat Error:",
            e
        )

        return {

            "error":
            str(e)

        }