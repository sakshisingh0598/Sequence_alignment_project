# Sequence Alignment Algorithm

## Overview

This repository contains a Python implementation of two algorithms for solving the Sequence Alignment problem:

1. **Basic Algorithm**: A traditional dynamic programming approach for sequence alignment with polynomial time and space complexity.
2. **Memory-Efficient Algorithm**: An optimized version of the basic algorithm, which significantly reduces the memory requirements using a divide-and-conquer strategy while maintaining comparable time complexity.

## Problem Statement

Sequence alignment is a fundamental problem in bioinformatics, where we aim to identify similarities between two sequences (e.g., DNA, RNA, or protein sequences). The traditional approach for this problem requires substantial memory, especially for large sequences. This project provides a solution to mitigate memory usage without compromising the performance of the alignment process.

## Insights

- The **Basic Algorithm** has a time complexity of \(O(mn)\) and a space complexity of \(O(mn)\), where \(m\) and \(n\) are the lengths of the sequences.
- The **Memory-Efficient Algorithm** reduces the space complexity to \(O(\min(m, n))\) by storing only two rows or columns of the dynamic programming matrix at a time.
- Despite the memory savings, both algorithms exhibit similar performance in terms of time complexity.

## Tech Stack

- **Python**: Main programming language for implementation.
- **NumPy**: For handling large arrays efficiently.
- **Matplotlib**: For generating performance graphs of memory and time complexity.
- **Jupyter Notebooks**: Used for documenting the results and analysis.

## Performance

### Memory vs. Problem Size (M+N)
- **Basic Algorithm**: Shows linear growth in memory usage as the size of the problem increases.
- **Memory-Efficient Algorithm**: Shows a polynomial decrease in memory usage, making it more suitable for large datasets.

### Time vs. Problem Size (M+N)
- **Basic and Efficient Algorithms**: Both show polynomial growth in time, with the efficient algorithm being slightly slower due to the additional recursion.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/sequence-alignment.git
    ```
    ```
3. Run the sequence alignment:
    ```bash
    python align_sequences.py
    ```

## Graphs and Analysis

- The results of the algorithms' performance are visualized using graphs for memory and time complexities, available in the Jupyter notebooks.

## Contributions

- **Equal Contribution**: The project was developed collaboratively by the team members, with each contributing equally to the implementation and analysis.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
"""
file_path = "/mnt/data/README.md"
with open(file_path, "w") as file:
    file.write(readme_content)

file_path
