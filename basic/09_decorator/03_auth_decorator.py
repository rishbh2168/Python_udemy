from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(role):
        if role != "admin":
            print("access denies : need afmin role only")

        else:
            return func(role)
    return wrapper

@require_admin

def chai_inventory(user_role):
    print("access approved: welcome admin!")

chai_inventory("user")
chai_inventory("admin")