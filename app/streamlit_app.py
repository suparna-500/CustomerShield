import streamlit as st
from src.predict import predict_churn
import pandas as pd

st.set_page_config(page_title="CustomerShield AI", layout="wide", page_icon="🛡️")

# ── Custom CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* ── Google Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hide default Streamlit chrome ── */
    #MainMenu, footer, header {visibility: hidden;}

    /* ── Hero Section ── */
    .hero {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        border-radius: 20px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .hero::before {
        content: "";
        position: absolute;
        top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%);
        animation: pulse 6s ease-in-out infinite;
    }
    @keyframes pulse {
        0%, 100% {transform: scale(1); opacity: 0.6;}
        50% {transform: scale(1.1); opacity: 1;}
    }
    .hero h1 {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
        position: relative;
    }
    .hero p {
        color: #cbd5e1;
        font-size: 1.15rem;
        font-weight: 300;
        position: relative;
    }
    .hero .tagline {
        display: inline-block;
        margin-top: 1rem;
        padding: 0.4rem 1.2rem;
        border: 1px solid rgba(167,139,250,0.4);
        border-radius: 999px;
        color: #a78bfa;
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        position: relative;
    }

    /* ── Card Wrapper ── */
    .card {
        background: linear-gradient(145deg, #1e1b4b, #1a1a2e);
        border: 1px solid rgba(99,102,241,0.2);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(99,102,241,0.15);
    }
    .card h3 {
        color: #e0e7ff;
        font-weight: 600;
        margin-bottom: 0.3rem;
        font-size: 1.1rem;
    }
    .card p {
        color: #94a3b8;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }

    /* ── Section Header ── */
    .section-header {
        color: #c7d2fe;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .section-sub {
        color: #64748b;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }

    /* ── Predict Button ── */
    div.stButton > button {
        width: 100%;
        padding: 0.9rem 2rem;
        font-size: 1.1rem;
        font-weight: 700;
        color: #fff;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: all 0.3s;
        letter-spacing: 0.5px;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #818cf8, #a78bfa);
        box-shadow: 0 6px 25px rgba(99,102,241,0.45);
        transform: translateY(-1px);
    }

    /* ── Result Cards ── */
    .result-card {
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        margin-top: 1rem;
    }
    .result-high {
        background: linear-gradient(145deg, #450a0a, #7f1d1d);
        border: 1px solid #dc2626;
    }
    .result-low {
        background: linear-gradient(145deg, #052e16, #14532d);
        border: 1px solid #22c55e;
    }
    .result-card h2 {
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .result-card .prob {
        font-size: 3rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    .result-card .advice {
        font-size: 0.95rem;
        padding: 0.6rem 1rem;
        border-radius: 10px;
        margin-top: 1rem;
        display: inline-block;
    }

    /* ── Progress bar colour ── */
    .stProgress > div > div > div {
        border-radius: 10px;
    }

    /* ── Stats row ── */
    .stat-box {
        background: rgba(99,102,241,0.08);
        border: 1px solid rgba(99,102,241,0.18);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    .stat-box .num {
        font-size: 1.5rem;
        font-weight: 700;
        color: #a78bfa;
    }
    .stat-box .label {
        font-size: 0.78rem;
        color: #94a3b8;
        margin-top: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)


# ── Hero Section ────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🛡️ CustomerShield AI</h1>
    <p>Predict customer churn before it happens. Retain more. Grow faster.</p>
    <div class="tagline">✨ Powered by Machine Learning</div>
</div>
""", unsafe_allow_html=True)

# # ── Quick Stats Row ─────────────────────────────────────────────────────────
# s1, s2, s3, s4 = st.columns(4)
# with s1:
#     st.markdown('<div class="stat-box"><div class="num">93.2%</div><div class="label">Model Accuracy</div></div>', unsafe_allow_html=True)
# with s2:
#     st.markdown('<div class="stat-box"><div class="num">7,043</div><div class="label">Customers Analyzed</div></div>', unsafe_allow_html=True)
# with s3:
#     st.markdown('<div class="stat-box"><div class="num">26.5%</div><div class="label">Avg Churn Rate</div></div>', unsafe_allow_html=True)
# with s4:
#     st.markdown('<div class="stat-box"><div class="num">< 1s</div><div class="label">Prediction Speed</div></div>', unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# ── Input Section ───────────────────────────────────────────────────────────
st.markdown('<div class="section-header">📋 Customer Profile</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Fill in the details below and hit <b>Predict</b> to assess churn risk.</div>', unsafe_allow_html=True)

col_left, col_spacer, col_right = st.columns([5, 0.5, 5])

with col_left:
    st.markdown("""<div class="card"><h3>📅 Account Information</h3>
    <p>How long has this customer been with us?</p></div>""", unsafe_allow_html=True)
    tenure = st.slider(
        "Tenure (Months)",
        min_value=0, max_value=72, value=12,
        help="Number of months the customer has stayed with the company",
    )
    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0, max_value=200.0, value=70.0, step=5.0,
        help="The amount charged to the customer monthly",
    )

with col_right:
    st.markdown("""<div class="card"><h3>⚙️ Service Details</h3>
    <p>What services does this customer use?</p></div>""", unsafe_allow_html=True)
    contract = st.selectbox(
        "Contract Type",
        ["Month-to-month", "One year", "Two year"],
        help="Length of the customer's contract",
    )
    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No"],
        help="Whether the customer has online security add-on",
    )
    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No"],
        help="Whether the customer has tech support add-on",
    )

st.markdown("<br>", unsafe_allow_html=True)

# ── Predict Button ──────────────────────────────────────────────────────────
if st.button("🔮  Predict Churn Risk"):

    input_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        # include encoded values depending on your training structure
    }

    with st.spinner("Analyzing customer profile..."):
        prediction, probability = predict_churn(input_data)

    # ── Results ─────────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">📈 Prediction Results</div>', unsafe_allow_html=True)

    res_left, res_spacer, res_right = st.columns([5, 0.5, 5])

    with res_left:
        if prediction == 1:
            st.markdown(f"""
            <div class="result-card result-high">
                <h2 style="color:#fca5a5;">⚠️ High Risk of Churn</h2>
                <div class="prob" style="color:#ef4444;">{probability:.0%}</div>
                <p style="color:#fecaca;">Churn Probability</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card result-low">
                <h2 style="color:#86efac;">✅ Low Risk of Churn</h2>
                <div class="prob" style="color:#22c55e;">{probability:.0%}</div>
                <p style="color:#bbf7d0;">Churn Probability</p>
            </div>
            """, unsafe_allow_html=True)

    with res_right:
        st.markdown("<br>", unsafe_allow_html=True)

        # Probability gauge bar
        st.markdown("**Risk Meter**")
        st.progress(min(probability, 1.0))

        # Contextual advice
        if probability > 0.7:
            st.markdown("""
            <div class="advice" style="background:rgba(239,68,68,0.12); border:1px solid #dc2626;
                 border-radius:10px; padding:1rem; color:#fca5a5; margin-top:1rem;">
                🚨 <b>Critical:</b> Very high churn risk detected. Immediate retention action
                recommended — consider a personal outreach, loyalty discount, or service upgrade.
            </div>""", unsafe_allow_html=True)
        elif probability > 0.4:
            st.markdown("""
            <div class="advice" style="background:rgba(234,179,8,0.1); border:1px solid #ca8a04;
                 border-radius:10px; padding:1rem; color:#fde68a; margin-top:1rem;">
                ⚡ <b>Moderate Risk:</b> This customer may be considering alternatives.
                A targeted offer or check-in call could make all the difference.
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="advice" style="background:rgba(34,197,94,0.1); border:1px solid #16a34a;
                 border-radius:10px; padding:1rem; color:#86efac; margin-top:1rem;">
                🎉 <b>Looking Good!</b> This customer appears satisfied.
                Keep up the great service to maintain loyalty.
            </div>""", unsafe_allow_html=True)

# ── Footer ────────────────────��─────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; color:#475569; font-size:0.8rem; padding:1rem 0; border-top:1px solid #1e293b;">
    Built with ❤️ using Streamlit &nbsp;•&nbsp; CustomerShield AI &nbsp;•&nbsp; © 2026
</div>
""", unsafe_allow_html=True)