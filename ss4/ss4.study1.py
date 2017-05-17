while True:
    a= input("Nhap:")
    letter_counts = {}
    for letter in a:
        letter_counts[letter] = letter_counts.get(letter, 0) +1
        print(letter_counts)
