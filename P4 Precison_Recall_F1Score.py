# Practical 4 :  Implementation of Evaluation Metrics for IR Systems (Precision, Recall, F-1 Score) 

def calculate_precision(tp, fp):
    
    if tp + fp == 0:
        return 0.0 
    return tp / (tp + fp)


def calculate_recall(tp, fn):
    
    if tp + fn == 0:
        return 0.0 
    return tp / (tp + fn)


def calculate_f1_Score(precision, recall):
    
    if precision + recall == 0:
        return 0.0 
    return 2 * (precision * recall) / (precision + recall)


def evaluate_retrieval(relevant_docs, retrieved_docs):
    
    tp = len(relevant_docs & retrieved_docs) 
    fp = len(retrieved_docs - relevant_docs)
    fn = len(relevant_docs - retrieved_docs)
    
    precision = calculate_precision(tp, fp)
    recall = calculate_recall(tp, fn)
    f1_score = calculate_f1_Score(precision, recall)
    
    return tp, fp, fn, precision, recall, f1_score


relevant_documents = {1, 2, 3, 5, 7}
retrieved_documents = {1, 2, 4, 5, 6}

tp, fp, fn, precision, recall, f1_score = evaluate_retrieval(relevant_documents, retrieved_documents)

print("\n ==== Evaluation Metrics for Information Retrieval ==== ")
print(f"True Positives : {tp}")
print(f"False Positives : {fp}")
print(f"False Negatives : {fn}")
print(f"Precision : {precision}")
print(f"Recall : {precision}")
print(f"F1-Score : {f1_score}")