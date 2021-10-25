import numpy as np
from numpy import linalg as LA
from functions import solve
from scipy.linalg import svd

num_springs=int(input("How many springs are in your system?\t"))

boundary_condition = int(input("What type of boundary condition would you like to apply?\n1. Fixed-Fixed\n2. Fixed-Free\n3. Free-Free\n"))

# receive mass inputs
mass_list = []

if (boundary_condition == 1):
    num_masses = num_springs - 1
elif (boundary_condition == 2):
    num_masses = num_springs
elif (boundary_condition == 3):
    num_masses = num_springs + 1
    

for i in range(num_masses): 
    mass = int(input('What is mass ' + str(i + 1) + '?\t')) 
    mass_list.append(mass)

c_list = []

# receive spring constants
for i in range(num_springs):
    c = int(input('What is the spring constant of spring ' + str(i + 1) + '?\t'))
    c_list.append(c)

# generate difference matrix
A = np.zeros((num_springs, num_masses))
np.fill_diagonal(A, 1)
np.fill_diagonal(A[1:], -1)

# Addition: Alternate approach to solving free-free
if(boundary_condition == 3):
    # perform svd on A transpose
    U, s, VT = svd(np.matrix(A))

    U * s * VT


    
u, e, w, At, c, f = solve(num_springs, mass_list, c_list, A)

U_A, singular_A, VT_A = svd(A)
U_At, singular_At, VT_At = svd(At)
U_c, singular_c, VT_c = svd(c)

eig_A = np.sqrt(singular_A)
eig_At = np.sqrt(singular_At)
eig_c = np.sqrt(singular_c)

c_num_A = singular_A.max() / singular_A.min()
c_num_At = singular_At.max() / singular_At.min()
c_num_c = singular_c.max() / singular_c.min()

condition_number_A = LA.cond(A)

report = open('report.txt','w')
report.write('The displacements of the springs are:\n' + str(u[0].round(2).tolist()) + 
            '\n\nThe elongations of the springs are:\n' + str(e.round(2).tolist()) + 
            '\n\nThe Internal forces within the springs are:\n' + str(w.round(2).tolist()) + 
            '\n\nThe condition number of A is: ' + str(c_num_A.round(2)) + 
            '\nThe singular values of A are: ' + str(singular_A.round(2).tolist()) + 
            '\nThe eigenvalues of A are: ' + str(eig_A.round(2).tolist()) + 
            '\n\nThe condition number of At is: ' + str(c_num_At.round(2)) +
            '\nThe singular values of At are: ' + str(singular_At.round(2).tolist()) + 
            '\nThe eigenvalues of At are: ' + str(eig_At.round(2).tolist()) + 
            '\n\nThe condition number of c is: ' + str(c_num_c.round(2)) +
            '\nThe singular values of c are: ' + str(singular_c.round(2).tolist()) +
            '\nThe eigenvalues of c are: ' + str(eig_c.round(2).tolist()))
            

