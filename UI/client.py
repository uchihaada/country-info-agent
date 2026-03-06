import streamlit as st
import requests

API_URL = "https://country-info-agent-t3ds.onrender.com"

st.set_page_config(
    page_title="Country Info AI Agent",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Country Info AI Agent")
st.caption("Ask anything about countries")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("Settings")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.button("🔎 Check API"):
        try:
            r = requests.get("https://country-info-agent-t3ds.onrender.com")
            if r.status_code == 200:
                st.success("API is running")
            else:
                st.error("API not responding")
        except:
            st.error("API not reachable")


# ---------- CHAT HISTORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ---------- USER INPUT ----------
user_input = st.chat_input("Ask about a country...")

if user_input:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Thinking indicator
    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"question": user_input}
                )

                if response.status_code == 200:
                    answer = response.json()["answer"]
                else:
                    answer = "⚠️ API returned an error."

            except Exception as e:
                answer = f"❌ Connection error: {e}"

        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
