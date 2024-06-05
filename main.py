import subprocess


pliki_python = {
    1: "camera.py",
    2: "video.py",
}
moduly_opis = {
    1: "detekcja pinowych znaków drogowych z użyciem domyślnej kamery",
    2: "detekcja inowych znaków drogowych z wybranego nagrania wideo",
}
def uruchom_skrypt(wybrana_opcja):
    plik_python = pliki_python.get(wybrana_opcja)

    if plik_python:
        subprocess.run(["python", plik_python])
    else:
        print("Nieprawidowa opcja")

if __name__ == "__main__":
    while True:

        print("Moduły programu:")
        for i, plik in pliki_python.items():
            print(f"{i}: {plik} - {moduly_opis[i]}")
        print("q: Wyjdź")
        print()
        print()
        dane_wej = input("Wprowadź liczbę odpowiadającą części programu (q by zakończyć program): ")
        
        if dane_wej.lower() == 'q':
            break
        
        try:
            plik_cyfra = int(dane_wej)
            uruchom_skrypt(plik_cyfra)
        except ValueError:
            print("Nieprawidłowa opcja. Wprowadź poprawną liczbę lub 'q' by zakończyć program.")