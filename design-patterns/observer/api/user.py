from lib.email import send_email
from lib.db import create_user, find_user
from lib.log import log
from lib.slack import post_slack_message
from lib.stringtools import get_random_string

def register_new_user(name: str, email: str, password: str):
    # create an entry in the database
    user = create_user(name, email, password)

    # post a Slack message to sales department
    post_slack_message("sales", f"{user.name} has registered with email address {user.email}. Please spam this person")

    # send a welcome email
    send_email(user.name, user.email, "Welcome", f"Thanks for registering, {user.name}!\Regards, The DevNotes Team")

def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)

    # send a password reset message
    send_email(user.name, user.email, "Reset your password", f"To reset your password, use this secure code: {user.reset_code}.\nRegards, The DevNotes Team")

    # write server log
    log(f"User with email {user.email} requested a password reset.")