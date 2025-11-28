from utils.job_api import get_jobs

class JobDiscoveryAgent:
    def __init__(self, profile_summary):
        self.profile = profile_summary
    
    def find_jobs(self):
        # Find jobs based on skills and career goal
        recommended_jobs = get_jobs(self.profile["skills"], self.profile["career_goal"])
        return recommended_jobs
