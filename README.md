# Copyright Notice

proctorX, Copyright(c) 2019, Cem Önder


# proctorX

A software that tracks the amount of time user runs applications on a linux running system. User can run the program in the background as well visalize the data obtained from these sessions.

 * pick the programs you want to track through the GUI

![alt text](https://i.ibb.co/4Vk80r6/prx.png)

* start recording the activity!

![alt text](https://i.ibb.co/V3ZYqw3/prx4.png)

* then create pie charts or bar charts based on the data obtained by checking the desired applications to include in the plots

![alt text](https://i.ibb.co/8M09nv4/prx2.png)   

* Example Pie Chart: 

![alt text](https://i.ibb.co/Hg4WdVD/Screen-Shot-2019-08-12-at-6-49-35-PM.png)

* Example Bar Chart: 

![alt text](https://i.ibb.co/MR2Q20h/Screen-Shot-2019-08-12-at-6-49-49-PM.png)


# How It Works ?

* everytime a user adds a new program to be tracked a new `trackable` object is created. This object has information regarding the application's current track status, last time its activity has been ordered to be tracked as well as its current total run-time.

* When the user starts recording a `recorder` object  is assigned its own thread

* with the help of the `fileIO` and python `os` library, it checks every second whether a particular application is currently running.

* once the user stops the activity, the `manager` object, orders all `trackable`s that were asked to be tracked in the last recording session to update its data and write to the file. 

* when data is asked to be plotted, a `visualizer` object with the help of a `fileIO` object first retrieves the data and then creates the charts

# Build Instructions

PyPi package builder is currently in Progress. 

For the time being in order to build proctorX you need to complete the following steps:

`pip3 install numpy`

`pip3 install matplotlib`

`pip3 install PyQt5`

after following the steps and cloning the repository, the program can be executable with:

`python3 src/userInterface.py`