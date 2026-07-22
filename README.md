# CareerPath

CareerPath is a local Streamlit app that provides interactive career guidance using Google Gemini.
The project currently contains one working file:

- `chatbot.py` — the Streamlit application.

## What it does
The app lets you choose one of four career assistance flows:

1. **Skill Roadmap**
   - Generates a personalized learning roadmap for your chosen domain.
   - Asks for your current year or professional level and available learning hours.
   - Uses AI to produce a phased plan, project ideas, and time allocation tips.

2. **Career Insights**
   - Provides role-specific guidance, salary expectations, and growth advice.
   - Collects your target job role, experience level, and optional location.

3. **Certification Guidance**
   - Recommends certifications tailored to your selected domain and skill level.
   - Helps identify which certifications are most useful for your goals.

4. **Project Ideas**
   - Suggests practical project ideas for your domain and current skill level.
   - Helps build a portfolio with relevant hands-on work.

## Requirements
- Python 3.11+ (or compatible Python 3.x)
- `streamlit`
- `google-genai`
- `gtts`

## Install
Open PowerShell in the project folder and run:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Set your Gemini API key before running the app:

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

## Run the app
Start the Streamlit app from the project folder:

```powershell
streamlit run chatbot.py
```

Then open your browser at:

```text
http://localhost:8501
```

## How to use the app
1. Open the app in the browser.
2. Choose a goal from the dropdown: Skill Roadmap, Career Insights, Certification Guidance, or Project Ideas.
3. Fill in the questions that appear for the chosen flow.
4. Click the action button to generate the AI response.

## Notes
- The app uses the Gemini API client from `google-genai`.
- `gtts` is used to generate audio output and play it automatically in the app.
- A hardcoded API key is currently present in `chatbot.py`. Replace it with your own if required.

## API key setup
Set a valid Google Gemini API key as an environment variable:

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

## Troubleshooting
- If `streamlit` is not found, install it again and confirm the Python environment matches:

```powershell
python -m pip install streamlit
```

- If `google-genai` fails to install, ensure your Python version is supported:

```powershell
python -m pip install google-genai
```

- If the app cannot connect or hangs, the Gemini API key may be invalid or rate-limited.

- If the audio fails, it will still show the AI response in text.

## Helpful commands
```powershell
cd path\to\your\project
python -m pip install -r requirements.txt
streamlit run chatbot.py
```
