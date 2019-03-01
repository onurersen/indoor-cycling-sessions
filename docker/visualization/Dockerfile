FROM alpine
MAINTAINER Berat Onur Ersen<onurersen@gmail.com>

VOLUME ["/www"]

RUN apk add --no-cache libpng freetype libstdc++ python-dev python py-pip
RUN apk add -U --no-cache --virtual .build-deps \
		linux-headers \
	    gcc \
	    build-base \
	    libpng-dev \
	    musl-dev \
	    freetype-dev \
		musl-dev \
		g++ \
		gcc \
		git \
		curl

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h \
	&& pip install numpy \
	&& pip install matplotlib \
	&& pip install pandas \
	&& apk del .build-deps \
	&& rm -rf /var/cache/apk/*