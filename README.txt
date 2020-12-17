

Measuring Behavioural Similarity of Cellular Automata
=====================================================


Peter Turney
December 17, 2020


Initial Setup
=============

This document describes how to install and run this software in 
Windows 10. With some changes, you should also be able to run it 
in Linux or Mac OS.

(1) Download and Install Golly

Golly is a C++ program for the simulation of cellular automata:

- https://en.wikipedia.org/wiki/Golly_(program)

I used the 64-bit version of Golly 3.3 for Windows 10 
(golly-3.3-win-64bit.zip):

- http://golly.sourceforge.net/
- https://sourceforge.net/projects/golly/files/golly/golly-3.3/
  
Golly is stored in a zip file. I created a directory called Golly64
and put the contents of the zip file in this directory:

- C:\Users\peter\Golly64

(2) Download and Install Python

Golly can be extended with scripts written in Python or Lua. Model-S is
a set of Python scripts that run with Golly.

I used Python 2.7 for Windows. Golly 3.3 is designed to work with Python 2.X
but not Python 3.X. Here is some information on using Python with Golly:

- http://golly.sourceforge.net/Help/python.html

(3) Download and Install Numpy and Statistics

Numpy provides Python numerical functions needed by for making probability
vectors. After Python has been installed, Numpy can be installed in 
Windows 10 by opening a command prompt and executing the following 
commands:

> cd \Python27\Scripts
> pip install numpy
> pip install statistics


Vectors for Semi-totalistic Rules
=================================

Following the steps below will result in a list of all 262,144 
semi-totalistic rules with probability vectors assigned to them.
A probability vector has 72 elements that characterize the behaviour
of the given rule.  

(1) Step 1

- run "scoring_initialize.py"
- this will generate a list of all 262,144 semi-totalistic rules
- processing these rules is slow, so we assume the task will be 
  shared by several different CPUs
- "scoring_initialize.py" will generate a list of all 262,144 
  semi-totalistic rules and assign each rule to one of the CPUs
- set the desired number of CPUs by editing the parameter "num_cpus"
  in "scoring_parameters.py"
- set the desired name of the output file by editing the parameter
  "rule_file_name" in "scoring_parameters.py"

(2) Step 2

- run "scoring_main.py"
- this will read the output file from Step 1 and generate statistics
  for the 262,144 semi-totalistic rules
- suppose you have 6 CPUs available for scoring
- set "num_cpus = 6" in "scoring_parameters.py"
- repeat the following for i = 1, 2, ..., 6:
  - set "current_cpu_id = i" in "scoring_parameters.py"
  - open Golly and run "scoring_main.py"
  - this will create a file with scores for CPU number i
  - it could take about a day to run
  - go back to the top of this loop without waiting for CPU number i 
    to stop running
- proceed to Step 3 when all 6 copies of Golly are done running

(3) Step 3

- run "scoring_merge.py"
- this will merge the scoring files generated in Step 2 into a
  single file




