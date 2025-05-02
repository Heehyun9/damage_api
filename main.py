# main.py 서버 실행
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routers import predict_router  # ✅ 손상 + 가격 예측 통합 라우터

app = FastAPI(default_response_class=JSONResponse)

# ✅ Spring 연동을 위한 CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 시에는 도메인 제한 권장 (예: ["http://localhost:8080"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 라우터 등록 (통합된 손상 + 가격 예측)
app.include_router(predict_router.router)

@app.get("/")
async def root():
    return {"message": "🚀 FastAPI 통합 서버 정상 작동 중!"}