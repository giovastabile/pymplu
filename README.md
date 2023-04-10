### 0. Introduction
**PyMPLU** that stands for Python MatPlotLib Utilities is a package that implements a number of utilities to make plotting with Matplotlib easier.

### 1. Prerequisites
**PyMPLU** requires
* Matplotlib
* Numpy

### 2. Installation via PIP
To install the package with pip run:
```
> pip install git+https://github.com/giovastabile/pymplu.git
```
To uninstall the package:
```
> pip uninstall pymplu
```

### 3 Installing from source
The official distribution is on GitHub, and you can clone the repository using
```bash
> git clone https://github.com/giovastabile/pymplu
```

To install the package just type:
```bash
> python setup.py install
```

To uninstall the package you have to rerun the installation and record the installed files in order to remove them:

```bash
> python setup.py install --record installed_files.txt
> cat installed_files.txt | xargs rm -rf
```

### 4 License

See the [LICENSE](LICENSE.rst) file for license rights and limitations (BSD).