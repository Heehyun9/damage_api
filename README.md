# TrustRide AI - 차량 손상 및 가격 예측 API

- 이 프로젝트는 차량 이미지를 분석하여 손상 여부를 판단하고, 차량 정보를 기반으로 예상 가격을 계산하는 API를 제공합니다.
- "TrustRide_AI" 라는 중고차 거래 플랫폼을 구성하고 있는 AI 기능중 하나 입니다. 
- 실제 구현방식을 알고 싶으시다면 아래의 링크를 통해 보실 수 있습니다.
- 참고 (TrustRide_AI Repo : - https://github.com/TrustRide/TrustRide_AI.git)
- cursor AI 사용

## 주요 기능

- 차량 이미지 기반 손상 감지
- 차량 정보 기반 가격 예측
- 손상 정도에 따른 감가율 적용

## 모델 훈련 관련 Colab ipynb 파일

- 가격 예측 모델 : https://colab.research.google.com/drive/18Z4rwyWq1vD4xuHeV6xeMM4d9g8d3Wcb?usp=sharing
- 이미지 손상 탐지 모델 : https://colab.research.google.com/drive/1-OHylgW5yMJOtUGZWOdxJGAFY_2a0fwP?usp=sharing


## 기술 스택

- FastAPI
- PyTorch
- LightGBM
- scikit-learn
- PIL
- Python


## 설치 방법

1. 가상환경 생성 및 활성화:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

2. 의존성 설치:
```bash
pip install -r requirements.txt
```

3. 모델 파일 준비:
- `models/` 디렉토리에 필요한 모델 파일들을 배치

4. 서버 실행:
```bash
uvicorn app:app --reload
```

## API 엔드포인트

- POST `/carpredict`: 차량 이미지와 정보를 받아 손상 및 가격 예측
- GET `/carpredict/health`: API 상태 확인



## 보안 및 개인정보

- API 키와 민감한 정보는 환경 변수로 관리
- 업로드된 이미지는 임시 저장 후 삭제

## 라이선스

[라이선스 정보 입력] 

## 참고자료 
- 회고록 :
- 블로그 : 
