# Practical 2 : Implementation of Retrieval Models (Boolean Model and Vector Model)

from collections import defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class BooleanRetrieval:
    
    def __init__(self, documents):
        
        self.documents = documents
        self.inverted_index = defaultdict(set) 
        self.build_index()
        
    def build_index(self):
        
        for doc_id, text in self.documents.items():
            words = set(text.lower().split()) 
            
            for word in words:
                self.inverted_index[word].add(doc_id)
                
    def boolean_search(self, query):
        
        terms = query.lower().split() 
        result_set = set(self.documents.keys())
        
        operation = "AND" 
        
        for term in terms:
            if term == "and":
                operation == "AND"
            elif term == "or":
                operation == "OR"
            elif term == "not":
                operation == "NOT"
            else:
                if operation == "AND":
                    result_set &= self.inverted_index.get(term, set())
                elif operation == "OR":
                    result_set |= self.inverted_index.get(term, set())
                elif operation == "NOT":
                    result_set -= self.inverted_index.get(term, set())
                    
        return result_set
    
class VectorSpaceRetrieval:
    
    def __init__(self, documents):
        
        self.documents = documents
        self.vectorizer = TfidfVectorizer()
        self.doc_ids = list(documents.keys())
        self.doc_vectors = self.vectorizer.fit_transform(documents.values())
        
    def vector_search(self, query):
        
        query_vector = self.vectorizer.transform([query])
        similarities = np.dot(self.doc_vectors, query_vector.T).toarray().flatten()
        
        ranked_results = sorted(zip(self.doc_ids, similarities), key=lambda x: x[1], reverse=True)
        
        return ranked_results
    
    
documents = {
    1: "Web content extraction involves retrieving structured data",
    2: "Search engines use document indexing for efficient retrieval",
    3: "Document retrieval is important in web mining applications",
    4: "Indexing helps in retrieving relevant documents based on query terms" 
}

boolean_index = BooleanRetrieval(documents)

boolean_queries = ["retrieval AND document", "document OR indexing", "retrieval NOT indexing"]

print("\n ==== Boolean Retrieval Results ==== ")
for query in boolean_queries:
    result = boolean_index.boolean_search(query)
    print(f"Query : '{query}' -> Documents : {sorted(result) if result else 'No matching documents'}")
    

vector_index = VectorSpaceRetrieval(documents)

vector_queries = ["document retrieval", "web mining", "structured data"]

print("\n ===== Vector Space Model Results ===== ")
for query in vector_queries:
    result = vector_index.vector_search(query)
    print(f"Query : '{query}' -> Ranked Documents : {[(doc, round(float(score), 4)) for doc, score in result if score > 0]}")