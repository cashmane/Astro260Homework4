
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def f(x):
    return np.sqrt(x)+np.cos(x)

def trueDeriv(x):
    return (1/(2*np.sqrt(x)))-np.sin(x)

sparseRange = np.arange(0, 4*np.pi, 0.8)
fineRange = np.arange(0, 4*np.pi, 0.1)

linear = interp1d(sparseRange, f(sparseRange))
cubic = interp1d(sparseRange, f(sparseRange), kind='cubic')
linearDeriv = interp1d(sparseRange, trueDeriv(sparseRange))
cubicDeriv = interp1d(sparseRange, trueDeriv(sparseRange), kind='cubic')

plt.plot(fineRange, f(fineRange),color='blue')
plt.plot(fineRange, trueDeriv(fineRange),color='purple')
plt.plot(sparseRange, linear(sparseRange),'-',color='orange')
plt.plot(sparseRange, cubic(sparseRange),'--',color='green')
plt.plot(sparseRange, linearDeriv(sparseRange),'-',color='orange')
plt.plot(sparseRange, cubicDeriv(sparseRange),'--',color='green')
plt.xlabel('X')
plt.ylabel('sqrt(x)+cos(x)')
plt.legend(['f(x)','Derivative', 'linear f(x)', 'cubic f(x)',
            'linear deriv', 'cubic deriv'], loc='best')
plt.show()


