from fastapi import FastAPI

app = FastAPI()

@app.get("/")
@app.get("/api/index")
def home():
    return {"status": "ok", "message": "Flutter AI Brain is running!"}

@app.get("/ask")
def ask(question: str = "Hello"):
    return {"question": question, "answer": f"Brain says: {question}"}
