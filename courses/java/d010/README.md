# 21/10/19 Java lesson

## What I learned(Important)

* [Hello.java](Hello.java)
    * how to print standard output
* [ScannerEx.java](ScannerEx.java)
    * how to take standard input with scanner
* [GradingSwitch.java](GradingSwitch.java)
    * how to use if else
    * how to use switch

```java
      switch(integer,string or char variable){
        case integer,string or char literal1:
        action code1;
        break;
        case integer,string or char literal2:
        action code2;
        break;
        (and more cases)
default:
        default_action code;
        break;
        }
```

* if variable in switch has same valued with case literal, it activates all action codes below itself(even default!)
  until met break
* if there is no case matched, just default action code works
* not familiar with switch which is not in python

## What I studied myself

* java.lang.Math
    * method : min, max, pow
* java.util.Arrays
    * method : sort, reverseOrder, toString
* String
    * method : join
* while(conditional), for(initial condition; conditional; steps to take)

* if(conditional) else(conditional)
    * We could use ? and : replacing if else condition with "conditional ? true progress : false progress"

## What I didn't understand

## What I want to know more

* Different between int and Integer class (Solving)
* what is enum?

## etc(Additional)

* How to format on save in vscode
    * setting - search format on save - check it
* How to format java
    1. press Ctrl + , to open the setting
    2. click Open Settings(JSON) on Top Right Corner
    3. enter below

```json
      "[java]": {
"editor.defaultFormatter": "redhat.java",
},
```

## Practice problems
