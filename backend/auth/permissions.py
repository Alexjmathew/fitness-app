from .models import Role, RoleName, Permission

# Define roles and their permissions
ROLES = {
    RoleName.REGULAR_USER: Role(
        name=RoleName.REGULAR_USER,
        permissions=[
            Permission.VIEW_EXERCISES,
            Permission.PERFORM_EXERCISES,
            Permission.VIEW_REPETITION_SCORES,
            Permission.VIEW_FATIGUE_DATA,
            Permission.VIEW_ADAPTATION_PREDICTIONS
        ],
        description="Standard user with basic exercise and feedback access"
    ),
    
    RoleName.TRAINER: Role(
        name=RoleName.TRAINER,
        permissions=[
            Permission.VIEW_EXERCISES,
            Permission.PERFORM_EXERCISES,
            Permission.CREATE_EXERCISE_PLAN,
            Permission.MODIFY_EXERCISE_PLAN,
            Permission.VIEW_REPETITION_SCORES,
            Permission.VIEW_FATIGUE_DATA,
            Permission.VIEW_ADAPTATION_PREDICTIONS,
            Permission.VIEW_USER_DATA,
            Permission.OVERRIDE_FATIGUE_WARNINGS
        ],
        description="Trainer with ability to create/modify plans and view client data"
    ),
    
    RoleName.PHYSICAL_THERAPIST: Role(
        name=RoleName.PHYSICAL_THERAPIST,
        permissions=[
            Permission.VIEW_EXERCISES,
            Permission.PERFORM_EXERCISES,
            Permission.CREATE_EXERCISE_PLAN,
            Permission.MODIFY_EXERCISE_PLAN,
            Permission.VIEW_REPETITION_SCORES,
            Permission.VIEW_FATIGUE_DATA,
            Permission.VIEW_ADAPTATION_PREDICTIONS,
            Permission.VIEW_USER_DATA,
            Permission.OVERRIDE_FATIGUE_WARNINGS,
            Permission.PRESCRIBE_THERAPY
        ],
        description="Physical therapist with rehabilitation permissions"
    ),
    
    RoleName.RESEARCHER: Role(
        name=RoleName.RESEARCHER,
        permissions=[
            Permission.VIEW_EXERCISES,
            Permission.ACCESS_RESEARCH_DATA,
            Permission.VIEW_EMOTIONAL_STATE,
            Permission.VIEW_REPETITION_SCORES,
            Permission.VIEW_FATIGUE_DATA,
            Permission.VIEW_ADAPTATION_PREDICTIONS
        ],
        description="Researcher with access to anonymized data for analysis"
    ),
    
    RoleName.ADMINISTRATOR: Role(
        name=RoleName.ADMINISTRATOR,
        permissions=[p for p in Permission],  # All permissions
        description="System administrator with full access"
    )
}

def has_permission(user: User, required_permission: Permission) -> bool:
    """Check if user has the required permission through any of their roles"""
    for role_name in user.roles:
        role = ROLES.get(role_name)
        if role and required_permission in role.permissions:
            return True
    return False
