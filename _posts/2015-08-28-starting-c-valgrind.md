---
title: 'Valgrind on Mac 10.9'
layout: default
---

# Starting Out With C, Valgrind On Mac OS.X 10.9 
https://github.com/fredericgermain/valgrind/

```sh
# Make sure I have autoconf and automake both installed.
brew install automake
brew install autoconf

# Grab Frederic's patched valgrind on his "homebrew" branch
git clone https://github.com/fredericgermain/valgrind/ -b homebrew
cd valgrind

# Because he placed VEX as a git submodule, we have to make sure we clone it too
git submodule init
git submodule update

# Now Valgrind will compile
./autogen.sh
./configure --prefix=/usr/local   # set the stage for sudo make install to place our compiled valgrind binary as /usr/local/bin/valgrind
make
sudo make install
```
