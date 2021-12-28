# 21/10/18 html, css lesson
 
## What I learned(Important)

* (file) display.html : difference of inline, inline-block, block in display tag and float tag
  * inline : act as letter. if you define size more than contents, outer part just goes to padding.
  * inline-block : act as letter. but can define sertain width and height.
  * block : act as full-viewpoint-width box. if you define size, left width just goes to margin.
  * float : similar with inline-block but cant text-align.  
  you should give margin with child or padding with parent.  
  and parent can't recognize size of float object, you should give overflow: hidden to parent
    > the exact mechanism is parent don't know exact float child's position
* Responsible web
  * Used when we want to match all devices that have different viewpoints.
  * type below in \<head> and it will give you information of device width

    ```html
    <meta name="viewport" content="width=device-width, inital-scale=1.0" />
    ```

  * using @media(media quarry), set max-width as @media (max-width: ???px)
    * [more informations](https://nykim.work/84)

## What I studied myself

## What I didn't understand

## What I want to know more

## etc(Additional)

* [great site to understand what is responsive web](ttps://www.samsungsds.com/kr/company/overview/about_comp_over.html)

## Practice problems

* [quiz.html](quiz.html)
