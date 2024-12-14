import pandas as pd

data = {
    'Kabupaten/Kota': [
        'Kabupaten Bogor', 'Kabupaten Sukabumi', 'Kabupaten Cianjur', 'Kabupaten Bandung',
        'Kota Bandung', 'Kota Bogor', 'Kota Bekasi', 'Kota Cimahi',
        'Kota Cirebon', 'Kabupaten Purwakarta', 'Kota Depok', 'Kabupaten Subang'
    ],
    'Produksi Sampah (ton/hari)': [
        971.59, 356.02, 355.69, 1489.04,
        1630, 567, 1923, 369,
        245, 384.43, 1469.77, 1012.45
    ],
    'Tahun': [
        2021, 2021, 2021, 2021,
        2020, 2020, 2020, 2020,
        2019, 2019, 2019, 2019
    ]
}

df = pd.DataFrame(data)

masukan_tahun = 2020
total_produksi = 0
for _, row in df.iterrows():
    if row['Tahun'] == masukan_tahun:
        total_produksi += row['Produksi Sampah (ton/hari)']

print(f"Total banyaknya produksi sampah di Jawa Barat pada tahun {masukan_tahun}: {total_produksi} ton/hari")

total_per_tahun_dict = {}
for _, row in df.iterrows():
    tahun = row['Tahun']
    produksi = row['Produksi Sampah (ton/hari)']
    if tahun in total_per_tahun_dict:
        total_per_tahun_dict[tahun] += produksi
    else:
        total_per_tahun_dict[tahun] = produksi

total_per_tahun = pd.DataFrame(list(total_per_tahun_dict.items()), columns=['Tahun', 'Total Produksi (ton/hari)'])
print("\nTotal banyaknya produksi sampah per tahun di Kabupaten/Kota:")
print(total_per_tahun)

total_kota_per_tahun_dict = {}
for _, row in df.iterrows():
    kota = (row['Tahun'], row['Kabupaten/Kota'])
    produksi = row['Produksi Sampah (ton/hari)']
    if kota in total_kota_per_tahun_dict:
        total_kota_per_tahun_dict[kota] += produksi
    else:
        total_kota_per_tahun_dict[kota] = produksi

total_kota_per_tahun = pd.DataFrame(
    [(kt[0], kt[1], thn) for kt, thn in total_kota_per_tahun_dict.items()],
    columns=['Tahun', 'Kabupaten/Kota', 'Total Produksi (ton/hari)']
)
print("\nTotal produksi sampah pada Kabupaten/Kota per tahun:")
print(total_kota_per_tahun)

total_per_tahun.to_csv('total_per_tahun.csv', index=False)
total_kota_per_tahun.to_csv('total_per_kota_per_tahun.csv', index=False)

with pd.ExcelWriter('produksi_sampah.xlsx') as writer:
    total_per_tahun.to_excel(writer, sheet_name='Total sampah Per Tahun', index=False)
    total_kota_per_tahun.to_excel(writer, sheet_name='Total sampah Kota Per Tahun', index=False)
