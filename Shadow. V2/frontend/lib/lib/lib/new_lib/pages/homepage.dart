import 'package:flutter/material.dart';

class Homepage extends StatelessWidget {
  const Homepage({super.key});

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
                  'Welcome to Shadowbox',
                  style: TextStyle(
                    fontSize: 26,
                    color: Color(0xFF00BCD4),
                  ),
                ),
                const SizedBox(height: 25),
                const Text(
                  'Your creative space awaits.',
                  style: TextStyle(color: Color(0xFF777777)),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
