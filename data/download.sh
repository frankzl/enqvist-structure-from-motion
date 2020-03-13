#!/bin/bash

wget http://vision.maths.lth.se/calledataset/orebro/orebro1.zip
mkdir input
mv orebro1.zip input/
cd input
unzip orebro1.zip -d orebro1
