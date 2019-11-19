# gopro
openCV with GoPro



# How to compile your opencv on Mac


```
  cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=/Users/frank/cv/opencv_contrib/modules \
    -D PYTHON3_LIBRARY=`python3 -c 'import subprocess ; import sys ; s = subprocess.check_output("python-config --configdir", shell=True).decode("utf-8").strip() ; (M, m) = sys.version_info[:2] ; print("{}/libpython{}.{}.dylib".format(s, M, m))'` \
    -D PYTHON3_INCLUDE_DIR=`python3 -c 'import distutils.sysconfig as s; print(s.get_python_inc())'` \
    -D PYTHON3_EXECUTABLE=/Users/frank/venv/gopro/bin/python3 \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
		-D ENABLE_CXX11=ON \
    -D BUILD_EXAMPLES=ON ..
```

# issues & fix

1. Use `opencv_contrib/modules` instead of `opencv_contrib` for `OPENCV_EXTRA_MODULES_PATH`
2. Set `ENABLE_CXX11` to `ON`
3. if you has `limits.h` not found issue, you should run `brew reinstall gcc`
