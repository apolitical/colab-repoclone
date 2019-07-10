import os
from subprocess import call
from getpass import getpass


class RepoClone:
    def __init__(self, repo, branch="master", method="env"):
        """
        __init__

        Gathers user's GitHub credentials and clones desired repository
        with push/pull capabilities.

        """

        if method == "env":
            self.env_authentication()
        else:
            self.cli_authentication()

        repo_url = repo.split("//")[1]
        self.repo_name = repo.split("/")[-1].replace(".git", "")
        self.access_repo = f"https://{self.github_user}:{self.github_key}@{repo_url}"
        self.branch = branch

        self.clone()

    def clone(self):
        """
        clone

        Clones repository into Google Colab environment using username and
        access key to provide push/pull capabilities.

        """

        if self.branch == "master":
            clone_cmd = f"git clone {self.access_repo}"
        else:
            clone_cmd = f"git clone --branch {self.branch} {self.access_repo}"

        call(clone_cmd, shell=True)
        call(f"git config --global user.name {self.github_user}", shell=True)
        call(f"git config --global user.email {self.github_email}", shell=True)

    def pull(self):
        """
        pull

        Pulls latest changes to GitHub repo into local Google Colab environment

        """

        call("git pull", shell=True)

    def push(self, commit_msg="Latest Commit from Google Colab", file_path="."):
        """
        push

        Changes directory into this repo, then commits and pushes latest changes
        to GitHub from Google Colab.

        KEYWORDS:
            commit_msg - message for this commit to GitHub
            file_path - path to specific files desired to push, defaults to all 
                files in repository.

        """

        call(f"cd /content/{self.repo_name}", shell=True)

        call(f"git add {file_path}", shell=True)
        call(f"git commit -m {commit_msg}", shell=True)
        call("git push", shell=True)

    def env_authentication(self):
        """
        env_authentication

        Checks environment variables for GitHub credentials. Used only when
        method keyword passed to class instance is "env"

        """

        self.github_key = os.getenv("GITHUB_KEY")
        self.github_user = os.getenv("USER_NAME")
        self.github_email = os.getenv("USER_EMAIL")
        if None in [self.github_key, self.github_user, self.github_email]:
            raise EnvironmentError(
                "Using method='env', GITHUB_KEY, USER_NAME, USER_EMAIL must be provided in the environment"
            )

    def cli_authentication(self):
        """
        cli_authentication

        Uses getpass module to get user's GitHub credentials from standard input.
        Used only if method keyword passed to class instance is *not* "env"

        """

        self.github_key = getpass("Enter your GitHub Authorization Token: ")
        self.github_user = getpass("Enter your GitHub Username: ")
        self.github_email = getpass("Enter your GitHub Email: ")
