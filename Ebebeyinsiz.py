# Ebebeyinsiz kod
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("student_data.csv")

df = df[["studytime", "G1", "G2", "G3"]]

X = df[["studytime", "G1", "G2"]]  # Akademik ilgi ve önceki notlar
y = df["G3"]  # Hedef: son not

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)

# Değerlendirme
mse = mean_squared_error(y_test, y_pred)
op = model.score(X_test, y_test)  # R^2 doğruluk skoru

# Çıktılar
print(f"Ortalama Kare Hata (MSE): {mse:.2f}")
print(f"Modelin R^2 doğruluk skoru: {op:.4f}")
print(f"accuracy = {op * 100:.2f}")
print(f"\nBu model, test verisi üzerinde yaklaşık %{op * 100:.2f} doğruluk sağlamaktadır.")
