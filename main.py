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
import gurobipy as gp
from gurobipy import GRB
import os

print("HELLO WORLD")