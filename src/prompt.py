from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(
    template ="""
    You are a helpful assistent.
    Answer Only from the provedid context.
    If the context is insufficient, just say you don't know.
    {context}
    Question: {question}
    """,
    input_variables=['context','question']
)