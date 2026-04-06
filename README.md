# ResumeAI - Professional Resume Feedback Tool

🚀 **AI-powered Resume Intelligence**  

ResumeAI is an intelligent resume analyzer that mimics a professional recruiter. It extracts content from uploaded PDFs, analyzes resumes using a GenAI model, and delivers structured, actionable feedback. This tool goes beyond generic advice and highlights strengths, weaknesses, missing elements, ATS compatibility, and improvement suggestions.  

---

## Features

- **Resume Analysis Like a Recruiter:** Provides professional insights with actionable recommendations.  
- **Strengths & Weaknesses Identification:** Highlights sections to keep and areas to improve.  
- **Missing Sections Detection:** Flags underrepresented or absent resume elements.  
- **ATS Friendliness Assessment:** Scores resumes for applicant tracking systems compatibility.  
- **Bullet Point Improvements:** Suggests improvements for weak bullets.  
- **Structured, Readable Feedback:** Returns results in a clear, predictable format.  

---

## Project Structure

The project is organized for clarity and scalability:  



**File Responsibilities:**  
- `app.py` → User interface for uploading resumes and displaying results.  
- `resume_parser.py` → Extracts readable text from PDF resumes using PyMuPDF.  
- `feedback_engine.py` → Sends extracted text to the GenAI model and retrieves structured feedback.  
- `prompts.py` → Stores the AI prompt guiding analysis.  
- `.env` → Secures API keys (never hardcoded).  

---

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/Fauzan555/AI_Resume_Analyzer_Using_GenAI-Groq-API-.git
cd resume_ai_analyzer


# Install Dependencies

streamlit
pymupdf
python-dotenv
groq

# Setup Environment Variables

GROQ_API_KEY=your_groq_api_key_here

How It Works
1. Upload Resume

The user uploads a PDF resume through the Streamlit interface.

2. Extract Text

resume_parser.py extracts readable text from the PDF using PyMuPDF.

3. AI Feedback

feedback_engine.py sends the extracted text to the Groq-powered LLaMA model with a structured prompt from prompts.py. The AI returns feedback in a structured format:

Overall Summary
Strengths
Weaknesses
Missing or Underrepresented Sections
Bullet Point Improvements
ATS Friendliness Score
Final Actionable Suggestions
4. Display Results

Streamlit presents the AI feedback in a glassmorphism-style card with subtle animations for readability.

UI Highlights
Modern Dark Theme: Custom gradient background for professional appearance.
Glassmorphism Cards: Clear separation of content for better readability.
Animated Feedback Container: Enhances UX without distraction.
Google Fonts (Inter): Clean, modern typography.

Flow: Upload PDF → Click “Generate Professional Feedback” → View structured results.

Example Feedback Output
