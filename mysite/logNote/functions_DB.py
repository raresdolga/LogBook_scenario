import os
import hashlib
from logNote.models import User,Log

def test():
	return 6;

def check_user(email):
        if User.objects.filter(email=email).exists():
            return True
        return False