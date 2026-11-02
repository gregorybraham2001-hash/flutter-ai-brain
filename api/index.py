from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "Flutter AI Brain is running!"}

@app.get("/ask")
def ask(question: str = "Hello"):
    return {"question": question, "answer": f"AI Brain received: {question}. Working!"}

@app.post("/ask")
def ask_post(data: dict):
    q = data.get("question", "Hello")
    return {"question": q, "answer": f"AI Brain received: {q}. Working!"}
