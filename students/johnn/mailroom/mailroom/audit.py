"""
Add an audit entry when an object is modified.
"""

import datetime
import logging


def audit_log(called_function):
    """
    outside function

    We expect to be passed a function and will return a function
    (which wraps the called function)
    """
    def audit_log_inner(self, *args, **kwargs):
        """
        inside function

        log information to the target object about what function was called
        and what parameters were passed.
        """
        from mailroom import security
        if not hasattr(self, "audit"):
            self.audit = []
        if security.user:
            user = security.user
        else:
            raise PermissionError("You must be logged in to make changes.")
        now = datetime.datetime.utcnow().isoformat() + "Z"
        self.audit.append({"time": now,
                           "user": user,
                           "action": called_function.__name__,
                           "args": args,
                           "kwargs": kwargs})
        logging.debug("called {}, with {}, {}".format(
            user, called_function.__name__, args, kwargs),
            extra={ "user": security.user })
        result = called_function(self, *args, **kwargs)
        return result
    return audit_log_inner
