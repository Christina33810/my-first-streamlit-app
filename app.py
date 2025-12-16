import streamlit as st

tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
with tab1:
    st.write("Content for Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")
with tab2:
    st.write("Content for Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for feedback in customer_feedback:
        st.write(f"- {feedback}")
with tab3:
    st.write("Content for Market Trends")
    market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")

