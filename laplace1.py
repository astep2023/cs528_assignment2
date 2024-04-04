import numpy as np
import pandas as pd

df = pd.read_csv("adult.csv")
age_limit = 25

filtered_data = df[df['age'] > age_limit]

# Compute average age
average_age = filtered_data['age'].mean()

# Global sensitivity calculation
max_age = filtered_data['age'].max()
global_sensitivity = average_age - 26

# Laplace noise function
def add_laplace_noise(query_result, epsilon, sensitivity):
    scale = sensitivity / epsilon
    noise = np.random.laplace(0, scale)
    return query_result + noise

# Query result without noise
query_result = average_age

# Adding noise for 0.5-differential privacy
epsilon_0_5 = 0.5
noisy_result_0_5 = add_laplace_noise(query_result, epsilon_0_5, global_sensitivity)

# Adding noise for 1-differential privacy
epsilon_1 = 1
noisy_result_1 = add_laplace_noise(query_result, epsilon_1, global_sensitivity)

print("Query Result (Without Noise):", query_result)
print("Noisy Result (0.5-Differential Privacy):", noisy_result_0_5)
print("Noisy Result (1-Differential Privacy):", noisy_result_1)
