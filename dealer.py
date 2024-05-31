
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')
  time.sleep(1)
def otp(length):
  characters = string.ascii_letters + string.digits
  otp = ''.join(random.choice(characters) for i in range(length))
  return otp


def resend_otp() :
  print(Fore.RED + "Kode OTP salah, anda telah melewati batas percobaan.")
  print("1. Kirim ulang kode OTP")
  print("2. Kembali ke Awal")
  print("Atau bisa menghubungi layanan hotline kami 08223-3421")
  choose = int(input("Pilihanmu: "))
  if choose == 1:
    payment()
  elif choose == 2:
    start()
  else:
    print(Fore.RED + "Pilihan tidak tersedia, Coba lagi")
    resend_otp()
def payment():
    chance = 3
    otp_code = otp(6)
    for i in range(3):
        time.sleep(3.5)
        otp_user = input(f"kami telah menerima Pembayaran anda silahkan masukan kode OTP untuk Komfirmasi= {Fore.BLUE + otp_code}: ")
        if otp_user == otp_code:
            print("Kami Sedang Menyiapkan Pesanan Anda")
            for i in loader(range(100), colour='green', desc='Mengecek Pembayaran'):
                time.sleep(random.uniform(0.1, 0.01))
            print(Fore.GREEN + 'Terima kasih, pesanan anda akan kami kirim.')
            print(Fore.GREEN + f'Senang melayani anda {name_guest}, Have a Good Day:)')
            break
        else:
            if i < 2:
                print(Fore.RED + f"Kode OTP salah, anda masih punya kesempatan {chance -1} kali lagi ")
                chance -= 1
            else:
              resend_otp()

def greeting():
  clear_terminal()
  global name_guest
  print('-----Hai Selamat Pagi Ada yang bisa kami bantu -----')
  time.sleep(0.6)
  print("-----Perkenal kan Nama saya MIMI saya akan memandu anda untuk memilih mobil impian anda------")
  time.sleep(0.6)
  print("----- sebelum lanjut, Jika Berkenan Boleh kah MIMI tahu Nama Anda ? ")
  
  name_guest = input("Siapakah Nama Anda: ")
  time.sleep(0.6)
  print("Salam Kenal :)")
  print(f"Selamat Datang Saudara {name_guest} di Toko kami")

  time.sleep(0.8)
  print("----Berikut Merupakan List Mobil yang kami Punya")  
  time.sleep(2.5)
  
  
  
def isTransaction():
  global transaction
  print("1. lanjut ke Pembelian")
  print("2. back")
  while True:
    choose = input("Choose: ")
    if choose.isdigit():
      choose = int(choose)
      if choose == 1:
        transaction = True
        break 
      elif choose == 2:
        transaction = False
        break
      else : 
        print("Pilihan tidak tersedia, Coba lagi")
    else :
        print("Pilihan tidak tersedia, Coba lagi")
  
# 5
def page_transaction():
  clear_terminal()
  global car_id
  global car_series
  global transaction
  global car_price
  global car_year
  global car_brand
  found = False
  transaction = False
  
  showCar(car_id, car_series)
  cars_data = cars[car_id].get(car_series)
  
  while not found:
    pilih_mobil = input('Pilih mobil impianmu mana yang kamu inginkan (no / series): ').lower()
    for  car in cars_data:
      if pilih_mobil == car['series'].lower() or pilih_mobil == car['no'] :
        found = True
        car_series = car['series']
        car_price = car['price']
        car_year = car['year']
        print(Fore.MAGENTA + "Pilihan anda adalah " + car["series"] + Style.RESET_ALL)
        car_path = display_car(car_brand)
        displaying = Image.open(car_path)
        displaying.show()
        time.sleep(0.5)
        break
    if not found :
      print("Pilihan tidak tersedia, Coba lagi")
    
  while True :  
    confirm = input('apakah anda yakin dengan pilihan anda \n1. Yes \n2. No\nPilihanmu : ').lower()
    if confirm == '1' or confirm == 'yes':
      inputDataUser()
      break   
    elif confirm == '2' or confirm == 'no':
      start()
      break 
    else :
      print("Pilihan tidak tersedia, Coba Lagi")