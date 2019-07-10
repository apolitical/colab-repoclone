# __init__.py for colab_repoclone

name = "colab_repoclone"
__version__ = "0.1.0"

import sys

if "google.colab" in sys.modules:
    import colab_env
from colab_repoclone.git_access import RepoClone


def clone_repository(repo, branch="master", method="env"):
    """
    clone_repository

    Call this method to create an instance of a cloned GitHub 
    repository in the Google Colab environment. You can then use
    the class methods to push and pull from this repo directly
    from Colab.

    INPUTS:
        repo - the link to the GitHub repository for cloning

    KEYWORDS:
        branch="master" - the specific branch to clone, if desired
        method="env" - indicates where to look for your GitHub credentials.
            "env" will expect them in your environment variables, anything
            else will prompt the user to input them.

    RETURNS:
        A RepoClone instance

    """

    return RepoClone(repo, branch=branch, method=method)
