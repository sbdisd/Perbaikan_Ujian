# Meminta input dari pengguna
n = int(input("Masukkan nilai n: "))

# Menghitung jumlah bilangan 1 hingga n
total = 0
for i in range(1, n + 1):
    total += i

# Menampilkan hasil
print(f"Jumlah bilangan dari 1 hingga {n} adalah {total}")
