import csv

file = open("raw_titles1.csv", "r", encoding="utf-8-sig")
#Functions reader from library
reader = csv.reader(file)
#Heading in the csv
header = next(reader)

#Delete column "id" (header)
del header[1]
#Delete column "imdb_id" (header)
del header[9]
#Add column "Quantity Genres" (header)
header.append("Quantity Genre")

file_new = open("raw_titles_new1.csv", "w", encoding="utf-8-sig", newline='')
#Function writer from library
writer = csv.writer(file_new)
# Write header in the clean csv
writer.writerow(header)

#Create a dictionary of age certificate for each film's labels
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

# Use for each row in the csv file
for row in reader:
    #Delete column "id" (row)
    del row[1]
    #Delete column "imdb_id" (row)
    del row[9]

    #Check the above rows, if empty replace it with 0
    if row[8] == "":
        row[8] = '0'
    if row[4] == "":
        row[4] = '0'
    if row[9] == "":
        row[9] = '0'
    if row[10] == "":
        row[10] = '0'

    # Fix name, Use the python capitalize() method to return a string where the 
    # first character is uppercase and the rest is lowercase.
    name_film = row[1].capitalize()
    row[1] = name_film

    # Convert the above rows from string to int
    row[8] = int(float(row[8])) # row "seasons"
    row[9] = int(float(row[9])) # row "imdb_score"
    row[10] = int(row[10]) # row "imdb_votes"

    # Remove "['']" and "\'" use strip() and replace()
    genres = row[6].strip("['']").replace("\'", '')
    row[6] = genres

    # Remove "[]" and "\'" use strip() and replace()
    # Use replace() to change the abbreviations of a country name to a specific country name
    product_count = row[7].replace("\'", '').strip("[]")
    row[7] = product_count.replace("BS", "Bahamas").replace("FO", "Faroe Islands").replace("NZ", "New Zealand").replace("GR", "Greece").replace("US", "The United States").replace("GB","The United Kingdom").replace("BF", "Burkina Faso").replace("AU", "Australia").replace("JP", "Japan").replace("EG", "Egypt").replace("DE", "Germany").replace("ES", "Spain").replace("MX", "Mexico").replace("CO", "Colombia").replace("IN", "India").replace("DZ", "Algeria").replace("LB", "Lebanon").replace("BE", "Belgium").replace("NO", "Na Uy").replace("FR", "France").replace("CA", "Canada").replace("SU", "The Soviet Union").replace("PS", "Palestine").replace("TR", "Turkey").replace("IT", "Italy").replace("BR", "Brasil").replace("PE", "Peru").replace("HK", "Hong Kong").replace("AR", "Argentina").replace("IE", "Ireland").replace("GH", "Ghana").replace("KR", "Korea").replace("BG", "Bulgaria").replace("CN", "People 'Republic of China").replace("RU", "Russia").replace("SG", "Singapore").replace("MA", "Roma").replace("UY", "Na Uy").replace("TW", "Taiwan").replace("DK", "Denmark").replace("MY", "Malaysia").replace("CH","China").replace("CL", "Chile").replace("KW", "Kuwait").replace("NG", "Nigeria").replace("ZA", "South Africa").replace("SA", "Saudi Arabia").replace("AT", "Austria").replace("NL", "Netherlands").replace("SE", "Sweden").replace("CZ", "Czech Republic").replace("PH", "Philippines").replace("TH", "Thailand").replace("AE", "United Arab Emirates").replace("HU", "Hungary").replace("ID", "Indonesia").replace("IL", "Israel").replace("FI", "Finland").replace("RO", "Romania").replace("CD", "Democratic Republic of the Congo").replace("PL", "Poland").replace("VE", "Venezuela").replace("IS", "Iceland").replace("NZ", "New Zealand").replace("UA", "Ukraine").replace("IR", "Iran").replace("JO", "Jordan").replace("QA", "Qatar").replace("HR", "Croatia").replace("SY", "Syria").replace("VN", "Vietnam").replace("PR", "Puerto Rico").replace("IQ", "Iraq").replace("KH", "Cambodia").replace("CU", "Cuba").replace("LU", "Luxembourg").replace("KE", "Kenya").replace("RS", "Serbia").replace("AL", "Albania").replace("TZ", "Tanzania").replace("GE", "Georgia").replace("ZW", "Zimbabwe").replace("CM", "Cameroon").replace("PK", "Pakistan").replace("BD", "Bangladesh").replace("CY", "Cyprus").replace("LT", "Lithuania").replace("MW", "Malawi").replace("PT", "Portugal").replace("AO", "Angola").replace("GT", "Guatemala").replace("MZ", "Mozambique").replace("AF", "Afghanistan").replace("NA", "Namibia").replace("IO", "British Indian Ocean Territory")

    # age_certification change to number by age
    # Use for each to iterate over each item in "row" where "index" is the index and "value" is the value of each item. 
    # And the enumerate() function is used to add a counter for the index to the list
    for index, value in enumerate(row):
        print(f'{index}: {value}')
        # Check if the value is in the pre-initialized age dictionary
        if value in age_dict:
            # Replace any age value found in "row" with the value in "age_dict"
            row[index] = age_dict[value]

    # Covert str to list
    str = row[6].split()
    # Get the number in each genre
    quantity_genre = len(str)
    #add quantity genre number row
    row.append(quantity_genre)
    
    # write row in the clean csv
    writer.writerow(row)

print("Done")
# close old file and new file
file.close()
file_new.close()