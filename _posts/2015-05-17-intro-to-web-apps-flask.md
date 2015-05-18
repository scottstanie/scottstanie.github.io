---
title: 'An Introduction to Web Apps With Flask'
layout: default
---

## What is Flask

[Flask](https://github.com/mitsuhiko/flask/) is an example of a Python ***web application framework***. Specifically, it calls itself a *microframework* because it provides less up front. Before we dive in to how to use flask, let's take a step back and look at what a the very basics of how the internet works so you know what a **web application** consists of, and why you'd want to use a **web framework** to make one.


## The Internet in brief
The crux of how the internet works in most sites (in two steps):  
- A client sends a request to visit some website  
- A serve sends back some files to display in the browser  
If you understand that, you can skip to the next section. For slightly more details\*:  

The internet is a global network of computers, each with a specific address. These addresses look something like xxx.xxx.xxx.xxx, x being a number from 0-255.  When you go to your browser and type `www.google.com`, you are sending a Hypertext Transfer Protocol (HTTP\*\*) request that says "Send me the data from the IP address with the name google.com". Then your request goes to a **domain name service** (DNS) which keeps track of the IP address for `google.com`. To see this, type fewuhaof.com, and you will get a DNS error, since there is no address for that gibberish name. Once the DNS gets the address you need, your ISP can send your request to the right computer.  
So if that is all that happens on your end when you type `google.com`, what is the thing that responded on the other end? That is where a **web server** comes in. Once your request to `GET` the data from `google.com` reached the right IP address, it was met by a *server*, which is just a computer located somewhere that is connected to the internet and sits waiting for incoming requests. Once it receives a request like yours (to `GET google.com`), it will send back the files needed to show the Google web page, which are HTML, CSS, and JavaScript files. 

\*[For an even more detailed overview of the internet, see here.](http://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)  
\*\*Note: Don't confuse HTTP with HTML. HTTP is a *protocol*: it gives directions to computers on how to talk to each other over the internet. *HTML* is HyperText Markup Language, which is just text with some directions to a browser on how to display properly like a web page.  



## What is a web app?
Where does a web app come into the picture described above? Once the server has received your request to see a page, it translates the request to the web app to process. Thus, the web app is the program that runs and decides what should be done with every user that visits a website. For simple static websites (ones that just show an HTML page with no user inputs), that program in Python could look as simple as:

    def serve_page():
      return "<html><body>Hello, World.</body></html>"

This function would be called each time a visitor requests the page, and it would send back the barebones HTML to display "Hello, World." A more complicated web app like facebook, would might contain JavaScript to allow interactions between the browser and the user, databases to keep track of prior information about the user, and various other parts.  
Naturally, this examples also ignores a lot of other code that needs to run to accept the request and talk to the server to send back the info. There is a lot of boilerplate code that goes into every application that needs to run on the internet, and this is where web application *frameworks* come in.


### Web application frameworks

So what is a **web application framework**? [As described here](http://www.fullstackpython.com/web-frameworks.html), web frameworks are reusable code libraries that make it easier to build a reliable, scalable, and maintainable web app. They help reuse code common for HTTP operations and for typical application functionality, such as:  
  1. URL routing  
  2. HTML, [XML](http://www.w3schools.com/xml/), [JSON](http://json.org/), and other output format templating  
  3. Database manipulation  
  4. Security against [Cross-site request forgery (CSRF)](http://en.wikipedia.org/wiki/Cross-site_request_forgery) and other attacks  

The various points above will come up as you learn more about Flask, so don't worry if you don't know what any of these mean yet.

To read a little more about frameworks in general, check you this [good tutorial by Jeff Knupp](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/), which contains a good deal of front matter about HTTP servers.


## Actually getting started with Flask
Now that we have the primer with info needed to see how web apps fit into the internet, the best way to start learning what these functions of a framework are for is to see them in action. Let's make the simplest Flask app possible.

#### Installing:
If you're not sure what a virtual environment is, see this [into to virtual environments and the `pip` installer](http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/). Assuming we have Python 2.7 and `pip` installed, start by creating the virtual environment for your project and activate it. I put all my envs in `~/envs/`)\*   I'll call it `myapp`:  
  
    cd ~/envs/ && virtualenv myapp && source ~/envs/myapp/bin/activate
 
Now make a folder where the project will live. Lets call it `myapp` as well:

    mkdir myapp && cd myapp
 
Install Flask:

    pip install flask


\* Note: some people like using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/), which can simplify the creation and management of virtual environments. Whether or not you use the wrapper tool, virtual envs are *strongly* recommended, especially for projects (like websites) that will be run on multiple locations.

#### Our First App

Now we can make a simple web app ([as shown in the Flask quickstart](http://flask.pocoo.org/docs/0.10/quickstart)) by creating a file called `hello.py` and fill it with the following:

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()

If we run `python hello.py`, open a browser, and go to `http://localhost:5000`, we will see our app running and presenting the page with "Hello World!"

#### What is happening here?

So how does this create a web app that is suddenly visible in your browser?

1. First, we make an `Flask` instance, which handles much of the application boilerplate code described above for serving and receiving requests. We pass it the title of the module (`__name__` here) so the app knows where to look for files.  
2. The `@app.route` is a [decorator](https://realpython.com/blog/python/primer-on-python-decorators/) which tells the app what to do for each URL. The only URL we handle here is `/`, the root URL.   
3. The function below the decorator handles all the logic of what to serve, and returns text or HTML  
4. The `app.run()` code tells the `Flask` instance to start, with `if __name__ == "__main__":` being provided to say "only run this if the module is called directly" (i.e., not by an import).  

When you ran this, you saw:
    
    (myapp)Scott:mysite scott$ python hello.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

By default, Flask will run on the localhost, where your local machine acts as a web server. This means that typing `http://localhost:5000` goes through the same steps outlined about, but instead of going to some external server for the site, the browser just looks at what is running on your computer, which is your program, until you press `ctrl-C` to stop it. The `5000` is just another port that a server might go through to reach an application. Port 80 is the usual port for external websites. See the [Internet tutorial link](http://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm) for more info on this.  
So once you visited the root URL of `localhost`, our application received this request, ran the function `hello()` and returned the string `Hello World!`.

#### Routing
We now have a basic output when going to the root level domain (the `/`). How do we handle more routes? Simple: add more decorators. To return the same output for two different routes, we can simply stack the decorators:

    @app.route("/index")
    @app.route("/")
    def hello():
        return "Hello World!"

Now if we visit `http://localhost:5000/index`, we get the same output: Both of these routes receive the same function.  


#### Templates
How do we actually display HTML for our app? Instead of just a text string, we can hve our routing functions return HTML files. We can make a folder called `templates` and put our basic HTML file into it:

    <!doctype html>
    <head>
      <title>My App</title>
    </head>
    <body>
      Hello, World!
    </body>

Add the following import to the top of hello.py:

    from flask import render_template

And now the rendering function can look like this:

    @app.route("/index")
    @app.route("/")
    def hello():
        return render_template('index.html')

We have our first template being rendered.  
These templates can function as reusable layouts in order to minimize duplicated HTML. See http://flask.pocoo.org/docs/0.10/tutorial/templates/ for a further example on it. Try working through the entire tutorial for the info on a full basic functions of a flask app.

Also, [this tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is a very detailed walk through, though slightly outdated.

## Polis Interlude
https://git.adverplex.com/social/polis-templater/tree/scott


### Finally: "Full stack"? 

As alluded to above, the Python application is only one part of the *stack*. You may have heard the term *full-stack* developer get thrown around without knowing what is this stack that they are developing. The stack simply refers to the series of technologies required to build, run, and deploy an app on the internet. The Python program may handle the logic of what to serve each user, but it does not store data, nor does it handle HTTP requests directly. The four major parts of the stack (in the traditional sense) are:
1. The **operating system** running the programs
2. The **web server** handling the incoming requests
3. The **database** for storing all website info
4. The **application language** (i.e. Python)

[For an idea on what some people see as the responsibilities of the "full stack developer", see here](http://www.laurencegellert.com/2012/08/what-is-a-full-stack-developer/)
