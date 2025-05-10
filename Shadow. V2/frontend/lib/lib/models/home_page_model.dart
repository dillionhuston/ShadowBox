import 'package:flutter/material.dart';

class AppState extends ChangeNotifier {
  String? _currentSectionName;
  Widget? _currentOpenPage;

  String? get currentSectionName => _currentSectionName;
  Widget? get currentOpenPage => _currentOpenPage;

  void setSectionName(String? sectionName) {
    _currentSectionName = sectionName;
    notifyListeners();
  }
  void setOpenPage(Widget? openPage) {
    _currentOpenPage = openPage;
    notifyListeners();
  }
}