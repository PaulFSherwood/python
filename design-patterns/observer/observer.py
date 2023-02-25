from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

# register a new user
register_new_user("Arjan", "BestPasswordEver", "hi@arjanegges.com")

# send a password reset message
password_forgotten("hi@arjanegges.com")

# upgrade a plan
upgrade_plan("hi@arjanegges.com")

