import streamlit as st
import tempfile, json
from pdf_extractor import extract_slides
from slide_parser import parse_slides
from llm_evaluator import run_evaluation
from aggregator import aggregate, to_json

st.set_page_config(page_title="AI Pitch Deck Evaluator", layout="wide")
st.title(" AI Pitch Deck Evaluator")
st.caption("Evaluate your startup pitch deck from an investor's perspective.")

uploaded_file = st.file_uploader("Upload your pitch deck (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Extracting slides..."):
        slides = extract_slides(tmp_path)
        deck_text = parse_slides(slides)

    st.success(f" Extracted {len(slides)} slides")

    with st.expander("View extracted slide text"):
        st.text(deck_text)

    if st.button(" Evaluate Pitch Deck"):
        with st.spinner("Evaluating with AI... this may take 20-30 seconds"):
            results = run_evaluation(deck_text)
            report = aggregate(results)

        st.subheader(f" Overall Score: {report['overall_score']} / 10")

        for dim in report["dimensions"]:
            with st.expander(f"**{dim['dimension']}** — Score: {dim['score']}/10"):
                st.markdown("####  Strengths")
                for s in dim["strengths"]:
                    st.markdown(f"- {s}")

                st.markdown("####  Weaknesses")
                for w in dim["weaknesses"]:
                    st.markdown(f"- {w}")

                st.markdown("####  Investor Insights")
                for i in dim["investor_insights"]:
                    st.markdown(f"- {i}")

        st.subheader(" Full JSON Report")
        st.json(report)
        st.download_button("Download JSON Report", to_json(report), "report.json", "application/json")