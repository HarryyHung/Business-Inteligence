import csv

file = open("raw_titles1.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)
header = next(reader)

del header[1]
del header[9]
header.append("Quantity Genre")

file_new = open("raw_titles_new1.csv", "w", encoding="utf-8-sig", newline='')
writer = csv.writer(file_new )
writer.writerow(header)

age_dict = {"TV-MA": "18+", "R": "17+",
            "NC-17": "17-18+", "PG": "18+",
            "TV-PG": "18+", "TV-14": "14+",
            "G": "All Ages", "TV-G": "All Ages",
            "PG-13": "13+", "TV-Y": "5+",
            "TV-Y7": "7+"}

# count_dict = {"US": "The United States", "GB": "The United Kingdom", "BF": "Burkina Faso", "AU": "Australia",
#               "JP": "Japan", "EG": "Egypt", "DE": "Germany", "ES": "Spain", "MX": "Mexico", "CO": "Colombia",
#               "IN": "India", "DZ": "Algeria", "LB": "Lebanon", "BE": "Belgium", "NO": "Na Uy",
#               "FR": "France", "CA": "Canada", "SU": "The Soviet Union", "PS": "Palestine", "TR": "Turkey",
#               "IT": "Italy", "BR": "Brasil", "PE": "Peru", "HK": "Hong Kong", "AR": "Argentina",
#               "IE": "Ireland", "GH": "Ghana",
#               }

for row in reader:
    del row[1]
    del row[9]

    if row[8] == "":
        row[8] = '0'
    if row[4] == "":
        row[4] = '0'
    if row[9] == "":
        row[9] = '0'
    if row[10] == "":
        row[10] = '0'

    # Fix name
    title = row[1].capitalize()
    row[1] = title

    # Convert to int
    row[8] = int(float(row[8]))
    row[9] = int(float(row[9]))
    row[10] = int(float(row[10]))

    # Remove "[]"
    genres = row[6].strip("['']").replace("\'", '')
    row[6] = genres

    product_count = row[7].replace("\'", '').strip("[]")
    row[7] = product_count.replace("BS", "Bahamas").replace("FO", "Faroe Islands").replace("NZ", "New Zealand").replace("GR", "Greece").replace("US", "The United States").replace("GB","The United Kingdom").replace("BF", "Burkina Faso").replace("AU", "Australia").replace("JP", "Japan").replace("EG", "Egypt").replace("DE", "Germany").replace("ES", "Spain").replace("MX", "Mexico").replace("CO", "Colombia").replace("IN", "India").replace("DZ", "Algeria").replace("LB", "Lebanon").replace("BE", "Belgium").replace("NO", "Na Uy").replace("FR", "France").replace("CA", "Canada").replace("SU", "The Soviet Union").replace("PS", "Palestine").replace("TR", "Turkey").replace("IT", "Italy").replace("BR", "Brasil").replace("PE", "Peru").replace("HK", "Hong Kong").replace("AR", "Argentina").replace("IE", "Ireland").replace("GH", "Ghana").replace("KR", "Korea").replace("BG", "Bulgaria").replace("CN", "People 'Republic of China").replace("RU", "Russia").replace("SG", "Singapore").replace("MA", "Roma").replace("UY", "Na Uy").replace("TW", "Taiwan").replace("DK", "Denmark").replace("MY", "Malaysia").replace("CH","China").replace("CL", "Chile").replace("KW", "Kuwait").replace("NG", "Nigeria").replace("ZA", "South Africa").replace("SA", "Saudi Arabia").replace("AT", "Austria").replace("NL", "Netherlands").replace("SE", "Sweden").replace("CZ", "Czech Republic").replace("PH", "Philippines").replace("TH", "Thailand").replace("AE", "United Arab Emirates").replace("HU", "Hungary").replace("ID", "Indonesia").replace("IL", "Israel").replace("FI", "Finland").replace("RO", "Romania").replace("CD", "Democratic Republic of the Congo").replace("PL", "Poland").replace("VE", "Venezuela").replace("IS", "Iceland").replace("NZ", "New Zealand").replace("UA", "Ukraine").replace("IR", "Iran").replace("JO", "Jordan").replace("QA", "Qatar").replace("HR", "Croatia").replace("SY", "Syria").replace("VN", "Vietnam").replace("PR", "Puerto Rico").replace("IQ", "Iraq").replace("KH", "Cambodia").replace("CU", "Cuba").replace("LU", "Luxembourg").replace("KE", "Kenya").replace("RS", "Serbia").replace("AL", "Albania").replace("TZ", "Tanzania").replace("GE", "Georgia").replace("ZW", "Zimbabwe").replace("CM", "Cameroon").replace("PK", "Pakistan").replace("BD", "Bangladesh").replace("CY", "Cyprus").replace("LT", "Lithuania").replace("MW", "Malawi").replace("PT", "Portugal").replace("AO", "Angola").replace("GT", "Guatemala").replace("MZ", "Mozambique").replace("AF", "Afghanistan").replace("NA", "Namibia").replace("IO", "British Indian Ocean Territory")

    # Covert str to list
    str = row[6].split()

    # age_certification đổi sang số theo độ tuổi and country đổi thành tên nước cụ thể
    for index, value in enumerate(row):
        if value in age_dict:
            row[index] = age_dict[value]
    
    # thêm cột số lượng genre
    quantity_genre = len(str)
    row.append(quantity_genre)

    writer.writerow(row)

print("Done")
file.close()
file_new.close()
