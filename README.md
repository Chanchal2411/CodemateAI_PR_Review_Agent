# PR Review Agent 🚀

An **AI-powered Pull Request Review Agent** that reviews PRs across **GitHub, GitLab, and Bitbucket**.  
It automatically analyzes code changes, provides feedback, and assigns a **quality score** – helping developers catch issues before merging.  

---

## 📌 Features
- ✅ Works with **multiple git servers** (GitHub, GitLab, Bitbucket)  
- ✅ Reviews **pull requests / merge requests** for code quality, standards, and possible bugs  
- ✅ Provides **feedback suggestions** for improvements  
- ✅ Generates a **PR Quality Score**  
- ✅ Modular and extensible **Python-based design**  

---

## ⚡ Possible Enhancements
- Inline review comments (GitHub/GitLab style)  
- AI-driven performance/security suggestions  

---

## 🔧 Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>

2. **Create & activate virtual environment**  
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Linux/Mac

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt


4. **Set your tokens (for GitHub, GitLab, OpenAI)**
   ```bash
   set GITHUB_TOKEN=your_github_token
   set GITLAB_TOKEN=your_gitlab_token
   set OPENAI_API_KEY=your_openai_api_key

## ▶️ Usage

### Run on **GitHub**
    python -m codemate.cli --provider github --owner <owner> --repo <repo> --pr <pr_number>

### Run on **GitLab**
    python -m codemate.cli --provider gitlab --owner <group_or_username> --repo <repo_name> --pr <mr_number>


---

## 🌐 Links

🔗 **Live App**: https://lnkd.in/gWaw24S8  
💻 **GitHub Repo**: https://lnkd.in/gwusuAFc  
📹 **Demo Video**: https://lnkd.in/g8p5SHVG  

---

## 📹 Demo

🎥 Watch Demo Video : https://drive.google.com/file/d/1JGWGMxrcpGYxufCdgqJ3WxJGt7gsGWSM/view?usp=drive_link 

---

## 🤝 Acknowledgements

Built as part of **#SRMHacksWithCodemate 💡**  
Special thanks to **CodeMate** and **SRM University**.
