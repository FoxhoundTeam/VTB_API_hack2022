def do_insert(collection, document):
    result = collection.insert_one(document)
    return result


def do_find(collection, params=None):
    documents = []
    for document in collection.find(params):
        documents.append(document)
    return documents
