# ALMA technical test

## How to run

Install Python and run locally or use [![gitpod](https://img.shields.io/badge/Open%20in-Gitpod-C8597A.svg)](https://gitpod.io/#https://github.com/Haegh/alma_test).  
To run the application, you need to be in the *foobar_app* repository and use the command `python main.py`.

## Explanations

### Architecture

Classic architecture with all the code in the *foobar_app* repository.  
File _main.py_ is the entrypoint of the application.  
Folder *classes* contains the 2 classes of the project : Game and Robot.  
Folder *tests* contains the test files : Use `pytest` command to launch the test.  

### Game

Class representing the game.  
It is the environnment where the robots can work.  
All resources gathered by the robots belong to the game.  
The `play` methods is the core of the game and launch all the tasks that represent the robots. Each task is launched concurrently with `asyncio.gather`. All resources can be obtained by different robot/task, then we use `asyncio.Lock` to not have concurrency problems with these shared resources.  

### Robot

Class representing the robot.  
The robot has only an id and a status representing the last action that they have done.  
All the actions that a robot can do is represented by a method.  
Moreover, the variable `time_translation` can be modified to accelerate or slow the game.  

## Documentation

It is possible to generate sphinx documentation.  
In the folder docs, use the command `make html`.  
The folder *_build* will be generated and you will see the documentation in the */docs/_build/html* folder.  
The documentation is generated from the code dosctring.  
