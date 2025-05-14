import 'package:flutter/material.dart';

class ProfilesOverview extends StatefulWidget {
  const ProfilesOverview({super.key});

  @override
  State<ProfilesOverview> createState() => _ProfilesOverviewState();
}

class _ProfilesOverviewState extends State<ProfilesOverview> {
  @override
  Widget build(BuildContext context) {
    return Center(
        child: Text("Overview")
    );
  }
}
