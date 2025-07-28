import os
import fitz  # PyMuPDF
import json
from typing import List, Dict

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def is_valid_heading(text: str) -> bool:
    text = text.strip()
    if not text or len(text) < 4:
        return False
    if ":" in text or text.lower().startswith(("mission", "goal", "regular", "distinction")):
        return False
    return True

def extract_outline_from_pdf(pdf_path: str) -> Dict:
    doc = fitz.open(pdf_path)
    title = ""
    font_sizes = []

    for page_num in range(min(3, len(doc))):
        blocks = doc[page_num].get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span.get("text", "").strip()
                    size = span.get("size", 0)
                    font_sizes.append(size)
                    if len(text.split()) > 3 and size >= max(font_sizes or [0]):
                        title = text

    max_font = max(font_sizes or [0])
    min_font = min(font_sizes or [1])
    threshold_h1 = max_font * 0.9
    threshold_h2 = (max_font + min_font) / 2

    outline: List[Dict] = []

    for page_num in range(len(doc)):
        blocks = doc[page_num].get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span.get("text", "").strip()
                    size = span.get("size", 0)
                    if not is_valid_heading(text) or text == title:
                        continue
                    level = None
                    if size >= threshold_h1:
                        level = "H1"
                    elif size >= threshold_h2:
                        level = "H2"
                    if level:
                        if not any(h["text"] == text and h["page"] == page_num for h in outline):
                            outline.append({
                                "level": level,
                                "text": text,
                                "page": page_num
                            })

    return {
        "title": title,
        "outline": outline
    }

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            result = extract_outline_from_pdf(input_path)
            output_filename = os.path.splitext(filename)[0] + ".json"
            with open(os.path.join(OUTPUT_DIR, output_filename), "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
