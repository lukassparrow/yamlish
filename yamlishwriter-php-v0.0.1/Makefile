# Makefile for YAMLish

PHP      = /usr/bin/php
PROVE    = prove -r t

VERSION  = 0.0.1
DISTNAME = yamlishwriter-php-v$(VERSION)

default:

test:
	PHP=$(PHP) $(PROVE)

dist: manifest
	./dist.sh $(DISTNAME)

manifest:
	rm -f MANIFEST
	find . -type f | grep -vE '\.svn|\.DS_Store|\.tmproj' > MANIFEST
	echo './MANIFEST' >> MANIFEST
	