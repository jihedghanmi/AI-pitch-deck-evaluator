AI Pitch Deck Evaluator

An AI-powered tool that evaluates startup pitch decks from a venture capital investor’s perspective.

Overview

This application analyzes a pitch deck (PDF format) and generates a structured evaluation, simulating how real investors assess early-stage startups.

The system extracts and evaluates the content across three key dimensions used in venture capital decision-making.

Evaluation Dimensions

1. Investor Communication \& Deck Clarity

Evaluates grammar, structure, readability, and information density.

2. Narrative \& Founder Storytelling

Checks the standard startup narrative flow:
Cover → Problem → Solution → Market → Business Model → Traction → Go-To-Market → Team → Ask

3. Problem–Solution Fit (Investment Lens)

Assesses whether the problem is clearly defined, whether the solution addresses it effectively, and how strong the causal link is between both.

Each dimension produces:

Score
Key strengths
Key weaknesses
Investor-style insights and risks

The final score is the average of all three dimensions.

Tech Stack
Tool	Purpose
Streamlit	Web interface
PyMuPDF	PDF text extraction
Google Gemini 2.0 Flash	AI evaluation engine
python-dotenv	Environment variable management
Setup Instructions

1. Install dependencies
pip install -r requirements.txt
2. Configure API key
Create a .env file in the project root:

GEMINI\_API\_KEY=your\_api\_key\_here

Get your API key from:
https://aistudio.google.com







3. Run the application

streamlit run app.py





Project Structure

pitch-deck-evaluator/
├── app.py              # Main Streamlit application
├── pdf\_extractor.py    # PDF text extraction logic
├── slide\_parser.py     # Slide formatting utilities
├── llm\_evaluator.py    # Gemini evaluation engine
├── aggregator.py       # Score aggregation logic
├── .env.example        # Environment variable template
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

Output

For each pitch deck, the system generates:

Individual dimension scores
Strengths and weaknesses
Investor-focused insights
Overall aggregated score

A structured JSON report is also generated for download after evaluation.

Notes
Only text-based PDF files are supported (scanned PDFs may not work correctly)
Optimized for English-language pitch decks
Gemini API free tier has usage limits depending on account quota
The current evaluation is optimized for concise pitch decks. Extended analysis mode is planned for future iterations

