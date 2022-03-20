#!/usr/bin/env python3.7

# Copyright 2021, Gurobi Optimization, LLC

# This example formulates and solves the following simple MIP model
# using the matrix API:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary

import numpy as np
import scipy.sparse as sp
import gurobipy as gp
from gurobipy import GRB
import os


# Gurobi WLS license file
# Your credentials are private and should not be shared or copied to public repositories.
# Visit https://license.gurobi.com/manager/doc/overview for more information.
WLSACCESSID = 'ad45e2a0-cd40-47ef-bbfe-6a38ec08a968'
WLSSECRET = '0025ed22-6165-4271-9878-4e32200e51ce'
LICENSEID = 781920

# Create environment with WLS license
e = gp.Env(empty=True)
e.setParam('WLSACCESSID', WLSACCESSID)
e.setParam('WLSSECRET', WLSSECRET)
e.setParam('LICENSEID', LICENSEID)
e.start()


# Create the model within the Gurobi environment
m = gp.Model(env=e, name="matrix1")

# Create variables
x = m.addMVar(shape=3, vtype=GRB.BINARY, name="x")

# Set objective
obj = np.array([1.0, 1.0, 2.0])
m.setObjective(obj @ x, GRB.MAXIMIZE)

# Build (sparse) constraint matrix
data = np.array([1.0, 2.0, 3.0, -1.0, -1.0])
row = np.array([0, 0, 0, 1, 1])
col = np.array([0, 1, 2, 0, 1])

A = sp.csr_matrix((data, (row, col)), shape=(2, 3))

# Build rhs vector
rhs = np.array([4.0, -1.0])

# Add constraints
m.addConstr(A @ x <= rhs, name="c")

# Optimize model
m.optimize()

print(x.X)
print('Obj: %g' % m.objVal)