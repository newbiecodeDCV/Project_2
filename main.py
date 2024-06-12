from Prompt import prompt
from langchain_openai import  ChatOpenAI
from load_dotenv import load_dotenv
from Rag import retriever
from langchain_core.runnables import RunnablePassthrough
from Prompt import prompt
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo-0125")
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
chain = (
    {"context": retriever | format_docs,"question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

x = chain.invoke('Bạn có biết gì về du lịch ở Đà Nẵng không')






print(x)