class LearnClass:
    count = 0  # class variable(member variable)

    def selfid(self):
        return id(self)  # self variable has same id with instance self

    def selfTest(a, b, c=0):  # python treat a as self!
        print(a, b, c)

    def instanceTest(self):
        self.count += 1  # makes count to instance variable permanantly
        # and increse instance variable value

    def memberTest(self):
        LearnClass.count += 5  # increse class variable value


# class: makes instances
# object:
# instance: made by class
# function:
# method: function only works specific class


## 1. self only works for instance (not even for class itself!)
print("1.")
Class1 = LearnClass()
print(f"LearnClass's id: {id(LearnClass)}")
print(f"Class1's id: {id(Class1)}")
try:
    print(f"LearnClass's self's id: {LearnClass.selfid()}")
except:
    print("LearnClass's self's id: ")
    print("TypeError: selfid() missing 1 required positional argument: 'self'")
    # this occurs because self only works with instance not class!
print(f"LearnClass.sefid(3): {LearnClass.selfid(3)}")
# and self(the first argument) just becomes normal argument
print(f"Class1's self's id: {Class1.selfid()}")
print("\n")


## 2. self is forced to define as methods first parameter
print("2.")
Class1.selfTest(1, 2)
# python even not confused on whether a=1,b=2,c=0 or a=self,b=1,c=2!
# this shows python automatically accept first parameter as self for method (not function!)
try:
    Class1.selfTest(1, 2, 3)
except:
    print(
        "TypeError: selfTest() takes from 2 to 3 positional arguments but 4 were given"
    )  # occurs error! because hello has 4 input parameters self, 1, 2, 3!
print("\n")


## 3. class variable and instance variable
print("3.")
Class2 = LearnClass()
print(f"LearnClass's count: {LearnClass.count}")
print(f"Class1's count: {Class1.count}")
print(f"Class2's count: {Class2.count}")
Class1.memberTest()  # increse class variable value
print(f"LearnClass's count: {LearnClass.count}")  # all same!
print(f"Class1's count: {Class1.count}")
print(f"Class2's count: {Class2.count}")
Class1.instanceTest()  # increase instance variable value
print(f"LearnClass's count: {LearnClass.count}")
print(f"Class1's count: {Class1.count}")  # Class1's count just seperated with others!
print(f"Class2's count: {Class2.count}")
Class1.memberTest()  # increse class variable value
print(f"LearnClass's count: {LearnClass.count}")
print(f"Class1's count: {Class1.count}")  # LearnClass.count doesn't work with Class1!
print(f"Class2's count: {Class2.count}")
