# car-sim
Car Simulation

## Install

### Environment Pre-requisites

python 3, pip and virtualenv need to be locally installed.  My versions are below.

```bash
$ python3 --version
Python 3.7.3

$ pip3 --version
pip 19.1.1

$ virtualenv --version
16.7.2
```

If you do not have these installed, then download the latest from the offical libraries.
[Here](https://stackoverflow.com/questions/49470367/install-virtualenv-and-virtualenvwrapper-on-macos) is good advice for python and virtualenv install on macbook and OSX.
[Here](https://www.python.org/downloads/) is the official download page for python 3.
[Here](https://virtualenv.pypa.io/en/20.7.2/) is the official home page for virtualenv.

Use your favorite code editor and if you do not have one I recommend [vsCode](https://code.visualstudio.com/).  It is free.

### Installing

To get your code up and running, first let's clone the repo locally then compose the project:

```bash
cd <PATH_OF_CHOICE_TO_YOUR_ROOT_DEV_FOLDER>
git clone https://github.com/eusholli/car-sim
cd car-sim/
```

Let's activate the virtual python environment and install the dependancies

```bash
virtualenv venv
. venv/bin/activate
pip install pandas 
```

### Working

To start your vscode editor from the terminal and open it in your project type ```code .```

When you have finished your work you can deactivate the virtualenv in your terminal by typing ```deactivate``` in your terminal. If you do not do this and change directory, you will carry on using the car-sim virtualenv and risk installing dependancies in the wrong virtualenv.

When returning in a new terminal to start working again, enter the working directory (.../car-sim) and only type ```. venv/bin/activate``` to re-activate the virtualenv.
