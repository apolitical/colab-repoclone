import os
from getpass import getpass


class RepoClone:
    def __init__(self, repo, branch="master", method="env"):
        """
        __init__

        Gathers user's GitHub credentials and clones desired repository
        with push/pull capabilities.

        """

        if method == "env":
            self.github_key = os.getenv("GITHUB_KEY")
            self.github_user = os.getenv("USER_NAME")
            self.github_email = os.getenv("USER_EMAIL")
            if None in [self.github_key, self.github_user, self.github_email]:
                raise EnvironmentError(
                    "To use the *env* keyword you must provide a GitHub username, \
                    email and access token in your vars.env file"
                )
        else:
            self.get_access()

        repo_url = repo.split("//")[1]
        self.repo_name = repo.split("/")[-1].replace(".git", "")
        self.access_repo = "https://{GITHUB_USER}:{GITHUB_KEY}@{REPO_URL}".format(
            GITHUB_USER=self.github_user, GITHUB_KEY=self.github_key, REPO_URL=repo_url
        )
        self.branch = branch

        self.clone()

    def clone(self):
        """
        clone

        Clones repository into Google Colab environment using username and
        access key to provide push/pull capabilities.

        """

        if self.branch == "master":
            clone_cmd = "git clone {ACCESS_REPO}".format(ACCESS_REPO=self.access_repo)
        else:
            clone_cmd = "git clone --branch {BRANCH} {ACCESS_REPO}".format(
                BRANCH=self.branch, ACCESS_REPO=self.access_repo
            )

        os.system(clone_cmd)
        os.system(
            "git config --global user.name {GITHUB_USER}".format(
                GITHUB_USER=self.github_user
            )
        )
        os.system(
            "git config --global user.email {GITHUB_EMAIL}".format(
                GITHUB_EMAIL=self.github_email
            )
        )

    def pull(self):
        """
        pull

        Pulls latest changes to GitHub repo into local Google Colab environment

        """

        os.system("git pull")

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

        os.system("cd /content/{REPO_NAME}".format(REPO_NAME=self.repo_name))

        os.system("git add {FILE_PATH}".format(FILE_PATH=file_path))
        os.system("git commit -m {COMMIT_MSG}".format(COMMIT_MSG=commit_msg))
        os.system("git push")

    def get_access(self):
        """
        get_access

        Uses getpass module to get user's GitHub credentials from standard input.
        Used only if method keyword passed to class instance is *not* "env"

        """

        self.github_key = getpass("Enter your GitHub Authorization Token: ")
        self.github_user = getpass("Enter your GitHub Username: ")
        self.github_email = getpass("Enter your GitHub Email: ")
