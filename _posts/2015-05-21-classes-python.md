---
title: Classes in Python
layout: default
---

# Classes in Python

First, what is a class?  
A class is simply a logical grouping of data and functions, where the functions are called *methods* of the class. They are really a modelling technique used in the organization of programs, which falls under ***object oriented programming (OOP)***.  
In python, [everything is an **object**](https://pythoninternal.wordpress.com/2014/08/11/everythings-an-object/), and defining a class is defining a blueprint for creating objects.  


### Object Oriented Terminology
First, let's go over the basic terms used in OOP.  

- **Class**: A user-defined *prototype* for an object that defines a set of attributes that characterize any object of the class. The attributes are **data members** (class variables and instance variables) and **methods**, accessed via dot notation.

- **Class variable**: A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

- **Data member**: A class variable or instance variable that holds data associated with a class and its objects.

- **Function** overloading: The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

- **Instance** variable: A variable that is defined inside a method and belongs only to the current instance of a class.

- **Inheritance**: The transfer of the characteristics of a class to other classes that are derived from it.

- **Instance**: An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

- **Instantiation**: The creation of an instance of a class.

- **Method** : A special kind of function that is defined in a class definition.

- **Object**: A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.

- **Operator overloading**: The assignment of more than one function to a particular operator.


## Why use classes?
Programming using OOP is really just a preference- [there are other paradigms] (http://cs.lmu.edu/~ray/notes/paradigms/) that can accomplish the same thing, some being better suited to certain problems than others. OOP can make problems conceptually easier to understand and visualize, [even there are some strong opinions against it](http://c2.com/cgi/wiki?ArgumentsAgainstOop). You can accomplish the same thing by using module-level (global) variables, but globals in general are a bad idea.


### Defining your own class
Let's give a basic definition of a class:

{% highlight python %}
class Employee:
    '''Common base class for all employees'''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
     
    def printSelf(self):
        return "Name : %s, Salary: %s" % (self.name, self.salary)
{% endhighlight %}



The variable empCount is a **class variable** whose value is shared among **all instances** of a this class. This can be accessed as `Employee.empCount` from inside the class or outside the class.

The first method `__init__()` is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.

You declare other class methods like normal functions with the exception that the first argument to each method is self.  You do not need to include it when you call the methods. If you make an instance `employee = Employee('scott', '10000')`, then calling `employee.printSelf()` implicitly adds the self to the argument list.



#### `__str__` and `__repr__`
OOP has uses in most languages, but Python has some pecularities in its class implementation.

- The goal of `__str__` is to be readable  
- The goal of `__repr__` is to be unambiguous  

As an example, you might have this for a game board class:

{% highlight python %}
class BoardState(object):
    def __init__(self,
            pieces=(0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0,
                0, 0, 0, 0,)):
        self.pieces = pieces

{% endhighlight %}
If you initialze an object, it will be represented like this:

{% highlight python %}
In [1]: bs = BoardState()

In [2]: bs
Out[2]: <__main__.BoardState at 0x10b3c22d0>
{% endhighlight %}

Using `print` yeilds the same results. This is because it is using the default `__repr__` method. (which also is the default `__str__` method). It is *unambiguous* because it tells you exactly where it is in memory. However, you might want a little more detail about what is in the class.

{% highlight python %}
    def __repr__(self):
        return "%s with pieces %s" % (self.__class__, self.__dict__)
{% endhighlight %}
Now you would see:

{% highlight python %}
In [2]: bs
Out[2]: <class __main__.BoardState> with pieces {'pieces': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)}
{% endhighlight %}

However, this is still ugly on sight. To really visualize it, you might define something like this:

{% highlight python %}
    def __str__(self):
        all_str = ''
        for row_idx in range(4):
            row = self.pieces[4*row_idx: 4*(row_idx + 1)]
            str_row = ' '.join(str(item) for item in row)
            all_str += str_row + '\n'
        return all_str
{% endhighlight %}

Now when we print, it looks like this:

{% highlight python %}
In [3]: print bs
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
{% endhighlight %}


*For a detailed explanation of `__repr__` vs `__str__`, [see here](http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python)

#### Other private methods of a class (string example)

{% highlight python %}
In [27]: t = 'foo'
In [29]: t.__
t.__add__           t.__format__        t.__gt__            t.__mod__           t.__repr__          t.__subclasshook__
t.__class__         t.__ge__            t.__hash__          t.__mul__           t.__rmod__
t.__contains__      t.__getattribute__  t.__init__          t.__ne__            t.__rmul__
t.__delattr__       t.__getitem__       t.__le__            t.__new__           t.__setattr__
t.__doc__           t.__getnewargs__    t.__len__           t.__reduce__        t.__sizeof__
t.__eq__            t.__getslice__      t.__lt__            t.__reduce_ex__     t.__str__
{% endhighlight %}

__lt__, __le__, __eq__, __ne__, __gt__ and __ge__: Called to compare the object with another object. These will be called if defined, otherwise Python will fall-back to using __cmp__.
__call__: Lets an object be "called" e.g. so that you can write things like this: obj(arg1,arg2,...).
Python also lets you define methods that let an object act like an array (so you can write things like this: `obj[2] = "foo"`), or like a numeric type (so you write things like this: `print(obj1 + 3*obj2)`.


### Special Attributes of Python Classes
Special attributes:  

- `__name__` is the class name; 

- `__module__` is the module name in which the class was defined; 

- `__dict__` is the dictionary containing the class’s namespace; 

- `__bases__` is a tuple (possibly empty or a singleton) containing the base classes, in the order of their occurrence in the base class list;

- `__doc__` is the class’s documentation string, or None if undefined.


## Overloading methods
If your class has a special way you want to perform a builtin operation- say, addition- then you can explicitly define that and override it for your class:

{% highlight python %}
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

>> Vector (7, 8)
{% endhighlight %}

## Class Methods vs Instance Methods

{% highlight python %}
class Employee:
    '''Common base class for all employees'''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def __str__(self):
        return "Name : %s, Salary: %s" % (self.name, self.salary)

    @classmethod
    def displayCount(self):
        print "Total Employees: %d" % Employee.empCount
{% endhighlight %}


## Inheritance
`super` method


### The @property method
Used to define setters and getters of class attributes. For example,

{% highlight python %}
@property
def audience_selected(self):
    return self.counters['audience']['selected'].get()
{% endhighlight %}

This, being part of a class, now allows us to call `self.audience_selected`. That will then call this function unstead of just having some number stored there. If we wrote

{% highlight python %}
@audience_selected.setter
def audience_selected(self, value):
    self.counters['audience']['selected'].set(value)
{% endhighlight %}

We would have a setter for `self.audience_selected = value`

{% highlight python %}
class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
{% endhighlight %}
    
