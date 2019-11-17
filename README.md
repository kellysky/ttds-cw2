********************
#Introduction
~~~~
The project is C program, aimed to soleve Percolate problem.

The project will create serveral clusters which has the same number in every grid of cluster and check whether percolation has occurred.

The program will writes out two files: one data file and one image file.

There are six arguments in the program.All the arguments required by the program should be specified by user via  command line.

map_grid: L means the length of the map.

datafile: means that user should input the filename of data file.

percolatefile:  means that user should input the filename of image file.

rho: means that user should specify a value of density from 0 to 1 to decide whether the grid is filled.

seed: means that user should input the value of random seed used for generating random number.

MAX: means that user should specify a MAX value.
~~~~
****
****
#Environment dependance
~~~~
C compilers: gcc

Operating system: Linux

Test tool: CUnit
~~~~
****
#Setup steps:
~~~~
1 Enter into Percolate directory: cd ~/USER_PATH/Percolate, USER_PATH is the path that user store the program.

2 Build Makefile: make run map_grid=$(map_grid) datafile=$(datafile) percolatefile=$(percolatefile) seed=$(seed) rho=$(rho) MAX=$(MAX)
               eg: `make run map_grid=20 datafile=map.dat percolatefile=map.pgm seed=1564 rho=0.40 MAX=400 `
________________________________________________________________________________________________________________________________________________
~~~~
#Test:
~~~~
1 Enter into Percolate directory: cd ~/USER_PATH/Percolate

2 Set environement path, input command as below:  
              export C_INCLUDE_PATH=$HOME/include:$C_INCLUDE_PATH
              export LIBRARY_PATH=$HOME/lib:$LIBRARY_PATH
              export LD_LIBRARY_PATH=$HOME/lib:$LD_LIBRARY_PATH


3 Build Makefile: make test
~~~~
#Project structure:
~~~~
Directory: 
    1 src: 
          percolate.h: the headers file of percolation

          percolate.c: the file contains all functions of precolation problem

          percolate_program.c: the file of main function
    2 test:
          percolate_cunit_test.h: the headers file of test function, define all the test function and external variables

          percolate_cunit_test.c: the file contains all test functions

          cunit_test_drivers.c: the file of main function, initialise the CUnit test registry and add suite
~~~~
#Created file (if you has excuted the example command in setup setps):
~~~~
a.out: the compiled file of percolated.c.

map.dat: a data file contains the values of each square.

map.pgm: a image file of square.

CUnit-Test-Results.xml: the report of test results
~~~~

#File instruction:
~~~~
map.dat: you can view this file by using this command "cat map.dat".

map.pgm: you can view this image by using this command "display map.pgm" or "gimp map.pgm".
~~~~


