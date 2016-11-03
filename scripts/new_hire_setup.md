# New Hire Setup

You've just got a brand new computer. Here's a few essentials you'll want to get up and running quickly:

## Basic technical skills:

#### Terminal
For the essential terminal commands, check out the [Learn Python The Hard Way appendix](http://learnpythonthehardway.org/book/appendixa.html). You should learn these as a bare minimum.
I would also recommend downloading [iTerm2](https://www.iterm2.com/) to navigate the terminal. Some people also use [ZSH](http://www.zsh.org/).

#### Text Editor
Start learning how to use some text editor. If you are quite new to programming, [Sublime Text](http://www.sublimetext.com/) is popular and very intuitive to use, as well as quick to become decently proficient. [Vim](http://www.vim.org/) and [Emacs](http://www.gnu.org/software/emacs/) are the two most widely used editors, but they each have a bit of a learning curve. Pick one to start and stick with it for awhile before switching.

Regardless of which you pick, it is highly recommended to get a good [linter](https://en.wikipedia.org/wiki/Lint_(software)) for your text editor, specifically one that has [PEP8](https://www.python.org/dev/peps/pep-0008/) support. This may be annoying at first if you are not used to standard coding practice, but it goes miles it terms of making your code more readable for everyone else. 

If you are using sublime, you can install these packages using [sublime package control](https://packagecontrol.io/installation#st2). One you have that, install [SublimeLinter](http://www.sublimelinter.com/en/latest/about.html), sublimelinter-flake8, autopep8, and (if your team uses it) also get [editorconfig](https://github.com/sindresorhus/editorconfig-sublime).

#### Git
Git is used for [this tutorial](https://try.github.io/levels/1/challenges/1) or [this tutorial](http://gitimmersion.com/lab_01.html) to get a feel for the basic commands, and eventually you'll want to [read at least the first 3 chapters to know how Git works](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control).

#### Python
One of the best tutorials is [Learn Python the Hard Way](http://learnpythonthehardway.org/book/). This is especially good if Python is your first language. Getting through around chapter 39 will give you most of the basics you need.

#### SQL
You'll need to know some SQL to do any sort of analysis here. MySQL, PostgreSQL, and Amazon Redshift are all flavors of SQL, and you'll probably want to learn the variety that you'll used most often first. However, [the Khan Academy tutorial](https://www.khanacademy.org/computing/computer-programming/sql) is a simple first intro, and [SQL zoo](http://sqlzoo.net/wiki/SQL_Tutorial) is good for exploring the basic commands as well.


## System Configuration

#### Installing packages
[Homebrew](http://brew.sh/) is a *package manager*, meaning that it installs things you need (along with all the packages they need to run) and keeps track of when they need updates.  
To install, just go to your terminal and run
`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

Homebrew is for Mac OS X, so it gives you extra installations that don't come with by default Apple computers. Most programming languages have their own (probably several) package managers, which install things specific to that language.

Homebrew installs packages all in a specific path, and you'll want to add that to the list of paths your computer looks for (the `PATH` environment variable). To do so, type `cd` to go to your home directory, then type:  
`echo "export PATH=/usr/local/bin:$PATH" > .bash_profile`  
This adds `/usr/local/bin` onto `PATH`

#### Python
To install extra outside packages and libraries for Python, [use pip](https://en.wikipedia.org/wiki/Pip_(package_manager)).  To get this, it is actually easiest to reinstall python using homebrew (even though OS X comes with it pre-installed). This will give us both pip and [setuptools](https://packaging.python.org/en/latest/projects.html#setuptools), which is an additional tool that helps with Python packages.

    brew install python

We'll also want [virtualenv](http://simononsoftware.com/virtualenv-tutorial/), which is a tool in python to help set up separate environments with python packages that won't clash with each other. There are many places to read about what they do and why they are useful. To get it, simply run

    pip install virtualenv

If you get permissions errors, make the `sudo pip install virtualenv`.   

https://pip.readthedocs.io/en/1.1/requirements.html Extra reading on pip and requirements files

#### .bashrc and .bash_profile
These are two files that will run shell commands when you open a terminal window. For the differences between them, [see here](http://www.joshstaiger.org/archives/2005/07/bash_profile_vs.html) [or here](http://unix.stackexchange.com/questions/129143/what-is-the-purpose-of-bashrc-and-how-does-it-work).  

In short, you probably want to only maintain one of these files, so at the top of your `.bash_profile`, you can put:

    if [ -f ~/.bashrc ]; then
       . ~/.bashrc
    fi

And here are some 'nice-to-have's in your `.bashrc`:

    # .bashrc

    # Source global definitions
    if [ -f /etc/bashrc ]; then
      . /etc/bashrc
    fi

    # set PATH so it includes user's private bin if it exists
    if [ -d "/usr/local/bin" ] ; then
        PATH="/usr/local/bin:$PATH"
    fi

    if [ -d "/usr/local/sbin" ] ; then
        PATH="/usr/local/sbin:$PATH"
    fi

    if [ -z "$SSH_AUTH_SOCK" ] ; then
      eval `ssh-agent -s`
    fi

    alias ..='cd ..'
    alias cl='clear'
    alias lm='ls -laxo | more'
    alias rm='rm -i'

    # Git shortcuts
    alias st='git status'
    alias ci='git commit'
    alias gpl='git pull'
    alias gk='git checkout'


If you've used homebrew, you want to include  
    export PATH=/usr/local/bin:$PATH


If you don't use virtualenvwrapper, virtual environment shortcuts are a must:
    # virtual environments
    alias quiz='source ~/envs/quizenv/bin/activate'
    alias watch='source ~/envs/watchtower/bin/activate'

The above assumes you are storing your virtual environments in one place (maybe ~/envs/)

### Common Errors

    ImportError: No module named <SOME OUTSIDE PACKAGE>

The happens when you do not have the package installed. Have you already run `pip install <package>`? If so, are you inside your virtual environment?


    ImportError: No module named <SOME PACKAGE INSIDE YOUR REPO>

This error occurs when you have code set up in different folders and are trying to import something from a different package. ('packages' is the word Python uses for a folder with an `__init__.py` file http://docs.python-guide.org/en/latest/writing/structure/#packages).

If this occurs in some repo often, you should put inside your .bashrc a line like this:

    export PYTHONPATH=/path/to/that/repo:$PYTHONPATH

where `/path/to/that/repo` should change for you.

This will ensure Python knows where to look for your packages inside that repo.

Alternatively, if you just want to be able run your scripts from the root of your repo and have it automatically add your current directory, you can add:

    export PYTHONPATH=".:$PYTHONPATH"

