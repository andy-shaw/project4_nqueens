Author: Andy Shaw
Date: 10/8/2013
Course: CSE 3521 - Survey of Artificial Intelligence, Assignment03

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

------------------------------------Compilation/Running---------------------------------------------
This program is compatible with Python 2.6 (runs on the OSU Linux machines)

To run the Hill Climbing algorithm, enter the HillClimbing directory and invoke the command:
$ python testHarnessHillClimbing.py boardSize [SILENT]
    -> boardSize is an integer greater than 4
    -> NOTE: for boardSize>7 expect longer computation times
    -> SILENT is an optional flag to display the iteration output or not
    
To run the Genetic algorithm, enter the Genetic directory and invoke the command:
$ python testHarnessGeneticAlgorithm.py boardSize mutationRate populationSize [SILENT]
    -> boardSize is an integer greater than 4
    -> mutationRate is a float between 0 and 1
    -> populationSize is an integer greater than 1

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

---------------------------------------Known Errors-------------------------------------------------
PUT STUFF HERE IF APPLIES

----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------

------------------------------------------Notes-----------------------------------------------------
* The Hill Climbing algorithm experiences noticeably increasing computation time from sizes greater 
    than 5.  The unit for the following measurements are in seconds.  The algorithm was run 5 times
    per board size.
    Size        Avg         Min         Max
    ------     --------    --------     --------
    4             0.037       0.000        0.115
    5             0.081       0.010        0.250
    6            24.843       1.365       38.971
    7            29.335       4.305       73.512
    8           746.793      43.523     2014.704
    
    I consider it to take a long time when it takes more than 10 minutes to complete the program.  
    One thing to consider is the process can be greatly sped up with the introduction of 
        multiprocessing.