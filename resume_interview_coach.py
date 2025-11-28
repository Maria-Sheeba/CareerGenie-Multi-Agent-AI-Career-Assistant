class ResumeInterviewAgent:
    def __init__(self, profile, jobs):
        self.profile = profile
        self.jobs = jobs
    
    def resume_tips(self):
        # Example tips
        return [
            "Highlight relevant projects in your resume.",
            "Use action verbs for achievements.",
            "Keep your resume under 1 page."
        ]
    
    def interview_tips(self):
        return [
            "Prepare for common technical interview questions.",
            "Practice STAR method for behavioral questions.",
            "Research the company before interview."
        ]
