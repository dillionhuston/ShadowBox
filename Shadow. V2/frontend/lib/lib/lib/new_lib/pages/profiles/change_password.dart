import 'package:flutter/material.dart';

class ChangePasswordPage extends StatelessWidget {
  const ChangePasswordPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Card(
          child: Padding(
            padding: const EdgeInsets.all(40),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Text(
                  'Change Password',
                  style: TextStyle(
                    fontSize: 26,
                    color: Color(0xFF00BCD4),
                  ),
                ),
                const SizedBox(height: 25),
                Container(
                  padding: const EdgeInsets.all(12),
                  color: const Color(0xFFF44336),
                  child: const Text(
                    'Always use a strong, unique password to protect your account.',
                    style: TextStyle(
                      color: Color(0xFFFFFFFF),
                      fontWeight: FontWeight.bold,
                    ),
                    textAlign: TextAlign.center,
                  ),
                ),
                const SizedBox(height: 20),
                TextField(
                  decoration: const InputDecoration(
                    labelText: 'Current Password',
                  ),
                  style: const TextStyle(color: Color(0xFFFFFFFF)),
                  obscureText: true,
                ),
                const SizedBox(height: 20),
                TextField(
                  decoration: const InputDecoration(
                    labelText: 'New Password',
                  ),
                  style: const TextStyle(color: Color(0xFFFFFFFF)),
                  obscureText: true,
                ),
                const SizedBox(height: 20),
                TextField(
                  decoration: const InputDecoration(
                    labelText: 'Confirm New Password',
                  ),
                  style: const TextStyle(color: Color(0xFFFFFFFF)),
                  obscureText: true,
                ),
                const SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {},
                  child: const Text('Update Password'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
