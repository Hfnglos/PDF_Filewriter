I want an app which takes an Notion Database as an Input (maybe even a whole Page with multiple Databases) and transforms each "file" into a clean PDF file.
I have to read the .md Files and have to read the different special characters and delete them from the .pdf File. I also have to change the kind of fond(?) and I want the font to be able to be changes via Settings in the app.
## To Dos
- [ ] Designing the layouts of my app
- [ ] Adding the basic layout to my App
	- [ ] Window 1 (Adding the Files)
	- [ ] Window 2 (Changing the settings for the pdf)
- [ ] Python Tutorial for reading .md and writing .pdf files
	- [ ] How to make different font sizes?
	- [ ] How to make Heading 1, Heading 2,... for example
- [ ] Checking what kind of Blocks I have in Notion and what their feature is
## Notion Blocks
- Heading 1-4 (#)
- Toggle Heading 1-3 (#>)
- Text ()
- Bulleted List (-)
- Numbered List (1.)
- To Do List (- [ ])
- Toggle List (>)
- Divider (---)
- Image
- Code
- Math
- Link
- Fett
- Kursiv
- 
## GUI - PySide6
- [x] How to Install PySide6
- [ ] How to use Themes for PySide6
- [ ] Watching Tutorials for PySide6
## Possible Problems
- 2 '*' direkt hinter einander (Bsp.: *java.util.**)
	- "java.util.*" soll kursiv, aber das Programm wird sehr wahrscheinlich nur "java.util." kursiv schreiben