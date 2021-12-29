# 21/11/05 $lesson-name$

## What I learned(Important)

### Inheritance

* how to declare
    * when A is super class and B is subclass:

  ```java
  $class B extends A{
    (codes);  
  }
  ```

    * when you declare B, A automatically declared first!

* Inheritance and Access modifier
    * top-level class should have public or default access modifier
    * class that has same named with file can only use public access modifier
    * you can only inheritance public class
    * if super class is in same package : you can access to public, protected and default members
    * if super class is in different package : you can only access to public and protected members

* Inheritance and constructor
    * If there is no request in subclass's constructor for super class's constructor, interpreter just select default
      constructor(no input parameter) of super class
    * If you want to choose super class's constructor, you can use `super($parameter1$,...)` at the first of subclass's
      target constructor declare code

* Upcasting and Down casting
    * Upcasting: assign subclass -> super class
      > `$super-class-name$ $variable-name$ = $sub-instance-name$;`  
      >`$super-class-name$ $variable-name$ = new $sub-class-name$;`
    * Down casting: assign super class -> subclass
      > `$sub-class-name$ $variable-name$ = ($sub-class-name$) $super-instance-name$;`
  > for simple, Upcasting is same as covering information. whenever member is not override, subclass acts like superclass first declared with constructor.
  > And Down casting is unveiled for subclass declare that was already covered before.  
  > So, you can't downcast to subclass that doesn't declare before(has no information(member) for that subclass)  
  > Most importantly, covering upper I said doesn't mean actual data differential(losing or gaining).  
  > whether you cast or not, the declared instance's information never changes

## What I studied myself

* pointer
    * pointer operator
        * how to use: \*$address$ -> show address's value
    * reference operator
        * how to use: &$variable-name$ -> show variable's address
    * pointer variable : It's value equals target's address
        * declare : `$target-type$* $variable-name$ = nullptr` or `$target-type$* $variable-name$ = $target-address$`
      > important! pointer operator in pointer type declare doesn't work actually(doesn't think variable as address). It just shows this type is pointer type
    * reference variable: It's address equals target's address
        * declare : `$target-type$& $variable-name$ = $target-variable$`
      > Same as pointer variable, & after type doesn't do anything except announcing this is reference type

## What I didn't understand

* When we make subclass, superclass also made. Then how reference variable merge both class?  
  or do they make 2 reference variables at once?
* How superclasses constructor defines parameter?(Solved)

## What I want to know more

## etc(Additional)

* [how to parse string to int](https://stackoverflow.com/questions/194465/how-to-parse-a-string-to-an-int-in-c/6154614#6154614)
    * `std::stoi($string-variable$)`

## Practice problems

## Useful links

<https://stackoverflow.com/questions/18446171/how-do-compilers-assign-memory-addresses-to-variables>
