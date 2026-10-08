import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 0.8
K_I = 0.05
K_D = 0.3
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

velocities = []
errors = []
times = []
for i in range(STEPS):
    desired_acceleration, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle_percentage = acceleration_to_throttle_percentage(desired_acceleration)
    update(car, throttle_percentage)
    velocities.append(car["v"])
    errors.append(error)
    times.append(car["t"])


plt.figure()
plt.plot(times, velocities)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.show()


plt.figure()
plt.plot(times, errors)
plt.xlabel("Time (s)")
plt.ylabel("Error (m/s)")
plt.title("Error vs Time")
plt.show()