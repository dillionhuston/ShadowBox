# ShadowBox 📦
**Secure & Private Cloud Storage - Your Digital Fort Knox**

![GitHub stars](https://img.shields.io/github/stars/dillionhuston/shadowbox?style=social)
![GitHub forks](https://img.shields.io/github/forks/dillionhuston/shadowbox?style=social)
![GitHub issues](https://img.shields.io/github/issues/dillionhuston/shadowbox)
![License](https://img.shields.io/badge/license-MIT-blue)

> *Your files, your control, your privacy.*

---
## 🚀 Overview
> ⚠️ **Prototype Warning**: ShadowBox is in early development. Avoid using it for sensitive or production data.

ShadowBox is a **privacy-first**, **encrypted** cloud storage solution built with **Python**, **Flask**, and **SQL**. Designed for security and scalability, it leverages **object-oriented programming** principles to ensure maintainability. Our vision is a decentralized, secure file-sharing platform that puts user control first.

![ShadowBox Demo](https://via.placeholder.com/800x400?text=ShadowBox+Demo)

---
## 🎯 Core Features (MVP)
- 🔒 **AES-256 Encrypted File Uploads**
- 🧑‍💻 **User Authentication & File Ownership**
- 📂 **Secure File Storage & Retrieval**
- ⏰ **Expiring Links & Access Controls**
- 🛠️ **Modular OOP Architecture**

---
## 🔐 Security Implementation
### Encryption
- **AES-256 encryption** in GCM mode provides:
  - Data confidentiality
  - Authentication (tampering detection)
  - Built-in integrity checking

### Key Derivation
- PBKDF2 with SHA-256
- 100,000 iterations for brute-force resistance
- Random 16-byte salt
- 32-byte key length

### File Storage
- Files are stored with sanitized names
- Files are saved with `.enc` extension
- Physical paths are not exposed to users

---
## 🛠️ Tech Stack
| Component | Technology |
| --- | --- |
| **Backend** | Python (Flask), OOP Design |
| **Frontend** | Jinja2, HTML, CSS, JavaScript |
| **Database** | SQLite (PostgreSQL planned) |
| **Encryption** | AES-256, RSA (end-to-end planned) |

---
## ⚙️ Installation
Get ShadowBox up and running in minutes:
```bash
# Clone the repository
git clone https://github.com/dillionhuston/shadowbox.git
cd shadowbox

# Install dependencies
pip install -r requirements.txt

# Launch the app
flask run
```
> **Note**: Run from the root directory or `/static` based on your setup.

---
## 🌲 Branches
- `main`: Functional prototype. Expect some rough edges.
- `ShadowBox-V2`: Work-in-progress refactor. Cleaner, more scalable architecture.

---
## 🔍 Error Handling
The system implements comprehensive error logging and handling:
- All operations are logged at appropriate levels (INFO, DEBUG, ERROR)
- User-facing errors display friendly messages
- System errors are logged with detailed information for troubleshooting
- Exception catching preserves application stability

---
## ⚙️ Configuration
Application settings are managed through the Config class:
- `ENCRYPTED_FILE_PATH`: Location where encrypted files are stored
- Additional configuration variables are defined in the Config class

---
## 🛤️ Roadmap
- ✅ **Phase 1**: Core encryption & file uploads (MVP complete)
- 🔄 **Phase 2**: Refactor for scalability (ShadowBox-V2 in progress)
- ⏳ **Phase 3**: Decentralized storage (IPFS or custom nodes)
- 🚀 **Phase 4**: Real-time sharing, collaboration, monetization

### Coming Soon
- File sharing with expiring links
- Enhanced permission controls
- End-to-end encryption implementation
- Multi-device synchronization

---
## 🤝 Contributing
We're excited to build ShadowBox with the community! Here's how to jump in:
1. Fork and clone the repo:
   ```bash
   git clone https://github.com/dillionhuston/shadowbox.git
   ```
2. Choose a branch: `main` (prototype) or `ShadowBox-V2` (refactor).
3. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Commit your changes and push.
5. Open a **Pull Request** 🎉

---
## 📌 User Guide
Check out the [User Guide](./USER_GUIDE.md) for detailed instructions on using ShadowBox.

---
## 💎 Why Star This Project?
- 🔒 **Privacy First**: True encryption that even we can't access
- 📚 **Learn From It**: Great example of secure application design
- 🌱 **Support Innovation**: Help us grow a privacy-focused alternative
- 🤝 **Join Early**: Be part of a growing privacy-focused community

---
## 📬 Contact & Support
- 🐛 **Bugs or Questions**: Open an issue.
- 💡 **Feedback or Ideas**: Reach out via GitHub.
- 🔄 **Pull Requests**: Always welcome!

---
## 📄 License
**MIT License** – Free to use, modify, and share.  


---
*ShadowBox: Because privacy shouldn't be optional.*
