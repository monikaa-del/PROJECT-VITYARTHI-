def analyze(user_skills, role_skills):

    matched = []

    for skill in role_skills:
        if skill in user_skills:
            matched.append(skill)

    score = (len(matched) / len(role_skills)) * 100

    missing_skills = []

    for skill in role_skills:
        if skill not in user_skills:
            missing_skills.append(skill)

    return score, missing_skills 
