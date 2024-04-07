import pandas as pd
import math
import random

df = pd.read_csv('adult.csv')

# Compute frequency counts for each "Education" category
education_values = data['education'].value_counts()
most_frequent_education = education_values.idxmax()

# (a) Compute Global Sensitivity
global_sensitivity = education_values.max() - education_values.min()

# The exponential mechanism function
def exponential_mechanism(epsilon):
    # Compute Utility Scores
    def compute_utility_score(sensitivity, epsilon):
        utility_scores = dict()
        for education, values in education_values.items():
            utility_scores[education] = math.exp(epsilon * values / (2 * sensitivity))
        return utility_scores

    utility_scores = compute_utility_score(global_sensitivity, epsilon)

    # Compute total utility for normalization
    total_utility = sum(utility_scores.values())

    # Compute probabilities
    def compute_probabilities(utility_scores, total_utility):
        probabilities = dict()
        for education, utility in utility_scores.items():
            probabilities[education] = utility / total_utility
        return probabilities

    probabilities = compute_probabilities(utility_scores, total_utility)

    # Generate noisy probabilities for epsilon.

    def generate_noisy_probabilities(probabilities, epsilon):
        noisy_probabilities = dict()
        for education, probability in probabilities.items():
            noisy_probabilities[education] = probability * math.exp(epsilon)
        return noisy_probabilities

    noisy_probabilities = generate_noisy_probabilities(probabilities, epsilon)

    # (b) Generate Noisy Result
    def generate_noisy_result(probabilities):
        random_value = random.random()
        cumulative_probability = 0.0
        for education, probability in probabilities.items():
            cumulative_probability += probability
            if random_value <= cumulative_probability:
                return education

    noisy_result = generate_noisy_result(noisy_probabilities)
    return noisy_result

print("Query Result (Without Noise):", most_frequent_education)

epsilon_0_5 = 0.5
epsilon_1 = 1.0

print("Noisy Result (0.5-Differential Privacy):", exponential_mechanism(epsilon_0_5))
print("Noisy Result (1-Differential Privacy):", exponential_mechanism(epsilon_1))