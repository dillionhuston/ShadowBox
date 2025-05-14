import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class SectionPage {
  String name, path;
  Widget pageWidget;
  bool listed = true;

  SectionPage({required this.name, required this.path, required this.pageWidget, this.listed=true});

  GoRoute toGoRoute({Widget Function(Widget)? builder}) {
    return GoRoute(
      path: path,
      builder: (context, state) => builder == null ? pageWidget : builder(pageWidget)
    );
  }

  static SectionPage fromMap(Map<String, dynamic> map) {
    return SectionPage(
      name: (map.containsKey("name") ? map["name"] : "<NoName>"),
      path: (map.containsKey("path") ? map["path"] : "/NoPath"),
      pageWidget: (map.containsKey("pageWidget") ? map["pageWidget"] : const Placeholder()),
      listed: (map.containsKey("listed") ? map["listed"] : true)
    );
  }
}

class Section {
  String name, path;
  String? redirectPath;
  bool listed = true;
  List<SectionPage> pages = [];

  Section({required this.name, required this.path, this.redirectPath, this.listed=true});

  ShellRoute toShellRoute({Widget Function(Widget)? builder}) {
    List<GoRoute> routes = [
      GoRoute(
        path: path,
        redirect: redirectPath == null ? null : ((context, state) => redirectPath)
      )  // Section route
    ];
    for (SectionPage page in pages) {
      routes.add(page.toGoRoute());
    }
    return ShellRoute(
      builder: (context, state, child) => builder == null ? child : builder(child),
      routes: routes
    );
  }
}

class SectionManager {
  static Map<String, Section>? _sectionsMap;
  static List<SectionPage>? _globalPages;

  static void setSectionsMap(Map<String, Map<String, dynamic>> sectionsMap) {
    _sectionsMap = <String, Section>{};
    sectionsMap.forEach((key, values) {
      Section res = Section(name: key, path: "/$key");
      if (values.containsKey("name")) {
        res.name = values["name"];
      }
      if (values.containsKey("redirectPath")) {
        res.redirectPath = values["redirectPath"];
      }
      if (values.containsKey("pages")) {
        for (Map<String, dynamic> pageMap in values["pages"]) {
          res.pages.add(SectionPage.fromMap(pageMap));
        }
      }
      if (values.containsKey("listed")) {
        res.listed = values["listed"];
      }
      (_sectionsMap as Map<String, Section>)[key] = res;
    });
  }
  static void setGlobalPages(List<Map<String, dynamic>> globalPages) {
    _globalPages = globalPages.map((pageMap) => SectionPage.fromMap(pageMap)).toList();
  }

  static GoRouter? getGoRouter({String? initialLocation, Widget Function(Widget)? builder}) {
    if (_sectionsMap == null) return null;
    List<RouteBase> routes = [];

    _sectionsMap?.forEach((key, value) {
      routes.add(value.toShellRoute(
        builder: builder
      ));
    });
    _globalPages?.forEach((page){
      routes.add(page.toGoRoute(
        builder: builder
      ));
    });

    return GoRouter(
      initialLocation: initialLocation,
      routes: routes
    );
  }

  static List<Section> getAllSections() => List<Section>.from(_sectionsMap?.values ?? Iterable.empty());
  static List<SectionPage> getAllGlobalPages() => _globalPages ?? [];
}