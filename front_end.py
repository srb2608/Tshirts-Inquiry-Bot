import streamlit as st
from main import get_few_shot_db_chain

# ---------- Page Config ----------
st.set_page_config(
    page_title="T-Shirts Q&A",
    page_icon="👕",
    layout="centered"
)

st.markdown("""
<style>
    /* App background */
    .main {
        background-color: #000000;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #000000;
    }

    /* Title */
    .title-text {
        font-size: 40px;
        font-weight: 700;
        color: #ffffff;
        text-align: center;
    }

    /* Subtitle */
    .subtitle-text {
        font-size: 16px;
        color: #bbbbbb;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Input label */
    label {
        color: #ffffff !important;
        font-size: 16px;
    }

    /* Text input */
    input {
        background-color: #111111 !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        border: 1px solid #333333 !important;
    }

    /* Answer box */
    .answer-box {
        background-color: #111111;
        color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(255,255,255,0.05);
        margin-top: 20px;
        font-size: 18px;
    }

    /* Headers */
    h1, h2, h3, h4 {
        color: #ffffff;
    }

    /* Divider */
    hr {
        border: 1px solid #222222;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="title-text">👕 T-Shirts Q&A</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Ask questions about t-shirt inventory, stock, sizes, and colors</div>',
    unsafe_allow_html=True
)

# ---------- Input ----------
q = st.text_input(
    "🔍 Enter your question",
    placeholder="e.g. How many white Nike t-shirts are available in size M?"
)

if q:
    with st.spinner("Thinking... 🤔"):
        try:
            chain = get_few_shot_db_chain()
            a = chain.run(q)

            st.markdown("### ✅ Answer")
            st.markdown(f'<div class="answer-box">{a}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error("⚠️ Something went wrong while processing your question.")
            st.exception(e)

st.markdown("---")
st.markdown(
    "<center style='color:#777777;'>Powered by LangChain • SQL • Streamlit</center>",
    unsafe_allow_html=True
)
