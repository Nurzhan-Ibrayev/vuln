# Static Testing in Early Development Phases

An automated static code analysis pipeline that integrates Semgrep with GitHub Actions and OpenAI to provide intelligent security and quality feedback on every commit.

## 🚀 Overview

This project demonstrates the implementation of static testing within modern CI/CD workflows. It automatically analyzes code for security vulnerabilities, code quality issues, and best practice violations, then generates human-readable reports with AI-enhanced explanations.

### Key Features

- **Automated Analysis**: Triggers on every commit and pull request
- **Security-First**: Detects SQL injection, command injection, and other OWASP Top 10 vulnerabilities
- **AI-Enhanced Feedback**: Uses OpenAI to generate developer-friendly explanations
- **Comprehensive Reporting**: Creates detailed Markdown reports with actionable recommendations
- **Zero Configuration**: Works out-of-the-box with minimal setup

## 🛠️ Technology Stack

- **GitHub Actions** - CI/CD automation
- **Semgrep** - Static analysis engine
- **OpenAI API** - Intelligent report generation
- **Python** - Report processing and generation
- **Markdown** - Documentation and reporting format

## 🔧 Setup Instructions

### Prerequisites

- GitHub repository with Actions enabled
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Python 3.9+ (for local testing)

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/[your-username]/vuln.git
   cd static-testing-project
   ```

2. **Add OpenAI API Key to GitHub Secrets**
   - Go to your repository Settings → Secrets and variables → Actions
   - Add new secret: `OPENAI_API_KEY` with your OpenAI API key

3. **Enable GitHub Actions**
   - The workflow will automatically trigger on pushes to `main` or `develop` branches
   - Pull requests will also trigger analysis and receive automated comments




## 🔍 How It Works

1. **Trigger**: Developer commits code or creates pull request
2. **Analysis**: GitHub Actions runs Semgrep static analysis
3. **Processing**: Python script processes JSON results
4. **AI Enhancement**: OpenAI generates human-readable explanations
5. **Reporting**: Markdown report is generated and stored
6. **Feedback**: Results are commented on pull requests automatically



## 🚦 CI/CD Integration

The project includes a complete GitHub Actions workflow that:

- Runs on every push and pull request
- Installs all dependencies automatically
- Executes Semgrep with optimal rule sets
- Generates AI-enhanced reports
- Uploads artifacts for download
- Comments results on pull requests

## 🔒 Security Considerations

- API keys are stored securely in GitHub Secrets
- Reports don't include sensitive code snippets
- Analysis runs in isolated GitHub Actions environment
- All dependencies are pinned to specific versions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request


## 🔗 Useful Links

- [Semgrep Documentation](https://semgrep.dev/docs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)

---

⭐ **Star this repository if you found it helpful!**
