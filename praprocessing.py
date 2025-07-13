import pandas as pd
import zipfile
import os

def load_and_clean_csv(filepath, label=None, source=None):
    try:
        df = pd.read_csv(filepath, engine="python", on_bad_lines='skip')
        
        # Identifikasi kolom isi email
        if 'text' in df.columns:
            df = df[['text']]
        elif 'body' in df.columns:
            df = df.rename(columns={'body': 'text'})
            df = df[['text']]
        else:
            df.columns = ['text']
        
        # Bersihkan teks
        df['text'] = df['text'].astype(str).str.strip()
        df = df[df['text'].str.len() > 5]
        
        # Tambahkan label dan source jika ada
        if label is not None:
            df['label'] = label
        if source is not None:
            df['source'] = source
        
        return df

    except Exception as e:
        print(f"❌ Gagal membaca {filepath}: {e}")
        return pd.DataFrame(columns=['text', 'label', 'source'])

if __name__ == "__main__":
    print("🚀 Mulai preprocessing...")

    # Ekstraksi jika belum diekstrak
    if os.path.exists("archive.zip"):
        with zipfile.ZipFile("archive.zip", 'r') as zip_ref:
            zip_ref.extractall("dataset")
        print("✅ ZIP berhasil diekstrak.")
    else:
        print("❌ File ZIP tidak ditemukan.")
        exit()

    # Muat masing-masing dataset
    paths = {
        "dataset/human-generated/phishing.csv":  (1, "human"),
        "dataset/human-generated/legit.csv":     (0, "human"),
        "dataset/llm-generated/phishing.csv":    (1, "ai"),
        "dataset/llm-generated/legit.csv":       (0, "ai")
    }

    all_dfs = []
    for path, (label, source) in paths.items():
        df = load_and_clean_csv(path, label=label, source=source)
        print(f"✅ {path} dimuat, jumlah data: {len(df)}")
        all_dfs.append(df)

    # Gabungkan
    df_full = pd.concat(all_dfs, ignore_index=True)

    # Cek hasil
    print("\n📊 Distribusi label:")
    print(df_full['label'].value_counts())
    print("\n📊 Sumber data:")
    print(df_full['source'].value_counts())

    # Simpan
    df_full.to_csv("cleaned_dataset.csv", index=False)
    print("\n💾 Dataset hasil preprocessing disimpan ke 'cleaned_dataset.csv'")

