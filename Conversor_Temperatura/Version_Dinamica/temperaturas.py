

# --------------------------------------------
# Conversion escala Kelvin
def kelvinToCelsius(x):
    return x - 273.75


def kelvinToFahrenheit(x):
    return x * float(9) / 5 - 459.67


# --------------------------------------------
# Conversion escala Celsius
def celsiusToKelvin(x):
    return x + 273.15


def celsiusToFahrenheit(x):
    return x * float(9) / 5 + 32


# --------------------------------------------
# Conversion escala Fahrenheit
def fahrenheitToKelvin(x):
    return (x + 459.67) * float(5) / 9


def fahrenheitToCelsius(x):
    return (x - 32) * float(5) / 9
