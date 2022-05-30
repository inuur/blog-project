from __future__ import absolute_import

from .celery_setup import app as celery_app
from .task import send_email

__all__ = ['celery_app']
