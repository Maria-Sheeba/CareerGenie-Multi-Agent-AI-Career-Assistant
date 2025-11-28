def suggest_learning(user_skills, jobs):
    # Mock skill gap suggestions
    gap_skills = []
    required_skills = ["Python", "SQL", "React", "Django", "Git"]
    for skill in required_skills:
        if skill not in user_skills:
            gap_skills.append(skill)
    return gap_skills
