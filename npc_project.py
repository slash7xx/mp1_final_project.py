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
final_phrase = ["Feel free to look around the village.", "Good luck on the rest of your journey.", "Oh. And in case I don't see you again, good morning, good afternoon, and good night.", "I'm.... I'm.... I'm...........................SPONGEBOBBBBBBBBBB","ARSON CAN BENCH PRESS 2 BLACK HOLESSSSS", "I'm Santa's elf!", "A mere monkey can never defeat a lion.", "This guy- this guy has a dang hidden sparky. What a greasy bum."]
lvl = (range(1,100))
job = ["Farmer", "Blacksmith", "Merchant", "Guard", "Healer", "Hunter", "Bard", "Alchemist"]
height = (range(1,6.5).round(2))

gng = input("Generate NPC? y/n:")
if gng == "y" or "Y":
    npc_name = random.choice(names)
    npc_trait = random.choice(traits)
    npc_level = random.choice(lvl)
    npc_job = random.choice(job)
    print(f"Name: {npc_name}\nTrait: {npc_trait}\nLevel: {npc_level}\nJob: {npc_job}")
else:
    print("Wow. At least test ur code man.")

if gng == "y" or "Y":
    talk = input("Talk to NPC? y/n:")
    if talk == "y" or "Y":
        print(f"---------------{npc_name}---------------")
        print(f"Hi I'm {npc_name}. I'm lvl {npc_level} and my job is {npc_job}. Apparently, people know me for being {npc_trait}. I am {random.choice(height)} and {random.choice(final_phrase)}")
