# 🏦 Credit Card Customer Dataset 字段說明

## 字段總覽 Table of Contents

1. [CLIENTNUM](#CLIENTNUM)
2. [Attrition\_Flag](#Attrition_Flag)
3. [Customer\_Age](#Customer_Age)
4. [Gender](#Gender)
5. [Dependent\_count](#Dependent_count)
6. [Education\_Level](#Education_Level)
7. [Marital\_Status](#Marital_Status)
8. [Income\_Category](#Income_Category)
9. [Card\_Category](#Card_Category)
10. [Months\_on\_book](#Months_on_book)
11. [Total\_Relationship\_Count](#Total_Relationship_Count)
12. [Months\_Inactive\_12\_mon](#Months_Inactive_12_mon)
13. [Contacts\_Count\_12\_mon](#Contacts_Count_12_mon)
14. [Credit\_Limit](#Credit_Limit)
15. [Total\_Revolving\_Bal](#Total_Revolving_Bal)
16. [Avg\_Open\_To\_Buy](#Avg_Open_To_Buy)
17. [Total\_Amt\_Chng\_Q4\_Q1](#Total_Amt_Chng_Q4_Q1)
18. [Total\_Trans\_Amt](#Total_Trans_Amt)
19. [Total\_Trans\_Ct](#Total_Trans_Ct)
20. [Total\_Ct\_Chng\_Q4\_Q1](#Total_Ct_Chng_Q4_Q1)
21. [Avg\_Utilization\_Ratio](#Avg_Utilization_Ratio)
22. [Naive\_Bayes\_Classifier\_\*](#Naive_Bayes_Classifier_)

---

## 1. CLIENTNUM

* **英文：** Client number. Unique identifier for the customer holding the account
* **中文：** 客戶編號。持有帳戶的客戶唯一識別碼
* **範例：** `768805383`

---

## 2. Attrition\_Flag

* **英文：** Internal event (customer activity) variable - if the account is closed then 1 else 0
* **中文：** 是否流失（內部事件）。如果帳戶已關閉則為 1，否則為 0
* **範例：** `0`（未流失），`1`（已流失）

---

## 3. Customer\_Age

* **英文：** Customer's Age in Years
* **中文：** 客戶年齡（歲）
* **範例：** `45`

---

## 4. Gender

* **英文：** M=Male, F=Female
* **中文：** 性別。M=男性，F=女性
* **範例：** `M`、`F`

---

## 5. Dependent\_count

* **英文：** Number of dependents
* **中文：** 受扶養人數
* **範例：** `3`

---

## 6. Education\_Level

* **英文：** Educational Qualification of the account holder (example: high school, college graduate, etc.)
* **中文：** 教育程度（例如：高中、大學畢業等）
* **範例：** `High School`、`College`、`Graduate`、`Unknown`

---

## 7. Marital\_Status

* **英文：** Married, Single, Divorced, Unknown
* **中文：** 婚姻狀態（已婚、單身、離婚、未知）
* **範例：** `Married`、`Single`、`Divorced`、`Unknown`

---

## 8. Income\_Category

* **英文：** Annual Income Category of the account holder (< \$40K, \$40K - 60K, \$60K - \$80K, \$80K-\$120K, > \$120K, Unknown)
* **中文：** 年收入級距（< \$40K、\$40K-\$60K、\$60K-\$80K、\$80K-\$120K、> \$120K、未知）
* **範例：** `< $40K`、`$40K - $60K`、`Unknown`

---

## 9. Card\_Category

* **英文：** Type of Card (Blue, Silver, Gold, Platinum)
* **中文：** 卡片類型（藍卡、銀卡、金卡、白金卡）
* **範例：** `Blue`、`Silver`、`Gold`、`Platinum`

---

## 10. Months\_on\_book

* **英文：** Period of relationship with bank
* **中文：** 與銀行往來月數
* **範例：** `39`

---

## 11. Total\_Relationship\_Count

* **英文：** Total no. of products held by the customer
* **中文：** 客戶持有產品總數
* **範例：** `5`

---

## 12. Months\_Inactive\_12\_mon

* **英文：** No. of months inactive in the last 12 months
* **中文：** 過去 12 個月內未活躍月份數
* **範例：** `2`

---

## 13. Contacts\_Count\_12\_mon

* **英文：** No. of Contacts in the last 12 months
* **中文：** 過去 12 個月內聯絡次數
* **範例：** `3`

---

## 14. Credit\_Limit

* **英文：** Credit Limit on the Credit Card
* **中文：** 信用卡額度
* **範例：** `12691`

---

## 15. Total\_Revolving\_Bal

* **英文：** Total Revolving Balance on the Credit Card
* **中文：** 信用卡循環餘額
* **範例：** `777`

---

## 16. Avg\_Open\_To\_Buy

* **英文：** Open to Buy Credit Line (Average of last 12 months)
* **中文：** 可用信用額度（近 12 個月平均）
* **範例：** `11964`

---

## 17. Total\_Amt\_Chng\_Q4\_Q1

* **英文：** Change in Transaction Amount (Q4 over Q1)
* **中文：** 交易金額變化（第四季相對第一季）
* **範例：** `1.335`

---

## 18. Total\_Trans\_Amt

* **英文：** Total Transaction Amount (Last 12 months)
* **中文：** 總交易金額（過去 12 個月）
* **範例：** `1144`

---

## 19. Total\_Trans\_Ct

* **英文：** Total Transaction Count (Last 12 months)
* **中文：** 交易次數（過去 12 個月）
* **範例：** `42`

---

## 20. Total\_Ct\_Chng\_Q4\_Q1

* **英文：** Change in Transaction Count (Q4 over Q1)
* **中文：** 交易次數變化（第四季相對第一季）
* **範例：** `1.625`

---

## 21. Avg\_Utilization\_Ratio

* **英文：** Average Card Utilization Ratio
* **中文：** 平均卡片利用率
* **範例：** `0.061`

---

## 22. Naive\_Bayes\_Classifier\_Attrition\_Flag\_Card\_Category\_Contacts\_Count\_12\_mon\_Dependent\_count\_Education\_Level\_Months\_Inactive\_12\_mon\_1 / \_2

* **英文：** Naive Bayes
* **中文：** 樸素貝氏分類器相關的預測特徵（一般作為自動化產生的特徵，若非模型訓練所需可刪除）
* **範例：** `0.9987`、`0.0013`

---

# 📋 範例數據 Example

| CLIENTNUM | Attrition\_Flag | Customer\_Age | Gender | Dependent\_count | Education\_Level | Marital\_Status | Income\_Category | Card\_Category | Months\_on\_book | Total\_Relationship\_Count | Months\_Inactive\_12\_mon | Contacts\_Count\_12\_mon | Credit\_Limit | Total\_Revolving\_Bal | Avg\_Open\_To\_Buy | Total\_Amt\_Chng\_Q4\_Q1 | Total\_Trans\_Amt | Total\_Trans\_Ct | Total\_Ct\_Chng\_Q4\_Q1 | Avg\_Utilization\_Ratio | Naive\_Bayes\_Classifier\_1 | Naive\_Bayes\_Classifier\_2 |
| --------- | --------------- | ------------- | ------ | ---------------- | ---------------- | --------------- | ---------------- | -------------- | ---------------- | -------------------------- | ------------------------- | ------------------------ | ------------- | --------------------- | ------------------ | ------------------------ | ----------------- | ---------------- | ----------------------- | ----------------------- | --------------------------- | --------------------------- |
| 768805383 | 0               | 45            | M      | 3                | Graduate         | Married         | \$60K-\$80K      | Blue           | 39               | 5                          | 2                         | 3                        | 12691         | 777                   | 11964              | 1.335                    | 1144              | 42               | 1.625                   | 0.061                   | 0.9987                      | 0.0013                      |

---

如果你還需要進一步的範例、加強某個解釋、或想把這份說明自動轉成表格，也可以直接告訴我！
