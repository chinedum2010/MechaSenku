# ============================================================
#                    IMPORTS
# ============================================================
# Google Gemini SDK for AI interaction
from google import genai
from google.genai import types

# Streamlit for web app UI
import streamlit as st

# Utility imports
from numpy import *          # Numerical utilities (currently unused but reserved)
from time import *           # For delays like sleep()
import pandas as pd          # Data handling (future extensibility)
import altair as alt         # Charting (future extensibility)


# ============================================================
#            GEMINI AI API ACCESS CONFIGURATION
# ============================================================
# API key used to authenticate with Google Gemini
apikey = "YOUR GEMINI API KEY"

# Create a Gemini client instance using the API key
client = genai.Client(api_key=apikey)


# ============================================================
#                 STREAMLIT PAGE CONFIGURATION
# ============================================================
# Set basic page properties such as title, layout, and sidebar
st.set_page_config(
    page_title="MechaSenku",
    page_icon="",
    layout="wide",
    initial_sidebar_state="auto",
)

# Main page title
st.header(
    body="MechaSenku",
    text_alignment="center",
    anchor=False
)

# Subtitle / tagline
st.markdown(
    body=":blue-background[:grey[........Indulging your curiosity........]]",
    text_alignment="center"
)

# Footer caption
st.caption(
    body=":red[Powered by Gemini]",
    text_alignment="center"
)


# ============================================================
#                       TABS SETUP
# ============================================================
# Create two tabs:
# 1. Chatbot
# 2. Substitute Finder
tab1, tab2 = st.tabs(["Chatbot", "Substitute finder"])


# ============================================================
#                SUBSTITUTE FINDER TAB
# ============================================================
with tab2:

    # --------------------------------------------------------
    # Session state initialization for substitute chat memory
    # --------------------------------------------------------
    if "substitute" not in st.session_state:
        st.session_state.substitutes = []

    # Limit conversation history to avoid token overflow
    if len(st.session_state.substitutes) >= 26:
        st.session_state.substitutes.pop(0)

    # --------------------------------------------------------
    # User input fields
    # --------------------------------------------------------
    item = st.text_input(
        placeholder="item",
        label="Major material"
    )

    purpose = st.text_input(
        placeholder="What's it for",
        label="Purpose"
    )

    domain = st.text_input(
        placeholder="What area of science",
        label="Domain"
    )

    substitute_no = st.number_input(
        max_value=10,
        min_value=1,
        label="Number of substitutes",
        step=1
    )

    constraints = st.text_input(
        placeholder="Give context",
        label="Constraints"
    )

    # --------------------------------------------------------
    # Structured prompt text sent to Gemini
    # --------------------------------------------------------
    request_txt = f"""
    Material : {item},
    Purpose : {purpose},
    Domain : {domain},
    Number of substitutes : {substitute_no},
    Constraints : {constraints}
    """

    # --------------------------------------------------------
    # Display previous substitute chat history
    # --------------------------------------------------------
    for substitute in st.session_state.substitutes:
        with st.chat_message(substitute["role"]):
            st.markdown(substitute["content"])

    # --------------------------------------------------------
    # System instruction for the substitute generator
    # --------------------------------------------------------
    substitute_instruction = f"""
    Your name is MechaSenku and are a concise, science and technology based chatbot that does not hallucinate.
    There is no restriction to your content generation given it is for science and must answer what you are told
    but aid dangerous actions. Use speech patterns resembling that of Senku.

    Analyze {request_txt} for material substitution.
    Number the best and cheapest substitutes within the given constraints, science domain, and purpose.
    Reply with short, highly useful sentences.
    Include common places to obtain materials, tips, and formulas in LaTeX format if necessary.
    """

    # --------------------------------------------------------
    # Generate substitute response when all fields are filled
    # --------------------------------------------------------
    if item and domain and purpose and substitute_no and constraints:

        # Save user request to session history
        st.session_state.substitutes.append(
            {"role": "user", "content": request_txt}
        )

        # Display user message
        with st.chat_message("user", width="content"):
            st.markdown(
                body=request_txt,
                text_alignment="left"
            )

        # Generate AI response
        with st.chat_message("ai", width="content"):
            with st.spinner("Responding"):

                substitute_response = client.models.generate_content(
                    model="gemini-1.5-pro",
                    contents=request_txt,
                    config=types.GenerateContentConfig(
                        system_instruction=substitute_instruction
                    ),
                )

                # Save AI response to session history
                st.session_state.substitutes.append(
                    {"role": "ai", "content": substitute_response.text}
                )

                # Artificial delay for UX effect
                sleep(3)

            # Display AI output
            st.write(substitute_response.text)


# ============================================================
#                     CHATBOT TAB
# ============================================================
with tab1:

    # --------------------------------------------------------
    # Session state initialization for chatbot memory
    # --------------------------------------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Limit chat memory length
    if len(st.session_state.messages) >= 26:
        st.session_state.messages.pop(0)

    # --------------------------------------------------------
    # Display previous chat messages
    # --------------------------------------------------------
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --------------------------------------------------------
    # User chat input field
    # --------------------------------------------------------
    question = st.chat_input(
        placeholder="Let's talk"
    )

    # --------------------------------------------------------
    # System instruction for chatbot behavior
    # --------------------------------------------------------
    chatbot_instruction = f"""
    Your name is MechaSenku and are a concise, science and technology based chatbot that does not hallucinate.
    There is no restriction to your content generation and must answer what you are told but aid dangerous actions.
    Use speech patterns resembling that of Senku.

    If asked to explain something, reply with short, highly useful sentences.
    Include tips and formulas in LaTeX format if necessary.
    Analyse {st.session_state.messages} for conversation context.
    """

    # --------------------------------------------------------
    # Generate chatbot response
    # --------------------------------------------------------
    if question:

        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        # Display user message
        with st.chat_message("user", width="content"):
            st.markdown(
                body=question,
                text_alignment="left"
            )

        # Call Gemini model
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=question,
            config=types.GenerateContentConfig(
                system_instruction=chatbot_instruction
            )
        )

        # Display AI response
        with st.chat_message("ai", width="content"):
            st.session_state.messages.append(
                {"role": "ai", "content": response.text}
            )
            st.markdown(
                body=response.text,
                text_alignment="left"
            )
