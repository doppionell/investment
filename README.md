# 💹 Yen Investment Decision Support App

이 Streamlit 애플리케이션은 한국 원화 기준으로 엔화(JPY) 투자 타당성을 자동으로 분석해주는 도구입니다.

## 📊 기능
- 엑셀 파일(.xlsx) 업로드를 통한 경제지표 입력
- 실질금리차, 환헷지비용, 환율변동성, CDS 등을 반영한 투자 타당성 분석
- 종합 점수 산출 및 시각화

## 📝 사용 방법
1. `yen_investment_input.xlsx` 형식에 맞는 데이터를 준비하거나 샘플을 사용합니다.
2. 웹 애플리케이션에서 엑셀 파일을 업로드합니다.
3. 자동으로 분석 결과와 종합 점수를 확인할 수 있습니다.

## 📂 프로젝트 구조
```
investment/
├── yen_investment.py         # Streamlit 앱 메인 파일
├── yen_analysis_tool.py      # 투자 분석 함수 정의
├── requirements.txt          # 의존성 정의
└── README.md                 # 프로젝트 설명서
```

## 📦 설치 (로컬 개발 시)
```bash
pip install -r requirements.txt
streamlit run yen_investment.py
```

## 🔗 배포 링크
앱 실행 👉 [https://yeninvestment-aj9mavznh68epvnfdjf57r.streamlit.app](https://yeninvestment-aj9mavznh68epvnfdjf57r.streamlit.app)

---

Made with ❤️ by [doppionell](https://github.com/doppionell)
