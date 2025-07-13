import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

print("🚀 Memulai pelatihan model...")

# 1. Muat dataset yang telah diproses dari tahap preprocessing
df = pd.read_csv("cleaned_dataset.csv")
print(f"✅ Data dimuat: {df.shape[0]} baris")

# 2. TF-IDF vektorisasi terhadap kolom 'text'
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(df["text"])
y = df["label"]

print(f"✅ TF-IDF selesai: {X.shape[0]} dokumen, {X.shape[1]} fitur")

# 3. Bagi data menjadi 70% latih dan 30% uji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(f"✅ Data dibagi: {X_train.shape[0]} latih, {X_test.shape[0]} uji")

# 4. Buat dan latih model Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42)
rf.fit(X_train, y_train)
print("✅ Model Random Forest berhasil dilatih")

# 5. Lakukan prediksi
y_pred = rf.predict(X_test)

# 6. Evaluasi hasil
print("\n📊 Hasil Evaluasi Model:")
print(classification_report(y_test, y_pred, digits=4))
