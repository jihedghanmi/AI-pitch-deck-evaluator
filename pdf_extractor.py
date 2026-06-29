import fitz  # PyMuPDF

def extract_slides(pdf_path):
    doc = fitz.open(pdf_path)
    slides = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        slides.append({
            "slide_number": i + 1,
            "text": text if text else "[No text on this slide]"
        })
    return slides