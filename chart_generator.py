import numpy as np
import matplotlib.pyplot as plt

# Sample data: Problem sizes and corresponding times for two algorithms
problem_sizes = np.array([16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968])
times_basic = np.array([0.19097328186035156, 0.5240440368652344, 1.6238689422607422, 5.561113357543945, 12.876033782958984, 21.51036262512207, 51.11098289489746, 80.95121383666992, 122.51496315002441, 168.09701919555664, 305.93323707580566, 465.06690979003906, 646.1071968078613, 898.9467620849609, 1147.7749347686768])  # Basic algorithm times
# times_efficient = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])  # Efficient algorithm times

# Creating the plot
plt.figure(figsize=(10, 5))
plt.plot(problem_sizes, times_basic, label='Basic Algorithm', marker='o')
# plt.plot(problem_sizes, times_efficient, label='Memory Efficient Algorithm', marker='x')

# Adding titles and labels
plt.title('Algorithm Performance Comparison')
plt.xlabel('Problem Size (m+n)')
plt.ylabel('Time in Milliseconds')
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()
