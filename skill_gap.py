from utils.learning_resources import suggest_learning

class SkillGapAgent:
    def __init__(self, profile_summary, jobs):
        self.profile = profile_summary
        self.jobs = jobs
    
    def suggest_skills(self):
        # Mock skill gap analysis
        return suggest_learning(self.profile["skills"], self.jobs)
