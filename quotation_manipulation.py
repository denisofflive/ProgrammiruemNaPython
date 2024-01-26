# Манипуляции с цитатой
# Демонстрирует строковые методы

# цитата из Томаса Уотсона. который в 1943 г. был директором IBM
quote = "I think there is a world market for maybe five computers."

print("Original quote:")
print(quote)

print("\nIn uppercase:")
print(quote.upper())

print("\nIn lowercase:")
print(quote.lower())

print("\nAs a title:")
print(quote.title())

print("\nWith a minor replacement:")
print(quote.replace("five", "millions of"))

print("\nOriginal quote is still:")
print(quote)

input("\n\nPress the enter key to exit.")
