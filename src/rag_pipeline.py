from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def build_chain(retriever, llm):
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    parallel_chain = RunnableParallel({
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    })

    prompt = PromptTemplate(
        template="""
        You are a helpful assistant. Use only the provided context to answer factually.
        If the context is insufficient, just say \"I don't know.\"

        Context:
        {context}

        Question: {question}
        """,
        input_variables=['context', 'question']
    )
    parser = StrOutputParser()

    chain = parallel_chain | prompt | llm | parser
    return chain