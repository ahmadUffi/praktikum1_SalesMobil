from tabulate import tabulate


cars = [
    {
        'BestSeller': [
            {
              'series' : "bestSupra",
              'price' : 20000000,
              'year' : 2020,
            },
            {
              'series' : "bestMio",
              'price' : 30000000,
              'year' : 2020,
            },
            {
              'series' : "bestBeat",
              'price' : 30000000,
              'year' : 2020,
            }
        ],
        'CIVIC' : [
            {
              'series' : "turbo",
              'price' : 20000000,
              'year' : 2020,
            },
            {
              'series' : "r3",
              'price' : 30000000,
              'year' : 2020,
            },
            {
              'series' : "GTR",
              'price' : 30000000,
              'year' : 2020,
            }
        ],
        'BMW' : [
            {
              'series' : "BMWturbo",
              'price' : 20000000,
              'year' : 2020,
            },
            {
              'series' : "BMWr3",
              'price' : 30000000,
              'year' : 2020,
            },
            {
              'series' : "BMWGTR",
              'price' : 30000000,
              'year' : 2020,
            }
        ]
    }
]


# ini kerjaan gua

# Mendapatkan data CIVIC

civic_data = cars[0].get("CIVIC")

# Membuat header untuk tabel
headers = ["Series", "Price", "Year"]

# Membuat data dalam format yang sesuai untuk tabulate
table_data = [[car['series'], car['price'], car['year']] for car in civic_data]

# Menampilkan tabel
print(tabulate(table_data, headers, tablefmt="pretty"))

# showing WElcoming 
def showWelcoming():
    return "Welcome to Uler Dealers"


# memilih jenis yang dicari dan rekomendasi best seller 
    

# memunculkan mobil yang dipilih dan back sama pemebelian 


# lanjut transaksi 

#   input 







