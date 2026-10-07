"""Validation helpers for ST445."""
from datetime import datetime, timezone

# Your code here

def valid_country_code(code):
  """Return True only for excately two uppercase mletters A to Z."""
  return(
    isinstance(code, str) and
    len(code) == 2 and
    code.isupper() and
    code.isalpha() and
    code.isascii()
  )

def parse_timestamp(stamp):
  """Convert an ISO 8601 timestamp with a timezone to UTC."""
  if stamp.endswith("Z"):
    stamp = stamp[:-1] + "+00:00"

  dt = datetime.fromisoformat(stamp)

  if dt.tzinfo is None:
    raise ValueError("No timezone")

  return dt.astimezone(timezone.utc)
  
