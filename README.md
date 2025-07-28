# pdf-outline-extractor

---

### ✅ **Challenge 1A: Structured PDF Outline Extraction**

**Goal**:
Develop a Dockerized solution that extracts structured outlines (Title, H1, H2, H3) from PDF files and outputs standardized JSON for each input file.

**Key Features**:

* Automatically processes all PDFs in `/app/input`
* Extracts document title and headings with page numbers and levels
* Outputs conform to a predefined JSON schema
* Fully containerized and works offline
* Optimized for ≤10s runtime on 50-page PDFs using ≤16GB RAM

**Repo Includes**:

* `process_pdfs.py` – Outline extraction logic using `PyMuPDF`
* `Dockerfile` – Lightweight, cross-platform build for `linux/amd64`
* `README.md` – Execution guide, validation checklist, and structure
* Sample input/output + schema in `sample_dataset/`

**Execution**:

```bash
docker build --platform linux/amd64 -t pdf-processor .
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output:/app/output --network none pdf-processor
```

---

### ✅ **Challenge 1B: Persona-Driven Document Intelligence**

**Goal**:
Create a CPU-only system that intelligently analyzes a set of PDFs to extract and rank the most relevant sections based on a provided **persona** and **job-to-be-done**.

**Key Features**:

* Accepts multiple related PDFs + a `persona.json` input
* Extracts semantically relevant sections and refines summaries
* Ranks sections by relevance using a modular scoring pipeline
* Outputs metadata, ranked sections, and refined subsections in JSON

**Repo Includes**:

* `persona_extractor.py` – Section extraction and ranking logic
* `Dockerfile` – Offline container with NLP tools and PDF parsing
* `README.md` – Input/output format, scoring criteria, architecture
* `approach_explanation.md` – Methodology behind extraction logic

**Execution**:

```bash
docker build --platform linux/amd64 -t persona-analyzer .
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output:/app/output --network none persona-analyzer
```

---

### 🔒 Common Compliance (Both Challenges)

| Requirement           | Status                     |
| --------------------- | -------------------------- |
| CPU-only              | ✅ Supported                |
| Model Size Limit      | ✅ ≤ 200MB (1A), ≤ 1GB (1B) |
| Network Calls         | ✅ None                     |
| Runtime Limit         | ✅ < 10s (1A), < 60s (1B)   |
| AMD64 Compatible      | ✅ Yes                      |
| JSON Schema Adherence | ✅ Conformant               |

---


