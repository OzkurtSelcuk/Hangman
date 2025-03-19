import tkinter as tk
import random

class AdamAsmaca:
    def __init__(self, root):
        self.root = root
        self.root.title("Adam Asmaca")
        
        # Pencereyi ortalamak
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # Olası kelimeler listesi
        self.kelimeler = ["python", "bilgisayar", "programlama", "yapayzeka", "oyun", "matematik", "istanbul", "java"]
        # Rastgele bir kelime seç
        self.secilen_kelime = random.choice(self.kelimeler)
        self.tahmin_edilen = ["_"] * len(self.secilen_kelime)  # Başlangıçta boş çizgiler
        self.yanlis_tahminler = []
        self.hak = 6  # Maksimum yanlış tahmin hakkı

        # Ekran düzenlemeleri
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.label_tahmin = tk.Label(self.frame, text=" ".join(self.tahmin_edilen), font=("Helvetica", 20), width=20)
        self.label_tahmin.pack(pady=10)

        self.label_yanlis = tk.Label(self.frame, text="Yanlış Tahminler: ", font=("Helvetica", 14), width=20)
        self.label_yanlis.pack(pady=10)

        self.entry = tk.Entry(self.frame, font=("Helvetica", 20), width=5)
        self.entry.pack(pady=10)

        self.button = tk.Button(self.frame, text="Tahmin Et", command=self.tahmin_et, font=("Helvetica", 14))
        self.button.pack(pady=10)

        self.label_hak = tk.Label(self.frame, text=f"Kalan Hak: {self.hak}", font=("Helvetica", 14), width=20)
        self.label_hak.pack(pady=10)

    def tahmin_et(self):
        harf = self.entry.get().lower()  # Kullanıcıdan gelen harf

        # Eğer geçerli bir harf değilse, giriş kutusunu temizle ve çık
        if len(harf) != 1 or not harf.isalpha():
            self.entry.delete(0, tk.END)
            return

        # Daha önce tahmin edilmiş harfleri kontrol et
        if harf in self.tahmin_edilen or harf in self.yanlis_tahminler:
            self.entry.delete(0, tk.END)
            return

        # Harf doğruysa
        if harf in self.secilen_kelime:
            for i, karakter in enumerate(self.secilen_kelime):
                if karakter == harf:
                    self.tahmin_edilen[i] = harf
        else:
            # Yanlışsa, yanlış tahminlere ekle ve hakları azalt
            self.yanlis_tahminler.append(harf)
            self.hak -= 1

        # Etiketleri güncelle
        self.label_tahmin.config(text=" ".join(self.tahmin_edilen))
        self.label_yanlis.config(text="Yanlış Tahminler: " + ", ".join(self.yanlis_tahminler))
        self.label_hak.config(text=f"Kalan Hak: {self.hak}")
        
        # Oyun bitti mi? (Kelime tamamlandı ya da hak bitti)
        if "_" not in self.tahmin_edilen:
            self.label_tahmin.config(text="🎉 Tebrikler! Kelimeyi bildin: " + self.secilen_kelime)
            self.button.config(state="disabled")  # Butonu devre dışı bırak
        elif self.hak <= 0:
            self.label_tahmin.config(text="😢 Üzgünüm, kaybettin! Doğru kelime: " + self.secilen_kelime)
            self.button.config(state="disabled")  # Butonu devre dışı bırak
        
        # Entry kutusunu temizle
        self.entry.delete(0, tk.END)

# Tkinter penceresini başlat
root = tk.Tk()
oyun = AdamAsmaca(root)
root.mainloop()
