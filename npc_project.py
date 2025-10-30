import random
traits = [
    "energetic", "smart", "brave", "adventurous", "curious", "creative",
    "stoic", "empathetic", "witty", "loyal", "ambitious", "calm",
    "playful", "reckless", "cautious", "observant", "stubborn",
    "cheerful", "mysterious", "hangry",
]
names = [
    "Aria", "Finn", "Mira", "Thorne", "Lila", "Kade", "Rowan", "Sylas",
    "Nia", "Jax", "Eira", "Bram", "Soren", "Lyra", "Kai", "Maeve",
    "Orion", "Zara", "Hugo", "Tessa", "Elias", "Rhea", "Dorian", "Ivy",
    "Pax", "Seraph", "Elowen", "Garrick", "Isla", "Milo", "Fen", "Vesper",
    "Nolan", "Cora", "Lucan", "Petra", "Ash", "Nova", "Theo", "Beck",
]
lvl = (range(1,100))
person = input("Generate NPC? Yes/No:")
if person == "yes" or "Yes":
    npc_name = random.choice(names)
    npc_trait = random.choice(traits).capitalize()
    npc_level = random.choice(lvl)
    npc_height = random.uniform(4.5, 7.0).__round__(2)
    print(f"Random NPC generated. Name is: {npc_name}, Trait: {npc_trait}, lvl: {npc_level}")
else:
    print("Wow. At least test your code man")
talking =  input("Do you want to talk to them? Yes/No:")
if talking == "yes" or "Yes":
    print(f"\n\t\t\t\t-------{npc_name}-------")
    print(f"|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
            |Hi I'm {npc_name}, I'm lvl {npc_level}. I am very {npc_trait} and I am {npc_height} ft tall. Its nice to meet you! Feel free to adventure and look around the village!|
            |----------------------------------------------------------------------------------------------------------------------------------------------------------------------|")

else:
    print("At least be polite, you created them and now you ignore them. Shame.")