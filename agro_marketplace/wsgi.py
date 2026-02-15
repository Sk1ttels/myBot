"""WSGI entrypoint for Railway.

Run:
  gunicorn wsgi:app --bind 0.0.0.0:$PORT
"""

from src.web_panel.app import app  # noqa: F401
