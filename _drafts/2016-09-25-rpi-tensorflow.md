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

other tips:
sshing without password: http://stackoverflow.com/a/9386143/4174466

Test camera:


    import picamera
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.capture('img.jpg')


    pi@raspberrypi:~ $ cd tensorflow/
    pi@raspberrypi:~/tensorflow $ tensorflow/contrib/pi_examples/label_image/gen/bin/label_image --image="/home/pi/img.jpg"
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:144] Loaded JPEG: 720x480x3
    W tensorflow/core/framework/op_def_util.cc:332] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:378] Running model succeeded!
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] laptop (228): 0.76845
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] notebook (552): 0.222748
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] mouse (511): 0.00354489
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] desktop computer (550): 0.000468951
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] computer keyboard (543): 0.000426971


Install streaming: http://elinux.org/RPi-Cam-Web-Interface

Running ./start.sh
Finally!!

    pi@raspberrypi:~/tensorflow $ time tensorflow/contrib/pi_examples/label_image/gen/bin/label_image --image="/dev/shm/mjpeg/cam.jpg"
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:144] Loaded JPEG: 512x288x3
    W tensorflow/core/framework/op_def_util.cc:332] Op BatchNormWithGlobalNormalization is deprecated. It will cease to work in GraphDef version 9. Use tf.nn.batch_normalization().
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:378] Running model succeeded!
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] laptop (228): 0.153317
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] notebook (552): 0.115842
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] cowboy hat (881): 0.0539073
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] potter's wheel (566): 0.0360643
    I tensorflow/contrib/pi_examples/label_image/label_image.cc:272] clog (979): 0.0253038
