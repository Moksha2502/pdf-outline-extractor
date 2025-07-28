
# Challenge 1B: Persona-Driven Document Intelligence

## 🚀 Overview

This repository contains the solution to **Round 1B** of the Adobe India Hackathon 2025. The objective is to develop an intelligent PDF processing system that extracts and prioritizes the most relevant sections from a collection of PDFs based on a **persona** and a **job-to-be-done**.

The solution is fully containerized using Docker, runs **offline on CPU**, and processes PDF collections to generate structured and ranked insights.

---

## 🎯 Challenge Objective

Design and build a system that:
- Accepts a **set of 3–10 PDF documents**
- Accepts a **persona** and a **job-to-be-done**
- Extracts **relevant sections** from the PDFs
- Ranks extracted sections by **importance**
- Provides **refined sub-section summaries**
- Outputs a structured JSON file conforming to the required schema

---

## 📂 Folder Structure

```

challenge\_1b/
├── Dockerfile
├── persona\_extractor.py
├── requirements.txt
├── input/
│   ├── doc1.pdf
│   ├── doc2.pdf
│   └── persona.json
├── output/
│   └── output.json (generated)
├── sample\_dataset/
│   ├── input/ (optional test PDFs)
│   ├── output\_schema.json
├── README.md
├── approach\_explanation.md

````

---

## ⚙️ Docker Instructions

### 🔧 Build the Docker Image

```bash
docker build --platform linux/amd64 -t persona-analyzer .
````

### ▶️ Run the Docker Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  persona-analyzer
```

* Input PDFs and `persona.json` should be in the `input/` folder.
* Output `output.json` will be saved in the `output/` folder.
* The container is run in a **read-only, no-network environment** as required.

---

## 📌 Input Specification

### 1. PDF Documents

* A collection of **3 to 10 PDF files** placed in the `/app/input` directory.
* Must be research papers, reports, textbooks, or any domain documents.

### 2. Persona File (`persona.json`)

```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"
}
```

---

## ✅ Output Format (`output.json`)

```json
{
  "metadata": {
    "documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "...",
    "job_to_be_done": "...",
    "processed_at": "2025-07-26T18:00:00Z"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "section_title": "Graph Attention Networks",
      "importance_rank": 1
    },
    ...
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "refined_text": "Graph Attention Networks improve prediction accuracy in drug discovery by weighting neighborhood nodes...",
      "section_title": "Graph Attention Networks"
    }
  ]
}
```

---

## 🧠 Methodology Summary

See [`approach_explanation.md`](./approach_explanation.md) for a detailed description of:

* How persona + job drive relevance
* How sections are ranked
* NLP techniques and logic used for summarization
* Trade-offs and optimizations

---

## ✅ Constraints Met

| Constraint               | Status          |
| ------------------------ | --------------- |
| CPU Only                 | ✅ Yes           |
| ≤ 1GB model size         | ✅ Yes           |
| ≤ 60 sec processing time | ✅ Optimized     |
| No Internet Access       | ✅ Fully Offline |
| Docker AMD64 Support     | ✅ Supported     |

---

## 🧪 Testing Suggestions

Test with different combinations:

* Business reports + Analyst persona
* Academic papers + Researcher persona
* Education content + Student persona

---

## 📚 Dependencies

* `PyMuPDF` – PDF text and layout extraction
* `transformers` (if used) – Lightweight summarization
* `nltk`, `re`, `json`, `datetime`

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

## 🔒 Important Notes

* All processing is **offline**
* No hardcoded values, filenames, or logic
* Supports cross-platform and diverse document types

---

## 📬 Contact

For queries or clarifications, feel free to reach out via GitHub Issues.

---

```

Let me know if you also want the `approach_explanation.md`, `persona_extractor.py`, or `requirements.txt`.
```
