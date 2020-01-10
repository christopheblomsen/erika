from Heun import * #This is where all the ODESolver stuff is located
import matplotlib.pyplot as plt #you know what this for I hope

def predator_prey(x0, y0, r, a, m, b, T, n):
    """
    This is a function that will use the Heun class to calculate the Population growth of an area
    with intiial conditions (see parenthesis)
    """
    def rhs(u, t):
        """
        A function within the function, u = is all the variables off the derivative and t is time
        """
        x, y = u #extracts x and y from u list/array
        dx = r*x - a*x*y #taken from problem
        dy = -m*y + b*x*y #same
        return [dx, dy] #returns the dx dy given

    U0 = [x0, y0] #initial conditions

    solver = Heun(rhs, U0, T, n) #uses the Heun class, view Heun.py for further info
    u, t = solver.solve()
    x = u[:,0]; y = u[:,1] #the [:,0] gets all the data from the first coloumn in the table
    return x, y, t #returns the shit

r = m = 1 #given by problem
a = 0.3; b = 0.2
x0 = 1; y0 = 1
T = 20; n = 100

x, y, t = predator_prey(x0,y0, r, a, m, b, T, n) #uses the above function as stated

plt.plot(t, x, t, y) #pretty straight forward
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(["x", "y"]) #another way to do it
plt.show()
