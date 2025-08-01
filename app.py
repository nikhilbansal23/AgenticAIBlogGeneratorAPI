import uvicorn
from fastapi import FastAPI,Request
from src.graphs.graphbuilder import GraphBuilder
from src.llms.groqllm import GroqLLM

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


## api

@app.post("/blogs")
async def create_blog(request: Request):
    """
    Endpoint to create a blog based on the provided topic.
    """
    data = await request.json()
    topic = data.get("topic","")
    language = data.get("language","")

    ## get the llm object
    groq_llm = GroqLLM()
    llm = groq_llm.get_llm()

    ## get the graph
    graph_builder = GraphBuilder(llm)
    if topic and language:
        graph=graph_builder.setup_graph(usecase="language")
        state=graph.invoke({"topic":topic,"current_language":language.lower()})
    elif topic:
        graph=graph_builder.setup_graph(usecase="topic")
        state=graph.invoke({"topic":topic})
    
    return {"data":state}

if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)

    
    
