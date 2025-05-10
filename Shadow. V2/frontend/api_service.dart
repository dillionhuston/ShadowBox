import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:file_picker/file_picker.dart';

class ApiService {
  static const String baseUrl = 'http://127.0.0.1:5000';
  String? _token;

  ApiService() {
    _loadToken();
  }

  Future<void> _loadToken() async {
    final prefs = await SharedPreferences.getInstance();
    _token = prefs.getString('token');
  }

  Future<void> _saveToken(String token) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('token', token);
    _token = token;
  }

  Future<void> _clearToken() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove('token');
    _token = null;
  }

  Future<Map<String, dynamic>> signup(String username, String email, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/signup'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'username': username,
        'email': email,
        'password': password,
      }),
    );

    return _handleResponse(response);
  }

  Future<Map<String, dynamic>> login(String username, String password) async {
    final response = await http.post(
      Uri.parse('$baseUrl/login'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'username': username,
        'password': password,
      }),
    );

    final data = _handleResponse(response);
    if (data.containsKey('token')) {
      await _saveToken(data['token']);
    }
    return data;
  }

  Future<Map<String, dynamic>> logout() async {
    final response = await http.post(
      Uri.parse('$baseUrl/logout'),
      headers: {'Authorization': 'Bearer $_token'},
    );

    final data = _handleResponse(response);
    await _clearToken();
    return data;
  }

  Future<List<dynamic>> getDashboard() async {
    final response = await http.get(
      Uri.parse('$baseUrl/dashboard'),
      headers: {'Authorization': 'Bearer $_token'},
    );

    final data = _handleResponse(response);
    return data['files'];
  }

  Future<Map<String, dynamic>> uploadFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles();
    if (result == null) {
      return {'error': 'No file selected'};
    }

    final file = result.files.single;
    var request = http.MultipartRequest('POST', Uri.parse('$baseUrl/upload'));
    request.headers['Authorization'] = 'Bearer $_token';
    request.files.add(await http.MultipartFile.fromPath('file', file.path!));

    final response = await request.send();
    final responseBody = await response.stream.bytesToString();
    return _handleResponseStream(response, responseBody);
  }

  Future<File> downloadFile(int fileId, String filename) async {
    final response = await http.get(
      Uri.parse('$baseUrl/download/$fileId'),
      headers: {'Authorization': 'Bearer $_token'},
    );

    if (response.statusCode == 200) {
      final dir = Directory.systemTemp;
      final file = File('${dir.path}/$filename'.replaceAll('.enc', ''));
      await file.writeBytes(response.bodyBytes);
      return file;
    } else {
      final data = jsonDecode(response.body);
      throw Exception(data['error']);
    }
  }

  Map<String, dynamic> _handleResponse(http.Response response) {
    final data = jsonDecode(response.body);
    if (response.statusCode >= 200 && response.statusCode < 300) {
      return data;
    }
    throw Exception(data['error'] ?? 'Request failed');
  }

  Map<String, dynamic> _handleResponseStream(http.StreamedResponse response, String body) {
    final data = jsonDecode(body);
    if (response.statusCode >= 200 && response.statusCode < 300) {
      return data;
    }
    throw Exception(data['error'] ?? 'Request failed');
  }
}