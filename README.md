Cafe lentique is a tool set for making lenticular and bareer filter 3D and
animated images.

Currently available command line tools are:

**interlacer.py**
takes sequence of images and interleaves them.
Vertical strips.

**cropper.py**
takes sequence of alligned images taken by horizontally moved camera,
calculates gradually increasing offset and cuts each image to match
the window.

Future plans:
* gui with minimal dependencies and max cross-platform coverage
* row-by-row processing
* multi threaded processing
* teapot-friendly installation
* 2D-3D convertor
* pitch test producer

# Dependencies

**python3**

  virtualenv env -p python3
  . env/bin/activate.sh

**pillow**

  pip install -r require
