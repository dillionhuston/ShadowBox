# Secure File System User Guide

## Introduction

Welcome to the Secure File System! This application allows you to securely upload and store your sensitive files using strong encryption. Your files are protected with AES encryption using your personal key, ensuring that only you can access them.

## Getting Started

### Creating an Account

1. Navigate to the sign-up page by clicking "Sign Up" or going to `/signup`
2. Fill in the required information:
   - Username: Choose a unique username
   - Email: Provide a valid email address
   - Password: Create a strong password
3. Click "Sign Up" to create your account
4. You'll receive a confirmation message when your account is created successfully

### Logging In

1. Go to the login page at `/login`
2. Enter your username and password
3. Click "Login"
4. Upon successful login, you'll be redirected to the file upload page

### Logging Out

1. Click the "Logout" button from any page when you're logged in
2. Your session will be terminated, and all encryption keys will be cleared from memory

## Working with Files

### Uploading Files

1. After logging in, navigate to the upload page at `/upload`
2. Click "Choose File" to select a file from your device
3. Click "Upload" to securely upload your file
4. The system will:
   - Encrypt your file using your personal encryption key
   - Store the encrypted file securely
   - Show a confirmation message upon successful upload

### File Security

All files are protected using:

- **AES Encryption**: Industry-standard symmetric encryption
- **GCM Mode**: Provides both confidentiality and authentication
- **Personal Keys**: Each user has their own encryption key
- **Secure Storage**: Encrypted files are stored in a protected location

## Security Best Practices

For the best security:

1. **Use a Strong Password**: Choose a complex password that's difficult to guess
2. **Log Out When Finished**: Always log out when you're done using the system
3. **Keep Your Computer Secure**: Ensure your device is protected with up-to-date security software
4. **Be Mindful of Sensitive Data**: Even with encryption, exercise caution with extremely sensitive information

## Troubleshooting

### Common Issues

1. **Login Problems**:
   - Verify your username and password are correct
   - Ensure caps lock is off
   - Try resetting your password if you continue to have issues

2. **Upload Failures**:
   - Check your internet connection
   - Ensure the file isn't too large
   - Try a different file format if problems persist

3. **Security Warnings**:
   - If you receive any security warnings, log out immediately and contact support

### Getting Help

If you encounter any issues or have questions about using the system, please contact right away

