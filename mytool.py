import os


def getlistCk(ckname):
    if os.getenv(ckname) is None:
        return None
    return os.getenv(ckname).split('\n').split('@')