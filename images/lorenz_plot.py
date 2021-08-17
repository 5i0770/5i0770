#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def lorenz_equation(state, t):
    BETA = 8.0/3.0
    RHO = 28.0
    SIGMA = 10.0

    x = state[0]
    y = state[1]
    z = state[2]
    
    dx_dt = SIGMA*(y - x)
    dy_dt = x*(RHO - z) - y
    dz_dt = x*y - BETA*z
    
    dstate_dt = np.array([dx_dt, dy_dt, dz_dt])
    
    return dstate_dt
    
    
def create_plot(name, x, y):
    COLOR = '#ffbec7'
    
    fig, ax = plt.subplots()
    
    ax.plot(x, y, color=COLOR)
    fig.patch.set_visible(False)
    ax.axis('off')
    fig.savefig(name, format='svg', transparent=True)
    

if __name__ == '__main__': 
    START_TIME = 0.0 # [s]
    END_TIME = 40.0 # [s]
    TIMESTEPS = 0.01
    t = np.arange(START_TIME, END_TIME, TIMESTEPS)

    INITIAL_STATE = np.array([1.0, 1.0, 1.0])
    states = odeint(lorenz_equation, INITIAL_STATE, t)
    
    x_trajectory = states[:, 0]
    y_trajectory = states[:, 1]
    z_trajectory = states[:, 2]

    create_plot('lorenz_xy.svg', x_trajectory, y_trajectory)
    create_plot('lorenz_yz', y_trajectory, z_trajectory)
    create_plot('lorenz_xz', x_trajectory, z_trajectory)

