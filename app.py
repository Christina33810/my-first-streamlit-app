# 1. 导入Streamlit库，给它起个短名字st（方便后续使用，固定写法）
import streamlit as st

# 2. 在网页上显示大标题（相当于Word里的一号字体标题）
st.title("我的第一个Streamlit网页（GitHub版）")

# 3. 显示普通文字（相当于Word里的正文）
st.write("你好！我在GitHub上写Streamlit代码啦～")

# 4. 加一个数字输入框，让用户输入年龄（互动功能）
age = st.number_input("请输入你的年龄", min_value=0, max_value=100, value=20)

# 5. 显示用户输入的年龄（动态更新）
st.write(f"你输入的年龄是：{age}岁")
