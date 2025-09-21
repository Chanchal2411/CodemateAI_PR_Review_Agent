import gitlab

class GitLabAdapter:
    def __init__(self, token=None):
        self.gl = gitlab.Gitlab('https://gitlab.com', private_token=token)

    def fetch_pr(self, owner, repo_name, pr_number):
        project = self.gl.projects.get(f"{owner}/{repo_name}")
        mr = project.mergerequests.get(pr_number)
        files = [{"filename": f['new_path'], "content": f.get('diff', '')} for f in mr.changes()['changes']]
        return {"title": mr.title, "files": files}
