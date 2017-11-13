
def safe_input(message=""):
	try:
		output=input(message)
	except (EOFError, KeyboardInterrupt):
		return None
	else:
		return output

foo=safe_input("enter something ")

print()
print("you said:",foo)
