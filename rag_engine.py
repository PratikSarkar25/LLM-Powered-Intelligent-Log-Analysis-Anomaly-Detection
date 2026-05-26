import chromadb
from sentence_transformers import SentenceTransformer
import requests

client = chromadb.PersistentClient(path='chroma_db')
collection = client.get_or_create_collection('logs')
model = SentenceTransformer('all-MiniLM-L6-v2')


def build_index(df):
    docs = []
    ids = []
    for i,row in df.iterrows():
        txt = f"{row['timestamp']} | {row['level']} | {row['service']} | {row['message']}"
        docs.append(txt)
        ids.append(str(i))
    emb = model.encode(docs).tolist()
    collection.upsert(ids=ids, documents=docs, embeddings=emb)


def search_logs(query, k=5):
    q = model.encode([query]).tolist()
    res = collection.query(query_embeddings=q, n_results=k)
    return res['documents'][0]


# def ask_llm(prompt):
#     r = requests.post('http://localhost:11434/api/generate', json={
#         'model':'llama3.2:3b',
#         'prompt':prompt,
#         'stream':False
#     }, timeout=120)
#     return r.json()['response']

def ask_llm(prompt):
    r = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'llama3.2:3b',
            'prompt': prompt,
            'stream': False
        }
    )

    data = r.json()

    print("\n===== RAW LLM RESPONSE =====")
    print(data)

    return data.get('response', str(data))


def answer_query(query):
    docs = search_logs(query)
    context = '\n'.join(docs)
    prompt = f'''You are an enterprise log analyst. Use context to answer.\nContext:\n{context}\n\nQuestion:{query}\nAnswer clearly with root cause and remediation.'''
    return ask_llm(prompt)
    print("\n===== RETRIEVED LOGS =====")
    print(context)



