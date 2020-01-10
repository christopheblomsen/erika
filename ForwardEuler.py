"""Class(es) implementing the Forward Euler method for scalar ODEs."""

import numpy as np

class ForwardEuler:
    """
    Class for solving an ODE,

      du/dt = f(u, t)

    by the ForwardEuler solver.

    Class attributes:
    t: array of time values
    u: array of solution values (at time points t)
    n: number of time steps in the simulation
    k: step number of the most recently computed solution
    f: callable object implementing f(u, t)
    dt: time step (assumed constant)
    """
    def __init__(self, f, U0, T, n):
        if not callable(f):
            raise TypeError('f is not a function')
        self.f = lambda u, t: np.asarray(f(u, t))

        self.t = np.linspace(0, T, n +1)
        self.k = 0
        if isinstance(U0, (float, int)):
            # scalar ODE
            self.neq = 1
            self.u = np.zeros(n +1)
        else:
            # system of ODEs
            U0 = np.asarray(U0)
            self.neq = U0.size
            self.u = np.zeros((n + 1 , self.neq))
            self.U0 = U0

    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = self.U0

        for k in range(len(self.t)-1): #runs through the array
            self.k = k
            self.u[k+1] = self.advance()

        return self.u, self.t


    def advance(self):
        f, t, u, k = self.f, self.t, self.u, self.k
        dt = t[k+1]-t[k]

        u_new = u[k] + dt*f(u[k], t[k])
        return u_new
