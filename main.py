import streamlit as st
from streamlit_option_menu import option_menu
from page1 import text
from page2 import image
from page3 import details


def main():

    #st.title("Gemini 2.0 Thinking Experimental")

    with st.sidebar:
        selection = option_menu(
        menu_title="Main Menu",
        options=["About Gemini","Multimodal", "Image Generation"],
        icons=["book","pencil", "image"],
        menu_icon="cast",
        default_index=1
        )

    if selection == "Multimodal":
        text()

    elif selection == "Image Generation":
        image()

    elif selection == "About Gemini":
        details()


if __name__ == '__main__':
    main()
