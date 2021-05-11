from users.models import ActivityLog


def add_activity(user, action, success=True, **kwargs):
    return ActivityLog.objects.create(
        user=user, action=action, success=success, **kwargs
    )


class OrderDAO:
    @staticmethod
    def create_order():
        add_activity(user, "{} made an order worth {}".format(user, total))
