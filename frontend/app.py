import streamlit as st
import requests

# PAGE SETTINGS #

st.set_page_config(
    page_title="EnterpriseGPT",
    layout="wide"
)

# CUSTOM CSS  #

st.markdown("""
<style>

.stApp{
background-color:#0F1117;
}


/* Title */

.main-title{

font-size:42px;
font-weight:700;

text-align:center;

color:white;

margin-top:20px;
margin-bottom:5px;

font-family:sans-serif;

}


/* Subtitle */

.subtitle{

text-align:center;

font-size:16px;

color:#A0A0A0;

margin-bottom:35px;

}


/* Sidebar */

[data-testid="stSidebar"]{

background-color:#161A20;

}


/* Chat */

.stChatMessage{

background-color:#1A1D24;

padding:15px;

border-radius:10px;

margin-bottom:12px;

border:none;

}


/* Footer */

.footer{

text-align:center;

color:#808080;

font-size:13px;

margin-top:50px;

}

</style>

""", unsafe_allow_html=True)


#  CHAT HISTORY#

if "messages" not in st.session_state:

    st.session_state.messages=[]


# HEADER  #

st.markdown(
"""
<div class="main-title">

EnterpriseGPT

</div>

<div class="subtitle">

Intelligent document understanding powered by AI

</div>

""",
unsafe_allow_html=True
)


# SIDEBAR #

with st.sidebar:

    st.markdown("### Upload Documents")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        with st.spinner(
            "Processing..."
        ):

            files=[

                (
                    "files",
                    (
                        uploaded_file.name,
                        uploaded_file,
                        "application/pdf"
                    )
                )

            ]

            response=requests.post(
                "http://127.0.0.1:8000/upload",
                files=files
            )

            result=response.json()

            if "message" in result:

                st.success(
                    result["message"]
                )

            else:

                st.error(
                    result["error"]
                )


    st.markdown("---")

    st.caption("""
AI Powered

PDF Analysis

Smart Retrieval

Gemini + Pinecone
""")


#  DISPLAY CHAT  #

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


#  INPUT #

question=st.chat_input(
    "Ask anything from uploaded document..."
)


if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message(
        "user"
    ):

        st.write(
            question
        )



    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Thinking..."
        ):

            response=requests.post(
                "http://127.0.0.1:8000/chat",
                params={
                    "question":question
                }
            )

            result=response.json()

            answer=result.get(
                "answer",
                "No response received"
            )

            st.write(
                answer
            )



    st.session_state.messages.append(

        {
            "role":"assistant",
            "content":answer
        }

    )


#  FOOTER  #

st.markdown(
"""
<div class="footer">

EnterpriseGPT | FastAPI + Gemini + Pinecone

</div>
""",
unsafe_allow_html=True
)