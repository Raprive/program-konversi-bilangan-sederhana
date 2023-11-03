def biner_to_desimal(num):
	hasil = int(num, base=2)
	return ["biner ke desimal", hasil]


def desimal_to_biner(num):
	hasil = bin(int(num))
	hasil = str(hasil).removeprefix("0b")
	return ["desimal ke biner", hasil]


def biner_to_hex(num):
	hasil = hex(biner_to_desimal(num)[1])
	return ["biner ke heksadesimal", hasil]


def hex_to_biner(num):
	hasil = bin(hex_to_desimal(num)[1])
	hasil = str(hasil).removeprefix("0b")
	return ["heksadesimal ke biner", hasil]


def desimal_to_hex(num):
	hasil = hex(int(num))
	return ["desimal ke heksadesimal", hasil]


def hex_to_desimal(num):
	hasil = int(num, base=16)
	return ["heksadesimal ke desimal", hasil]


def main():
	while True:
		print("="*30)
		print("Silakan masukan salah satu pilihan: ")
		print("1. Biner ke desimal")
		print("2. Desimal ke biner")
		print("3. Biner ke hexa")
		print("4. Hexa ke biner")
		print("5. Desimal ke hexa")
		print("6. Hexa ke desimal")
		print("0. Keluar")
		pilihan = int(input("Masukkan pilihan: "))

		if pilihan == 0: return;

		if not (0 <= pilihan <= 6): continue;

		num = input("Masukkan angka yang ingin dikonversi: ")

		match (pilihan):
			case 1: hasil = biner_to_desimal(num)
			case 2: hasil = desimal_to_biner(num)
			case 3: hasil = biner_to_hex(num)
			case 4: hasil = hex_to_biner(num)
			case 5: hasil = desimal_to_hex(num)
			case 6: hasil = hex_to_desimal(num) 

		print(f"Hasil konversi dari bilangan {hasil[0]} adalah {hasil[1]}")


if __name__ == "__main__":
	main()
