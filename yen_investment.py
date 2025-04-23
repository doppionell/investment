import streamlit as st
import pandas as pd
from datetime import datetime
from yen_analysis_tool import yen_investment_analysis, sample_input

st.set_page_config(page_title="엔화 투자 의사결정 도구", layout="wide")
st.title("💹 엔화 투자 의사결정 자동 분석 도구")

st.markdown("""
이 도구는 한국 원화 기준으로 엔화 투자 타당성을 자동 분석합니다. 엑셀 데이터를 업로드하거나 샘플 데이터를 사용해보세요.
""")

# 파일 업로드
uploaded_file = st.file_uploader("엑셀 파일 업로드 (.xlsx)", type=["xlsx"])

if uploaded_file:
    try:
        input_data = pd.read_excel(uploaded_file)
        st.success("업로드 성공! 입력 데이터를 분석합니다.")
    except Exception as e:
        st.error(f"파일을 불러오는 중 오류 발생: {e}")
        input_data = sample_input()
else:
    st.info("샘플 데이터를 사용 중입니다. 사용자 엑셀 파일을 업로드하면 자동 교체됩니다.")
    input_data = sample_input()

# 입력 데이터 미리보기
st.subheader("🔎 입력 데이터 미리보기")
st.dataframe(input_data)

# 분석 실행
st.subheader("📊 분석 결과")
result = yen_investment_analysis(input_data.iloc[0])
st.dataframe(result)

# 종합 점수 강조
st.markdown(f"### ✅ 투자 종합 점수: **{result['Investment Score (총점)'].values[0]} / 20점**")

# 안내
st.markdown("""
---
- 점수는 환율 변동성, 환헷지 비용, CDS 리스크, 샤프지수 등을 종합하여 산출됩니다.
- 종합 점수가 14점 이상이면 투자 고려, 10~13점은 중립, 9점 이하는 보류 권장입니다.
---
""")
