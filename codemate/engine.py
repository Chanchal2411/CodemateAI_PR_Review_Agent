from .server_adapters.github_adapter import GitHubAdapter
from .server_adapters.gitlab_adapter import GitLabAdapter
from .analyzers.code_quality import analyze_code
from .analyzers.ai_feedback import generate_ai_feedback

def process_pr(provider, owner, repo, pr_number, token=None):
    if provider.lower() == "github":
        adapter = GitHubAdapter(token=token)
    elif provider.lower() == "gitlab":
        adapter = GitLabAdapter(token=token)
    else:
        raise NotImplementedError(f"Provider {provider} not supported yet.")

    pr_data = adapter.fetch_pr(owner, repo, pr_number)
    
    feedback = analyze_code(pr_data)
    
    ai_suggestions = generate_ai_feedback(pr_data)
    feedback.extend(ai_suggestions)
    
    score = max(0, 100 - len(feedback)*5)
    feedback.append(f"PR Quality Score: {score}/100")
    
    return feedback
