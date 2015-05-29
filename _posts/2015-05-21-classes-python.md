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

- **Class**: A user-defined *prototype* for an object that defines a set of features that characterize any object of the class. The features are **data members** (class variables and instance variables) and **methods**, accessed via dot notation.

- **Attribute**: A class variable or instance variable that holds data associated with a class and its objects.
  - Note that in OOP terminology,  "attributes", "fields", and "variables" are often used interchangeably.

- **Method**: A special kind of function that is defined in a class definition.

- **Member**: A term to describe either class methods or attributes

- **Instance**: An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

- **Instantiation**: The creation of an instance of a class.

- **Instance variable**: A variable that is defined inside a method and belongs only to the current instance of a class.

- **Class variable**: A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

- **Inheritance**: The transfer of the characteristics of a class to other classes that are derived from it.

- **Object**: A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.


## Why use classes?
Programming using OOP is really just a preference- [there are other paradigms] (http://cs.lmu.edu/~ray/notes/paradigms/) that can accomplish the same thing, some being better suited to certain problems than others. [While there are some strong opinions against it,](http://c2.com/cgi/wiki?ArgumentsAgainstOop) OOP can make some problems conceptually easier to understand and visualize. Among the things that using classes do for you:  

- Provide a logical grouping of functions  
- Allow you to share data for these functions to use  
- Provide a [namespace](http://en.wikipedia.org/wiki/Namespace) for these functions and data attributes  
- Structure programs to provide more reusable code
- Allows you to add new features to existing code
  - This point more apparent after seeing what a **subclass** is


You can accomplish the some of these things by using modules (specifically the namespace benefit), but using global variables, especially across code that will be shared and reused widely, is a bad idea. [More on why OOP is useful](http://inventwithpython.com/blog/2014/12/02/why-is-object-oriented-programming-useful-with-an-role-playing-game-example/)


### Defining your own class
Let's give a basic definition of a class:

{% highlight python %}
class Employee(object):
    '''Common base class for all employees'''

    def __init__(self, name=None, salary=10000):
        self.name = name
        self.salary = salary
     
    def print_self(self):
        return "Name : %s, Salary: %s" % (self.name, self.salary)

{% endhighlight %}


The first method `__init__()` is a special method, which is called the **class constructor** or **initialization method**. Python calls this when you create a new instance of this class: `employee = Employee()`. This method essentially first creates an empty `Employee` object, which gets passed as the `self` to the `__init__` method to be initialized. 

After initialization, you access class and instance methods with dot notation: `employee.name = 'Scott'`. To specify the name and salary of the employee right away, you use `employee = Employee('Scott', '10000')`. 

You declare other class methods like normal functions with the exception that the first argument to each method is `self`.  You do not need to include it when you call the methods. If you make an instance then calling `employee.print_self()` implicitly adds the self to the argument list. The function has access to all properties of that instance (`name` and `salary` above) as well as all **class variables**.

### Class variables

We can also add data to a class that will be shared among **all** instances created:

{% highlight python %}
class Employee(object):
    '''Common base class for all employees'''
    employee_count = 0

    def __init__(self, name=None, salary=10000):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
     
    def print_self(self):
        print "Name : %s, Salary: %s" % (self.name, self.salary)
{% endhighlight %}

The variable `employee_count` can be accessed inside the class or outside the class. This means you can call `employee.employee_count`, as you can for any normal class attribute, *or* `Employee.employee_count`, where the second is only true of class variables.


### Class methods vs instance methods

Similar to class variables, you can also define **class methods**:

{% highlight python %}
class Employee(object):
    '''Common base class for all employees'''
    employee_count = 0

    def __init__(self, name=None, salary=10000):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
   
    def print_self(self):
        print "Name : %s, Salary: %s" % (self.name, self.salary)

    @classmethod
    def display_count(self):
        print "Total Employees: %d" % Employee.employee_count
{% endhighlight %}

This can be accessed by the instance like a normal method or by calling `Employee.display_count`. Note that once you have defined a class, you can call this method *before any instances are created*.


## Inheritance

The real usefulness of classes come in when you get into **inheritance**. This is where you take a preexisting class make a **subclass** or **derived class* from it:

{% highlight python %}
class Analyst(Employee):
    '''Subclass of the Employee'''
    def __init__(self, name=None, salary=20000):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def speak_analyst(self):
        print "Let's make some graphs"

{% endhighlight %}

Notice that now instead of `object` as the argument passed to the class name, it's the base class `Employee` (`object` is used as Python makes a switch from older Python classes to 'new-style' classes. [See here for more](http://stackoverflow.com/questions/4015417/python-class-inherits-object))  
This `Analyst` class has an init function and only defines one new method, `speak_analyst`. However, because it inherited from `Employee`, it inherits *all methods from it as well*. This means that the following are all valid:

{% highlight python %}
>>> e = Employee(name='Sam')
>>> e.salary
10000
>>> e.employee_count
1

>>> a = Analyst(name='Scott', salary=30000)
>>> a.speak_analyst()
Let's make some graphs
>>> a.salary
30000 
>>> a.employee_count
2
>>> e.employee_count
2

{% endhighlight %}

Notice both the shared methods from the base class *and* the chared class attribute, `employee_count` that works from an `Analyst` instance. Also note that the new `Analyst` increased the `employee_count` of both `Employee` and `Analyst`. This however can be a dangerous way to implement shared data, as directly changing this attribute on an instance can cause it to lose track of the `employee_count` when others are created (it has overwritten the class attribute.)

Since the two classes above have the same `__init__` methods, we can shorten the `Analyst` definition a bit:

{% highlight python %}
class Analyst(Employee):
    '''Subclass of the Employee'''
    def __init__(self, name=None, salary=20000):
        Employee.__init__(self, name, salary)

    def speak_analyst(self):
        print "Let's make some graphs"

{% endhighlight %}

There is also a `super` method which can provide an alternate syntax (which becomes even cleaner in Python 3):

{% highlight python %}
class Analyst(Employee):
    '''Subclass of the Employee'''
    def __init__(self, name=None, salary=20000):
        super(Analyst, self).__init__(name, salary)

    def speak_analyst(self):
        print "Let's make some graphs"
{% endhighlight %}

This will do the exact same thing as the previous `Employee.__init__(...)` above. The use of `super` does not really come in until you start using **multiple inheritances**, where a single class is subclassed from two parent classes. [Read more about `super` here.](http://www.artima.com/weblogs/viewpost.jsp?thread=236275)

### Overloading methods

In OOP, **function overloading** is the assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.  
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



## Python-specific Class Features

OOP has uses in most languages, but Python has some pecularities in its class implementation.

### Public and Private Methods

In other languages, methods and member variables can be marked as **public** or **private**. Public methods can be called and public member variables can be set by any code, inside or outside of the class. Private methods can be called and private member variables can be set only by code inside the object's own class. 

The purpose of this is to allow the class to be something presented with a specific set of functions and attributes, and only have those be available to the user. These are the public methods. The private methods are anything that the designer of the class needs to make the public methods work properly. The user does not need to know *how* the public methods are implement, just that the *do* work exactly as described. Since good programming practice says to keep functions short and specific, breaking out complicated public methods into smaller private methods can make things logically simpler.

In Python, unlike other languages, no method is *fully* private. you may have seen methods start with a double underscore `__`. 

For example, at the bottom of many modules, you may see:

{% highlight python %}
if __name__ == '__main__':
    main()
{% endhighlight %}

This means that when the module is run directly (typing `python module.py`), the variable `__name__` will be set to `__main__` (as opposed to if the module is imported, in which case `__name__` will be the module you are importing into.)

These double underscore methods are (some of) the 'private' methods of an object. However, these methds are always visible to the user. If you type:

{% highlight python %}
>>> t = 'foo'
{% endhighlight %}

then type `t.__` and hit tab into iPython, you'll get all the `__` methods:

{% highlight python %}
>>> t.__
t.__add__           t.__format__        t.__gt__            t.__mod__           t.__repr__          t.__subclasshook__
t.__class__         t.__ge__            t.__hash__          t.__mul__           t.__rmod__
...
{% endhighlight %}

You can also see all methods (public and private) of an object with:
{% highlight python %}
[method for method in dir(object) if callable(getattr(object, method))]
{% endhighlight %}

Even though all methods are visible, it's still useful when creating classes to use private, or at least 'internal', methods. [The style convention](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) is to use a single underscore as a weak "internal use" indicator:


The leading and trailing double underscores in a Python `__method__` is described by the style guide as:

    ... "magic" objects or attributes that live in user-controlled namespaces. E.g. __init__ , __import__ or __file__ . Never invent such names; only use them as documented.'

[This SO answer describes the difference between the single and double underscore methods](http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python), and ['name mangling' is described here.](https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references)


### `__str__` and `__repr__`

Both of these methods are built into classes, and both do some kind of 'printing'.

- The goal of `__str__` is to be readable  
- The goal of `__repr__` is to be unambiguous  

As an example, you might have this for a 4x4 game board class:

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
>>> bs = BoardState()
>>> bs
<__main__.BoardState at 0x10b3c22d0>
{% endhighlight %}


Using `print` yeilds the same results. This is because it is using the default `__repr__` method. (which also is the default `__str__` method). It is *unambiguous* because it tells you exactly where it is in memory. However, you might want a little more detail about what is in the class.

{% highlight python %}
    def __repr__(self):
        return "%s with pieces %s" % (self.__class__, self.__dict__)
{% endhighlight %}
Now you would see:

{% highlight python %}
>>> bs
<class __main__.BoardState> with pieces {'pieces': (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)}
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
>>> print bs
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
{% endhighlight %}

The `Employee` class above could have also implemented its `print_self` method as its `__str__` in order to call `print employee`:

{% highlight python %}
class Employee(object):
    ...
    def __str__(self):
        return "Name : %s, Salary: %s" % (self.name, self.salary)
{% endhighlight %}

*For a detailed explanation of `__repr__` vs `__str__`, [see here](http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python)

#### Other private methods of a class (string example)

{% highlight python %}
>>> t = 'foo'
>>> t.__
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




### The @property method
This is used to define setters and getters of class attributes. For example,

{% highlight python %}
@property
def audience_selected(self):
    return self.counters['audience']['selected'].get()
{% endhighlight %}

This now allows us to call `self.audience_selected`, which is easier to call than the double nested call in the method. If we wrote

{% highlight python %}
@audience_selected.setter
def audience_selected(self, value):
    self.counters['audience']['selected'].set(value)
{% endhighlight %}

We would have a setter for `self.audience_selected = value`

Another example, where the `temperature` attribute is protected from ill-advised tampering by a user:

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
    
Now the user cannot set a temperature below -273, or they will et a `ValueError`.

## Final Notes

This was meant as an overview to many different parts of classes in Python. Since object oriented design is a very large field of study, learning to implement good classes in programs takes time, and often comes only after learning about other languages which use OOP principles.
