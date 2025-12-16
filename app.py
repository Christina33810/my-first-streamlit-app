import streamlit as st


# 大标题
st.title("个人信息收集")

# 小标题
st.header("1. 基本信息")

# 数字输入框：年龄
age = st.number_input("请输入你的年龄:", min_value=0, max_value=120, value=25)

# 下拉选择框：性别
gender = st.selectbox("请选择你的性别:", ["男", "女", "其他"])

# 按钮：提交
if st.button("提交信息"):
    # 成功提示
    st.success("信息提交成功！")
    # 显示用户输入的信息
    st.write(f"你的年龄：{age}，性别：{gender}")
