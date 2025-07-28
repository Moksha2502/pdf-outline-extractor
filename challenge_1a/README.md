

---

# 📘 Challenge 1A: PDF Structure Extraction

## Overview

This repository contains a containerized solution for **Challenge 1A** of Adobe's *Connecting the Dots* Hackathon 2025. The goal is to extract a structured outline (including title and headings of levels H1–H3) from PDF documents and generate valid JSON files for each input document.

This solution is optimized for **accuracy, speed**, and **compliance with resource constraints**, and is built to run inside a Docker container in an **offline AMD64 CPU-only environment**.

---

## 🚀 Features

* Detects and extracts **title** and **headings** (H1, H2) from PDFs
* Outputs structured **JSON files** per document
* Handles a variety of PDFs including forms, reports, and books
* Runs efficiently in Docker within the 10-second time limit
* Fully offline and compliant with memory and CPU limits

---

## 🗂 Directory Structure

```
challenge_1a/
├── Dockerfile               # Container configuration
├── process_pdfs.py         # Main Python script for extraction
├── input/                  # Folder for input PDF files (mounted at /app/input)
├── output/                 # Folder for generated JSON files (mounted at /app/output)
└── README.md               # You're reading it
```

---

## ⚙️ How to Build and Run

### 🔧 Step 1: Build the Docker Image

```bash
docker build --platform linux/amd64 -t pdf-processor .
```

### ▶️ Step 2: Run the Processor on Input Files

```bash
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-processor
```

---

## 📄 Output Format

The output is a `.json` file for each `.pdf` file in the `input` folder, matching the schema defined below:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 0 },
    { "level": "H2", "text": "What is AI?", "page": 1 }
  ]
}
```

* **Title**: Extracted from the top 3 pages using font-size heuristics.
* **Headings**:

  * H1: Large prominent section headings
  * H2: Subheadings based on size and positioning

---

## 🧠 Implementation Logic

The extraction logic in `process_pdfs.py` includes:

* PDF parsing using **PyMuPDF (fitz)** for efficient and lightweight access
* Font size-based heuristics to infer heading levels
* Page-wise scanning to identify valid headings and skip noise
* Deduplication and filtering of headings using rules

---

## 🧪 Testing Strategy

* ✅ **Simple PDFs**: Text-only and academic-style documents
* ✅ **Complex Layouts**: Government forms, stylized reports
* ✅ **Performance**: Tested for ≤ 10 seconds on 50-page files

---

## ✅ Requirements Checklist

* [x] Automatically processes all PDFs in `/app/input`
* [x] Generates valid JSON per file in `/app/output`
* [x] Conforms to output schema
* [x] Runs fully offline (no network access)
* [x] Executes within 10 seconds for 50 pages
* [x] Memory ≤ 16GB | CPU ≤ 8 cores
* [x] Model size ≤ 200MB (none used)

---

## 🐳 Dockerfile (in root)

```dockerfile
FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app
COPY process_pdfs.py .

RUN pip install --no-cache-dir pymupdf

CMD ["python", "process_pdfs.py"]
```

---

## 📁 Example Input/Output

| Input File (PDF)      | Output File (JSON)     |
| --------------------- | ---------------------- |
| `file01.pdf`          | `file01.json`          |
| `ApplicationForm.pdf` | `ApplicationForm.json` |

All outputs are stored in `/app/output`.

---

## 📌 Notes

* No external models or APIs are used — this is a rule-based implementation.
* If you're using this as a base, you may integrate a small ML model (≤ 200MB) in the future to enhance classification.

---

## 📬 Contact

If you have any questions or feedback, feel free to reach out via GitHub Issues (if permitted) or contact your team lead.

---

Let me know if you'd like a **prewritten `process_pdfs.py`** with improved logic or a **sample GitHub repo** template zip to help you upload directly.
