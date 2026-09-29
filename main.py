import json

from SRC.resume_reader import read_resume
from SRC.skill_extractor import extract_skills
from SRC.analyzer import analyze
from SRC.roadmap import generate_roadmap
from SRC.report_generator import generate_report

file_path = input("Enter Resume Path: ")

resume_text = read_resume(file_path)

skills = extract_skills(resume_text)

print("\nSkills Found:")

for skill in skills:
    print("-", skill)

# roles.json read karna
with open("DATA/roles.json", "r") as file:
    roles = json.load(file)

role_list = list(roles.keys())

print("\nAvailable Roles:\n")

for i, role in enumerate(role_list, start=1):
    print(i, role)

choice = int(input("\nChoose Role: "))

selected_role = role_list[choice - 1]

score, missing = analyze(
    skills,
    roles[selected_role]
)

print("\nMatch Score:", round(score, 2), "%")

print("\nMissing Skills:")

for skill in missing:
    print("-", skill)

#Generate Roadmap
generate_roadmap(missing)

generate_report(
    skills,
    score,
    missing
)
