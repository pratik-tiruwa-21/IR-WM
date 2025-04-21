# Practical 3 : Spelling Correction in information Retrieval systems Using Levenshtein Distance

from collections import defaultdict
import numpy as np


class InvertedIndex: 
    
    def __init__(self, documents): 
        
        self.documents = documents
        self.index = defaultdict(set)
        self.vocabulary = set()
        self.build_index()
        
        
    def build_index(self):
        
        for doc_id, text in self.documents.items():
            words = set(text.lower().split())
            self.vocabulary.update(words)
            
            for word in words:
                self.index[word].add(doc_id)
        
    
    def search(self, query):
        
        corrected_words = [self.correct_spelling(word) for word in query.lower().split()]
        print(f"Corrected Query : {' '.join(corrected_words)}")
        
        result_sets = [self.index[word] for word in corrected_words if word in self.index]
        
        if not result_sets:
            return set()
        
        return set.intersection(*result_sets)
        
        
    def correct_spelling(self, word):
        
        min_distance = float('inf')
        best_match = word
        
        for vocab_word in self.vocabulary:
            distance = self.levenshtein_distance(word, vocab_word)
            if distance < min_distance:
                min_distance = distance
                best_match = vocab_word
                
        return best_match
        
        
        
    def levenshtein_distance(self, s1, s2):
        
        len_s1, len_s2 = len(s1), len(s2)
        dp = np.zeros((len_s1 + 1, len_s2 + 1), dtype=int)
        
        for i in range(len_s1 + 1):
            for j in range(len_s2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i  
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] 
                else:
                       dp[i][j] = 1 + min(
                           dp[i - 1][j],
                           dp[i][j - 1],
                           dp[i - 1][j - 1]
                       )  
        return dp[len_s1][len_s2]
    
    
documents = {
    1: "Web content extraction involves retrieving structured data",
    2: "Search engines use document indexing for efficient retrieval", 
    3: "Document retrieval is important in web mining applications",
    4: "Indexing helps in retrieving relevant documents based on query terms"
}

index = InvertedIndex(documents)
queries = ["retrievel", "document indexig", "web minng", "structure data"]

print("\n ==== Spelling Correction and Document Retrieval === ")
for query in queries:
    result = index.search(query)
    print(f"Query : '{query}' -> Corrected Documents : {sorted(result) if result else 'No matching documents'}")