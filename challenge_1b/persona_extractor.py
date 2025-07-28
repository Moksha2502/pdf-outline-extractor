import os
import json
import time
import fitz  # PyMuPDF
from typing import List, Dict
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

# Load lightweight model (must be < 1GB and offline)
model = SentenceTransformer('all-MiniLM-L6-v2')  # ~80MB

def read_persona_job() -> Dict:
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".json"):
            with open(os.path.join(INPUT_DIR, file), "r", encoding="utf-8") as f:
                return json.load(f)
    raise FileNotFoundError("No persona/job JSON found in input.")

def extract_text_chunks(pdf_path: str) -> List[Dict]:
    doc = fitz.open(pdf_path)
    chunks = []
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                line_text = " ".join(span.get("text", "") for span in line.get("spans", []))
                if line_text.strip():
                    chunks.append({
                        "document": os.path.basename(pdf_path),
                        "page_number": page_num,
                        "text": line_text.strip()
                    })
    return chunks

def rank_relevance(chunks: List[Dict], query: str) -> List[Dict]:
    corpus = [chunk["text"] for chunk in chunks]
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(query_embedding, corpus_embeddings)[0]
    results = []
    for i, score in enumerate(scores):
        results.append({
            **chunks[i],
            "score": float(score)
        })
    return sorted(results, key=lambda x: x["score"], reverse=True)

def process_documents():
    start_time = time.time()

    persona_job = read_persona_job()
    persona = persona_job.get("persona", "")
    job = persona_job.get("job_to_be_done", "")
    query = f"{persona}: {job}"

    all_chunks = []
    input_docs = []

    for file in os.listdir(INPUT_DIR):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, file)
            chunks = extract_text_chunks(pdf_path)
            all_chunks.extend(chunks)
            input_docs.append(file)

    ranked = rank_relevance(all_chunks, query)
    top_sections = ranked[:10]

    section_summary = []
    subsection_analysis = []

    for rank, section in enumerate(top_sections, 1):
        section_summary.append({
            "document": section["document"],
            "page_number": section["page_number"],
            "section_title": section["text"][:80],
            "importance_rank": rank
        })
        subsection_analysis.append({
            "document": section["document"],
            "page_number": section["page_number"],
            "refined_text": section["text"]
        })

    output = {
        "metadata": {
            "input_documents": input_docs,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "section_summary": section_summary,
        "subsection_analysis": subsection_analysis
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "persona_analysis.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Processed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    process_documents()
