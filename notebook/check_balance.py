import pandas as pd

train_data = pd.read_csv('data/bank_train.csv')
test_data = pd.read_csv('data/bank_test.csv')
y_train = train_data['Attrition_Flag']
y_test = test_data['Attrition_Flag']

# 計算訓練集中目標變數的比例
train_counts = y_train.value_counts(normalize=True)
print("\n訓練集目標變數分佈:\n", train_counts * 100)

# 計算測試集中目標變數的比例
test_counts = y_test.value_counts(normalize=True)
print("\n測試集目標變數分佈:\n", test_counts * 100)