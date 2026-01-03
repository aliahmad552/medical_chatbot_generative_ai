from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from src.prompt import *
from src.helper import download_embeddings,format_docs
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableParallel
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = FastAPI()

# Static and template setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

embeddings = download_embeddings()

index_name = "my-index-v1" 
# Embed each chunk and upsert the embeddings into your Pinecone index.
vc = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = vc.as_retriever(search_type="similarity", search_kwargs={"k":3})

parallel_chain = RunnableParallel({
    "context": itemgetter('question') | retriever | RunnableLambda(format_docs),
    "question": itemgetter('question')
})

model = ChatOpenAI(model_name = 'gpt-4o-mini')

chain = parallel_chain | prompt | model | StrOutputParser()

# Home route
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/chat", response_class=PlainTextResponse)
async def chat(msg: str = Form(...)):
    print(msg)

    response = chain.invoke({"message": msg})
    answer = response["answer"]

    print("Response:", answer)
    return answer