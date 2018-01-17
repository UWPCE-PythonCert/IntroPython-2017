
def sleep_in(weekday=False, vacation=False):
    if vacation or not weekday:
        return True
    else:
        return False

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))
