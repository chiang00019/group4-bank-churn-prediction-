import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/BankChurners.csv')

sns.countplot(x='Attrition_Flag', data=df)
plt.title('customer churn distribution')
plt.show() 