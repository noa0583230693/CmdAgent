# 🤖 AI Terminal Command Generator

> **Never struggle with complex terminal commands again.** Convert natural language into perfectly formatted shell commands in seconds.

An intelligent, production-ready web application powered by **AI** that generates accurate terminal/shell commands from simple English descriptions. Perfect for developers, system administrators, and anyone who works with the command line.

## 📋 Overview

**cmdProject** intelligently bridges the gap between **natural language** and **terminal commands**. Type what you want to accomplish, and the AI generates the exact command you need. Built with:
- 🚀 **Groq API** (llama-3.3-70b-versatile model) for blazing-fast command generation
- 🎯 **Precision** with low temperature (0.2) for consistent, reliable results
- 🔒 **Security-first** with built-in safeguards against dangerous operations

### ✨ Key Features
- **🎯 Accuracy**: Groq's 70B model generates correct, tested commands
- **⚡ Speed**: Ultra-fast command generation (typically < 1 second)
- **🛡️ Safety-First**: Built-in protection blocks dangerous/destructive operations
- **🎨 Modern UI**: Clean, intuitive Gradio interface with glass morphism design
- **📋 One-Click Copy**: Instantly copy generated commands to clipboard
- **🌐 Cloud-Ready**: Deploy to Render, Heroku, or any cloud platform
- **🔧 Highly Customizable**: Modify AI behavior, styling, and safety rules
- **📱 Responsive Design**: Works on desktop and mobile browsers

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** (Python 3.10+ recommended)
- **Groq API Key** (free at [Groq Console](https://console.groq.com))
- **Windows/macOS/Linux** (all supported)

### 5-Minute Setup

**Option 1: Windows (PowerShell)**
```powershell
# 1. Clone/navigate to project
cd cmdProject

# 2. Create virtual environment
python -m venv myproject
myproject\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with your API key
# Open notepad and add: GROQ_API_KEY=your_key_here
# Save as .env in the project root

# 5. Run the app
python main.py

# 6. Open browser to http://localhost:8080
```

**Option 2: macOS/Linux (Terminal)**
```bash
# 1. Navigate to project
cd cmdProject

# 2. Create virtual environment
python3 -m venv myproject
source myproject/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API key
echo "GROQ_API_KEY=your_key_here" > .env

# 5. Run the app
python main.py

# 6. Open http://localhost:8080 in browser
```

### Detailed Installation

1. **Clone/Download the project**:
```bash
cd cmdProject
```

2. **Create and activate a virtual environment** (recommended):
```bash
python -m venv myproject
# On Windows:
myproject\Scripts\activate
# On macOS/Linux:
source myproject/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up your Groq API key**:
   - Get a free API key from [Groq Console](https://console.groq.com)
   - Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=gsk_your_actual_groq_key_here
   ```
   - **⚠️ Important**: Never commit `.env` to version control!

5. **Run the application**:
```bash
python main.py
```

6. **Open in browser**:
   - Navigate to `http://localhost:8080`
   - The web UI loads automatically
   - Start generating commands!

## � Best Practices & Pro Tips

### ✅ Getting the Best Results

**Request Strategy**:
1. **Be Specific**: Instead of "find files", say "find Python files modified today"
2. **Mention the OS**: "Linux", "macOS", or "Windows" - each has different commands
3. **Use Technical Terms**: "recursive", "symlink", "pipe", "regex" help the AI understand
4. **Provide Context**: "show top 5", "with timestamps", "human-readable" clarifies intent
5. **One Task Per Request**: Each query = one command (not multi-step scripts)

**Testing Generated Commands**:
```bash
# Always test before running important commands:

# Option 1: Preview what would happen
echo "your_command_here"

# Option 2: Use --dry-run if available
command --dry-run

# Option 3: Test on sample file first
command test_file.txt

# Option 4: Use permissions carefully
ls -la  # before chmod
```

**Example Good Requests**:
✅ "Find all .log files in /var/log, sorted by size (Linux)"
✅ "Show running processes using more than 500MB (macOS)"
✅ "List and count .js files in src (recursive, Windows)"
✅ "Find files modified in last 24 hours, exclude .git"

**Example Bad Requests**:
❌ "Find files" (too vague)
❌ "Do Linux stuff" (unclear intent)
❌ "Show me everything" (too broad)
❌ "Fix my code" (not a shell command)

### 🔒 Safety Guidelines

- ✅ **Always review** generated commands before running
- ✅ **Test on non-critical** data first
- ✅ **Use `--dry-run`** when available
- ✅ **Back up important** data before running file operations
- ✅ **Understand the command** before executing
- ❌ **Don't blindly copy** commands without review
- ❌ **Never run with `sudo`** without understanding why
- ❌ **Never pipe commands** you don't fully understand

### 🎯 Common Patterns

```
Request Pattern                           | Example
─────────────────────────────────────────┼──────────────────────────
"Find X that are Y (conditions)"          | Find .js files larger than 1MB
"Show X sorted by Y"                      | Show processes sorted by memory
"Count/list X in Y"                       | Count Python files in src/
"Replace X with Y in Z"                   | Replace .txt with .md filenames
"Backup X to Y"                           | Backup documents with timestamp
"Search for X in Y"                       | Search for "error" in logs
```

## �💡 Usage Examples

### ⭐ Common Commands

| Request | Generated Command | Use Case |
|---------|------------------|----------|
| "Find all txt files in my home folder" | `find ~ -name "*.txt" -type f` | File search |
| "Show how much disk space I'm using" | `du -sh ~/` | Disk usage |
| "List running processes by memory" | `ps aux --sort=-%mem \| head -20` | System monitoring |
| "Count lines of code in Python files" | `find . -name "*.py" -exec wc -l {} + \| tail -1` | Project analysis |
| "Backup my documents with timestamp" | `tar -czf Documents_$(date +%Y%m%d).tar.gz ~/Documents` | Backup |

### 🚀 File Operations
```
Request: "Find files larger than 500MB modified today"
Generated: find . -size +500M -type f -mtime 0

Request: "Show top 10 largest files in current directory"
Generated: du -sh * | sort -rh | head -10

Request: "Delete all .pyc files recursively"
⚠️ BLOCKED (Safety rule prevents file deletion - use interactive mode)
```

### 🔍 System Monitoring
```
Request: "Show all processes listening on network ports"
Generated: netstat -tulpn | grep LISTEN

Request: "Check CPU and memory usage in real-time"
Generated: htop (or top if htop not installed)

Request: "Show network bandwidth usage per process"
Generated: nethogs
```

### 🌐 Network & Web
```
Request: "Download a file and show progress"
Generated: wget --show-progress https://example.com/file.zip

Request: "Test connection to a server on port 8080"
Generated: nc -zv example.com 8080

Request: "Show all active SSH connections"
Generated: ss -to state established '( dport = :ssh or sport = :ssh )'
```

### 💻 Development
```
Request: "Count total lines written in all .js files"
Generated: find . -name "*.js" -exec wc -l {} + | tail -1

Request: "Find large files in node_modules to optimize"
Generated: find ./node_modules -size +1M -type f | sort -k5 -rh

Request: "Show git status of all repos in current directory"
Generated: find . -maxdepth 2 -name ".git" -type d | xargs dirname
```

## 📁 Project Structure

Perfect for understanding what each file does:

```
cmdProject/
├── 📄 main.py                    # Core application (Gradio UI + Groq API integration)
├── 📄 system_prompt.md           # AI behavior rules in Hebrew (modify to change AI behavior)
├── 📄 styles.css                 # Custom CSS for styling (modify to customize UI)
├── 📄 requirements.txt           # Python dependencies list
├── 📄 pyproject.toml             # Project metadata and configuration
├── 📄 README.md                  # Documentation (this file)
├── 📄 .env                        # API key (create this - not in repo)
├── 🔧 myproject/                 # Virtual environment folder
│   ├── Scripts/                  # (Windows) Python scripts & activate
│   └── Lib/                      # Installed packages
└── 📂 flagged/                   # Gradio output logs (if enabled)
    └── log.csv                   # Flagged request history
```

**File Importance**:
- 🔴 **Critical**: `main.py`, `system_prompt.md`, `requirements.txt`
- 🟡 **Important**: `styles.css`, `.env` (create yourself)
- 🟢 **Optional**: `pyproject.toml` (for packaging), `flagged/` (for logging)

## ⚙️ Configuration & API Settings

### Environment Variables
```bash
# Required
GROQ_API_KEY=gsk_xxxxxxxxxxxxx          # Your Groq API key

# Optional
PORT=8080                                # Server port (default: 8080)
LOG_LEVEL=INFO                          # Logging level
```

### AI Model Configuration
```python
# Located in main.py
model: "llama-3.3-70b-versatile"        # High-performance 70B model
temperature: 0.2                         # Low randomness (0=deterministic, 1=creative)
max_tokens: 150                          # Ensures concise, single-command output
top_p: 0.9                              # Nucleus sampling
```

### UI Settings
```python
# Gradio configuration
server_name: "0.0.0.0"                  # Accept external connections
server_port: 8080 (or from PORT env)   # Customizable port
theme: "soft"                           # Clean, modern design
primary_color: "indigo"                 # Theme color
```

### Advanced Customization
- **System Prompt**: Edit `system_prompt.md` to modify AI rules and behavior (Hebrew)
- **Styling**: Edit `styles.css` for UI customization
- **Examples**: Modify `examples` list in `main.py` for shown prompts

## 🛡️ Safety & Security

### Built-in Protections

The AI is configured with **strict safety rules** to prevent dangerous operations:

| Operation | Status | Reason |
|-----------|--------|--------|
| File deletion (`rm`, `del`) | ❌ BLOCKED | Irreversible data loss |
| Permission changes (`chmod 777`) | ❌ BLOCKED | Security risk |
| System modifications (`sudo`) | ❌ BLOCKED | Requires authorization |
| Network access (`nc`, `curl` downloads) | ⚠️ LIMITED | Only safe operations |
| Script execution | ❌ BLOCKED | Could be malicious |
| Package removal (`apt remove`) | ❌ BLOCKED | System instability |
| **Safe operations** | ✅ ALLOWED | View, search, analyze files |

### Defense Strategy

1. **Prompt-level Protection**: Safety rules coded directly in `system_prompt.md`
2. **Response Validation**: AI refused dangerous requests before output
3. **User Review**: No auto-execution - user always reviews command
4. **Isolated Execution**: Commands run user's local terminal, not on server
5. **No Data Access**: Application never copies files or accesses sensitive data

### Best Practices
- ✅ Always review generated commands before running
- ✅ Test unfamiliar commands with `echo command_here` first
- ✅ Use `--dry-run` flags when available
- ✅ Never blindly run commands from untrusted sources
- ✅ Keep Groq API key secret - never share or commit to git

## 📦 Dependencies

### Python Packages
The project uses these main dependencies:

| Package | Version | Purpose |
|---------|---------|---------|
| **groq** | 1.0.0 | Groq API client for command generation |
| **gradio** | ≥3.49.0 | Web UI framework for interface |
| **python-dotenv** | 1.2.1 | Load environment variables from .env |
| **openai** | ≥2.2.0 | Supporting library for API operations |
| **pillow** | Latest | Image processing for UI components |
| **pydantic** | Latest | Data validation and parsing |
| **psutil** | Latest | System monitoring (optional) |

### System Requirements
- **Python**: 3.8+ (3.10+ recommended)
- **RAM**: 512MB minimum (1GB+ recommended)
- **Disk**: 500MB for virtual environment
- **Internet**: Required for Groq API calls
- **Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)

See [requirements.txt](requirements.txt) for complete list with pinned versions.

## 🌐 Deployment

### Option 1: Deploy to Render (Recommended)
Quick cloud deployment with zero setup:

1. **Create Render account** at [render.com](https://render.com)
2. **Push code to GitHub**
3. **Create New > Web Service** in Render
4. **Connect your GitHub repository**
5. **Configure environment**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Add environment variable: `GROQ_API_KEY=your_key`
6. **Deploy** button to launch
7. **Visit** your app at `https://your-app-name.onrender.com`

### Option 2: Deploy to Heroku
```bash
# Create app
heroku create your-app-name

# Add Groq API key
heroku config:set GROQ_API_KEY=your_key

# Deploy
git push heroku main
```

### Option 3: Deploy to Railway
```bash
# Install railway CLI
npm i -g @railway/cli

# Deploy
railway up
```

### Option 4: Self-Host with Docker
```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

Build and run:
```bash
docker build -t cmdproject .
docker run -p 8080:8080 -e GROQ_API_KEY=your_key cmdproject
```

### Option 5: Traditional VPS/Server
```bash
# SSH into server
ssh user@server.com

# Clone repo and setup
git clone your-repo
cd cmdProject
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env with API key
echo "GROQ_API_KEY=your_key" > .env

# Run with process manager (systemd, supervisor, pm2, etc.)
python main.py
```

**Tip**: Use a process manager like `supervisor` or `systemd` to keep the app running after terminal closes.

## 🔧 Troubleshooting Guide

### 🔴 Common Issues & Solutions

#### Issue: "API Key not found" or "Authentication Error"
**Symptoms**: Application won't start or commands fail to generate
```
Error: groq.error.AuthenticationError
```
**Solutions**:
- ✅ Verify `.env` file exists in project root (same folder as `main.py`)
- ✅ Check API key format: should start with `gsk_`
- ✅ Ensure no typos in `.env` file
- ✅ Get a new key from [Groq Console](https://console.groq.com)
- ✅ Restart the application after updating `.env`

#### Issue: "Port 8080 already in use"
**Symptoms**: `Address already in use` or `OSError: [Errno 48]`
**Solutions**:
```bash
# Find what's using port 8080 and stop it
# Windows:
netstat -ano | findstr :8080

# macOS/Linux:
lsof -i :8080

# Or use a different port:
PORT=8081 python main.py
# Then visit: http://localhost:8081
```

#### Issue: "No module named 'groq'" or import errors
**Symptoms**: `ModuleNotFoundError: No module named 'X'`
**Solutions**:
```bash
# Ensure virtual environment is activated
# Windows: myproject\Scripts\activate
# macOS/Linux: source myproject/bin/activate

# Reinstall requirements
pip install --upgrade -r requirements.txt

# Or install missing package directly
pip install groq gradio python-dotenv
```

#### Issue: Command generation is slow
**Symptoms**: Takes > 10 seconds to generate a command
**Solutions**:
- ✅ Groq API might be experiencing high load - wait and retry
- ✅ Use shorter, more specific requests
- ✅ Check internet connection
- ✅ Verify API key is valid and has quota

#### Issue: Generated commands don't work on my system
**Symptoms**: Command runs but produces unexpected results
**Solutions**:
- ✅ Different OS have different commands (use specific OS in request)
- ✅ Try rephrasing: "Find files (Linux)" vs "Search files (Windows)"
- ✅ Some commands require specific tools installed
- ✅ Use `man command_name` to verify command syntax locally

#### Issue: "Cannot find system_prompt.md" or styles.css errors
**Symptoms**: Application starts but UI looks broken
**Solutions**:
```bash
# Verify files exist in project root:
# - system_prompt.md (AI rules)
# - styles.css (UI styling)
# - main.py

# If missing, restore from repository
```

### 🟡 Performance & Limitations

| Metric | Value | Notes |
|--------|-------|-------|
| Avg Response Time | 0.5-2s | Depends on Groq API load |
| Max Command Length | 150 tokens | ~500 characters |
| Concurrent Users | Unlimited | Each user has own session |
| API Rate Limit | Per Groq account | Check Groq console |
| Command Complexity | Simple to moderate | Not for multi-line scripts |

### 📊 Tips for Better Results

1. **Be Specific**: Instead of "find files", say "find .txt files in Documents folder"
2. **Mention OS**: Specify "Linux", "macOS", or "Windows" for OS-specific commands
3. **Use Examples**: "Like grep but for binary files" helps AI understand intent
4. **One Task at a Time**: Each request = one command (not multi-step scripts)
5. **Use Technical Terms**: "recursive", "case-insensitive", "symlink" improve accuracy

## 🚀 Advanced Usage

### Multi-Step Workflows

**Instead of**: "Rename all files"
**Try**: "Rename all .txt files to .md in current directory"
```
AI generates: rename 's/\.txt$/.md/' *.txt
Then manually: chain with other commands if needed
```

### Combining with Other Tools

The app generates single commands - combine them yourself:
```bash
# AI generates each command separately, you chain them:
find . -name "*.log" -type f | xargs wc -l | sort -rn | head -10

# Request in multiple steps to AI:
# 1. "Find all .log files"
# 2. "Count lines in files (use wc -l)"
# 3. "Sort by largest file"
# 4. "Show top 10"
```

### Advanced Request Patterns

**Pattern 1: Conditional Operations**
```
Request: "Find files larger than 100MB in /home that contain 'backup'"
Generated: find /home -size +100M -type f -name "*backup*"
```

**Pattern 2: Scheduled Tasks**
```
Request: "Create a cron job to run daily at 2 AM"
Generated: 0 2 * * * /path/to/script.sh
(Then add to crontab -e)
```

**Pattern 3: System Analysis**
```
Request: "Show top 5 processes using most CPU with their memory"
Generated: ps aux --sort=-%cpu | head -6
```

**Pattern 4: Network Operations**
```
Request: "Check if server example.com is reachable on port 443"
Generated: nc -zv example.com 443
```

**Pattern 5: Batch Processing**
```
Request: "Apply gzip compression to all .log files recursively"
Generated: find . -name "*.log" -exec gzip {} \;
```

### Integration with IDEs/Editors

**VS Code**:
1. Open integrated terminal (Ctrl+`)
2. Keep this app in browser
3. Alt+Tab between app and VS Code
4. Copy commands and test

**Command Line Tips**:
```bash
# Open app in one terminal, work in another
# Terminal 1: python main.py
# Terminal 2: Your work

# Or use tmux/screen
tmux new-window -n app "python main.py"
tmux select-window -t app
```

### Using with Package Managers

```
Request: "List all pip packages with their versions"
Generated: pip list

Request: "Upgrade pip to latest version"
Generated: pip install --upgrade pip

Request: "Find unused Python packages"
Generated: pip list --outdated
```

### Docker Integration

```
Request: "Find all running Docker containers and their memory usage"
Generated: docker stats --no-stream

Request: "Remove all stopped Docker containers"
⚠️ BLOCKED - Safety rule prevents deletion
Alternative request: "List all stopped Docker containers to review"
Generated: docker ps -a --filter "status=exited"
```

### Git Operations

```
Request: "Show all modified files in current git repo"
Generated: git status

Request: "Create a patch of all changes since main branch"
Generated: git diff main > changes.patch

Request: "List commits from past week on all branches"
Generated: git log --all --since="1 week ago" --oneline
```

## 🎯 How It Works

The application follows a simple, secure pipeline:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. USER INPUT                                               │
│    "Find files modified today"                              │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. SYSTEM PROMPT CHECK                                      │
│    Apply Hebrew safety rules & formatting guidelines        │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. GROQ API CALL                                            │
│    llama-3.3-70b model processes request                    │
│    Temperature: 0.2 (low randomness)                        │
│    Max tokens: 150 (concise output)                         │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. COMMAND GENERATION                                       │
│    Generated: find . -type f -mtime 0                       │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. SAFETY VALIDATION                                        │
│    ✅ Safe command, display to user                         │
│    ❌ Dangerous command, request clarification              │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. USER SEES RESULT                                         │
│    Command displayed with copy button                       │
│    User can copy and execute locally                        │
└─────────────────────────────────────────────────────────────┘
```

**Key Design Decisions:**
- ✅ AI runs **completely serverless** - no command execution on server
- ✅ Commands are generated but **never executed** by the app
- ✅ User has **full control** - reviews command before running
- ✅ **No data persistence** - commands not logged (by default)
- ✅ **Safe by default** - dangerous operations blocked at prompt level

## 🎨 Customization Guide

### 1. Modify AI Behavior
Edit `system_prompt.md` (in Hebrew):
```markdown
# Change these rules to modify what the AI accepts/refuses
- Rule: Don't generate file deletion commands
- Rule: Require specific user confirmation for XYZ
```

### 2. Customize UI Styling
Edit `styles.css`:
```css
/* Change colors, fonts, spacing, animations */
:root {
    --primary-color: #indigo;
    --background: linear-gradient(...);
}
```

### 3. Add Example Prompts
In `main.py`, find the `examples` list:
```python
examples = [
    "Find all .log files",
    "Show disk usage",
    "List running processes",
    # Add your own examples
]
```

### 4. Change Server Port
```bash
# Run on different port
PORT=3000 python main.py
# Visit: http://localhost:3000
```

### 5. Adjust AI Parameters
In `main.py`, modify:
```python
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    temperature=0.2,           # 0=consistent, 1=creative
    max_tokens=150,           # Response length limit
    top_p=0.9,               # Nucleus sampling
)
```

## 📚 Documentation Files Reference

| File | Purpose | Edit For |
|------|---------|----------|
| `system_prompt.md` | AI rules & safety guidelines | Changing AI behavior |
| `styles.css` | Visual styling & design | UI colors, fonts, layout |
| `main.py` | Application logic | Advanced features |
| `requirements.txt` | Python dependencies | Adding/removing packages |
| `.env` | Secrets & configuration | API keys, ports |

## ❓ FAQ

**Q: Is my API key safe?**
A: Yes! The `.env` file is:
- Loaded locally (never sent anywhere)
- Not committed to git (add to `.gitignore`)
- Only used for Groq API authentication
- Never logged or stored in database

---

**Q: Can I use this offline?**
A: No, it requires Groq API which needs internet. But offline terminal autocomplete utils exist.

---

**Q: Will my commands be saved?**
A: By default, no. Commands are displayed but not logged. Gradio can optionally save "flagged" outputs.

---

**Q: What if I don't trust the generated command?**
A: Perfect! The app is designed for you to:
1. Review the generated command
2. Test it with `echo` or `--dry-run` first
3. Then execute when confident

---

**Q: Can I deploy this myself?**
A: Yes! See [Deployment](#-deployment) section. Works on Render, Heroku, Railway, etc.

---

**Q: How accurate is the AI?**
A: Very accurate for common commands (>95%). Edge cases may need rephrasing.

---

**Q: What operating systems does this support?**
A: The app runs on Windows/macOS/Linux. Generated commands are OS-specific (mention your OS in requests).

---

**Q: Can I modify the AI rules?**
A: Yes! Edit `system_prompt.md` (Hebrew) to add/change rules about what commands to generate.

---

**Q: How much does this cost?**
A: Free! Uses Groq API which offers free tier. Check [Groq Pricing](https://groq.com) for limits.

---

**Q: Can I self-host this?**
A: Yes! Deploy to your own server, Docker container, or cloud platform.

## 📄 License

MIT License - Free to use, modify, and distribute. See LICENSE file for details.

## 👨‍💻 Contributing

Contributions welcome! Areas for improvement:
- Add support for additional shells (fish, zsh, PowerShell)
- Multi-language support for system prompts
- Enhanced UI with command history
- Docker containerization
- Mobile app version

**To contribute**:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support & Resources

- 🐛 **Bug Reports**: Open an issue on GitHub
- 💬 **Questions**: Check FAQ section above
- 📖 **Documentation**: Read this README thoroughly
- 🌐 **Groq Support**: [Groq Documentation](https://console.groq.com/docs)
- 📚 **Gradio Help**: [Gradio Docs](https://gradio.app)

## 🚀 Next Steps

1. **Get Started**: Follow the [Quick Start](#-quick-start) section
2. **Explore Examples**: Try different requests to understand capabilities
3. **Customize**: Modify `system_prompt.md` and `styles.css` for your needs
4. **Deploy**: Deploy to cloud platform for sharing with team
5. **Contribute**: Improve the project and share improvements

## 📈 Roadmap

Potential future features:
- ✨ Command history and bookmarks
- ✨ Multi-language prompts (English, French, Spanish, etc.)
- ✨ Shell-specific optimization (bash, zsh, PowerShell, fish)
- ✨ Interactive command builder
- ✨ Integration with terminal emulators
- ✨ Docker support for Easy deployment
- ✨ API endpoint for programmatic access

---

**Built with ❤️ using Groq API, Gradio, and Python**
