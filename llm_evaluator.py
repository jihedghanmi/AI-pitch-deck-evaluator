from google import genai
import os, json
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def evaluate(deck_text, dimension, prompt):
    full_prompt = f"""
You are a senior venture capital investor who has evaluated hundreds of pitch decks
and knows exactly what separates a Seed-fundable startup from an average one.
You think like Paul Graham, Marc Andreessen, and top-tier VC partners.

Analyze the following pitch deck and evaluate it on this dimension: {dimension}

{prompt}

Pitch Deck Content:
{deck_text}

Respond ONLY in this exact JSON format, no extra text, no markdown:
{{
  "dimension": "{dimension}",
  "score": <integer 1-10>,
  "strengths": ["...", "..."],
  "weaknesses": ["...", "..."],
  "investor_insights": ["...", "..."]
}}
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=full_prompt
    )
    text = response.text.strip().replace("```json", "").replace("```", "").strip()
    return json.loads(text)


def run_evaluation(deck_text):
    deck_text = deck_text[:3000]  # remove in production

    dimensions = [
        {
            "name": "Investor Communication & Deck Clarity",
            "prompt": """Evaluate how effectively this pitch deck communicates its ideas 
            in a clear, structured, and investor-ready format. Specifically assess:
            - Grammar, spelling, and linguistic accuracy
            - Unclear, ambiguous, or poorly structured phrasing
            - Overly complex or unnecessarily dense wording
            - Slides overloaded with information that reduce readability
            - Repetitive or unfocused content that weakens key messages
            Is this deck investment-grade in its presentation quality?"""
        },
        {
            "name": "Narrative & Founder Storytelling",
            "prompt": """Evaluate whether the pitch deck follows a logical and compelling 
            investment narrative. Check for the presence and quality of each of these 
            sections IN ORDER:

            1. Cover — Is the company name, tagline, and purpose immediately clear?
            2. Problem — Is a specific, painful problem introduced early and compellingly?
            3. Solution — Does the solution directly follow and address the problem?
            4. Product — Is the actual product explained clearly with features or demo?
            5. Market Opportunity — Is the TAM/SAM/SOM defined with credible sizing?
            6. Business Model — Is it clear how the company makes money?
            7. Traction / Early Signals — Are there metrics, pilots, revenue, or user growth?
            8. Go-to-Market Strategy — Is there a clear plan to acquire customers?
            9. Team — Are the founders introduced with relevant background?
            10. Ask — Is the funding amount and use of funds clearly stated?

            For each section note if it is: present and strong, present but weak, or missing entirely.
            Then evaluate whether the overall flow builds a convincing investment case."""
        },
        {
            "name": "Problem-Solution Fit (Investment Lens)",
            "prompt": """This is the core investment validation. Evaluate in this order:

            STEP 1 — Identify the core problem being addressed.
            STEP 2 — Identify the proposed solution.
            STEP 3 — Identify the causal link: why does this solution uniquely and 
            directly solve this specific problem?

            Then evaluate:
            - Is the problem clearly defined, specific, and meaningful?
            - Does it represent a real, frequent, or high-impact pain point?
            - Does the solution directly and logically address the problem?
            - Is the problem-solution fit strong enough to justify a venture-scale opportunity?
            - What would a skeptical investor challenge about this fit?"""
        }
    ]

    results = []
    for d in dimensions:
        result = evaluate(deck_text, d["name"], d["prompt"])
        results.append(result)
    return results