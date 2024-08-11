# from langchain_chroma import Chroma
# from langchain import hub
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
#
# llm = ChatOpenAI(model="gpt-4o-mini", openai_api_key="sk-proj-GaLPmq1cEwOIoOctb8sXT3BlbkFJGiU2jNLx4c5ibssFFLUp")
# embedding_model = OpenAIEmbeddings(openai_api_key="sk-proj-GaLPmq1cEwOIoOctb8sXT3BlbkFJGiU2jNLx4c5ibssFFLUp")
# vectorstore = Chroma(
#     persist_directory="/Users/khinmyatnoe/PycharmProjects/finalproject/app/my_vectorstore",
#     embedding_function=embedding_model
# )
# retriever = vectorstore.as_retriever()
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)
#
# prompt = hub.pull("rlm/rag-prompt")
# rag_chain = (
#         {"context": retriever | format_docs, "question": RunnablePassthrough()}
#         | prompt
#         | llm
#         | StrOutputParser()
# )