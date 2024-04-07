import pandas
import random
import math

df = pandas.read_csv("adult.csv")
age_limit = 25
average_age = 0
max_change = 0

filtered_data = df[df['age'] > age_limit]

# Compute average age
average_age = filtered_data['age'].mean()

# (a) Calculate Global Sensitivity
max_age = filtered_data['age'].max()
global_sensitivity = average_age - 26

# (b) Implement Laplace Noisen Mechanism
def add_laplace_noise(query_result, epsilon, sensitivity):
    scale = sensitivity / epsilon
    u = random.uniform(-0.5, 0.5)  
    noise = (-scale * math.copysign(1.0, u) * math.log(1 - 2 * abs(u)))
    return query_result + noise

# Query result without noise
query_result = average_age

# Adding noise for 0.5-differential privacy
epsilon_0_5 = 0.5
noisy_result_0_5 = add_laplace_noise(query_result, epsilon_0_5, global_sensitivity)

# Adding noise for 1-differential privacy
epsilon_1 = 1.0
noisy_result_1 = add_laplace_noise(query_result, epsilon_1, global_sensitivity)

print("Query Result (Without Noise):", query_result)
print("Noisy Result (0.5-Differential Privacy):", noisy_result_0_5)
print("Noisy Result (1-Differential Privacy):", noisy_result_1)