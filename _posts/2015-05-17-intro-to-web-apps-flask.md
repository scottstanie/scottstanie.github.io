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

This function would be called each time a visitor requests the page, and it would send back the barebones HTML to display "Hello, World."  
Naturally, this examples ignores a lot of other code that needs to run to accept the request and talk to the server to send back the info. There is a lot of boilerplate code that goes into every application that needs to run on the internet, and this is where web application *frameworks* come in.


### Web application frameworks

So now what is a **web application framework**? [As described here](http://www.fullstackpython.com/web-frameworks.html), web frameworks are reusable code libraries that make it easier to build a reliable, scalable, and maintainable web app. They help reuse code common for HTTP operations


#### Extra web app and web framework resources

[Brief on web frameworks](http://www.fullstackpython.com/web-frameworks.html)  
[Good tutorial on web frameworks](http://www.jeffknupp.com/blog/2014/03/03/what-is-a-web-framework/)

### "Full stack"? 

## Actually getting started with Flask

#### Installing:
[Virtual environments and the `pip` installer](http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/)

