from fastapi import APIRouter, status

from app.company.schema import CompanyBase
from app.ai.schema import AiSimulateGenerate

router = APIRouter(
    tags=["AI"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/ai-simulate",
    response_model=CompanyBase,
    status_code=status.HTTP_200_OK,
)
async def ai_simulate(ai_simulate_generate: AiSimulateGenerate):
    return {
        "company_name": "Example Inc.",
        "what_you_do": "We provide cloud-based solutions for digital transformation.",
        "products_services": "SaaS ERP, AI Chatbots, Custom Software Development.",
        "problems_solved": "Slow digital adoption, inefficient manual processes, lack of integration.",
        "what_makes_special": "We focus on speed, customization, and long-term client partnerships.",
        "success_stories": "Helped ABC Corp reduce costs by 40% in 6 months.",
        "client_process": "Discovery → Proposal → Development → Launch → Support.",
        "expected_results": "Faster workflows, increased ROI, scalable solutions.",
    }
