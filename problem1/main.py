# input
student_score = 80

# Process: Your Solution Code Here
def penilaian_siswa(nilai):
    if 80 <= nilai <= 100:
        return 'A'
    elif 65 <= nilai <= 79:
        return 'B+'
    elif 50 <= nilai <= 64:
        return 'B'
    elif 35 <= nilai <= 49:
        return 'C'
    elif 0 <= nilai <= 34:
        return 'D'
    else:
        return 'Nilai tidak valid'
    
nama = input("Nama siswa/i : ")
nilai_numerik = float(input("Nilai siswa/i : "))

nilai_huruf = penilaian_siswa(nilai_numerik)

# Output "Nilai A"
print(f"{nama} mendapatkan nilai {nilai_huruf}.")
