import numpy as np
from numpy import linalg as LA
from functions import solve, condition_number

gravity = 9.8
num_springs=int(input("How many springs are in your system?\t"))

boundary_condition = int(input("What type of boundary condition would you like to apply?\n1. Fixed-Fixed\n2. Fixed-Free\n3. Free-Free\n"))

# receive mass inputs
mass_list = []

if (boundary_condition == 1):
    num_masses = num_springs - 1
    A = np.zeros((num_springs, num_masses))
elif (boundary_condition == 2):
    num_masses = num_springs
    A = np.zeros((num_springs, num_masses))
elif (boundary_condition == 3):
    num_masses = num_springs + 1
    A = np.zeros((num_springs, num_masses))

for i in range(num_masses): 
    mass = int(input('What is mass ' + str(i + 1) + '?\t')) 
    mass_list.append(mass)

c_list = []

# receive spring constants
for i in range(num_springs):
    c = int(input('What is the spring constant of spring ' + str(i + 1) + '?\t'))
    c_list.append(c)

u, e, w, At, c, f = solve(num_springs, mass_list, c_list, A)

c_num_e = condition_number(e)
c_num_w = condition_number(w)
c_num_f = condition_number(f)

condition_number_A = LA.cond(A)

report = open('report.txt','w')
report.write('The displacements of the springs are:\n' + str(u[0].round(2).tolist()) + 
            '\n\nThe elongations of the springs are:\n' + str(e.round(2).tolist()) + 
            '\n\nThe Internal forces within the springs are:\n' + str(w.round(2).tolist()) + 
            '\n\nThe condition number of e is: ' + str(c_num_e.round(2)) + 
            '\n\nThe condition number of w is: ' + str(c_num_w.round(2)) + 
            '\n\nThe condition number of f is: ' + str(c_num_f.round(2)))

