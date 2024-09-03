user_input = int(input("Enter amount of money (in Baht): "))

while user_input < 0:
    user_input = int(input("Enter amount of money (in Baht): "))


def calculate(value):
    baht_notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    counts = [] 

    for baht in baht_notes:
        count = value // baht
        counts.append(count)
        value -= count * baht

    return counts


counts = calculate(user_input)
baht_notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

for i in range(len(baht_notes)):
    if counts[i] > 0:
        print(f"{baht_notes[i]}-Baht notes: {counts[i]}")
