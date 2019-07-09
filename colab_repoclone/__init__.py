# __init__.py for colab_repoclone

name = "colab_repoclone"
__version__ = "0.0.1"

import sys

if "google.colab" in sys.modules:
    import colab_env
from colab_repoclone.git_access import RepoClone


def load_repository(repo, branch="master", method="env"):
    return RepoClone(repo, branch=branch, method=method)
