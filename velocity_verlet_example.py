import numpy as np
import matplotlib.pyplot as plt

# Constants
m = 1.0        # Mass (kg)
k = 1.0        # Spring constant (N/m)
dt = 0.01      # Time step (s)
t_max = 10.0   # Total simulation time (s)

# Initialize position, velocity, acceleration
x = 1.0        # Initial position (m)
v = 0.0        # Initial velocity (m/s)
a = -k * x / m # Initial acceleration (F = -kx/m)

# Time evolution
time = np.arange(0, t_max, dt)
positions = []

for t in time:
    positions.append(x)

    # Velocity Verlet integration
    x_new = x + v * dt + 0.5 * a * dt**2
    a_new = -k * x_new / m  # Compute new acceleration
    v_new = v + 0.5 * (a + a_new) * dt

    # Update variables for next step
    x, v, a = x_new, v_new, a_new

# Plot results
plt.plot(time, positions)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Harmonic Oscillator Using Velocity Verlet")
plt.show()
