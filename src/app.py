import streamlit as st
from src.storage import load_trips
from src.ai_assistant import ask, TRAVEL_SYSTEM_PROMPT
from src.rag import rag_ask, ensure_index
from src.tools import run_agent

st.set_page_config(page_title="Trip Notes AI", page_icon="✈️")

st.title("Trip Notes AI")

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "agent_history" not in st.session_state:
    st.session_state.agent_history = []

# build RAG index
ensure_index()

# sidebar
st.sidebar.header("Trips")

trips = load_trips()
trip_names = [t["name"] for t in trips] if trips else ["(no trips yet)"]

selected_trip = st.sidebar.selectbox("Select a trip", trip_names)

# tabs
tab1, tab2, tab3 = st.tabs(["Chat", "Search", "Agent"])

# ---------------- CHAT ----------------
with tab1:
    st.header("Chat")

    for msg in st.session_state.chat_history:
        st.write(msg)

    user_input = st.chat_input("Ask something...")

    if user_input:
        st.session_state.chat_history.append(f"You: {user_input}")

        response = ask(user_input, TRAVEL_SYSTEM_PROMPT)

        st.session_state.chat_history.append(f"AI: {response}")
        st.rerun()

# ---------------- SEARCH ----------------
with tab2:
    st.header("Search")

    query = st.text_input("Search your guides")

    if query:
        result = rag_ask(query)
        st.write(result)

# ---------------- AGENT ----------------
with tab3:
    st.header("Agent")

    question = st.text_area("Ask the agent")

    if st.button("Ask the Agent"):
        result = run_agent(question)
        st.session_state.agent_history.append((question, result))

    for q, r in st.session_state.agent_history:
        st.write(f"Q: {q}")
        st.write(f"A: {r}")

    with st.expander("Tools available"):
        st.write("Weather tool, Budget tool, Guide search tool")
