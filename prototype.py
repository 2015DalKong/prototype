import pandas as pd
import streamlit as st
import plotly.graph_objects as go

merged_df = pd.read_csv('./data.csv')


# 인사말
"""
# Welcome to ImineSkin!

:heavy_exclamation_mark: 안녕하세요. 간단한 대시보드를 만들어보았습니다. :heavy_exclamation_mark:
"""
st.header("ProtoType Code")

st.divider()


st.dataframe(merged_df)


# 차트 설정
fig = go.Figure()
fig.add_trace(go.Scatter(x=merged_df['전기시점'], y=merged_df['전표(계)'], name='전표(천만원)', mode='lines'))
fig.add_trace(go.Bar(x=merged_df['전기시점'], y=merged_df['전표(수)'], name='전표(수)'))
fig.update_layout(
    title='전기시점별 전표 현황',
    xaxis_title='전기시점',
    yaxis=dict(title='전표(계)'),
    yaxis2=dict(
        title='전표(수)',
        overlaying='y',
        side='right',
        tickformat=',d'  # 천 단위마다 쉼표 추가
    )
)

# Streamlit에 차트 출력
st.plotly_chart(fig)
