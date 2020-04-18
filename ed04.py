# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letter = str(input("\nEnter a letter: ").lower())
vowels = ["a", "e", "i", "o", "u"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
if letter in vowels:
    print("\nThis letter is a vowel.")
elif letter in numbers:
    print("\nThis is a number.")
else:
    print("\nThis letters isn't a vowel.")
