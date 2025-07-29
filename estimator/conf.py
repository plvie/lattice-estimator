# -*- coding: utf-8 -*-
"""
Default values.
"""

from .simulator import GSA, CN11, LGSA
from .reduction import RC
from sage.all import exp

"""
Default models used to evaluate the cost and shape of lattice reduction.
This influences the concrete estimated cost of attacks.
"""
red_cost_model = RC.Blaster
red_cost_model_classical_poly_space = RC.ABLR21
red_shape_model = "GSA"
red_simulator = GSA

mitm_opt = "analytical"
max_n_cache = 10000


def ntru_fatigue_lb(n):
    return int((n**2.484)/exp(6))
