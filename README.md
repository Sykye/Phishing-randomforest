# 📧 Deteksi Phishing Email Menggunakan Random Forest

Repositori ini berisi implementasi kode Python untuk mendeteksi email phishing, baik yang dibuat oleh manusia maupun oleh model AI (LLM) seperti ChatGPT dan WormGPT. Pendekatan ini menggunakan metode ekstraksi fitur TF-IDF dan algoritma Random Forest untuk klasifikasi.

---

## 📁 Struktur File

| File                | Fungsi                                      |
|---------------------|---------------------------------------------|
| `preprocessing.py`  | Membersihkan dan menggabungkan dataset dari berbagai sumber |
| `model_training.py` | Mengubah teks menjadi TF-IDF, melatih model, dan mengevaluasi hasil |
| `cleaned_dataset.csv` | Dataset hasil preprocessing (opsional)      |

---

## 📊 Hasil Evaluasi Model

Model Random Forest menunjukkan performa sangat baik dengan hasil:

| Metrik     | Legitimate (0) | Phishing (1) |
|------------|----------------|--------------|
| Precision  | 1.0000         | 0.9699       |
| Recall     | 0.9817         | 1.0000       |
| F1-Score   | 0.9908         | 0.9847       |
| **Akurasi Total** | **0.9885** |              |

---

## 🔧 Teknologi

- Python 3.10+
- Scikit-learn
- Pandas
- TfidfVectorizer

---

## 📄 Sumber Dataset

Dataset berasal dari paper:
> *David versus Goliath: Can Machine Learning Detect LLM-Generated Text? A Case Study in the Detection of Phishing Emails*  
> ITASEC 2024 – F. Greco, G. Desolda, A. Esposito, A. Carelli.

---

## 🧠 Catatan

Repositori ini dibuat sebagai bagian dari proyek tugas akhir untuk mendeteksi serangan email phishing berbasis teks. Harap tidak digunakan untuk aktivitas yang melanggar etika atau hukum.

