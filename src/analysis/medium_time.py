import pandas as pd

results_dataset = pd.read_csv('../../dataset/results_0.csv', delimiter=';')

print(results_dataset['time'].median())
