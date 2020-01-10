from ForwardEuler import * #ForwardEuler is the same as ODESolver

class Heun(ForwardEuler): #Inherit everything from ForwardEuler class
    def advance(self): #new advance function that ForwardEuler can use
        u, t, f, k = self.u, self.t, self.f, self.k #just for ease of use
        dt = t[k+1] - t[k] #calculates dt
        u_m = u[k] + dt * f(u[k], t[k]) #calculates u_m in Heun
        u_new = u[k] + (dt/2)*f(u[k], t[k]) + (dt/2)*f(u_m, t[k+1]) #calculates the u_k+1 in Heun
        return u_new #returns it back to ForwardEuler
