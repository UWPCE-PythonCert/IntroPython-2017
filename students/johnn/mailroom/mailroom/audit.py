import datetime
"""
Add an audit entry when an object is modified.
"""

def audit_log(called_function):
    def audit_log_inner(self, *args, **kwargs):
        from mailroom import security
        if not hasattr(self, "audit"):
            self.audit = []
        if security.user:
            user = security.user
        else:
            raise PermissionError("You must be logged in to make changes.")
        now = datetime.datetime.utcnow().isoformat() + "Z"
        self.audit.append({ "time": now, "user": user, "action": called_function.__name__, "args": args, "kwargs": kwargs })
        result = called_function(self, *args, **kwargs)
        return result
    return audit_log_inner
