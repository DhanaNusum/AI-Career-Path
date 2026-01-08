🎓 CareerPath – AI-Powered Academic Assistant

CareerPath is an AI-powered academic assistant designed to help students and working professionals plan their learning journey with personalized roadmaps and guidance.
The platform addresses common career challenges by providing structured, personalized career development solutions.

## 🚀 Features
- **Skill Roadmap Generator**: Create personalized learning paths based on domain, academic year, and available time
- **Career & Salary Insights**: Get detailed information about job roles, required skills, salary ranges, and career progression
- **Certification Guidance**: Receive recommendations for relevant certifications based on domain and skill level
- **Project Ideas Generator**: Generate practical portfolio project ideas tailored to your expertise level
- **Certifications Directory**: Browse mandatory certifications organized by engineering branches (CSE, ECE, EEE, Mechanical, Civil)
- **User Authentication**: Simple login/signup system for personalized experience
- **AI Chatbot Integration**: Interactive chatbot powered by Google Gemini AI

  
## 🛠️ Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Streamlit
- **AI Integration**: Google Gemini AI (Gemini 2.5 Pro)
- **Text-to-Speech**: gTTS (Google Text-to-Speech)
- **Icons**: Font Awesome 6.4.0


## 📋 Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Google Gemini API key



## 🔧 Installation
1. Clone the repository:
git clone https://github.com/yourusername/CareerPath.git
cd CareerPath
2. Install required Python packages:
pip install streamlit google-genai gtts
3. Get your Google Gemini API key from Google AI Studio
4. Update the API key in chatbot.py:
client = genai.Client(api_key="YOUR_API_KEY_HERE")


🚀 Running the Application
Step 1: Start the Streamlit Backend
Open a terminal in the project directory and run:
streamlit run chatbot.py
The Streamlit app will be available at http://localhost:8501
Step 2: Open the Frontend
Option A: Direct File Open
Simply open index.html in your web browser
Option B: Local Server (Recommended)
Using Python:
python -m http.server 8000
Then open http://localhost:8000 in your browser


📁 Project Structure
CareerPath/├── chatbot.py              # Streamlit backend application
           ├── index.html               # Main landing page
           ├── get_started.html         # Login/Signup landing page
           ├── login.html               # User login page
           ├── signup.html              # User registration page
           ├── certifications.html      # Certifications directory
           └── README.md                # Project documentation
💡 Usage
1. Getting Started: Open index.html in your browser
2. Create Account: Click "Get Started" and sign up for a new account
3. Access Chatbot: Click the chatbot button (bottom-right) or the robot icon in the "Our Solution" section
4. Choose Your Goal: Select from:
->Skill Roadmap
->Career Insights
->Certifications
->Project Ideas
5. Get Personalized Guidance: Follow the interactive prompts to receive AI-generated recommendations


   
🎯 Key Features Explained
Skill Roadmap Generator
->Input your domain interest, academic year, and available hours
->Receive a structured learning path with phases, skills, projects, and resources
Career & Salary Insights
->Get information about specific job roles
->View salary ranges for different experience levels
->Understand required skills and career progression
Certification Guidance
->Find relevant certifications for your domain
->Filter by skill level (Beginner/Intermediate/Advanced)
->Access direct links to certification providers
Project Ideas Generator
->Generate portfolio project ideas
->Tailored to your domain and skill level
->Practical projects to showcase your abilities
🔐 Authentication
The current authentication system uses localStorage for demo purposes. Note: This is not secure for production use. For production, implement proper backend authentication with secure password hashing and database storage.



🙏 Acknowledgments
Google Gemini AI for powering the intelligent recommendations
Streamlit for the interactive backend framework
Font Awesome for icons

📄 Project Status
✅ Project Completed - All features have been implemented and tested.
