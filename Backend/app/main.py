from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.company.controller import router as company_router
from app.ai.controller import router as ai_router


Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Company",
    description="API to manage company information.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company_router)
app.include_router(ai_router)
