import streamlit as st
from streamlit_option_menu import option_menu

# 侧边栏菜单（对应课件的Option Menu）
with st.sidebar:
    selected = option_menu(
        menu_title="主菜单",  # 菜单标题
        options=["首页", "关于我们", "联系我们"],  # 菜单选项
        icons=["house", "info-circle", "envelope"],  # 图标（课件里的Bootstrap图标）
        default_index=0  # 默认选中第一个
    )

# 根据选中的菜单显示内容
if selected == "首页":
    st.title("欢迎来到首页")
elif selected == "关于我们":
    st.title("关于我们")
else:
    st.title("联系我们")
