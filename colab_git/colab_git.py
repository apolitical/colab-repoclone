try:
    import colab_env
except ImportError:
    raise ImportError("colab-git only works in a Google Colab notebook")

import os


class ColabGitHub:
    def __init__(self, repo, branch="master"):

        GITHUB_KEY = os.getenv("GITHUB_KEY")
        if GITHUB_KEY is None:
            GITHUB_KEY = raw_input("Please enter your Github Access Token: ")
        GITHUB_USER = os.getenv("USER_NAME")
        if GITHUB_USER is None:
            GITHUB_USER = raw_input("Please enter your Github Username: ")
        GITHUB_EMAIL = os.getenv("USER_EMAIL")
        if GITHUB_EMAIL is None:
            GITHUB_EMAIL = raw_input("Please enter your Github Email: ")

        repo_url = repo.split("//")[1]
        self.access_repo = "https://{GITHUB_USER}:{GITHUB_KEY}@{REPO_URL}".format(
            GITHUB_USER=GITHUB_USER, GITHUB_KEY=GITHUB_KEY, REPO_URL=repo_url
        )
        self.repo_name = repo.split("/")[-1].replace(".git", "")

        if branch == "master":
            clone = "git clone {ACCESS_REPO}".format(ACCESS_REPO=self.access_repo)
        else:
            clone = "git clone --branch {BRANCH} {ACCESS_REPO}".format(
                BRANCH=branch, ACCESS_REPO=self.access_repo
            )

        os.system(clone)
        os.system(
            "git config --global user.name {GITHUB_USER}".format(
                GITHUB_USER=GITHUB_USER
            )
        )
        os.system(
            "git config --global user.email {GITHUB_EMAIL}".format(
                GITHUB_EMAIL=GITHUB_EMAIL
            )
        )

        os.system("cd /content/{REPO_NAME}".format(REPO_NAME=self.repo_name))

    def colab_pull(self):
        os.system("git pull")

    def colab_push(self, commit_msg="Latest Commit from Google Colab", file_path="."):
        os.system("git add {FILE_PATH}".format(FILE_PATH=file_path))
        os.system("git commit -m {COMMIT_MSG}".format(COMMIT_MSG=commit_msg))
        os.system("git push")
