def parse_slides(slides):
    combined = ""
    for slide in slides:
        combined += f"\n--- Slide {slide['slide_number']} ---\n{slide['text']}\n"
    return combined