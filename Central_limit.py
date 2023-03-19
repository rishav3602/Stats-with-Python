##  Central limit theorem
import numpy as np 
from statistics import mode 
import seaborn as sns

population = np.random.binomial(10,0.5,10000)
print(population)
print(len(population))

print(sns.distplot(population))

size = int(len(population)*0.30)
sample_mean = list()

for i in range (100):
    sample = np.random.choice(population,size=size)
    sample_mean.append(np.mean(sample))

print(sample_mean)
print(sns.distplot(sample_mean))


""" we do the same thing by increasing the number of samples just in order to get the most accurate value"""
for i in range (300):
    sample = np.random.choice(population,size=size)
    sample_mean.append(np.mean(sample))

print(sample_mean)
print(sns.distplot(sample_mean))


for i in range (500):
    sample = np.random.choice(population,size=size)
    sample_mean.append(np.mean(sample))

print(sample_mean)
print(sns.distplot(sample_mean))


for i in range (1000):
    sample = np.random.choice(population,size=size)
    sample_mean.append(np.mean(sample))
print(sample_mean)
print(sns.distplot(sample_mean))
