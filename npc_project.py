import random
import sys #allows me to control runtime and exit program
traits = [
    "energetic", "smart", "brave", "adventurous", "curious", "creative",
    "stoic", "empathetic", "witty", "loyal", "ambitious", "calm",
    "playful", "reckless", "cautious", "observant", "stubborn",
    "cheerful", "mysterious", "hangry",
]#list of traits for NPC generation
names = [
    "Aria", "Finn", "Mira", "Thorne", "Lila", "Kade", "Rowan", "Sylas",
    "Nia", "Jax", "Eira", "Bram", "Soren", "Lyra", "Kai", "Maeve",
    "Orion", "Zara", "Hugo", "Tessa", "Elias", "Rhea", "Dorian", "Ivy",
    "Pax", "Seraph", "Elowen", "Garrick", "Isla", "Milo", "Fen", "Vesper",
    "Nolan", "Cora", "Lucan", "Petra", "Ash", "Nova", "Theo", "Beck",
]#names for NPC
final_phrase = ["Feel free to look around the village.", "Good luck on the rest of your journey.", "Oh. And in case I don't see you again, good morning, good afternoon, and good night.", "I'm.... I'm.... I'm...........................SPONGEBOBBBBBBBBBB","ARSON CAN BENCH PRESS 2 BLACK HOLESSSSS", "I'm Santa's elf!", "A mere monkey can never defeat a lion.", "This guy- this guy has a dang hidden sparky. What a greasy bum."]
lvl = (range(1,100))#BUNCH OF TRAITS FOR NPCs
job = ["Farmer", "Blacksmith", "Merchant", "Guard", "Healer", "Hunter", "Bard", "Alchemist"]
monies = (range(1,100))
#Variables for random gen
gng = input("Generate NPC? y/n: ").strip().lower()#First user input to start program. if user says no, kills program
if gng in ("n", "no"):
    print("At least test ur code man.")
    sys.exit(0)

try:
    count = int(input("How many NPCs do you want to generate? (1-100): ").strip())
except ValueError:#uses value error if user puts the wrong type of value
    count = 1
count = max(1, min(count, 100))#if there's trouble with code, asks user to gen npc and limits to 1-100

for i in range(count):#LOOPPPPPPPPPPPP :DDDDDDDDDDDD
    npc_name = random.choice(names)
    npc_trait = random.choice(traits)
    npc_level = random.choice(range(1, 101))
    npc_job = random.choice(job)
    npc_monies = random.choice(range(1, 101))#funsies loop that follows what number user chose.

    if npc_monies <= 15:#status system :)
        npc_stat = "a brokie"
    if npc_monies >15 and npc_monies <50:
        npc_stat = "an average Joe"
    if npc_monies >=50:
        npc_stat = "A sweat at life and people tell me to get a life bro."

    print(f"\n=== NPC #{i+1} ===") #generates heading for each npc stats Ex: ------NPC #1------
    print(f"Name: {npc_name}\nTrait: {npc_trait}\nLevel: {npc_level}\nJob: {npc_job}\nWorth: {npc_monies}")

    talk = input("Talk to this NPC? y/n: ").strip().lower()#more user inputs :)
    if talk in ("n", "no"):
        # if user doesn't want to talk, still says the little outro and exits
        print("\n\t\t\t\t----------CODE-----------")
        print("That's all the NPCs mate. Restart to generate more. Peace out lil bro.")
        sys.exit(0)
    elif talk in ("y", "yes"):
        print(f"\t\t\t\t---------------{npc_name}---------------")
        npc_height = round(random.uniform(1.0, 7.0), 2)
        print(f"Hi I'm {npc_name}. I'm lvl {npc_level} and my job is {npc_job}. Apparently, people know me for being {npc_trait}. I am {npc_height} ft tall, I'm also {npc_stat} and {random.choice(final_phrase)}")
    else:
        print("alr lil bro peace.")#continues to (if) next npc if user inputs n
        continue
    
    
    
    
    # If the select amount of NPCs are generated, stop code
    if i + 1 == count:
        print("\n\t\t\t\t----------CODE-----------")
        print("That's all the NPCs mate. Restart to generate more. Peace out lil bro.")
        sys.exit(0)
            











































































































































































































































































































