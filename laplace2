import numpy as np
import pandas
import random
import math

df = pandas.read_csv("adult.csv")
age_limit = 25
average_age = 0
max_change = 0

filtered_data = df[df['age'] > age_limit]
filtered_data = filtered_data.drop(["income","race","education","marital-status","occupation","workclass", "fnlwgt", "educational-num", "relationship", "gender", "capital-gain", "capital-loss", "hours-per-week", "native-country"], axis=1)
max_age = filtered_data['age'].max()
min_age = filtered_data['age'].min()

# Compute average age
average_age = filtered_data['age'].mean()

if abs(max_age - average_age) > abs(min_age - average_age):
    max_change = abs(max_age - average_age)
else:
    max_change = abs(min_age - average_age)
# Inject noise into query result

def laplace_noise(scale_parameter):
    u = random.uniform(-0.5, 0.5)  
    noise = -scale_parameter * math.copysign(1.0, u) * math.log(1 - 2 * abs(u))
    return noise

noisy_average_age_05 = average_age + laplace_noise(max_change / 0.5)
noisy_average_age_1 = average_age + laplace_noise(max_change)

print(filtered_data)
print("Average age:", average_age)
print("Noisy average age for 0.5-DP:", noisy_average_age_05)
print("Noisy average age for 1-DP:", noisy_average_age_1) 
