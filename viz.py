import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('data/customers.csv', sep=';')

def bar_sum(x, y):
    df_bar = df[[x, y]]
    df_bar = df_bar.groupby(by=[x], as_index=False).sum().sort_values(by=[y], ascending=False)
    df_bar[y] = df_bar[y] / 1000000
    plt.figure(figsize=(18, 6))
    plt.xticks(rotation=45)
    plt.title('Total {} by {} (m)'.format(y, x))
    return sns.barplot(x=x, y=y, data=df_bar);

