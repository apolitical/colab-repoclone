import os
from subprocess import call
from getpass import getpass


class LocalRepo:
    def __init__(self, repo, clone=True, branch="master", auth_method="env"):
        """
        __init__

        Gathers user's GitHub credentials and either clones or initializes
        desired repository.

        """

        if auth_method == "env":
            self.env_authentication()
        else:
            self.cli_authentication()

        repo_url = repo.split("//")[1]
        if clone:
            self.repo_dir = repo.split("/")[-1].replace(".git", "")
        else:
            self.repo_dir = input("Local Repository :: ")

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
        access key.

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
        access key.

        """
        try:
            os.chdir(f"/content/{self.repo_dir}")
        except OSError:
            print(
                f"No directory named {self.repo_dir} exists. Are you sure you made it?"
            )
            return

        call("git init", shell=True)
        origin = call(f"git remote add origin {self.access_repo}", shell=True)
        if origin:
            call("git remote rm origin", shell=True)
            origin = call(f"git remote add origin {self.access_repo}", shell=True)
            if origin:
                print(
                    f"Command: < git remote add origin {self.access_repo} > failed. Check your permissions and that this repository exists on GitHub."
                )
                return
        call(f"git config --global user.name {self.github_user}", shell=True)
        call(f"git config --global user.email {self.github_email}", shell=True)

        ## First must pull (in case repo already exists), then push and set remote as upstream
        pull = call("git pull origin master --allow-unrelated-histories", shell=True)
        if pull:
            print(
                "Command: < git pull origin master --allow-unrelated-histories > failed. Check your permissions."
            )
            os.chdir("/content")
            return

        add = call("git add .", shell=True)
        if add:
            print("Command: < git add . > failed. Check your permissions.")
            os.chdir("/content")
            return

        commit = call("git commit -m 'First Commit from Google Colab'", shell=True)
        if commit:
            print(
                f"Command: < git commit -m 'First Commit from Google Colab' > failed. Possibly because there were no files in /{self.repo_dir}"
            )
            os.chdir("/content")
            return

        push = call("git push --set-upstream origin master", shell=True)
        if push:
            print(
                "Command: < git push --set-upstream origin master > failed. Check your permissions."
            )

        os.chdir("/content")

    def pull(self):
        """
        pull

        Pulls latest changes from GitHub repo into local Google Colab environment

        """
        os.chdir(f"/content/{self.repo_dir}")

        pull = call("git pull", shell=True)
        if pull:
            print("Command: < git pull > failed. Check your permissions.")

        os.chdir("/content")

    def push(self, commit_msg=None, file_path="."):
        """
        push

        Commits and pushes latest changes to GitHub from Google Colab.

        KEYWORDS:
            commit_msg=None - message for this commit to GitHub. If none passed,
                will prompt for user input.
            file_path - path to specific files desired to push, defaults to all 
                files in repository.

        """
        if commit_msg is None:
            commit_msg = input("Commit Message :: ")

        check = """
        *************************************************************
        * Are you sure you want to push your changes?               *
        *                                                           *
        * Press "q" to abort. Press any other key to continue...    *
        *************************************************************
        """
        if input(check).lower() == "q":
            print("\n!! PUSH ABORTED !!\n")
            return

        os.chdir(f"/content/{self.repo_dir}")

        add = call(f"git add {file_path}", shell=True)
        if add:
            print(f"Command: < git add {file_path} > failed. Check your permissions.")
            os.chdir("/content")
            return

        commit = call(f"git commit -m '{commit_msg}'", shell=True)
        if commit:
            print(
                f"Command: < git commit -m '{commit_msg}' > failed. Possibly because no changes were made. Also ensure there were no single or double quotation marks in your commit message."
            )
            os.chdir("/content")
            return

        push = call("git push", shell=True)
        if push:
            print("Command: < git push > failed. Check your permissions.")

        os.chdir("/content")

    def new_branch(self, branch_name=None):
        """
        new_branch

        Creates a new branch off the current one and checks it out so future
        changes will be pushed to this new branch

        KEYWORDS:
            branch_name=None - the name of the new branch to create. If none
                passed, will prompt for user input.

        """
        if branch_name is None:
            branch_name = input("New Branch :: ")

        os.chdir(f"/content/{self.repo_dir}")

        brc = call(f"git branch {branch_name}", shell=True)
        if brc:
            print(
                f"Command: < git branch {branch_name} > failed. Check your permissions."
            )
            os.chdir("/content")
            return

        chk = call(f"git checkout {branch_name}", shell=True)
        if chk:
            print(
                f"Command: < git checkout {branch_name} > failed. Check that this branch exists."
            )
            os.chdir("/content")
            return

        self.branch = branch_name

        # Must push new branch to GitHub before making any changes to set the
        # upstream for future pushes from this branch
        push = call(f"git push --set-upstream origin {branch_name}", shell=True)
        if push:
            print(
                f"Command: < git push --set-upstream origin {branch_name} > failed. Check your permissions."
            )

        os.chdir("/content")

    def checkout(self, branch_name=None):
        """
        checkout

        Checks out an existing branch of the repository. All future pushes
        will push to this branch.

        KEYWORDS:
            branch_name=None - the name of the existing branch to checkout.
                If none passed, will prompt for user input.

        """

        if branch_name is None:
            branch_name = input("Checkout Branch :: ")

        os.chdir(f"/content/{self.repo_dir}")

        chk = call(f"git checkout {branch_name}", shell=True)
        if chk:
            print(
                f"Command: < git checkout {branch_name} > failed. Check that this branch exists."
            )
            os.chdir("/content")
            return

        self.branch = branch_name
        os.chdir("/content")

    def reset(self, commit=None):
        """
        reset

        Performs a hard reset of the local repo to the specified commit,
        then force pushes this to rollback the repository, deleting all
        intermediate commits in the process.

        KEYWORDS:
            commit=None - the commit id to rollback to. If none passed,
                defaults to the previous commit.

        """
        check = """
        *****************************************************************
        *                         !! CAUTION !!                         *
        *                                                               *
        * Are you sure you want to rollback to a previous commit?       *
        *                                                               *
        * This is a hard reset, meaning all commits between the current *
        * and the one you are rolling back to will be lost.             *
        *                                                               *
        * Press "q" to abort. Press any other key to continue...        *
        *****************************************************************
        """
        if input(check).lower() == "q":
            print("\n!! RESET ABORTED !!\n")
            return

        os.chdir(f"/content/{self.repo_dir}")

        if commit is None:
            reset_cmd = "git reset --hard"
        else:
            reset_cmd = f"git reset --hard {commit}"

        reset = call(reset_cmd, shell=True)
        if reset:
            print(
                f"Command: < {reset_cmd} > failed. Check the supplied commit id is a valid one."
            )

        push = call("git push --force", shell=True)
        if push:
            print(f"Command: < git push --force > failed. Check your permissions.")

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

        self.github_user = input("GitHub Username :: ")
        self.github_email = input("GitHub Email :: ")
        self.github_key = getpass("GitHub Authorization Token :: ")
