from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


# Example intent templates
DIRECT_QA_EXAMPLES = [
    "what is this error",
    "define timeout",
    "explain authentication failure",
    "why did server crash",
    "what caused database issue",
    "describe memory leak",
    "how to fix redis failure"
]

CLUSTER_EXAMPLES = [
    "find similar logs",
    "group repeated errors",
    "cluster timeout issues",
    "detect anomalies",
    "show recurring failures",
    "find patterns in logs",
    "identify repeated login attempts"
]


# Precompute embeddings
qa_emb = model.encode(DIRECT_QA_EXAMPLES)
cluster_emb = model.encode(CLUSTER_EXAMPLES)


class QueryRouter:

    def __init__(self, threshold=0.45):
        self.threshold = threshold

    def classify(self, query):

        q_emb = model.encode([query])

        qa_score = cosine_similarity(q_emb, qa_emb).max()
        cluster_score = cosine_similarity(q_emb, cluster_emb).max()

        # Additional semantic keyword boosting
        cluster_keywords = [
            'cluster',
            'group',
            'similar',
            'pattern',
            'repeated',
            'recurring',
            'anomaly',
            'trend',
            'multiple'
        ]

        qa_keywords = [
            'what',
            'why',
            'define',
            'explain',
            'describe',
            'how'
        ]

        query_lower = query.lower()

        for word in cluster_keywords:
            if word in query_lower:
                cluster_score += 0.15

        for word in qa_keywords:
            if word in query_lower:
                qa_score += 0.10

        print(f'QA Score: {qa_score}')
        print(f'Cluster Score: {cluster_score}')

        if cluster_score > qa_score:
            return 'cluster'

        return 'direct_qa'