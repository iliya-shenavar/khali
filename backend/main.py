from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS برای اجازه ارتباط با Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # بهتره فقط دامنه خاص مجاز باشه در پروژه واقعی
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/message")
def read_message():
    return {"message": "Hello from Backend"}
