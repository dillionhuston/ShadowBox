# ShadowBox API Reference

## Core Services

### EncryptionService

Handles the encryption and decryption of user files with AES-256 in GCM mode.

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `generate_key(password)` | Creates a cryptographic key from user password using PBKDF2 | `password` (str): User password | `tuple(bytes, bytes)`: Key and salt |
| `encrypt(file, filename)` | Encrypts a file using AES-GCM | `file`: File object, `filename` (str): Filename | None |
| `save_file(data, filename)` | Saves encrypted data to storage | `data` (bytes): Encrypted file data, `filename` (str): Sanitized filename | None |
| `decrypt(file_data)` | Decrypts previously encrypted file data | `file_data` (bytes): Encrypted data | `bytes`: Decrypted file content |

### FileStorageService

Manages physical file storage operations.

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `read_file(filedata)` | Reads file content from disk | `filedata`: File path or identifier | `bytes`: File content |
| `save_file(file_data, filename)` | Saves file data to disk | `file_data` (bytes): File content, `filename` (str): Name of file | None |
| `retrieve_file(file_id)` | Retrieves a file by ID (placeholder for future implementation) | `file_id`: File identifier | None |

## Authentication Module

### Routes

| Route | Method | Description | Request Data | Response |
|-------|--------|-------------|-------------|----------|
| `/signup` | GET | Displays signup page | None | HTML: Signup form |
| `/signup` | POST | Creates new user account | `username`, `password`, `email` | Redirect to login or error |
| `/login` | GET | Displays login page | None | HTML: Login form |
| `/login` | POST | Authenticates user | `username`, `password` | Redirect to file upload or error |
| `/logout` | GET | Logs out current user | None | Redirect to login page |

### User Model

Manages user accounts and authentication.

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `add_user(username, email, password)` | Creates new user account | `username` (str), `email` (str), `password` (str) | User object |
| `verify_hash(password, hash)` | Verifies password against stored hash | `password` (str), `hash` (str) | bool |
| `get_key(user)` | Retrieves encryption key for user | `user`: User object | bytes |

## File Management Module

### Routes

| Route | Method | Description | Request Data | Response |
|-------|--------|-------------|-------------|----------|
| `/upload` | GET | Displays file upload page | None | HTML: Upload form |
| `/upload` | POST | Processes file upload | File in form data | Redirect with success/error message |

### File Model

Tracks file metadata and ownership.

#### Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `add_file(filename, filepath)` | Records file in database | `filename` (str), `filepath` (str) | File object |

## Security Implementation

### Encryption

- AES-256 encryption in GCM mode provides:
  - Data confidentiality
  - Authentication (tampering detection)
  - Built-in integrity checking

### Key Derivation

- PBKDF2 with SHA-256
- 100,000 iterations
- Random 16-byte salt
- 32-byte key length

### File Storage

- Files are stored with sanitized names
- Files are saved with `.enc` extension
- Physical paths are not exposed to users

## Error Handling

The system implements comprehensive error logging and handling:

- All operations are logged at appropriate levels (INFO, DEBUG, ERROR)
- User-facing errors display friendly messages
- System errors are logged with detailed information for troubleshooting
- Exception catching preserves application stability

## Configuration

Application settings are managed through the Config class:
- `ENCRYPTED_FILE_PATH`: Location where encrypted files are stored
- Additional configuration variables are defined in the Config class

## Future API Extensions

Planned API expansions include:
- File sharing with expiring links
- Enhanced permission controls
- End-to-end encryption implementation
- Multi-device synchronization
