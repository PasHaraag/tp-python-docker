def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

if __name__ == "__main__":
    try:
        celsius = float(input("Entrez la température en °C : "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        print("Veuillez entrer une valeur numérique.")
