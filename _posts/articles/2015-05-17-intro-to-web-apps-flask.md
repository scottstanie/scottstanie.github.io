---
title: 'An Introduction to Web Apps With Flask'
layout: post
categories: articles
redirect_from:
- /tutorials/2015/05/17/intro/to/web/apps/flask
- /articles/2015/05/17/intro/to/web/apps/flask
---
# Web Apps and Flask

This is intended to be a overview of a wide variety of topics related to web applications and some needed prerequisite knowledge. There's also a very brief walkthrough on how to get started with Flask, as well as plenty of links along the way to learn more and find a full Flask tutorial.  
Target demo: people with some programming experience but with little to no web programming experience, or just generally tech-savvy people.

## What is Flask

[Flask](https://github.com/mitsuhiko/flask/) is an example of a Python [***web application framework***](http://en.wikipedia.org/wiki/Web_application_framework). Specifically, it calls itself a *microframework* because it provides less up front. Before we dive in to how to use flask, let's take a step back and look at what a the very basics of how the internet works so you know what a **web application** consists of, and why you'd want to use a **web framework** to make one.


## The Internet In Brief
The crux of how the internet works in most sites (in two steps):  
- A client sends a request to visit some website  
- A serve sends back some files to display in the browser  

If you understand that, you can skip to the next section. 

The internet is a global network of computers, each with a specific address. These addresses look something like xxx.xxx.xxx.xxx, x being a number from 0-255.  
![](http://1.bp.blogspot.com/-gTRV25VTdb8/T55rvji6cEI/AAAAAAAACXM/9clbBo-y0nY/s1600/dnslookups.png)  

When you go to your browser and type `www.google.com`, you are sending a Hypertext Transfer Protocol (HTTP\*) request that says "Send me the data from the IP address with the name google.com". Then your request goes to a **domain name service** (DNS) which keeps track of the IP address for `google.com`. To see this, type fewuhaof.com, and you will get a DNS error, since there is no address for that gibberish name. Once the DNS gets the address you need, your ISP can send your request to the right computer.  

So if that is all that happens on your end when you type `google.com`, what is the thing that responded on the other end? That is where a **web server** comes in. Once your request to `GET` the data from `google.com` reached the right IP address, it was met by a *server*, which is just a computer located somewhere that is connected to the internet and sits waiting for incoming requests. Once it receives a request like yours (to `GET google.com`), it will send back the files needed to show the Google web page, which are HTML, CSS, and JavaScript files.  

To see a `request`/`response` exchange in action, open up your terminal, and type `curl -v scottstanie.github.io`. Among other things, you'll see:

    * Connected to scottstanie.github.io (199.27.75.133) port 80 (#0)
    > GET / HTTP/1.1
    > User-Agent: curl/7.30.0
    > Host: scottstanie.github.io
    > Accept: */*
    >
    < HTTP/1.1 200 OK
    ...

This is the equivalent of going to your browser to visit this website, but all HTTP requests and server responses will print out in the terminal, as well as all the HTML and CSS files returned. The `GET / HTTP/1.1` you'll see is the beginning of the request, and the `HTTP/1.1 200 OK` starts the response.

\*Note: Don't confuse HTTP with HTML. HTTP is a *protocol*: it gives directions to computers on how to talk to each other over the internet. *HTML* is HyperText Markup Language, which is just text with some directions to a browser on how to display properly like a web page.  



## What is a web app?
Where does a web app come into the picture described above? Once the server has received your request to see a page, it translates the request to the web app to process. Thus, the web app is the program that decides what should be done with every user that visits a website. For simple static websites (ones that just show an HTML page with no user inputs), that program in Python could look as simple as:

    def serve_page():
      return "<html><body>Hello, World.</body></html>"

This function would be called each time a visitor requests the page, and it would send back the barebones HTML to display "Hello, World." A more complicated web app like Facebook, would might contain JavaScript to allow interactions between the browser and the user, databases to keep track of prior information about the user, and various other parts.  

Naturally, this examples also ignores a lot of other code that needs to run to accept the request and talk to the server to send back the info. There is a lot of boilerplate code that goes into every application that needs to run on the internet, and this is where web application *frameworks* come in.


### Web application frameworks

So what is a **web application framework**? [As described here](http://www.fullstackpython.com/web-frameworks.html), web frameworks are reusable code libraries that make it easier to build a reliable, scalable, and maintainable web app. They help reuse code common for HTTP operations and for typical application functionality, such as:  
  1. URL routing  
  2. Templating for HTML, [XML](http://www.w3schools.com/xml/), [JSON](http://json.org/), and other output formats  
  3. Database manipulation  
  4. Security against [Cross-site request forgery (CSRF)](http://en.wikipedia.org/wiki/Cross-site_request_forgery) and other attacks  

The various points above will come up as you learn more about Flask, so don't worry if you don't know what any of these mean yet. However, these points clearly do not cover all that is necessary to make a fully functioning website. So where does the rest of the *stack* come from?


### "Full stack"? 

You may have heard the term *full-stack* developer get thrown around without knowing what is this stack that they are developing. The stack simply refers to the **layers of technologies** required to build, run, and deploy an app on the internet. The Python program may handle the logic of what to show each user, but it does not store data, nor does it handle HTTP requests directly. The four major parts of the stack (in the traditional sense) are:  

1. The **operating system** running the programs  
2. The **web server** handling the incoming requests  
3. The **database** for storing all website info  
4. The **application language** (i.e. Python)  

Setting up #1-3 for your web app will not be covered here, as they are necessary once you have a handle on making a simple app and want to expand, scale, and deploy it.


# Actually getting started with Flask
Now that we have the primer with info needed to see where web apps fits into the internet, the best way to start learning what a framework does is to see it in action. Let's make the simplest Flask app possible.

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
How do we actually display HTML for our app? Instead of just a text string, we can have our routing functions return HTML files. We can make a folder called `templates` and put our basic HTML file into it:

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

To see how these templates can be reusable, check out [the Flask tutorial part on templating](http://flask.pocoo.org/docs/0.10/tutorial/templates/).  

#### Doing More
This is not intended to be a full tutorial on making a Flask app, as there have already been many good ones written. If you really want to get a grasp on Flask, [the site's own tutorial is quite good](http://flask.pocoo.org/docs/0.10/tutorial/). Working through the entire tutorial should give a feel of the basic functions of a flask app. Also, check out [the rest of the patterns in their docs on best practices](http://flask.pocoo.org/docs/0.10/patterns/). If their tutorial is not enough, there are plenty of other [full Flask tutorials](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/#.VVqLOlVVikq) out there, as well as [info on structuring apps](http://mattupstate.com/python/2013/06/26/how-i-structure-my-flask-applications.html).


### More Reading
[For an even more detailed overview of the internet, see here.](http://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)  

More about frameworks in general: [a good tutorial by Jeff Knupp](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/), containing quite a bit of front matter about HTTP servers.


[For an idea on what some people see as the responsibilities of the "full stack developer", see here](http://www.laurencegellert.com/2012/08/what-is-a-full-stack-developer/)

[This tutorial by Miguel Grinberg](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) is a very detailed walk through, though slightly outdated at this point.