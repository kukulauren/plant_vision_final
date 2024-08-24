from langchain_chroma import Chroma
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = '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'
llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key="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")
embedding_model = OpenAIEmbeddings(openai_api_key="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")
vectorstore = Chroma(
    persist_directory="/Users/khinmyatnoe/PycharmProjects/finalproject/app/my_vectorstore_final",
    embedding_function=embedding_model
)
retriever = vectorstore.as_retriever()
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

prompt = hub.pull("rlm/rag-prompt")
rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)
# answer=rag_chain.invoke('ဆီအုန်းစိုက်ပျိုးရေးအကြောင်းရှင်းပြပါ')
# print(answer)