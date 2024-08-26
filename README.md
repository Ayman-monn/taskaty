
<!-- ABOUT THE PROJECT -->
## About The Project

The project is a Taskaty CLI (Command Line Interface) program you can use it in terminal, it's a little bit like todo projects .
I built this project with my skills in python .


### Built With 
This Project is built with some python packages and library 
* argpars
* setuptools 
* datetime 
* tabulate


### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/Ayman-monn/taskaty.git
   ```
2. Go to the project directory 
3. Install Requirements 
   ```sh
   python -m venv venv
   ```
4. Install taskaty package
   ```sh
   pip install -e . 
   ```
5. After installing successfully you can enjoy taskaty package



<!-- USAGE EXAMPLES -->
## Usage
This packages is used like to do program you can add your tasks to do later .

Open the terminal and type:
```sh 
   taskaty --help
``` 
1. To Add a new task:
```sh
   taskaty add {task_name}
```
2. To show unfinished tasks yet:
```sh 
   taskaty list
```
3. To ahow all tasks either finished or unfinished:
```sh
   taskaty list -a 
```
4. Make task status finished:
```sh
   taskaty check -t {task_id}
```
5. Delete a specific task:
```sh
   taskaty remove -t {task_id}
```
6. Delete all tasks 
```sh
   taskaty remove -t {task_id}
```

