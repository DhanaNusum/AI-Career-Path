import streamlit as st
from google import genai
import random
from gtts import gTTS
import os
import uuid
import base64

# Page configuration
st.set_page_config(
    page_title="CareerPath - AI Career Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyAGxNiNz3AnPtdNN4m5-xfvsvbiPRxpIEQ")
# Custom CSS
st.markdown("""
<style>
    /* Main background - Lighter for better contrast */
    .main { 
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
        transition: background 0.3s ease;
    }
    
    /* Header styling - Darker for better visibility */
    .main-header { 
        color: #2D3436;
        text-align: center; 
        font-size: 3.5rem; 
        font-weight: bold; 
        margin-bottom: 0; 
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .main-header:hover {
        transform: translateY(-2px);
        text-shadow: 3px 3px 6px rgba(0,0,0,0.15);
        letter-spacing: 0.5px;
    }
    
    .sub-header { 
        color: #636e72; 
        text-align: center; 
        font-size: 1.5rem; 
        margin-bottom: 30px; 
        font-weight: 400;
        transition: all 0.3s ease;
    }
    
    .sub-header:hover {
        color: #2D3436;
        transform: scale(1.02);
    }
    
    /* Card styling - More contrast with hover */
    .card { 
        background: white; 
        border-radius: 15px; 
        padding: 25px; 
        margin: 15px 0; 
        box-shadow: 0 5px 15px rgba(0,0,0,0.1); 
        border-left: 5px solid #667eea;
        color: #2D3436;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(0,0,0,0.15);
        border-left: 5px solid #FF6B6B;
    }
    
    .card:before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .card:hover:before {
        left: 100%;
    }
    
    /* Ensure all text in cards is visible */
    .card h3, .card p { 
        color: #2D3436 !important; 
        transition: all 0.3s ease;
    }
    
    .card:hover h3 {
        color: #667eea !important;
        transform: translateX(5px);
    }
    
    /* Make radio button labels visible with hover */
    .stRadio label { 
        color: #2D3436 !important; 
        font-weight: 500;
        padding: 8px 12px;
        border-radius: 8px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stRadio label:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        transform: translateX(5px);
        color: #667eea !important;
    }
    
    /* Button styling with enhanced hover */
    .stButton>button { 
        background: linear-gradient(45deg, #667eea, #764ba2); 
        color: white; 
        border: none; 
        border-radius: 25px; 
        padding: 12px 30px; 
        font-size: 1.1rem; 
        font-weight: bold; 
        transition: all 0.3s ease; 
        width: 100%; 
        position: relative;
        overflow: hidden;
        z-index: 1;
    }
    
    .stButton>button:before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        transition: left 0.5s ease;
        z-index: -1;
    }
    
    .stButton>button:hover { 
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        color: white !important;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover:before {
        left: 0;
    }
    
    .stButton>button:active {
        transform: translateY(0) scale(0.98);
    }
    
    /* Make select box text visible with hover */
    .stSelectbox label { 
        color: #2D3436 !important; 
        font-size: 1.1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stSelectbox:hover label {
        color: #667eea !important;
        transform: translateY(-2px);
    }
    
    /* Select box dropdown hover effects */
    .stSelectbox>div>div {
        transition: all 0.3s ease;
    }
    
    .stSelectbox>div>div:hover {
        border-color: #667eea !important;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Make select box options visible with hover */
    .stSelectbox select option { 
        color: #2D3436;
        padding: 10px;
        transition: all 0.2s ease;
    }
    
    .stSelectbox select option:hover {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
    }
    
    /* Make sure dropdown text is visible */
    div[data-baseweb="select"] { 
        color: #2D3436 !important; 
        transition: all 0.3s ease;
    }
    
    /* Input field styling with hover */
    .stTextInput>div>div>input { 
        border-radius: 10px; 
        border: 2px solid #E0E0E0; 
        padding: 10px; 
        color: #2D3436;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:hover, 
    .stTextInput>div>div>input:focus { 
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
    }
            input, textarea {
    color: #000000 !important;
    background-color: #ffffff !important;
    caret-color: #000000 !important;
}
    
    .stTextInput label { 
        color: #2D3436 !important; 
        transition: all 0.3s ease;
    }
    
    .stTextInput:hover label {
        color: #667eea !important;
        transform: translateX(5px);
    }
    
    /* Selectbox styling with hover */
    .stSelectbox>div>div>select { 
        border-radius: 10px; 
        border: 2px solid #E0E0E0; 
        color: #2D3436;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stSelectbox>div>div>select:hover {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
    }
    
    /* Info box styling with hover */
    .success-box, .info-box, .warning-box {
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
    
    .success-box:hover { 
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(150, 206, 180, 0.3);
    }
    
    .info-box:hover { 
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(69, 183, 209, 0.3);
    }
    
    .warning-box:hover { 
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 30px rgba(255, 106, 106, 0.3);
    }
    
    /* Feature card colors with enhanced hover */
    .feature-card-1, .feature-card-2, .feature-card-3, .feature-card-4 { 
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card-1:hover { 
        transform: translateY(-8px) rotateX(5deg);
        box-shadow: 0 20px 40px rgba(255, 107, 107, 0.25);
        border-left: 5px solid #FF6B6B;
    }
    
    .feature-card-2:hover { 
        transform: translateY(-8px) rotateX(5deg);
        box-shadow: 0 20px 40px rgba(78, 205, 196, 0.25);
        border-left: 5px solid #4ECDC4;
    }
    
    .feature-card-3:hover { 
        transform: translateY(-8px) rotateX(5deg);
        box-shadow: 0 20px 40px rgba(69, 183, 209, 0.25);
        border-left: 5px solid #45B7D1;
    }
    
    .feature-card-4:hover { 
        transform: translateY(-8px) rotateX(5deg);
        box-shadow: 0 20px 40px rgba(150, 206, 180, 0.25);
        border-left: 5px solid #96CEB4;
    }
    
    /* Make feature card text visible with hover effects */
    .feature-card-1 h3, .feature-card-1 p,
    .feature-card-2 h3, .feature-card-2 p,
    .feature-card-3 h3, .feature-card-3 p,
    .feature-card-4 h3, .feature-card-4 p {
        color: #2D3436 !important;
        transition: all 0.3s ease;
    }
    
    .feature-card-1:hover h3 { color: #FF6B6B !important; }
    .feature-card-2:hover h3 { color: #4ECDC4 !important; }
    .feature-card-3:hover h3 { color: #45B7D1 !important; }
    .feature-card-4:hover h3 { color: #96CEB4 !important; }
    
    .feature-card-1:hover p { transform: translateX(5px); }
    .feature-card-2:hover p { transform: translateX(5px); }
    .feature-card-3:hover p { transform: translateX(5px); }
    .feature-card-4:hover p { transform: translateX(5px); }
    
    /* Chat bubble styling with hover */
    .user-bubble, .ai-bubble {
        transition: all 0.3s ease;
    }
    
    .user-bubble:hover { 
        transform: translateX(-5px) scale(1.02);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.2);
    }
    
    .ai-bubble:hover { 
        transform: translateX(5px) scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    /* Radio button container hover */
    .stRadio > div {
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stRadio > div:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
        transform: translateY(-3px);
        border-left: 4px solid #764ba2 !important;
    }
    
    /* Divider hover effect */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        transition: all 0.3s ease;
    }
    
    hr:hover {
        height: 3px;
        background: linear-gradient(90deg, transparent, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, transparent);
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
    }
    
    /* Spinner animation enhancement */
    .stSpinner > div {
        transition: all 0.3s ease;
    }
    
    /* Tab hover effects (if using tabs) */
    .stTabs [data-baseweb="tab"] {
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        color: #667eea !important;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# -------- Utility functions ----------
def ask(question, options=None, key=None):
    st.markdown(f'<div class="card feature-card-{random.randint(1,4)}">', unsafe_allow_html=True)
    st.markdown(f"**{question}**")
    if options:
        answer = st.radio("", options, key=key)
    else:
        answer = st.text_input("", key=key, placeholder="Type your answer here...")
    st.markdown('</div>', unsafe_allow_html=True)
    if answer == "":
        return None
    return answer

def generate_ai_response(prompt):
    with st.spinner("🎯 Generating personalized response..."):
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=prompt
        )
    return response.text

def speak_text(message="Output is generated", lang="en"):
    """Auto-play audio notification without user click"""
    try:
        tts = gTTS(text=message, lang=lang)
        # Unique filename avoids WinError 32
        audio_file = f"temp_{uuid.uuid4()}.mp3"
        tts.save(audio_file)

        # Read audio and encode
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()

        # Embed autoplay audio
        audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

        os.remove(audio_file)
    except Exception as e:
        st.warning(f"⚠️ TTS failed: {e}")

def normalize_year(raw_year):
    year_mapping = {
        "first": "First Year", "1st": "First Year", "1": "First Year",
        "second": "Second Year", "2nd": "Second Year", "2": "Second Year",
        "final": "Final Year", "3rd": "Final Year", "3": "Final Year",
        "graduate": "Graduate", "4th": "Graduate", "4": "Graduate"
    }
    return year_mapping.get(raw_year.strip().lower(), raw_year)

def display_feature_cards():
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown('<div class="card feature-card-1"><h3>🎯 Personalized Roadmaps</h3><p>Custom learning paths based on your goals and timeline</p></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="card feature-card-2"><h3>💼 Career Insights</h3><p>Salary data and career progression guidance</p></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="card feature-card-3"><h3>📜 Certification Guide</h3><p>Recommended certifications for skill validation</p></div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="card feature-card-4"><h3>🚀 Project Ideas</h3><p>Hands-on projects to boost your portfolio</p></div>', unsafe_allow_html=True)

# -------- Modules ----------
def skill_roadmap():
    st.markdown('<div class="info-box"><h3>🎯 Skill Roadmap Generator</h3><p>Create your personalized learning journey</p></div>', unsafe_allow_html=True)
    domain = ask("🎨 Which domain or area are you most interested in right now?", key="domain")
    if not domain: return st.markdown('<div class="warning-box">Please provide a domain to continue</div>', unsafe_allow_html=True)
    raw_year = ask("📚 Which year of study or professional level are you currently at?", key="year")
    if not raw_year: return st.markdown('<div class="warning-box">Please provide your current level</div>', unsafe_allow_html=True)
    year = normalize_year(raw_year)
    total_hours = ask("⏰ What is your total learning time (in hours) you can dedicate?", key="hours")
    if not total_hours: return st.markdown('<div class="warning-box">Please provide your available hours</div>', unsafe_allow_html=True)
    try: total_hours = float(total_hours)
    except: total_hours = 10.0

    if st.button("🚀 Generate My Skill Roadmap", key="roadmap_btn"):
        prompt = f"""
Create a vibrant, engaging skill roadmap for a {year} student interested in {domain}.
Total available time: {total_hours} hours.

Structure:
🎯 CLEAR PHASES with time allocation
📚 SPECIFIC skills per phase
🛠️ PRACTICAL projects
💡 LEARNING resources
⏰ TIME management tips
"""
        answer = generate_ai_response(prompt)
        st.markdown('<div class="success-box"><h3>✨ Your Personalized Skill Roadmap</h3></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="ai-bubble">{answer}</div>', unsafe_allow_html=True)
        speak_text()

def career_salary_insights():
    st.markdown('<div class="info-box"><h3>💼 Career & Salary Insights</h3><p>Get detailed career guidance and compensation data</p></div>', unsafe_allow_html=True)
    role = ask("🎯 What is the specific job role you are aiming for?", key="role")
    if not role: return st.markdown('<div class="warning-box">Please provide a job role</div>', unsafe_allow_html=True)
    exp = ask("📊 Experience level you're interested in?", ["🎓 Entry-Level", "💼 Mid-Level (3-5 years)", "👨‍💼 Senior (5+ years)"], key="exp")
    if not exp: return st.markdown('<div class="warning-box">Please select experience level</div>', unsafe_allow_html=True)
    location = st.text_input("🌍 Which city or region? (Optional)", key="location")

    if st.button("💰 Get Salary Insights", key="salary_btn"):
        prompt = f"""
Career insights for: {role}
Experience: {exp}
Location: {location if location else 'Global Average'}

Include salary ranges, skills, companies, growth, trends.
"""
        answer = generate_ai_response(prompt)
        st.markdown('<div class="success-box"><h3>💼 Career & Salary Insights</h3></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="ai-bubble">{answer}</div>', unsafe_allow_html=True)
        speak_text()

def certification_guidance():
    st.markdown('<div class="info-box"><h3>📜 Certification Guidance</h3><p>Boost your profile with the right certifications</p></div>', unsafe_allow_html=True)
    tech = ask("🛠️ Which domain would you like certification guidance for?", key="tech")
    if not tech: return st.markdown('<div class="warning-box">Please provide a domain</div>', unsafe_allow_html=True)
    level = ask("📊 What is your current skill level?", ["🌱 Beginner", "🚀 Intermediate", "🔥 Advanced"], key="level")
    if not level: return st.markdown('<div class="warning-box">Please select skill level</div>', unsafe_allow_html=True)

    if st.button("🎯 Get Certification Guide", key="cert_btn"):
        prompt = f"Suggest best certifications for {tech} at {level} level with details."
        answer = generate_ai_response(prompt)
        st.markdown('<div class="success-box"><h3>📜 Certification Guidance</h3></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="ai-bubble">{answer}</div>', unsafe_allow_html=True)
        speak_text()

def project_ideas():
    st.markdown('<div class="info-box"><h3>🚀 Project Ideas Generator</h3><p>Build impressive projects for your portfolio</p></div>', unsafe_allow_html=True)
    domain = ask("🎨 What domain or technology do you want the project to focus on?", key="proj_domain")
    if not domain: return st.markdown('<div class="warning-box">Please provide a domain</div>', unsafe_allow_html=True)
    level = ask("📊 What is your current skill level for this domain?", ["🌱 Beginner", "🚀 Intermediate", "🔥 Advanced"], key="proj_level")
    if not level: return st.markdown('<div class="warning-box">Please select skill level</div>', unsafe_allow_html=True)

    if st.button("💡 Generate Project Ideas", key="project_btn"):
        prompt = f"Suggest 3 practical project ideas for {domain} suitable for {level} level developer."
        answer = generate_ai_response(prompt)
        st.markdown('<div class="success-box"><h3>🚀 Project Ideas</h3></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="ai-bubble">{answer}</div>', unsafe_allow_html=True)
        speak_text()

# -------- Main ----------
def main():
    st.markdown('<h1 class="main-header">CareerPath</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">🎯 Empowering Skills for a Brighter Tomorrow</p>', unsafe_allow_html=True)
    display_feature_cards()
    st.markdown("---")
    st.markdown('<div class="card"><h2>🎯 What is your primary goal today?</h2></div>', unsafe_allow_html=True)

    goal_options = {
        "🎯 Skill Roadmap": "A. Create personalized learning path",
        "💼 Career Insights": "B. Get salary and career guidance",
        "📜 Certifications": "C. Find the right certifications",
        "🚀 Project Ideas": "D. Generate portfolio project ideas"
    }

    goal = st.selectbox("Choose your goal:", ["Select your goal..."] + list(goal_options.keys()))
    st.markdown("---")

    if "Skill Roadmap" in goal: skill_roadmap()
    elif "Career Insights" in goal: career_salary_insights()
    elif "Certifications" in goal: certification_guidance()
    elif "Project Ideas" in goal: project_ideas()
    else:
        st.markdown("""<div class="info-box"><h3>👋 Welcome to CareerPath!</h3><p>Select a goal from above to get started with your personalized career guidance.</p></div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()