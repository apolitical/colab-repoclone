import os
from subprocess import call
from getpass import getpass


class LocalRepo:
    def __init__(self, repo, clone=True, branch="master", auth_method="env"):
        """
        __init__

        Gathers user's GitHub credentials and either clones or initializes
        desired repository with push/pull capabilities.

        """

        if auth_method == "env":
            self.env_authentication()
        else:
            self.cli_authentication()

        repo_url = repo.split("//")[1]
        if clone:
            self.repo_dir = repo.split("/")[-1].replace(".git", "")
        else:
            self.repo_dir = input("Enter the name of your new repo: ")

        self.access_repo = f"https://{self.github_user}:{self.github_key}@{repo_url}"
        self.branch = branch

        if clone:
            self.clone()
        else:
            self.new()

    def clone(self):
        """
        clone

        Clones repository into Google Colab environment using username and
        access key to provide push/pull capabilities.

        """
        os.chdir("/content")

        if self.branch == "master":
            clone_cmd = f"git clone {self.access_repo}"
        else:
            clone_cmd = f"git clone --branch {self.branch} {self.access_repo}"

        call(clone_cmd, shell=True)
        call(f"git config --global user.name {self.github_user}", shell=True)
        call(f"git config --global user.email {self.github_email}", shell=True)

    def new(self):
        """
        new

        Initializes a new repository in Google Colab environment using username and
        access key to provide push/pull capabilities.

        """
        os.chdir(f"/content/{self.repo_dir}")

        call("git init", shell=True)
        origin = call(f"git remote add origin {self.access_repo}", shell=True)
        if origin != 0:
            call("git remote rm origin", shell=True)
            origin = call(f"git remote add origin {self.access_repo}", shell=True)
            if origin != 0:
                print(
                    f"Command: < git remote add origin {self.access_repo} > failed. Check your permissions and that this repository exists on GitHub."
                )
                return
        call(f"git config --global user.name {self.github_user}", shell=True)
        call(f"git config --global user.email {self.github_email}", shell=True)

        ## First must pull (in case repo already exists), then push and set remote as upstream
        pull = call("git pull origin master --allow-unrelated-histories", shell=True)
        add = call("git add .", shell=True)
        commit = call("git commit -m 'First Commit from Google Colab'", shell=True)
        push = call("git push --set-upstream origin master", shell=True)

        if add != 0:
            print("Command: < git add . > failed. Check your permissions.")
        if commit != 0:
            print(
                f"Command: < git commit -m 'First Commit from Google Colab' > failed. Possibly because there were no files in /{self.repo_dir}"
            )
        if push != 0:
            print(
                "Command: < git push --set-upstream origin master > failed. Check your permissions."
            )

        os.chdir("/content")

    def pull(self):
        """
        pull

        Pulls latest changes to GitHub repo into local Google Colab environment

        """
        os.chdir(f"/content/{self.repo_dir}")

        pull = call("git pull", shell=True)

        if pull != 0:
            print("Command: < git pull > failed. Check your permissions.")

        os.chdir("/content")

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

        os.chdir(f"/content/{self.repo_dir}")

        add = call(f"git add {file_path}", shell=True)
        commit = call(f"git commit -m '{commit_msg}'", shell=True)
        push = call("git push", shell=True)

        if add != 0:
            print(f"Command: < git add {file_path} > failed. Check your permissions.")
        if commit != 0:
            print(
                f"Command: < git commit -m '{commit_msg}' > failed. Possibly because no changes were made. Also ensure there were no single or double quotation marks in your commit message."
            )
        if push != 0:
            print("Command: < git push > failed. Check your permissions.")

        os.chdir("/content")

    def env_authentication(self):
        """
        env_authentication

        Checks environment variables for GitHub credentials. Used only when
        auth_method keyword passed to class instance is "env"

        """

        self.github_key = os.getenv("GITHUB_KEY")
        self.github_user = os.getenv("USER_NAME")
        self.github_email = os.getenv("USER_EMAIL")
        if None in [self.github_key, self.github_user, self.github_email]:
            raise EnvironmentError(
                "Using auth_method='env', GITHUB_KEY, USER_NAME, USER_EMAIL must be provided \
                in the environment"
            )

    def cli_authentication(self):
        """
        cli_authentication

        Uses getpass module to get user's GitHub credentials from standard input.
        Used only if auth_method keyword passed to class instance is *not* "env"

        """

        self.github_user = input("Enter your GitHub Username: ")
        self.github_email = input("Enter your GitHub Email: ")
        self.github_key = getpass("Enter your GitHub Authorization Token: ")
