# 21/12/27 JavaScript Lesson

## What I learned(Important)

* Array: used for data grouping
  * declare:
    * `var $target$ = [$value1$, $value2$, value3$]`
    * `var $target$ = Array.from({length:$array-length$}, ($value$, $index$) => $declare-value-with-index$)`
    * `var $target$ = new Array($value1$, $value2$, $value3$)`
  * check: `Array.isArray($target$)`
  * swallow copy: `var $target$ = [...$origin$]` or `var $target$ = Object.assign({}, $origin$)`
  * deep copy: `var $target$ = JSON.parse(JSON.stringify($origin$))`
  * Object to Array: `Array.from($target$)` or `Object.values($target$)`

## What I studied myself

* kotlin:
  * official language of Android
  * could either use back-end convert to java or front-end convert to javascript
  * safe with null case
  * concise than java
* kotlin to java: Tools-Kotlin-Show Kotlin Bytecode-Decompile in Intellij
* java to kotlin: Code-Convert Java File to Kotlin File

## What I didn't understand

## What I want to know more

## etc(Additional)

## Practice problems

* [arrays.js](arrays.js) ([view](https://lemontree1729.github.io/coding-academy/courses/javascript/d059/array.html))

## Useful links

* [kotlin](https://kotlinlang.org/)
