
def audit_log(called_function):
    def audit_log_inner(*args, **kwargs):
        print("AUDIT: ",repr(called_function(*args, **kwargs)))
        result = called_function(*args, **kwargs)
        return result
    return audit_log_inner