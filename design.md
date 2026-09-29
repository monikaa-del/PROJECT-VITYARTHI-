# System Design Document

# Smart Resume Analyzer & Skill Gap Finder

## 1. Overview

The Smart Resume Analyzer & Skill Gap Finder is a Python-based application designed to analyze a user's resume and compare it against predefined job role requirements.

The system extracts skills from a resume PDF, calculates a match percentage for a selected role, identifies missing skills, and generates a learning roadmap to help users improve their employability.

---

# 2. System Architecture

The application follows a modular architecture.

```text
+------------------+
|   Resume PDF     |
+------------------+
          |
          v
+------------------+
|  PDF Reader      |
+------------------+
          |
          v
+------------------+
| Skill Extractor  |
+------------------+
          |
          v
+------------------+
| Role Database    |
|  (roles.json)    |
+------------------+
          |
          v
+------------------+
| Skill Analyzer   |
+------------------+
          |
          +----------------+
          |                |
          v                v
+----------------+   +----------------+
| Match Score    |   | Missing Skills |
+----------------+   +----------------+
          |
          v
+------------------+
| Roadmap Generator|
+------------------+
          |
          v
+------------------+
| Report Generator |
+------------------+
```

---

# 3. Project Structure

```text
Resume-Analyzer
│
├── DATA
│   └── roles.json
│
├── REPORTS
│   └── analysis_report.txt
│
├── RESUME
│   └── sample_resume.pdf
│
├── SRC
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
└── PROBLEM_STATEMENT.md
```

---

# 4. Module Design

## 4.1 Resume Reader Module

### File

```text
resume_reader.py
```

### Responsibility

- Open PDF files
- Extract text from each page
- Return complete resume content

### Input

```text
Resume PDF Path
```

### Output

```text
Extracted Resume Text
```

---

## 4.2 Skill Extractor Module

### File

```text
skill_extractor.py
```

### Responsibility

- Scan extracted text
- Search predefined skills
- Create skills list

### Example

Input:

```text
Python, SQL, Git
```

Output:

```python
["Python", "SQL", "Git"]
```

---

## 4.3 Analyzer Module

### File

```text
analyzer.py
```

### Responsibility

- Compare user skills with role skills
- Calculate match percentage
- Identify missing skills

### Formula

```text
Match Percentage =
(Matched Skills / Required Skills) × 100
```

---

## 4.4 Roadmap Generator Module

### File

```text
roadmap.py
```

### Responsibility

Generate a learning roadmap based on missing skills.

### Example

```text
Week 1 : Learn SQL
Week 2 : Learn Flask
Week 3 : Learn Pandas
```

---

## 4.5 Report Generator Module

### File

```text
report_generator.py
```

### Responsibility

Generate and save analysis results in a text report.

### Output File

```text
REPORTS/analysis_report.txt
```

---

# 5. Data Design

## Role Dataset

Stored inside:

```text
DATA/roles.json
```

Example:

```json
{
  "Python Developer": [
    "Python",
    "Git",
    "SQL",
    "Flask",
    "Pandas"
  ]
}
```

---

# 6. Input Design

User provides:

```text
Resume PDF Path
```

Example:

```text
RESUME/sample_resume.pdf
```

User also selects a role:

```text
1. Python Developer
2. Data Analyst
3. AI Engineer
```

---

# 7. Output Design

The system displays:

```text
Skills Found
Match Percentage
Missing Skills
Learning Roadmap
```

Example:

```text
Skills Found:
Python
Git

Match Score:
40%

Missing Skills:
SQL
Flask
Pandas

Learning Roadmap:
Week 1 - SQL
Week 2 - Flask
Week 3 - Pandas
```

---

# 8. Workflow

```text
Start
  |
  v
Read Resume PDF
  |
  v
Extract Resume Text
  |
  v
Extract Skills
  |
  v
Choose Job Role
  |
  v
Compare Skills
  |
  v
Calculate Match Score
  |
  v
Identify Missing Skills
  |
  v
Generate Roadmap
  |
  v
Generate Report
  |
  v
End
```

---

# 9. Future Enhancements

- Graphical User Interface (GUI)
- AI-based Skill Recommendation
- Resume Scoring System
- Support for DOCX Files
- Machine Learning Integration
- Web-Based Dashboard
- Resume Ranking System

---

# 10. Conclusion

The Smart Resume Analyzer & Skill Gap Finder provides an automated solution for resume evaluation. The system helps users understand their current skill level, identify missing skills, and receive personalized learning recommendations for career growth.
