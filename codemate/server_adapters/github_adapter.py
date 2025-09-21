# codemate/server_adapters/github_adapter.py

from github import Github  # Make sure PyGithub is installed in your venv

class GitHubAdapter:
    def __init__(self, token=None):
        # Use token if provided, else unauthenticated
        self.g = Github(token) if token else Github()

    def fetch_pr(self, owner, repo_name, pr_number):
        repo = self.g.get_repo(f"{owner}/{repo_name}")
        pr = repo.get_pull(pr_number)
        files = [{"filename": f.filename, "content": f.patch or ""} for f in pr.get_files()]
        return {
            "title": pr.title,
            "files": files
        }
