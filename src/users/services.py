from users.models import User
from datetime import datetime


def update_request_time(*, user: User):
    user.last_request = datetime.now()
    user.save()
