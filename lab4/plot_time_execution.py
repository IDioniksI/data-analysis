import matplotlib.pyplot as plt
import seaborn as sns

operations = ['Reading and forming', 'Data cleaning', 'Normalization', 'Pearson correlation',
              'Spearman correlation', 'One hot encoding']

pandas_times = [7.4, 8.7, 0.03, 0.05, 1.0, 5.7]

numpy_times = [52.6, 3.1, 2.01, 4.3, 6.1, 7.7]

plt.figure(figsize=(12, 8))

with sns.color_palette("Set2"):
    sns.lineplot(x=operations, y=pandas_times, marker='o', label='pandas')
    sns.lineplot(x=operations, y=numpy_times, marker='o', label='numpy')
    plt.xlabel('Operations')
    plt.ylabel('Time (seconds)')
    plt.title('Time of execution for different operations')
    plt.legend()
    plt.xticks(rotation=15)
    plt.show()
