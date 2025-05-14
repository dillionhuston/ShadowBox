import 'package:flutter/material.dart';
import 'package:fronte/new_lib/main_page.dart';
import 'package:fronte/new_lib/pages/dashboard/overview.dart';
import 'package:fronte/new_lib/pages/homepage.dart';
import 'package:fronte/new_lib/pages/profiles/change_password.dart';
import 'package:fronte/new_lib/pages/profiles/overview.dart';
import 'package:fronte/new_lib/sections.dart';

// Note: To navigate to a pages, use context.go(<url>)
//  (which, context is from build function (Widget build(BuildContext context))

// A list of global pages (not belong to any section, like Home Page, Login Page,...)
final _sectionGlobalPages = [
  {
    "name": "Home Page",            // The name of the page (optional, use in case listed).
    "path": "/home",                // The path (url) to the page.
    "listed": false,                // Enable/disable to have a navigate button show up on the sidebar
                                    //   (optional, default to true).
    "pageWidget": const Homepage()  // The widget of the page.
  }
];

// A map of multiple section of pages
final _sectionLayoutMap = {
  "dashboard": {
    "name": "Dashboard",                        // The name of the section (optional, use in case listed).
    "path": "/dashboard",                       // The path (url) to the section.
    "listed": true,                             // Enable/disable to have a navigate button for the section
                                                //   and all of it's pages show up on the sidebar
                                                //   (optional, default to true).
    "redirectPath": "/dashboard/overview",      // The redirected path to a page of the section
                                                //   (like, the initial page).

    // A list of pages of the section
    "pages": [
      {
        "name": "Overview",                     // The name of the page (optional, use in case listed).
        "path": "/dashboard/overview",          // The path (url) to the page.
        "listed": true,                         // Enable/disable to have a navigate button show up on the sidebar
                                                //   (optional, default to true).
        "pageWidget": const DashboardOverview() // The widget of the page.
      },
      {
        "name" : "Information",
        "path": "/dashboard/information",
        "listed": true,
        "pageWidget": Center(child: Text("Information"))
      }
    ]
  },
  "profiles" : {
    "name": "Profiles",
    "path": "/profiles",
    "listed": true,
    "redirectPath": "/profiles/overview",
    "pages": [
      {
        "name": "Overview",
        "path": "/profiles/overview",
        "listed": true,
        "pageWidget": const ProfilesOverview()
      },
      {
        "name": "Change Password",
        "path": "/profiles/change_password",
        "listed": true,
        "pageWidget": const ChangePasswordPage()
      }
    ]
  }
};

void main() {
  SectionManager.setSectionsMap(_sectionLayoutMap);
  SectionManager.setGlobalPages(_sectionGlobalPages);
  runApp(const ShadowBoxApp());
}

class ShadowBoxApp extends StatelessWidget {
  const ShadowBoxApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Shadow Box',
      theme: ThemeData(
        scaffoldBackgroundColor: const Color(0xFF121212),
        primaryColor: const Color(0xFF00BCD4),
        textTheme: const TextTheme(
          bodyMedium: TextStyle(
            color: Color(0xFFFFFFFF),
            fontFamily: 'Segoe UI',
          ),
          labelLarge: TextStyle(
            color: Color(0xFF00BCD4),
            fontFamily: 'Segoe UI',
          ),
          headlineMedium: TextStyle(
            fontSize: 26,
            color: Color(0xFF00BCD4),
            fontFamily: 'Segoe UI',
          ),
        ),
        cardTheme: const CardTheme(color: Color(0xFF1E1E1E), elevation: 5),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            backgroundColor: const Color(0xFF03A9F4),
            foregroundColor: Colors.white,
            textStyle: const TextStyle(fontSize: 16, fontFamily: 'Segoe UI'),
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 12),
          ),
        ),
        textButtonTheme: TextButtonThemeData(
          style: TextButton.styleFrom(
            foregroundColor: const Color(0xFFCCCCCC),
            textStyle: const TextStyle(fontFamily: 'Segoe UI'),
          ),
        ),
        inputDecorationTheme: const InputDecorationTheme(
          filled: true,
          fillColor: Color(0xFF2A2A2A),
          labelStyle: TextStyle(
            color: Color(0xFFFFFFFF),
            fontFamily: 'Segoe UI',
          ),
          border: OutlineInputBorder(
            borderSide: BorderSide(color: Color(0xFF333333)),
            borderRadius: BorderRadius.all(Radius.circular(5)),
          ),
        ),
      ),
      routerConfig: SectionManager.getGoRouter(
        initialLocation: "/home",
        builder: (widget) => MainPageScaffold(child: widget)
      ),
      debugShowCheckedModeBanner: false,
    );
  }
}
