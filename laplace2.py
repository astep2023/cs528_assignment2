import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('adult.csv')  # Update 'adult.csv' with the correct file path

# Consider only the 'education' column
education_counts = data['education'].value_counts()

# Determine the most frequent education category (without noise)
most_frequent_education = education_counts.idxmax()

# (a) Calculate Global Sensitivity
# Global Sensitivity of the most frequent "Education" query
sensitivity = education_counts.max() - education_counts.min()


# (b) Implement Exponential Mechanism
def exponential_mechanism(data, epsilon):
    # Calculate scores for each education category
    scores = data.value_counts()
    num_categories = len(scores)

    # Apply Laplace mechanism with numerical stabilization
    max_score = scores.max()
    exponent_input = epsilon * (scores - sensitivity / (2 * num_categories) - max_score)
    probabilities = np.exp(exponent_input) / np.sum(np.exp(exponent_input))

    # Generate a sample using the Exponential mechanism
    sampled_index = np.random.choice(scores.index, p=probabilities)
    return sampled_index


# Set differential privacy parameters
epsilon_1 = 0.5
epsilon_2 = 1.0

# Generate noisy results for ε = 0.5
noisy_result_0_5 = exponential_mechanism(data['education'], epsilon_1)

# Generate noisy results for ε = 1.0
noisy_result_1 = exponential_mechanism(data['education'], epsilon_2)

# Display results
print("Most Frequent Education (without noise):", most_frequent_education)
print("Global Sensitivity:", sensitivity)
print("Noisy Result (ε = 0.5):", noisy_result_0_5)
print("Noisy Result (ε = 1.0):", noisy_result_1)
