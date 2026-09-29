# Problem Statement

## Title
Smart Resume Analyzer & Skill Gap Finder

## Background

Recruiters often receive hundreds of resumes for a single job role. Manually screening resumes and identifying whether a candidate possesses the required skills can be time-consuming and inefficient. Similarly, students and job seekers may find it difficult to understand whether their current skill set matches industry expectations for a particular role.

## Problem

There is a need for a system that can automatically analyze a resume, identify the candidate's skills, compare them with the requirements of a selected job role, and provide actionable feedback regarding missing skills and improvement areas.

## Objective

The objective of this project is to develop a Python-based Resume Analyzer that:

- Reads and analyzes resumes in PDF format.
- Extracts relevant technical skills from the resume.
- Compares extracted skills against predefined job role requirements.
- Calculates a match percentage between the resume and the selected role.
- Identifies missing skills.
- Generates a personalized learning roadmap for skill improvement.
- Produces an analysis report for future reference.

## Proposed Solution

The Smart Resume Analyzer uses Python and PDF processing techniques to extract text from resumes and identify technical skills using a predefined skills database. The extracted skills are compared with role-specific requirements stored in a JSON dataset. Based on the comparison, the system calculates a compatibility score and suggests skills that the candidate should learn to improve employability.

## Features

- PDF Resume Reading
- Automatic Skill Extraction
- Multiple Job Role Support
- Match Score Calculation
- Missing Skill Identification
- Learning Roadmap Generator
- Report Generation
- Command Line Execution

## Technologies Used

- Python
- PyPDF2
- JSON
- File Handling

## Expected Outcome

The system will help students and job seekers understand their strengths and weaknesses with respect to a chosen job role. It will provide a clear skill-gap analysis and recommend a roadmap for learning missing technologies, thereby assisting users in career development and interview preparation.

## Conclusion

This project demonstrates the practical application of Python in document processing, data analysis, and career guidance. The system offers a simple, scalable, and automated solution for resume evaluation and skill-gap analysis.
