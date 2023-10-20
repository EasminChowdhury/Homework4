import numpy as np
import matplotlib.pyplot as plt

#Initialization: Normalize the columns of A so that they sum to 1, resulting in the matrix M.
A = np.array([[0,1,1,0,0,0],[0,0,1,1,0,0],[1,0,0,0,0,0],[0,1,0,0,1,0],[0,1,0,1,0,1],[0,0,0,0,1,0]] , dtype=np.float64) #This is the adjacency matrix where the rows and columns respond to the pages
print("A=", A) #matrix
print("-" * 70)
column_sum= A.sum(axis=0) # column-sum array representing the sum of each column of A
M = A / column_sum # M is the normalized A by dividing A by the column_sum through element-wise division
print("M=", M)
print("-" * 70)

#PageRank Iteration:
r = np.array([1/6 , 1/6, 1/6, 1/6, 1/6, 1/6]) # This represents the initial rank of the pages
s = np.array([1/6 , 1/6, 1/6, 1/6, 1/6, 1/6])

diff= float("inf")
threshold = 1e-6
iteration = 0
α = 1

# Lists to store values of r and iteration
r_values = [] # I dont think this includes the initial R
iteration_values = []

while diff >= threshold:
      r_prime = (α * M @ r) + ((1-α) * s) # r′ = αMr + (1−α)s where α is 0.85 ,
      diff = np.max(abs(r_prime - r)) #
      r = (r_prime)
      r = r / np.linalg.norm(r)
      iteration += 1

      r_values.append(r.copy())  # Store a copy of r at each iteration
      iteration_values.append(iteration)

# Create a plot to visualize the r values over iterations
plt.figure(figsize=(8, 6))
for i in range(len(r_values[0])):
    plt.plot(iteration_values, [r[i] for r in r_values], label=f'Page {i + 1}')

plt.xlabel('Iteration')
plt.ylabel('PageRank Value')
plt.title('PageRank Values Over Iterations')
plt.legend()
plt.grid(True)
plt.show()
print("-" * 70)

#Analysis: Compare the PageRank results with the eigenvector of M corresponding to the largest eigenvalue.They should be closely related.
eigenvalues, eigenvectors = np.linalg.eig(M) # eigenvalues and eigenvectors of M
largest_eigenvalue_index = np.argmax(eigenvalues) # index of the largest eigenvalue of M
eigenvector = eigenvectors[:, largest_eigenvalue_index] # eigenvector corresponding to the largest eigenvalue of M
magnitude = np.linalg.norm(eigenvector) # Calculate the magnitude (Euclidean norm) of the eigenvector
normalized_eigenvector = eigenvector / magnitude # Normalize the eigenvector by dividing each element by its magnitude
real_eigenvector = np.real(normalized_eigenvector) # Get the real part of the complex eigenvector

print("eigenvector of M corresponding to the largest eigenvalue is ", real_eigenvector)
print("PageRank Results:", r_values[-1])