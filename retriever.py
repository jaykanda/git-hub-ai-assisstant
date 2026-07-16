from vectordb import vector_Store

def retrieval_search(userquery):

    vector_store_indexes = vector_Store()
    results = vector_store_indexes.similarity_search(
        userquery,
        k = 1
    )
    # print(f"retrieved results ===> {results}")
    return results
