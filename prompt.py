import streamlit as st
from langchain_core.messages import HumanMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# ✅ Create the endpoint correctly
endpoint = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-30B-A3B-Instruct",  # chat-supported model
    huggingfacehub_api_token="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"
)

# ✅ Wrap endpoint inside ChatHuggingFace
model = ChatHuggingFace(llm=endpoint)

# ✅ Streamlit UI
st.title("Chat with Hugging Face Model")

user_input = st.text_input("Enter your prompt")

if user_input:
    response = model.invoke([HumanMessage(content=user_input)])
    st.write("Response:", response.content)


