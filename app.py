import streamlit as st
from streamlit_option_menu import option_menu

# 主标题
st.title("测试侧边栏菜单")

# 侧边栏菜单核心代码
with st.sidebar:
    selected = option_menu(
        menu_title="主菜单",  # 菜单标题（可以留空，写""）
        options=["首页", "关于", "联系"],  # 菜单选项
        icons=["house", "info-circle", "envelope"],  # 图标（用Bootstrap图标，不用也可以）
        default_index=0,  # 默认选中第一个选项
    )

# 根据选中的选项显示内容
if selected == "首页":
    st.write("你选中了【首页】")
elif selected == "关于":
    st.write("你选中了【关于】")
else:
    st.write("你选中了【联系】")
