{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fixed_fixed(mass_list, c_list):\n",
    "    \n",
    "    # construct force matrix: force = mass * gravity\n",
    "    force_matrix = np.array(mass_list) * 9.8\n",
    "    \n",
    "    # generate diagonal matrix from spring constants\n",
    "    c_matrix = np.zeros((num_springs, num_springs))\n",
    "    np.fill_diagonal(c_matrix, c_list)\n",
    "    \n",
    "    A = np.zeros((num_springs, num_springs - 1))\n",
    "    np.fill_diagonal(A, 1)\n",
    "    np.fill_diagonal(A[1:], -1)\n",
    "    \n",
    "    \n",
    "    At = A.transpose()\n",
    "\n",
    "    # cast all objects to matrices\n",
    "    At = np.matrix(At)\n",
    "    A = np.matrix(A)\n",
    "    c_matrix = np.matrix(c_matrix)\n",
    "    force_matrix = np.matrix(force_matrix)\n",
    "    \n",
    "    # solve for k matrix: k = (A^t) * c * A\n",
    "    k = At * c_matrix * A\n",
    "    \n",
    "    # invert k to sove for u\n",
    "    kinv = np.linalg.inv(k)\n",
    "    \n",
    "    # solve for u (displacement vector): u = force * (k^-1)\n",
    "    u = force_matrix * kinv\n",
    "    \n",
    "    # solve for e (elongation vector): e = A * u\n",
    "    e = A*u.transpose()\n",
    "    \n",
    "    # solve for w: w = c * e\n",
    "    w = c_matrix * e\n",
    "    \n",
    "    return u"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}