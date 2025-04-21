# Practical 1 : Implementation of a Basic Document Retrieval System Using an Inverted Index in Python. 

from collections import defaultdict 

class InvertedIndex:
    
    def __init__(self, documents):
        
        self.documents = documents
        self.index = defaultdict(set)
        self.build_index()
        
    def build_index(self):
        
        for doc_id, text in self.documents.items():
            words = set(text.lower().split())
            
            for word in words:
                self.index[word].add(doc_id)
                
    def search(self, query):
        
        query_words = query.lower().split()
        
        if not query_words:
            return set()
        
        result_set = [self.index[word] for word in query_words if word in self.index]
        
        if not result_set:
            return set()
        
        return set.intersection(*result_set)
    

documents = {
    1: "Web content extraction involves retrieving structured data",
    2: "Search engines use document indexing for efficient retrieval",
    3: "Document retrieval is important in web mining applications",
    4: "Indexing helps in retrieving relevant documents based on query terms" 
}

index = InvertedIndex(documents)

queries = ["retrieval", "document indexing", "web mining", "structured data"]

for query in queries:
    result = index.search(query)
    print(f"Query : '{query}' -> Documents : {sorted(result) if result else 'No Matching Documents'}")