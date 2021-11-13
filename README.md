# Sightpy Weekend Raytracer

This Monte Carlo raytracer (path tracer) is a versatile implementation of [Peter Shirley Ray Tracing in One Weekend Book Series](https://raytracing.github.io/) which uses Python as the interface for the scene description.

The Python interface and coding-style is based on [sightpy](https://github.com/rafael-fuente/Python-Raytracer) , my readable, and easy-to-use Python raytracer. But unlike it, the core of this raytracer is written in C++ and therefore focuses in rendering the scenes as fast as possible. Also, I implemented multithreading, so the images are efficiently rendered in parallel.

## Installation

Just clone or download this repo and run:
```
python setup.py build_ext --inplace
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