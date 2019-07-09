# __init__.py for colab_git

name = "colab_git"
__version__ = "0.0.1"

from colab_git.colab_git import ColabGitHub


def load_repository(repo, branch="master"):

    return ColabGitHub(repo, branch=branch)
