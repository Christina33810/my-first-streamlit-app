import streamlit as st
from streamlit_option_menu import option_menu

st.title("布局设计演示")

# 1. 分3列显示（对应课件的Columns Layout）
col1, col2, col3 = st.columns(3)
with col1:
    st.header("第一列")
    st.write("1月销售额：10万")
with col2:
    st.header("第二列")
    st.write("2月销售额：15万")
with col3:
    st.header("第三列")
    st.write("3月销售额：12万")

# 2. 标签页显示（对应课件的Tabs Layout）
tab1, tab2, tab3 = st.tabs(["销售数据", "客户反馈", "市场趋势"])
with tab1:
    st.write("销售数据：总销售额37万")
with tab2:
    st.write("客户反馈：好评率95%")
with tab3:
    st.write("市场趋势：需求增长")

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
