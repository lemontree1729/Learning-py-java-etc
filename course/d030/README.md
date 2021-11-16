# 21/11/16 Java lesson

## What I learned(Important)

## What I studied myself

## What I didn't understand

## What I want to know more

## etc(Additional)

* I want to run c++, java and python with just pressing "F5"!
  * c++ have to run with task(should write launch.json and tasks.json) and java and python can't debug or run with "F5" key when tasks file exist(could be but I can't find easy way to specify launch.json and task.json for each language). so, I bind "F5" key with "Run java" and "Python: Run Python File" command using `editorLangId == $lang-name$` in "when" method. This makes when vscode recognize your file as python file, "F5" runs "Python: Run Python File", when your file is java file then "F5" runs "Run java" and other(c++ for now) runs tasked debug!
  * So how you exactly do it
    * Press "F5" on c++ file
    * Select "C++ (GDB/LLDB)" and "g++.exe"
    * Then vscode automately make launch and tasks.json for you
    * Click File -> Preferences -> Keyboard shortcuts
    * Search for "Run java", bind "F5" key and change when expression as `editorLangId == 'java'` with right click
    * Do same thing for "Python: Run Python File" and `editorLangId == 'python'`
    * Run java or python once pressing start button upper right
    * Now done!

## Practice problems

* [Quiz03.java](Quiz03.java)
* [Quiz04.java](Quiz04.java)
* [Quiz04.java](Quiz04.java)
* [Quiz09.java](Quiz09.java)
* [Quiz10.java](Quiz10.java)
* [Quiz11.java](Quiz11.java)
* [Quiz12.java](Quiz12.java)
* [Quiz13.java](Quiz13.java)
* [Quiz14.java](Quiz14.java)

## Useful links
