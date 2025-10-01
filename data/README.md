# 📂 Data Folder  

This folder should contain the **dataset if imported via the Excel file**, as well as any **modified versions of the dataset obtained after feature engineering, preprocessing, or other transformations** during the project.  

---

## 📊 Dataset: UCI Credit Card Default  
- Source: [UCI Credit Card Default Dataset](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)  
- Rows: 30,000 credit card clients  
- Features: 23  
- Target: `Y_default payment next month`  

---

## 📥 Option 1: Download Excel file manually  
You can download the original Excel file (`default of credit card clients.xls`) directly from the [UCI repository](https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients) and place it in this folder.  

---

## ⚡ Option 2: Load via Python (recommended)  
You can fetch the dataset programmatically using the [`ucimlrepo`](https://pypi.org/project/ucimlrepo/) package.  

```bash
pip install ucimlrepo
```

```python
from ucimlrepo import fetch_ucirepo 
import pandas as pd

# Fetch dataset 
default_of_credit_card_clients = fetch_ucirepo(id=350)  

# Features and target as pandas DataFrames
X = default_of_credit_card_clients.data.features 
y = default_of_credit_card_clients.data.targets  

# Merge into one DataFrame
df = pd.concat([X, y], axis=1)
print(df.head())

# Metadata
print(default_of_credit_card_clients.metadata)  

# Variable information
print(default_of_credit_card_clients.variables)  
```

---

## 🔎 Notes  
- The programmatic option excludes the `ID` column (not needed for modeling).  
- Both methods produce the same 30,000 records with consistent feature/target values.  
