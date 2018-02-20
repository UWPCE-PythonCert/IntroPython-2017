"""
Provides a cross-module mechanism for tracking user info.

Example:
  from mailroom import security
  security.user = 'Fred Q Smith'
  print(security.user)
"""

user = None
