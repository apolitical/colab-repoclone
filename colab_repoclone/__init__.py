# __init__.py for colab_repoclone

name = "colab_repoclone"
__version__ = "0.1.5"

import sys

if "google.colab" in sys.modules:
    import colab_env
from colab_repoclone.git_access import LocalRepo


def local_repository(repo, clone=True, branch="master", auth_method="env"):
    """
    local_repository

    Call this method to create an instance of a GitHub repository in the 
    Google Colab environment. You can then use the class methods to push
    and pull from this repo directly from Colab.

    INPUTS:
        repo - the link to the GitHub repository for cloning or the empty
                GitHub repo for initializing

    KEYWORDS:
        clone=True - indicates whether a new repository is being created
            locally and uploaded to GitHub, rather than a clone
        branch="master" - the specific branch to clone, if desired
        auth_method="env" - indicates where to look for your GitHub credentials.
            "env" will expect them in your environment variables, anything
            else will prompt the user to input them.

    RETURNS:
        A RepoClone instance

    """

    ## Branch is forced to "master" for creating new repositories
    if not clone:
        branch = "master"

    return LocalRepo(repo, clone=clone, branch=branch, auth_method=auth_method)
