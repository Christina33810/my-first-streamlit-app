# 1. 导入Streamlit库
import streamlit as st

# 2. 显示仪表盘大标题（对应课件的“Retail Business Dashboard”）
st.title("零售业务仪表盘")

# 3. 显示经理输入区的小标题（对应课件的“Manager Input Section”）
st.header("经理输入区域")
st.write("请输入月度销售目标并选择地区")

# 4. 数字输入框：输入月度销售目标（对应课件的“Numeric Input”）
sales_target = st.number_input(
    "输入月度销售目标（美元）：",  # 输入框提示文字
    min_value=0,  # 最小只能输0
    value=50000   # 默认值50000美元
)

# 5. 下拉菜单：选择地区（对应课件的“Dropdown List”）
region = st.selectbox(
    "选择地区：",  # 下拉菜单提示文字
    ["北部", "南部", "东部", "西部"]  # 下拉选项
)

# 6. 提交按钮：点击后显示结果（对应课件的“Submit Button”）
if st.button("提交"):
    # 显示成功提示（绿色文字，对应课件的“Success Message”）
    st.success("仪表盘已更新！")
    # 显示用户输入的信息（对应课件的“Display Entered Values”）
    st.write(f"月度销售目标：{sales_target}美元")
    st.write(f"选择的地区：{region}")
    # 额外逻辑：如果目标大于100000美元，显示鼓励文字（课件拓展要求）
    if sales_target > 100000:
        st.write("太棒了！你设定了一个有挑战的目标！")
