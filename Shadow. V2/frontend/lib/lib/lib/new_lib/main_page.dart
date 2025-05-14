import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:fronte/new_lib/sections.dart';

Widget getSectionPageWidget(SectionPage page, BuildContext context) {
  return TextButton(
    onPressed: () { context.go(page.path); },
    child: Container(
      alignment: Alignment.centerLeft,
      width: double.infinity,
      child: Text(
        page.name,
        style: TextStyle(
            fontWeight: FontWeight.normal,
            fontSize: 14,
            overflow: TextOverflow.fade
        ),
      ),
    ),
  );
}
Widget getExpandedSectionWidget(Section section, BuildContext context) {
  return SizedBox(
    width: double.infinity,
    child: Column(
      children: [
        TextButton(
          onPressed: () { context.go(section.path); },
          style: TextButton.styleFrom(
            alignment: Alignment.centerLeft,
            padding: EdgeInsets.symmetric(horizontal: 5)
          ),
          child: Container(
            alignment: Alignment.centerLeft,
            width: double.infinity,
            child: Text(
              section.name,
              style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                  overflow: TextOverflow.fade
              ),
            ),
          ),
        ),
        Container(
          padding: EdgeInsets.symmetric(horizontal: 5),
          width: double.infinity,
          child: Column(
            children: section.pages.map((page) {
              if (!page.listed) return null;
              return getSectionPageWidget(page, context);
            }).where((widget) => widget != null).cast<Widget>().toList(),
          ),
        )
      ],
    )
  );
}
List<Widget> getSidebarSectionsWidgetList(BuildContext context) {
  List<SectionPage> globalPages = SectionManager.getAllGlobalPages();
  List<Section> sections = SectionManager.getAllSections();

  List<Widget> res = [];
  for (SectionPage page in globalPages) {
    if (!page.listed) continue;
    res.add(getSectionPageWidget(page, context));
  }
  for (Section section in sections) {
    if (!section.listed) continue;
    res.add(getExpandedSectionWidget(section, context));
  }
  return res;
}

class MainPageScaffold extends StatefulWidget {
  final Widget? child;

  const MainPageScaffold({super.key, this.child});

  @override
  State<MainPageScaffold> createState() => _MainPageScaffoldState();
}

class _MainPageScaffoldState extends State<MainPageScaffold> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          SizedBox(
            width: 240,
            child: Container(
              color: const Color(0xFF1E1E1E),
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  const Text(
                    'ShadowBox',
                    style: TextStyle(fontSize: 26, color: Color(0xFF00BCD4)),
                  ),
                  const SizedBox(height: 30),
                  Expanded(
                    child: Padding(
                      padding: EdgeInsets.symmetric(horizontal: 10, vertical: 30),
                      child: ListView(
                        children: getSidebarSectionsWidgetList(context),
                      ),
                    ),
                  )
                ],
              ),
            ),
          ),
          Expanded(
            child: Column(
              children: [
                Container(
                  height: 70,
                  padding: const EdgeInsets.symmetric(
                    horizontal: 33,
                    vertical: 17,
                  ),
                  color: const Color(0xFF1F1F1F),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      const Text('Hello, User'),
                      const SizedBox(width: 14),
                      Container(
                        width: 40,
                        height: 40,
                        decoration: const BoxDecoration(
                          shape: BoxShape.circle,
                          border: Border(
                            top: BorderSide(
                              color: Color(0xFF03A9F4),
                              width: 2
                            ),
                            left: BorderSide(
                              color: Color(0xFF03A9F4),
                              width: 2,
                            ),
                            right: BorderSide(
                              color: Color(0xFF03A9F4),
                              width: 2,
                            ),
                            bottom: BorderSide(
                              color: Color(0xFF03A9F4),
                              width: 2,
                            ),
                          ),
                        ),
                        child: ClipOval(
                          child: Image.network(
                            'https://via.placeholder.com/40',
                            fit: BoxFit.cover,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                Expanded(
                  child: widget.child ?? Placeholder(),
                )
              ],
            )
          )
        ],
      )
    );
  }
}
