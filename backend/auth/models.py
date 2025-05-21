from enum import Enum
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RoleName(str, Enum):
    REGULAR_USER = "regular_user"
    TRAINER = "trainer"
    PHYSICAL_THERAPIST = "physical_therapist"
    RESEARCHER = "researcher"
    ADMINISTRATOR = "administrator"

class Permission(str, Enum):
    # Exercise permissions
    VIEW_EXERCISES = "view_exercises"
    PERFORM_EXERCISES = "perform_exercises"
    CREATE_EXERCISE_PLAN = "create_exercise_plan"
    MODIFY_EXERCISE_PLAN = "modify_exercise_plan"
    
    # Analysis permissions
    VIEW_EMOTIONAL_STATE = "view_emotional_state"
    VIEW_REPETITION_SCORES = "view_repetition_scores"
    VIEW_FATIGUE_DATA = "view_fatigue_data"
    VIEW_ADAPTATION_PREDICTIONS = "view_adaptation_predictions"
    
    # User management
    VIEW_USER_DATA = "view_user_data"
    MODIFY_USER_DATA = "modify_user_data"
    VIEW_ALL_USERS = "view_all_users"
    
    # System management
    MANAGE_SYSTEM = "manage_system"
    ACCESS_RESEARCH_DATA = "access_research_data"
    
    # Special permissions
    OVERRIDE_FATIGUE_WARNINGS = "override_fatigue_warnings"
    PRESCRIBE_THERAPY = "prescribe_therapy"

class Role(BaseModel):
    name: RoleName
    permissions: List[Permission]
    description: str

class User(BaseModel):
    id: str
    username: str
    email: str
    hashed_password: str
    roles: List[RoleName]
    disabled: bool = False
    created_at: datetime = datetime.now()
    last_login: Optional[datetime] = None
