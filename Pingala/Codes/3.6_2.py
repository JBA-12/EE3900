from turtle import color
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
import numpy as np

x = [1, 1]
for i in range(30): 
    x.append(x[-1] + x[-2])


# y(n) = x(n-1) + x(n+1)
# p_y = partial sum of y(k)/10^k

y = np.add(x[:30], x[2:])  # Add arguments element-wise. => y is an array where, y[0] = y(1) = x[0] + x[2]

p_y = [1]
for i in range(30): 
    p_y.append(p_y[-1] + (y[i]/10**(i+1)))

p_y_divided = [p/10 for p in p_y]

plt.stem(range(31), p_y_divided, label=r'$\frac{1}{10}\sum_{k=1}^n \frac{b_k}{10^k}$')

ans2 = 8/89
plt.axhline(ans2 ,color='g', label='8/89', linestyle = '--')
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.tight_layout()
plt.legend()
plt.savefig('../figs/3.6.png')
plt.show()