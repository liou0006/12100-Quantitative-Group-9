import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
# Updated, slower growth data

t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 23])

share = np.array([0.01, 0.015, 0.02, 0.025, 0.04, 0.07, 0.11, 0.15, 1.00])
shareEV = np.array([0.004, 0.003, 0.004, 0.006, 0.012, 0.024, 0.04, 0.07, 1.00])

def richards(t, Q, B, t0, v):
    K = 1 # Maximum market share (saturation level)
    return K * (1 + Q * np.exp(-B * (t - t0))) ** (-1/v)

Q = 1
B = 0.3
t0 = 12
v = 1

p0 = [Q, B, t0, v]
params, _ = curve_fit(richards, t, shareEV, p0=p0, maxfev=10000)
t_plot = np.linspace(0, 23, 100)
share_pred = richards(t_plot, *params)

plt.figure(figsize=(8, 5))
plt.scatter(t, share, color='red', label='Observed data')
plt.plot(t_plot, share_pred, label='Richards curve fit', lw=2)
plt.xlabel('Years since 2017')
plt.ylabel('EV Share')
plt.title('EV Diffusion with Slower Early Growth')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Check at 2040 (t=23)
share_2040 = richards(23, *params)
print(f"Richards curve at 2040 (t=23): {share_2040:.4f}")
print("Fitted parameters: Q={:.3f}, B={:.3f}, t0={:.3f}, v={:.3f}".format(*params))