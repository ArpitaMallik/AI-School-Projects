import streamlit as st
import requests

st.set_page_config(
    page_title="LLaMA Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.markdown("""
    <style>
        .main-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #1f77b4;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            font-size: 1rem;
            color: #666;
            margin-bottom: 1.5rem;
        }
        .summary-box {
            background-color: #f7f9fc;
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid #dbe4f0;
        }
        .footer-note {
            text-align: center;
            color: #888;
            font-size: 0.85rem;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📝 LLaMA Text Summarizer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Paste your text below and generate a concise summary using your local LLaMA model.</div>',
    unsafe_allow_html=True
)

with st.container():
    user_input = st.text_area(
        "Enter your text here",
        height=250,
        placeholder="Paste article, paragraph, notes, or document text here..."
    )

col1, col2 = st.columns([1, 5])

with col1:
    summarize_clicked = st.button("Summarize", use_container_width=True)

with col2:
    clear_clicked = st.button("Clear", use_container_width=True)

if clear_clicked:
    st.rerun()

if summarize_clicked:
    if not user_input.strip():
        st.warning("Please enter some text before summarizing.")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    "http://localhost:8000/summarize/",
                    data={"text": user_input},
                    timeout=500
                )

                if response.status_code == 200:
                    summary = response.json().get("summary", "Error generating summary.")

                    st.markdown("### Summary")
                    st.markdown(
                        f'<div class="summary-box">{summary}</div>',
                        unsafe_allow_html=True
                    )

                    st.success("Summary generated successfully.")
                else:
                    st.error(f"Server returned an error: {response.status_code}")

            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the backend. Make sure your API server is running on localhost:8000.")
            except requests.exceptions.Timeout:
                st.error("The request timed out. Try a shorter text or check if the model is overloaded.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.markdown('<div class="footer-note">Built with Streamlit + LLaMA + FastAPI</div>', unsafe_allow_html=True)