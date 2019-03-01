FROM alpine:3.6

MAINTAINER Berat Onur Ersen<onurersen@gmail.com>

ENV OPENCV_LIB https://github.com/opencv/opencv/archive/3.3.0.tar.gz
ENV OPENCV_LIB_VER 3.3.0
ENV PYPA_PIP https://bootstrap.pypa.io/get-pip.py
ENV CC /usr/bin/clang
ENV CXX /usr/bin/clang++
ENV TESSERACT_TRAINED_DATA https://raw.githubusercontent.com/tesseract-ocr/tessdata/master/eng.traineddata

RUN apk add -U --no-cache --virtual=build-deps \
    linux-headers \
	libgcc \
	libxml2-dev \
	libxslt-dev \
	libffi-dev \
	lcms2-dev \
	python3-dev \
	g++ \
	openssl-dev \
	jpeg-dev \
	freetype-dev \
	build-base \
	openjpeg-dev \
	musl-dev \
	make \
	cmake \
	ninja \
	clang \
	clang-dev \
	zlib-dev 
	
RUN apk add --no-cache \
	python3 \
	gcc \
	libxml2-dev \
	libxslt-dev \
	libffi-dev \
	libjpeg \
	tesseract-ocr \
	jpeg \
	musl \
	freetype \
	openjpeg \
	ninja \
	curl \
	zlib 
	
RUN curl $PYPA_PIP | python3
RUN ln -s /usr/bin/python3 /usr/bin/python 
RUN curl $TESSERACT_TRAINED_DATA -o /usr/share/tessdata/eng.traineddata 
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h 
RUN pip install -U --no-cache-dir Pillow pytesseract numpy

RUN mkdir /opt && cd /opt && \
	curl -L $OPENCV_LIB | tar zx && \
    cd opencv-$OPENCV_LIB_VER && \
    mkdir build && cd build && \
	cmake -G Ninja \
          -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/usr/local \
          -D WITH_FFMPEG=NO \
          -D WITH_IPP=NO \
          -D PYTHON_EXECUTABLE=/usr/bin/python \
          -D WITH_OPENEXR=NO .. && \
    ninja && ninja install && \
    ln -s /usr/local/lib/python3.6/site-packages/cv2.cpython-36m-x86_64-linux-gnu.so \
          /usr/lib/python3.6/site-packages/cv2.so && \
    apk del build-deps && \
    rm -rf /var/cache/apk/*