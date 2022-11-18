# List of animes (First list item is the Genre)
genres = [
    ["Action", "Hunter × Hunter", "Fire Force", "Akame ga Kill"],
    ["Chill", "My Neighbor Totoro", "Girls'Last Tour", "Komi can’t communicate"],
    ["Mystery", "Great Pretender", "Death Note", "Black Butler"],
    ["Comedy", "Mob Psycho 100", "Bloodline Blockade", "Blood Lad"],
]
print("----------------------------------------")
print("What type of Anime Genre do you want ?\n")
# Gets input and saves it as "input"
input = input("Action | Chill | Mystery | Comedy  : ")
print("---------------------------------------- \n")
# Getting every genre comparing it with the input and printing the animes
# If the Genre is not found an Error message will print
for i in genres:
    if i[0] == input:
        print(input + " Animes: ", end="")
        print(*i[1:], sep=", ")
        break
else:
    print("Looks like we dont have the Genre " + input + "（ ´Д｀；）")
print("----------------------------------------")
