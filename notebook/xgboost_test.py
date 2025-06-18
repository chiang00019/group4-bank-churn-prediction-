import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost_test import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import shap

df_train = pd.read_csv('data/bank_train.csv')
df_test = pd.read_csv('data/bank_test.csv')
# 拔掉UUID, 客戶編號, 以及兩個分類器的結果
Y_train = df_train['Attrition_Flag']
X_train = df_train.drop(columns=['Attrition_Flag', "CLIENTNUM"])

Y_test = df_test['Attrition_Flag']
X_test = df_test.drop(columns=['Attrition_Flag', "CLIENTNUM"])

print("原始特徵維度：", X_train.shape)

categorical_cols = X_train.select_dtypes(include='object').columns
print(f"需要進行 One-Hot Encoding 的類別型欄位: {list(categorical_cols)}")

X_train_encoded = pd.get_dummies(X_train, columns=categorical_cols, drop_first=True)
X_test_encoded = pd.get_dummies(X_test, columns=categorical_cols, drop_first=True)
print(f"One-Hot Encoding 後 Train 的特徵維度: {X_train_encoded.shape}")
print(f"One-Hot Encoding 後 Test 的特徵維度: {X_test_encoded.shape}")

label_encoder = LabelEncoder()
Y_train_encoded = label_encoder.fit_transform(Y_train)
Y_test_encoded = label_encoder.fit_transform(Y_test)
print(f"\n目標變數編碼對應關係: {label_encoder.classes_} -> {label_encoder.transform(label_encoder.classes_)}")

print(f"\n訓練集目標變數分佈:")
print(pd.Series(Y_train).value_counts(normalize=True))  
print(f"\n測試集目標變數分佈:")
print(pd.Series(Y_test).value_counts(normalize=True))   

xgb_model = XGBClassifier(
    random_state=42,
    use_label_encoder=False, 
    eval_metric='logloss'    
)
xgb_model.fit(X_train_encoded, Y_train_encoded)

y_pred = xgb_model.predict(X_test_encoded)
y_pred_proba = xgb_model.predict_proba(X_test_encoded)[:, 1] # 預測為正例 (流失) 的機率

print("混淆矩陣：")
print(confusion_matrix(Y_test_encoded, y_pred))

print("\n分類報告 (Classification Report):")
print(classification_report(Y_test_encoded, y_pred, target_names=label_encoder.classes_))

fpr, tpr, thresholds_roc = roc_curve(Y_test_encoded, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

explainer = shap.TreeExplainer(xgb_model)
shap_values = explainer.shap_values(X_test_encoded)

plt.figure(figsize=(12, 8))
shap.summary_plot(shap_values, X_test_encoded, show=False)
plt.title("SHAP Summary Plot (Beeswarm)")
plt.show()

plt.figure(figsize=(12, 6))
shap.summary_plot(shap_values, X_test_encoded, plot_type="bar", show=False)
plt.title("SHAP Feature Importance (Bar Plot)")
plt.show()