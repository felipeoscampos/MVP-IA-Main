def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():

    celsius = float(input("Digite a temperatura em graus Celsius: "))
    
    fahrenheit = celsius_para_fahrenheit(celsius)
    
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
