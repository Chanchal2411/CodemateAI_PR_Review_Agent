import os
import argparse
from .engine import process_pr

def main():
    parser = argparse.ArgumentParser(description="Codemate PR Analyzer CLI")
    parser.add_argument("--provider", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--pr", type=int, required=True)
    args = parser.parse_args()

    token = os.getenv("GITHUB_TOKEN") or os.getenv("GITLAB_TOKEN")
    feedback = process_pr(args.provider, args.owner, args.repo, args.pr, token=token)

    print("Feedback:")
    for f in feedback:
        print(f"- {f}")

if __name__ == "__main__":
    main()
