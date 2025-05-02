import pickle
import lightgbm as lgb

# 모델 저장
def save_model(model, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)

# 모델 불러오기
def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model

# txt 모델을 pkl로 변환
model = lgb.Booster(model_file='models/lgbm_price_model.txt')
save_model(model, 'models/lgbm_price_model.pkl')

print("모델 변환이 완료되었습니다.")