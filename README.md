# GT Course Tree Crawler 🕷
> A crawler that scrapes course requisite information data from Georgia Tech's OSCAR system for the [GT Course Tree](https://github.com/devarsirawal/gt-course-tree)

## 🚀 Running Locally

### Setup

#### Requirements
* [Python 3.7.9](https://www.python.org/downloads/release/python-379/)

#### Creating the Virtual Environment
To begin development, it will help to create a Python virtual environment specifically for this project. To create one, run in your terminal:

```
python3 -m venv crawler-env
```

Then, activate your virtual environment by running:

```
source crawler-env/bin/activate
```

#### Installing Dependencies
This project uses the following Python packages:
* [requests](https://docs.python-requests.org/en/master/)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [antlr4-python3-runtime](https://pypi.org/project/antlr4-python3-runtime/)

To install these dependencies, run: 

```
pip install -r requirements.txt
```

### Running the Application

To run the application, run:

```
python crawler.py
```

## 🤝 Credits 
All credit for the grammars used in this project go to [jazevedo620](https://github.com/jazevedo620) and the [GT Scheduler](https://github.com/gt-scheduler) team. The original grammars and visitor patterns can be found [here](https://github.com/gt-scheduler/crawler/tree/master/src/steps/prereqs)
