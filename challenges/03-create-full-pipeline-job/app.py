"""Temperature converter — write a pipeline to build and test this app."""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    c = 100
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f}°F")

    f = 32
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c}°C")


if __name__ == "__main__":
    main()
