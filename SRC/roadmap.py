def generate_roadmap(missing_skills):

    print("\nLearning Roadmap:")

    week = 1

    for skill in missing_skills:
        print(f"Week {week}: Learn {skill}")
        week += 1
