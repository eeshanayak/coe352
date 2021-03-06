# Spring Mass System Project

## Purpose
For this project, I analyzed spring-mass systems with the following boundary conditions: 
1. Fixed-Fixed
2. Fixed-Free
3. Free-Free

The user inputs the number of springs in the system and the boundary condition. Depending on these values, the program determines how many masses are in the system and prompts the user to input the values of the masses and the spring constants. Then, the program runs an algorithm to solve the system and output the displacements, elongations, and internal forces of the springs.

## Usage (Example: Fixed-Fixed with 4 springs)
Run the following in the terminal:
```python3 Project_1.py```

The program will prompt you as follows:
```
How many springs are in your system?    4
What type of boundary condition would you like to apply?
1. Fixed-Fixed
2. Fixed-Free
3. Free-Free
1
What is mass 1? 1
What is mass 2? 1
What is mass 3? 1
What is the spring constant of spring 1?        1
What is the spring constant of spring 2?        1
What is the spring constant of spring 3?        1
What is the spring constant of spring 4?        1
```

The results appear in anoutput file titled 'report.txt'

```
The displacements of the springs are:
[[14.7, 19.6, 14.7]]

The elongations of the springs are:
[[14.7, 4.9, -4.9, -14.7]]

The Internal forces within the springs are:
[[14.7, 4.9, -4.9, -14.7]]

The condition number of A is: 2.41
The singular values of A are: [1.85, 1.41, 0.77]
The eigenvalues of A are: [1.36, 1.19, 0.87]

The condition number of At is: 2.41
The singular values of At are: [1.85, 1.41, 0.77]
The eigenvalues of At are: [1.36, 1.19, 0.87]

The condition number of c is: 1.0
The singular values of c are: [1.0, 1.0, 1.0, 1.0]
The eigenvalues of c are: [1.0, 1.0, 1.0, 1.0]
```

## Free-Free Discussion
If you try to run the Free-Free system, you get the following error:
```
kinv = np.linalg.inv(k)
numpy.linalg.LinAlgError: Singular matrix
```
In a Free-Free system, the difference matrix, A, does not have a full rank because there are more masses than springs, giving us more unknowns than equations. Because A does not have a full rank, it is not invertible, and we get a singular matrix that is unsolvable.

## Free-Free Solution Alternate Method: SVD
To try to solve the free-free system using SVD, I called SVD on the difference matrix, A. I noticed that if I tried multiplying the factored output back into the original matrix, I got a matrix dimension issue, therefore I could not plug it back in to solve for the force vector, and further the internal stress and elongation vectors.