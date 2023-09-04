import pandas as pd

def excel_to_csv(excel_file, csv_file):         # kodun uzun hali
    try:
        # Excel dosyasını pandas kütüphanesiyle okuyun
        df = pd.read_excel(excel_file)

        # DataFrame'i CSV dosyasına yazın
        df.to_csv(csv_file, index=False)

        print("Başarıyla dönüştürüldü!")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    excel_file = "test12.xlsx"  # Dönüştürmek istediğiniz Excel dosyasının adını buraya yazın
    csv_file = "dosya.csv"     # CSV dosyasının adını buraya yazın
    excel_to_csv(excel_file, csv_file)