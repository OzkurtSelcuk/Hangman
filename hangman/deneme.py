import tkinter as tk
import random

# Kelime listesi
kelimeler = ["python", "bilgisayar", "programlama", "yapayzeka", "oyun", "matematik", "istanbul", "java"]
secilen_kelime = random.choice(kelimeler)
tahmin_edilen = ["_"] * len(secilen_kelime)
yanlis_tahminler = []
hak = 6

# Fonksiyon: Harf tahmini işlemi
def tahmin_et():
    global hak
    harf = giris.get().lower()
    giris.delete(0, tk.END)

    if len(harf) != 1 or not harf.isalpha():
        bilgi_label.config(text="⚠️ Lütfen tek bir harf girin.")
        return
    if harf in tahmin_edilen or harf in yanlis_tahminler:
        bilgi_label.config(text="⚠️ Bu harfi zaten denedin.")
        return

    if harf in secilen_kelime:
        for i, karakter in enumerate(secilen_kelime):
            if karakter == harf:
                tahmin_edilen[i] = harf
        bilgi_label.config(text="✅ Doğru tahmin!")
    else:
        yanlis_tahminler.append(harf)
        hak -= 1
        bilgi_label.config(text="❌ Yanlış tahmin!")

    # Güncellemeleri yansıt
    kelime_label.config(text=" ".join(tahmin_edilen))
    hak_label.config(text=f"Kalan Hak: {hak}")
    yanlis_label.config(text="Yanlış Harfler: " + ", ".join(yanlis_tahminler))

    if "_" not in tahmin_edilen:
        bilgi_label.config(text="🎉 Tebrikler, kelimeyi buldun!")
        tahmin_butonu.config(state=tk.DISABLED)
    elif hak == 0:
        bilgi_label.config(text=f"😢 Oyun bitti! Kelime: {secilen_kelime}")
        tahmin_butonu.config(state=tk.DISABLED)

# Arayüz kurulumu
pencere = tk.Tk()
pencere.title("Adam Asmaca - Tkinter")
pencere.geometry("500x300")
pencere.resizable(False, False)

kelime_label = tk.Label(pencere, text=" ".join(tahmin_edilen), font=("Arial", 24))
kelime_label.pack(pady=20)

hak_label = tk.Label(pencere, text=f"Kalan Hak: {hak}", font=("Arial", 14))
hak_label.pack()

yanlis_label = tk.Label(pencere, text="Yanlış Harfler: ", font=("Arial", 12))
yanlis_label.pack(pady=5)

giris = tk.Entry(pencere, font=("Arial", 14), width=5, justify="center")
giris.pack()

tahmin_butonu = tk.Button(pencere, text="Tahmin Et", font=("Arial", 12), command=tahmin_et)
tahmin_butonu.pack(pady=10)

bilgi_label = tk.Label(pencere, text="", font=("Arial", 12))
bilgi_label.pack()

pencere.mainloop()
