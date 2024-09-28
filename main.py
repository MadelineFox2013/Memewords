meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "NT":"İyi denemeydi",
            "EZ":"Kolaydı",
            "GG":"iyi oyundu",
            "NP":"Önemli Değil",
            "FF":"Teslim ol"
            "ROFL":"bir şakaya karşılık cevap"
            "SHEESH":"onaylamamak"
            "CREEPY":"korkunç"
            "AGGRO":"agresifleşmek/sinirlenmek"
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Böyle bir kelime bulunamadi")
