---
title: 'Raspberry Pi Robot for $100 that sees with Tensor Flow.'
layout: post
categories: articles
redirect_from:
- /tutorials/2016/09/25/rpi/tensorflow
- /articles/2016/09/25/rpi/tensorflow
---
# Raspberry Pi Robot for $100

Coming soon: verifying that you can in fact make this for $100- https://www.oreilly.com/learning/how-to-build-a-robot-that-sees-with-100-and-tensorflow

Problem issue
https://github.com/tensorflow/tensorflow/issues/4680

Not fixed until november https://github.com/tensorflow/tensorflow/pull/5307

Installation:
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/makefile#raspberry-pi
Then
https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/pi_examples#building-the-examples

tensorflow/contrib/makefile/download_dependencies.sh
sudo apt-get install -y autoconf automake libtool gcc-4.8 g++-4.8
cd tensorflow/contrib/makefile/downloads/protobuf/
./autogen.sh
./configure
make
sudo make install
sudo ldconfig  # refresh shared library cache
cd ../../../../..
make -f tensorflow/contrib/makefile/Makefile HOST_OS=PI TARGET=PI \
 OPTFLAGS="-Os -mfpu=neon-vfpv4 -funsafe-math-optimizations -ftree-vectorize" CXX=g++-4.8
sudo apt-get install -y libjpeg-dev
