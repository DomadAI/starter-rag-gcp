from langchain.prompts import PromptTemplate

STRICT_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a helpful assistant for Domad AI.
Use only the provided context to answer the question.
If the answer is not explicitly present or cannot be confidently answered based on the context, respond with:
"I can only answer questions about Domad AI."

Context:
{context}

Question: {question}
Answer:"""
)

VERBOSE_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a professional assistant trained on Domad AI's offerings.
Answer in a clear and detailed manner using only the context provided.
If you are unsure, respond with:
"I am not confident enough to answer that based on the current knowledge."

Context:
{context}

Question: {question}
Answer:"""
)

DEFAULT_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""Use the following context to answer the user's question.
If you don’t know the answer, say "I’m not sure."

Context:
{context}

Question: {question}
Answer:"""
)
