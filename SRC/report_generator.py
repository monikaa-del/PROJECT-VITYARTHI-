def generate_report(skills, score, missing):

    with open("REPORTS/analysis_report.txt", "w") as file:

        file.write("RESUME ANALYSIS REPORT\n")
        file.write("=" * 30 + "\n\n")

        file.write("Skills Found:\n")

        for skill in skills:
            file.write(f"- {skill}\n")

        file.write(f"\nMatch Score: {round(score,2)}%\n\n")

        file.write("Missing Skills:\n")

        for skill in missing:
            file.write(f"- {skill}\n")

    print("\nReport Generated Successfully!")
