"""Cleaning helpers for ST445."""

MISSING = {"", "NA", "N/A", "NULL", "-999", "."}


def to_float(raw, missing=MISSING):
    """Convert a raw string to a float, or return None if it is a missing marker."""
    raw = raw.strip()
    if raw in missing:
        return None
    return float(raw)


def is_missing(raw, column):
    """True if raw is a missing marker in this column. NA is Namibia in country_code."""
    if raw == "NA" and column == "country_code":
        return False
    return raw in MISSING


def describe(value):
    """Format a cleaned value for display."""
    return "missing" if value is None else f"{value:.1f}"
