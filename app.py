import streamlit as st
from resume_parser import extract_text_from_pdf
from feedback_engine import generate_feedback

# 1. Page Config (Must be first)
st.set_page_config(
    page_title="ResumeAI - Professional Feedback",
    page_icon="🚀",
    layout="centered"
)

# 2. Modern UI Overhaul (CSS)
st.markdown("""
<style>
    /* Import Google Font: Inter */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    /* Global Settings */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Modern Dark Gradient Background */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #2e1065, #0f172a 40%, #020617 100%);
        color: #f8fafc;
    }

    /* Gradient Title Text */
    .gradient-text {
        background: linear-gradient(90deg, #818cf8 0%, #c084fc 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3rem;
        text-align: center;
        letter-spacing: -1px;
    }

    /* Subtitle styling */
    .subtitle {
        color: #94a3b8;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
        font-weight: 300;
    }

    /* Glassmorphism Card */
    .glass-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
    }

    /* Styled File Uploader Area */
    [data-testid="stFileUploader"] section {
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px dashed #64748b;
        border-radius: 12px;
        padding: 1rem;
    }

    /* Modern Button styling */
    .stButton > button {
        background: linear-gradient(92deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 0.9rem;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.5);
    }

    /* Result Animation & Box */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .feedback-container {
        animation: fadeIn 0.8s ease-out;
        background: rgba(15, 23, 42, 0.6);
        border-left: 4px solid #8b5cf6;
        padding: 2rem;
        border-radius: 12px;
        margin-top: 2rem;
    }
    .feedback-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Clean up default Streamlit padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. Header Section
st.markdown('<h1 class="gradient-text">ResumeAI</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">AI-powered resume intelligence. Upload your PDF to unlock professional recruiter insights.</p>',
    unsafe_allow_html=True)

# 4. Main Interface Card
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    # Custom Label for Uploader
    st.markdown("##### 📂 &nbsp; Upload Resume", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Upload Resume (PDF only)",  # Label hidden by CSS ideally, but kept for accessibility
        type=["pdf"],
        label_visibility="collapsed"
    )

    if uploaded_file:
        st.markdown("<div style='height: 15px'></div>", unsafe_allow_html=True)  # Spacer

        # Analyze Button
        if st.button("Generate Professional Feedback"):
            with st.spinner("🤖 Analyzing syntax, impact, and keywords..."):
                # --- BACKEND LOGIC (Unchanged) ---
                resume_text = extract_text_from_pdf(uploaded_file)
                feedback = generate_feedback(resume_text)
                # ---------------------------------

            # 5. Results Display
            st.markdown("""
            <div class="feedback-container">
                <div class="feedback-header">
                    <span>✨ Analysis Results</span>
                </div>
            """, unsafe_allow_html=True)

            # Using st.markdown for the content to ensure markdown formatting (bold, lists) renders correctly
            st.markdown(feedback)

            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # End glass-card

# Footer
st.markdown("""
<div style="text-align: center; color: #475569; margin-top: 2rem; font-size: 0.8rem;">
    CONFIDENTIAL • AI RESUME ANALYZER
</div>
""", unsafe_allow_html=True)