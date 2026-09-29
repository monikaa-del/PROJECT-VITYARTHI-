def extract_skills(text):

    skills_db = [
        "Python",
        "C++",
        "Java",
        "SQL",
        "Git",
        "HTML",
        "CSS",
        "Flask",
        "Pandas",
        "Excel",
        "Tableau",
        "Machine Learning"
    ]

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills
