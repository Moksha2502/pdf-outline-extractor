


📘 Challenge 1B: Persona-Driven Document Intelligence

🧩 Overview

This repository contains the solution for **Round 1B** of the Adobe India Hackathon 2025. The objective is to develop an intelligent PDF analysis system that extracts and ranks the most relevant content from a set of documents based on a user-defined **persona** and a **job-to-be-done**.

The solution is fully containerized with Docker, runs offline on CPU, and generates structured, insightful output in the specified JSON format.

---

 🎯 Problem Statement

You are given:
- A collection of **3 to 10 PDF documents**
- A `persona.json` file describing a user role and a task

You must build a system that:
- Extracts semantically relevant sections from the PDFs
- Ranks the sections in order of importance
- Summarizes the most relevant subsections
- Returns a structured output in JSON format

---

 📁 Repository Structure

```

challenge\_1b/
├── Dockerfile                  # Docker configuration
├── persona\_extractor.py       # Main processing script
├── requirements.txt           # Python dependencies
├── input/                     # Input PDFs and persona JSON
│   ├── doc1.pdf
│   ├── doc2.pdf
│   └── persona.json
├── output/                    # Output directory (populated at runtime)
│   └── output.json
├── sample\_dataset/            # (Optional) test cases or schemas
│   ├── input/
│   └── output\_schema.json
├── approach\_explanation.md    # Explanation of the methodology
└── README.md                  # This documentation

````

---

 ⚙️ Execution Guide

 🔧 Build Docker Image

```bash
docker build --platform linux/amd64 -t persona-analyzer .
````

 ▶️ Run Docker Container

```bash
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  persona-analyzer
```

> 🔐 The input directory is mounted as read-only. No internet access is permitted within the container.

---

📦 Input Format

 1. Documents

A folder containing 3–10 PDF files (e.g., `doc1.pdf`, `doc2.pdf`, etc.).

 2. Persona File (`persona.json`)

Example:

```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare a literature review on graph neural networks for drug discovery"
}
```

---

## ✅ Output Format

The expected output is a structured JSON file with the following schema:

```json
{
  "metadata": {
    "documents": ["doc1.pdf", "doc2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Prepare a literature review on graph neural networks",
    "processed_at": "2025-07-26T18:00:00Z"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "section_title": "Graph Attention Networks",
      "importance_rank": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "refined_text": "Graph Attention Networks are effective for drug discovery...",
      "section_title": "Graph Attention Networks"
    }
  ]
}
```

---

## 🧠 Methodology Summary

See [`approach_explanation.md`](./approach_explanation.md) for a complete explanation of:

* Text extraction techniques
* Relevance scoring logic
* Section ranking strategy
* Subsection summarization pipeline

---

 ✅ Constraints Met

| Constraint            | Status             |
| --------------------- | ------------------ |
| CPU-only              | ✅ Supported        |
| Model size ≤ 1GB      | ✅ Compliant        |
| Processing time ≤ 60s | ✅ Optimized        |
| Offline / No network  | ✅ Fully Air-gapped |
| Architecture: AMD64   | ✅ Compatible       |

---

 📚 Dependencies

All dependencies are listed in `requirements.txt` and installed during Docker build.

Key libraries:

`PyMuPDF` for PDF parsing
 `transformers` (optional) for summarization
 `nltk`, `scikit-learn`, `json`, `datetime` for NLP and logic

To install locally:

```bash
pip install -r requirements.txt
```



🔍 Testing Guidelines

Test with diverse combinations of:

* PDF complexity (layouts, languages, formats)
* Persona types (student, analyst, researcher, etc.)
* Job objectives (summarize, review, extract)



📑 Validation Checklist

[x] Input PDFs and persona are processed correctly
[x] Output is generated as `output.json`
[x] Section ranking reflects persona needs
[x] Subsection summaries are relevant
[x] Output conforms to required schema
[x] Container executes within constraints


📬 Contact & Support

For clarifications or collaboration, please use the GitHub issue tracker.

All logic is generic and does not rely on hardcoded values. No external APIs are used. The container is built to comply strictly with the competition rules.



