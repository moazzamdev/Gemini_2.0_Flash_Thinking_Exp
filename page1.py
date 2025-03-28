import streamlit as st
from PyPDF2 import PdfReader
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationSummaryMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
import base64
import io
import time
from PIL import Image
import os
# Set your Google API key here
GOOGLE_API_KEY = os.environ.get("api_key")


def convert_to_base64(uploaded_file):
    """Convert uploaded image to Base64 format (supports JPEG and PNG)"""
    image = Image.open(uploaded_file)
    buffered = io.BytesIO()

    # Preserve format (default to PNG if unknown)
    format = image.format if image.format in ["JPEG", "PNG"] else "PNG"

    image.save(buffered, format=format)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def text():
    st.title("Gemini 2.0 Thinking Experimental")
    st.sidebar.title("Capabilities:")

    # Add bullet points
    st.sidebar.markdown("""
            - **Text Queries**
            - **Visual Queries**
            - **PDF Support**
           
            """)
    st.markdown("""
    <style>
        .anim-typewriter {
            animation: typewriter 3s steps(40) 1s 1 normal both, 
                       blinkTextCursor 800ms steps(40) infinite normal;
            overflow: hidden;
            white-space: nowrap;
            border-right: 3px solid;
            font-family: serif;
            font-size: 0.9em;
        }
        @keyframes typewriter {
            from { width: 0; }
            to { width: 100%; }
        }
        @keyframes blinkTextCursor {
            from { border-right-color: rgba(255,255,255,0.75); }
            to { border-right-color: transparent; }
        }
        .dot-pulse {
            position: relative;
            left: -9999px;
            width: 10px;
            height: 10px;
            border-radius: 5px;
            background-color: #9880ff;
            color: #9880ff;
            box-shadow: 9999px 0 0 -5px;
            animation: dot-pulse 1.5s infinite linear;
            animation-delay: 0.25s;
        }
    </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.chat_history = StreamlitChatMessageHistory()
        st.session_state.memory = ConversationSummaryMemory(
            llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash-thinking-exp-01-21", google_api_key=GOOGLE_API_KEY),
            memory_key="history",
            chat_memory=st.session_state.chat_history
        )

    # Initialize Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-thinking-exp-01-21",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.3,
        streaming=True,
        timeout=120,
        max_retries=6

    )

    # Display chat messages
    chat_container = st.container()
    with chat_container:
        # Show initial bot message
        if len(st.session_state.messages) == 0:
            animated_text = '<div class="anim-typewriter">Hello 👋, how may I assist you today?</div>'
            # st.chat_message("assistant").markdown(animated_text, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": "Hello 👋, how may I assist you today?"})

        # Display historical messages
        for message in st.session_state.messages[0:]:  # Skip first static message
            if message["role"] == "user":
                if message.get("image"):
                    st.chat_message("user", avatar="🧑").markdown(
                        f"""{message["content"]}<br><br>{'<img src="' + message["image"] + f'" width="50" style="margin-top: 10px; border-radius: 8px;">' if message["file_type"] == "application/pdf" else '<img src="' + message["image"] + f'" width="200" style="margin-top: 10px; border-radius: 8px;">'}<br> {f'<i style="font-size: 12px;">{message["file_name"]}</i>' if message["file_type"] == "application/pdf" else message["file_name"] if message["file_type"] else ''}""",
                        unsafe_allow_html=True
                    )
                else:
                    st.chat_message("user", avatar="🧑").markdown(message["content"])
            else:
                st.chat_message("assistant", avatar="🤖").markdown(message["content"])

    # Chat input with multimodal support
    user_input = st.chat_input("Say something", accept_file=True, file_type=["png", "jpg", "jpeg", "pdf"])

    if user_input:
        file_type = None
        file_name = ""
        image_base64 = convert_to_base64("pdf_icon.png")
        image_url = f"data:image/jpeg;base64,{image_base64}"
        # Process user input
        #image_url = ""
        message_content = [{"type": "text", "text": user_input.text}]
        files = user_input["files"]


        if files:
            file_type = files[0].type
            

        if file_type in ["image/png", "image/jpg", "image/jpeg"]:
            uploaded_file = user_input["files"][0]
            image_base64 = convert_to_base64(uploaded_file)
            image_url = f"data:image/jpeg;base64,{image_base64}"

            message_content.append({"type": "image_url", "image_url": image_url})
        text = ""
        if file_type == "application/pdf":
            uploaded_file = user_input["files"][0]
            file_name = files[0].name
            pdf_reader = PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                text += page.extract_text()
            #st.sidebar.write(text)
            prompt = "this is pdf data: \n"+text +"this is user asking about pdf:"+user_input.text
            message_content = [{"type": "text", "text": prompt}]
            message_content.append({"type": "text", "text": file_name})
            #message_content.append({"type": "image_url", "image_url": image_url})
        # Add user message to UI
        with chat_container:
            if file_type:
                st.chat_message("user", avatar="🧑").markdown(
                    f"""
                    {user_input.text}
                    <br><br>
                    {'<img src="' + image_url + f'" width="50" style="margin-top: 10px; border-radius: 8px;">' if file_type == "application/pdf" else '<img src="' + image_url + f'" width="200" style="margin-top: 10px; border-radius: 8px;">' if file_type else ''}
                    <br>
                     {f'<i style="font-size: 12px;">{file_name}</i>' if file_type == "application/pdf" else file_name if file_type else ''}
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.chat_message("user", avatar="🧑").markdown(user_input.text)

        # Store in session state
        st.session_state.messages.append({
            "role": "user",
            "content": user_input.text,
            "image": image_url if user_input["files"] else "",
            "file_name" : file_name,
            "file_type" : file_type
        })

        # Create LangChain message
        user_message = HumanMessage(content=message_content)
        st.session_state.chat_history.add_message(user_message)

        # Generate streaming response
        history = st.session_state.chat_history.messages
        typing_container = st.empty()

        def stream_generator(history, user_message):
            # Placeholder for "Thinking..." and "Typing..."
            typing_container = st.empty()

            # Show "Thinking..." first
            typing_container.markdown('<p class="fade-text">Thinking...</p>', unsafe_allow_html=True)

            st.markdown("""
                <style>
                    @keyframes fade {
                        0% { opacity: 0.3; }
                        50% { opacity: 1; }
                        100% { opacity: 0.3; }
                    }
                    .fade-text {
                        font-size: 16px;
                        font-weight: bold;
                        color: #3498db;
                        animation: fade 1.5s infinite;
                    }
                </style>
            """, unsafe_allow_html=True)

            response = llm.stream(history + [user_message])

            # Buffer for partial words
            buffer = ""

            # Flag to change message
            first_chunk_received = False

            # Pause settings
            PAUSE_AFTER = {".", "!", "?", ",", ";", ":"}
            PAUSE_MULTIPLIER = 2.5  # Pause longer for punctuation

            for chunk in response:
                if not first_chunk_received:
                    typing_container.empty()
                    typing_container.markdown('<p class="fade-text">Typing...</p>', unsafe_allow_html=True)
                    first_chunk_received = True

                content = buffer + chunk.content
                words = content.split(' ')

                # Check if last word is complete
                if not content.endswith(' '):
                    buffer = words.pop()
                else:
                    buffer = ""

                for word in words:
                    yield word + ' '  # Stream word-by-word

                    # Add delay for natural pauses
                    base_delay = 0.03
                    last_char = word[-1] if word else ''
                    time.sleep(base_delay * PAUSE_MULTIPLIER if last_char in PAUSE_AFTER else base_delay)

            # Yield any remaining content in buffer
            if buffer:
                yield buffer
                time.sleep(0.03)

            # Clear "Typing..." message after response finishes
            typing_container.empty()

        # Generate streaming response
        with st.chat_message("assistant", avatar="🤖"):

            full_response = st.write_stream(
                stream_generator(
                    st.session_state.chat_history.messages,
                    user_message
                )
            )

            typing_container.empty()  # Remove status message

        # Update session state
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response
        })

        # Update conversation memory
        ai_message = AIMessage(content=full_response)
        st.session_state.chat_history.add_message(ai_message)
        st.session_state.memory.save_context(
            {"input": user_message.content},
            {"output": ai_message.content}
        )
        #st.sidebar.write(user_message)
