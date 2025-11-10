import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("消費趨勢智慧分析平台")

page = st.sidebar.selectbox("功能選擇", [
    "可預測消費趨勢模型",
    "分析市場趨勢",
    "試算獲利潛力組合"
])

if page == "可預測消費趨勢模型":
    st.subheader("📈 可預測消費趨勢模型")
    data = pd.DataFrame({
        "月份": ["Jan","Feb","Mar","Apr","May","Jun"],
        "銷售量": [4000,3000,2000,2780,1890,2390],
        "趨勢線": [2400,1398,9800,3908,4800,3800]
    })
    st.line_chart(data.set_index("月份"))

elif page == "分析市場趨勢":
    st.subheader("📊 市場趨勢分析")
    fig, ax = plt.subplots()
    ax.bar(['北部','中部','南部','東部'], [50,40,70,30], color=['#007bff','#17a2b8','#28a745','#ffc107'])
    ax.set_ylabel("平均月支出（千元）")
    ax.set_title("地域性消費差異")
    st.pyplot(fig)

else:
    st.subheader("💡 試算獲利最具潛力的品項或組合")
    st.write("根據商品特性模擬不同定價與銷售策略。")
