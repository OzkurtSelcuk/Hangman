import random

# Olası kelimeler listesi
kelimeler = ["python", "bilgisayar", "programlama", "yapayzeka", "oyun", "matematik","istanbul","java"]

# Rastgele bir kelime seç
secilen_kelime = random.choice(kelimeler)
tahmin_edilen = ["_"] * len(secilen_kelime)  # Boş harf çizgileri
yanlis_tahminler = []
hak = 6  # Maksimum yanlış tahmin hakkı

print("🎮 Adam Asmaca Oyununa Hoş Geldiniz!")
print(" ".join(tahmin_edilen))  # Başlangıçta boş çizgileri göster

while hak > 0 and "_" in tahmin_edilen:
    print(f"\nKalan Hak: {hak}")
    print(f"Yanlış Tahminler: {', '.join(yanlis_tahminler)}")
    
    harf = input("Bir harf tahmin et: ").lower()

    if len(harf) != 1 or not harf.isalpha():
        print("⚠️ Lütfen sadece tek bir harf girin!")
        continue
    
    if harf in tahmin_edilen or harf in yanlis_tahminler:
        print("⚠️ Bu harfi zaten tahmin ettin!")
        continue

    if harf in secilen_kelime:
        for i, karakter in enumerate(secilen_kelime):
            if karakter == harf:
                tahmin_edilen[i] = harf
    else:
        yanlis_tahminler.append(harf)
        hak -= 1

    print(" ".join(tahmin_edilen))  # Güncellenmiş tahmin durumu

# Oyun bitti, sonucu göster
if "_" not in tahmin_edilen:
    print("\n🎉 Tebrikler! Kelimeyi bildin:", secilen_kelime)
else:
    print("\n😢 Üzgünüm, kaybettin! Doğru kelime:", secilen_kelime)
