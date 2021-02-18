import numpy as np
import math
import matplotlib.pyplot as plt

def getDistance(xval1, yval1, xval2, yval2):
    '''returns distance between two points when given
        coordinates'''
    distance = math.sqrt((xval2-xval1)**2+(yval2-yval1)**2)
    return distance

def f(x, y):
    '''A badly coded way of returning the total potential for a point
        in a single function.'''
    return -((1/(4*np.pi*8.85418782e-12*(np.sqrt((x-Charge1[0])**2+(y-Charge1[1])**2)))+
            (1/(4*np.pi*8.85418782e-12*(np.sqrt((x-Charge2[0])**2+(y-Charge2[1])**2))))))

def centralDiffx(x, y, h=.01):
    '''Returns the partial derivative of f with respect to x.'''
    return (f(x+h, y)-f(x-h, y))/(2*h)

def centralDiffy(x, y, h=.01):
    '''Returns the partial derivative of f with respect to y.'''
    return (f(x,y+h) - f(x, y-h))/(2*h)
    
def calculatePotential(charge, distance):
    '''Calculate the electric potential for a point give the charge
        and the distance from the point.'''
    potential = charge/(4*np.pi*8.85418782e-12*distance)
    return potential

if __name__ == "__main__":
    Charge1 = (-0.05, 0, 1) #xpos, ypos, charge
    Charge2 = (0.05, 0, 1) #xpos, ypos, charge
    #generate x,y values
    spacing = 0.01 #<--spacing 0.01 m = 1 cm
    x_range = np.arange(-0.5, 0.5, spacing)
    y_range = np.arange(-0.5, 0.5, spacing)
    xs, ys  = np.meshgrid(x_range, y_range)

    distance1 = np.sqrt((Charge1[0]-xs)**2+(Charge1[1]-ys)**2)
    distance2 = np.sqrt((Charge2[0]-xs)**2+(Charge2[1]-ys)**2)
    distance1[distance1<.0001] = None
    distance2[distance2<.0001] = None
    
    totalPotential = (calculatePotential(Charge1[2], distance1)+
                      calculatePotential(Charge2[2], distance2))
    
    plt.contourf(xs,ys,(totalPotential))
    #plt.ylim(-0.1,0.1)
    #plt.xlim(-0.1,0.1)
    
    plt.colorbar()
    plt.show()

    xdiff = centralDiffx(xs, ys)
    ydiff = centralDiffy(xs, ys)


    print('Partial at point (0,0) is', centralDiffx(0, 0), 'i',
          centralDiffy(0, 0),'j')
    print('Partial at point (.05,.07) is', centralDiffx(.05, .07),'i',
          centralDiffy(.05, .07),'j')
    plt.clf()
    plt.streamplot(xs,ys,xdiff,ydiff) #is not working, was unable to figure out why.
    plt.show()

            
                              
            
            
            
