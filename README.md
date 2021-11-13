# Sightpy Weekend Raytracer

This raytracer is a versatile implementation of [Peter Shirley Ray Tracing in One Weekend Book Series](https://raytracing.github.io/) which uses Python as the interface for the scene description.

The Python interface and coding-style is based on [sightpy](https://github.com/rafael-fuente/Python-Raytracer) , my successful, readable, and easy-to-use Python raytracer. But unlike it, the core of this raytracer is written in C++ and therefore focuses in rendering the scenes as fast as possible. Also, it features multithreading.

## Installation

Just clone or download this repo and run:
```
python setup.py install
```
You need to have a C++ compiler installed on your computer in order to run this command successfully.

## Examples

See the examples to see how to render the following images:

```
python example1.py
```

![N|Solid](/images/example1.png)

```
python example2.py
```

![N|Solid](/images/example2.png)