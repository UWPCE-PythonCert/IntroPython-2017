import datetime

def audit_log(called_function):
    def audit_log_inner(self, *args, **kwargs):
        if not hasattr(self, "_audit"):
            self._audit = []
        try:
            _ = user
        except NameError:
            raise PermissionError("You must be logged in to make changes.")
        now = datetime.datetime.utcnow().isoformat() + "Z"
        message =  self.__name__ + "." + called_function.__name__ + " called with " + repr(args) + "," + str(kwargs)
        self._audit.append({ "time": now, "user": user, "action": message })
        result = called_function(self, *args, **kwargs)
        return result
    return audit_log_inner
