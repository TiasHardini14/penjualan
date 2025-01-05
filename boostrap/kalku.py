def tambah(a, b):
    """Return the sum of a and b."""
    return a + b

def kurang(a, b):
    """Return the difference of a and b."""
    return a - b

def kali(a, b):
    """Return the product of a and b."""
    return a * b

def bagi(a, b):
    """Return the division of a by b, handling division by zero."""
    if b == 0:
        return "Pembagian dengan nol tidak diperbolehkan."
    else:
        return a / b

def main():
    while True:
        # Display the menu of operations
        print("\nPilih Operasi:")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("0. Keluar")
        
        # Request input from the user
        operasi = input("Pilih operasi (1/2/3/4/0): ")

        # Exit the program if 0 is selected
        if operasi == "0":
            print("Keluar dari program.")
            break
        
        # Request two numbers as input
        try:
            bilangan1 = float(input("Masukkan bilangan pertama: "))
            bilangan2 = float(input("Masukkan bilangan kedua: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        
        # Perform the operation based on user choice
        if operasi == "1":
            hasil = tambah(bilangan1, bilangan2)
            print(f"Hasil: {bilangan1} + {bilangan2} = {hasil}")
        elif operasi == "2":
            hasil = kurang(bilangan1, bilangan2)
            print(f"Hasil: {bilangan1} - {bilangan2} = {hasil}")
        elif operasi == "3":
            hasil = kali(bilangan1, bilangan2)
            print(f"Hasil: {bilangan1} * {bilangan2} = {hasil}")
        elif operasi == "4":
            hasil = bagi(bilangan1, bilangan2)
            if isinstance(hasil, str):
                print(hasil)  # Display error message if division by zero
            else:
                print(f"Hasil: {bilangan1} / {bilangan2} = {hasil}")
        else:
            print("Pilihan tidak valid. Silakan pilih operasi yang benar.")

# Run the program
if __name__ == "__main__":
    main()
