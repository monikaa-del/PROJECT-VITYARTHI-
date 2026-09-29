# PROJECT-VITYARTHI-
# RESUME-ANALYZER-SKILL-GAP-FINDER
# Smart Resume Analyzer & Skill Gap Finder

## Overview

This project analyzes a resume PDF and compares it with job role requirements.

## Features

- PDF Resume Reading
- Skill Extraction
- Role Selection
- Match Score Calculation
- Missing Skill Detection
- Learning Roadmap Generation
- Report Generation

## Technologies Used

- Python
- PyPDF2
- JSON

## Project Structure

Resume-Analyzer
│
├── DATA
├── REPORTS
├── RESUME
├── SRC
├── main.py
└── requirements.txt

## Installation

```bash
pip install -r requirements.txt
resume-analyzer/
│
├── DATA/
│   └── roles.json
│
├── REPORTS/
│   └── analysis_report.txt
│
├── RESUME/
│   └── sample_resume.pdf
│
├── SRC/
│   ├── resume_reader.py
│   ├── skill_extractor.py
│   ├── analyzer.py
│   ├── roadmap.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
├── README.md
├── DESIGN.md
├── PROBLEM_STATEMENT.md

## Sample Output

Skills Found:
- Python
- Git

Match Score:
40%

Missing Skills:
- SQL
- Flask
- Pandas

Learning Roadmap:
Week 1: Learn SQL
Week 2: Learn Flask
Week 3: Learn Pandas
