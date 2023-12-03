import uuid
from datetime import datetime

# system prompt components
with open('./prompts/constitution.txt', 'r') as file:
    CONSTITUTION = file.read().replace('\n', '')

with open('./prompts/serious.txt', 'r') as file:
    PERSONA = file.read().replace('\n', '')

with open('./prompts/limiter.txt', 'r') as file:
    LIMITER_PROMPT = file.read().replace('\n', '')

# account class 
class User():

    def __init__(self, name, email, dob, identity, child_name, child_dob, goals):
        self.name = name
        self.email = email
        self.dob = datetime.strptime(dob, "%Y-%m-%d")
        self.age = (datetime.today() - self.dob).days // 365
        self.identity = identity 
        self.child_name = child_name
        self.child_dob = datetime.strptime(child_dob, "%Y-%m-%d")
        self.child_age = (datetime.today() - self.child_dob).days // 365
        self.goals = goals
        self.user_context = f"""Remember, the user is a human named {self.name} who's a {self.age} year-old {self.identity}. """
        self.child_context = f"""Remember, the user's child is a {self.child_age} years old human named {self.child_name}. """
        self.system_prompt = CONSTITUTION + PERSONA + self.user_context + self.child_context + LIMITER_PROMPT
        self.id = str(uuid.uuid4())
    
    def __repr__(self):
        return f"""
        <UserInfo>: 
        name:            {self.name} 
        email:           {self.email} 
        id:              {self.id}
        dob:             {self.dob} 
        age:             {self.age}
        identity:        {self.identity} 
        child name:      {self.child_name} 
        child dob:       {self.child_dob} 
        child age:       {self.child_age}
        goals:           {self.goals}
        """