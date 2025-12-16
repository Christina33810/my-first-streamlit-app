import streamlit as st

# 创建一个数字输入框，提示文字是“Enter your age:”
age = st.number_input(
    "Enter your age:",
    min_value=0,    # 最小能输入0
    max_value=120,  # 最大能输入120
    value=25        # 默认值是25
)
# 显示用户输入的年龄
st.write(f"Your age is {age}")
