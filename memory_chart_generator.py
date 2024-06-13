import numpy as np
import matplotlib.pyplot as plt

# Sample data: Problem sizes and corresponding times for two algorithms
problem_sizes = np.array([16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968])
memory_basic =  np.array([0, 48, 176, 704, 1584, 2704, 6064, 10608, 16450, 24064, 42160, 65808, 93632, 129856, 155680])
#memory_efficient = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5])  # Efficient algorithm times

# Creating the plot
plt.figure(figsize=(10, 5))
plt.plot(problem_sizes, memory_basic, label='Basic Algorithm', marker='o')
# plt.plot(problem_sizes, memory_efficient, label='Memory Efficient Algorithm', marker='x')

# Adding titles and labels
plt.title('Algorithm Performance Comparison')
plt.xlabel('Problem Size (m+n)')
plt.ylabel('Memory in KB')
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()
