# 21/11/22 JavaScript lesson

## What I learned(Important)

* What is DOM?
  * Document Object Model
  * Make each HTML's tag as object
* [DOM CRUD(create, read, update, delete) in JavaScript](app.js)
  * create: `document.createElement('$tag-name$')`
  * read: `$target-parent$.querySelector('$css-selector$')` to select one(first) element
    * to select all, use querySelectorAll. this will return Array-like objects
    * be prevent greediness of querySelectorAll, use `:scope` selector
  * update: `$target$.$attribute-to-change$ = $attribute-value$`
  * delete: `$target$.remove()` or `$parent-of-target$.removeChild($target$)`

## What I studied myself

## What I didn't understand

## What I want to know more

## etc(Additional)

## Practice problems

* [practice1.js](practice1.js)
* [practice2.js](practice2.js)

## Useful links
