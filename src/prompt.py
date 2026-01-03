from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(
    template ="""You are a medical assistant.

Use the provided context to answer the question.
If the context is insufficient, use your general medical knowledge,
but clearly mention when the answer is not fully supported by the documents.

Context:
{context}

Question:
{question}

Answer:""",
    input_variables=['context','question']
)