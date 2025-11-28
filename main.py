from agents.profile_analyzer import ProfileAnalyzerAgent
from agents.job_discovery import JobDiscoveryAgent
from agents.skill_gap import SkillGapAgent
from agents.resume_interview_coach import ResumeInterviewAgent

def run_careergenie(user_profile):
    print("=== CareerGenie: AI Career Assistant ===\n")
    
    # 1. Analyze user profile
    profile_agent = ProfileAnalyzerAgent(user_profile)
    profile_summary = profile_agent.analyze()
    print(f"Profile Summary: {profile_summary}\n")
    
    # 2. Job recommendations
    job_agent = JobDiscoveryAgent(profile_summary)
    job_recommendations = job_agent.find_jobs()
    print("Job Recommendations:")
    for job in job_recommendations:
        print(f"- {job}")
    print()
    
    # 3. Skill gap analysis
    skill_agent = SkillGapAgent(profile_summary, job_recommendations)
    skill_suggestions = skill_agent.suggest_skills()
    print("Skill Gap Recommendations:")
    for skill in skill_suggestions:
        print(f"- {skill}")
    print()
    
    # 4. Resume & interview coaching
    resume_agent = ResumeInterviewAgent(user_profile, job_recommendations)
    resume_tips = resume_agent.resume_tips()
    interview_tips = resume_agent.interview_tips()
    print("Resume Tips:")
    for tip in resume_tips:
        print(f"- {tip}")
    print("\nInterview Tips:")
    for tip in interview_tips:
        print(f"- {tip}")

if __name__ == "__main__":
    # Example user profile
    user_profile = {
        "name": "Maria",
        "education": "B.E. Computer Science",
        "skills": ["Python", "HTML", "CSS", "SQL"],
        "experience": "Internship at XYZ",
        "career_goal": "Software Developer"
    }
    run_careergenie(user_profile)
