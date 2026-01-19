def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        is_admin = kwargs.get("admin", False)
        if not is_admin:
            print("Access Denied: Admin privileges required")
            return
        return func(*args, **kwargs)
    return wrapper