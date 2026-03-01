import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# Updated, slower growth data

# t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 23])
t = np.array([2007, 2008, 2009, 2010, 2011, 2012, 2013, 
              2014, 2015, 2016, 2017, 2018, 2019, 2020, 
              2021, 2022, 2023, 2024, 2040
])

t = t - 2007

# share = np.array([0.01, 0.015, 0.02, 0.025, 0.04, 0.07, 0.11, 0.15, 1.00])
share = np.array([
    0.000074, 0.000069, 0.000067, 0.000103, 0.000137, 0.000341, 0.000556, 
    0.000674, 0.001253, 0.003299, 0.003513, 0.003464, 0.003869, 0.005848, 
    0.011707, 0.023896, 0.040225, 0.070763, 0.95
])

def richards(t, Q, B, t0, v):
    K = 0.95 # Maximum market share (saturation level)
    
    return K * (1 + Q * np.exp(-B * (t - t0))) ** (-1/v)

Q = 1
B = 0.3
t0 = 20
v = 0.3

p0 = [Q, B, t0, v]
params, _ = curve_fit(richards, t, share, p0=p0, maxfev=10000)
t_plot = np.linspace(0, 33, 100)
share_pred = richards(t_plot, *params)

plt.figure(figsize=(8, 5))
plt.scatter(t, share, color='red', label='Observed data')
plt.plot(t_plot, share_pred, label='Richards curve fit', lw=2)
plt.xlabel('Years since 2007')
plt.ylabel('EV Share')
plt.title('EV Diffusion with Slower Early Growth')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Check at 2040 (t=23)
t_2040 = 2040 - 2007
share_2040 = richards(t_2040, *params)
print(f"Richards curve at 2040 (t=23): {share_2040:.4f}")
print("Fitted parameters: Q={:.3f}, B={:.3f}, t0={:.3f}, v={:.3f}".format(*params))