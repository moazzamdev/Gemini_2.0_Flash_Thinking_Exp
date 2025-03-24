import streamlit as st
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Coming Soon", page_icon="⏳", layout="centered")
# Streamlit app
def image():


    # Custom Styling
    st.markdown(
        """
        <style>
            .center-text {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #FF6F61;
                margin-top: 20%;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display Message
    st.markdown('<p class="center-text">🚀 Coming Soon... Stay Tuned! ⏳</p>', unsafe_allow_html=True)
