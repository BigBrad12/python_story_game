from sys import exit
import os
import time
import subprocess
i = 0
teleported = True
loop = 0

def clear_screen():
    system_name = os.uname().sysname.lower()

    if 'darwin' in system_name:
        # macOS or iOS
        subprocess.call('clear', shell=True)
    else:
        # Assume other Unix-like systems
        clear_screen()

def start(i):
    clear_screen()
    if i == 0:
        print(
'''Welcome adventurer!
Select your character:

1. High Elf Mage
2. White Wizard
3. Ogre Chieftain''')
    elif i > 0:
        print(
'''Select your character:
1. High Elf Mage
2. White Wizard
3. Ogre Chieftain''')
    else:
        print('''Stars wheele overhead, and every day is as long as the life age of the earth.
But it is not the end. You feel light in you again.
You've been sent back until your task is done.

1. High Elf Mage
2. White Wizard
3. Ogre Chieftain''')
    select_character()



def select_character():
    hero = int(input("> "))
    clear_screen()

    if hero == 1:
        elf()
    elif hero == 2:
        wizard()
    else:
        ogre()
    print("Are you sure?\n1. Yes\n2. No")
    i = int(input('> '))
    clear_screen()
    if i == 2:
        start(i)
    clear_screen()
    teleported = False
    spawn_and_gate_choice(teleported, hero)




def spawn_and_gate_choice(teleported, hero):
    clear_screen()
    if teleported == False:
        print('''You spawn in an inter universal space-time, standing on a floor of light that reflects all the colors of the known spectrum.
Three light bridges extend a short distance, leading to three gateways...


One of the gateways emits nothing at all. Utterly lifeless.
Another radiates raw energy, and a feint red glow.
The last ebbs mist and feintly smells of rot.
1: Go to the lifeless gate
2: Go the gate radiating energy
3: Go to the rotting, misty gate''')
    else:
        print('''You have chosen to flee and returned to inter universal space-time highway.

One of the gateways emits nothing at all. Utterly lifeless.
Another radiates raw energy, and a feint red glow.
The last ebbs mist and feintly smells of rot.
1: Go to the lifeless gate
2: Go the gate radiating heat and energy
3: Go to the rotting, misty gate''')
    gate = int(input("> "))
    clear_screen()
    riddle(gate, hero, loop)



def riddle(gate, hero, loop):
    if loop == 0:
        print("A riddle appears (Smeagol riddle), floating in the air...")
    if gate == 1:
        print(
'''
This thing all things devours;
Birds, beasts, trees, flowers;
Gnaws iron, bites steel;
Grinds hard stones to meal;
Slays king, ruins town,
And beats mountain down.''')
    elif gate == 2:
        print(
'''
It cannot be seen, cannot be felt,
Cannot be heard, cannot be smelt.
It lies behind stars and under hills,
And empty holes it fills.
It comes out first and follows after,
Ends life, kills laughter.''')
    else:
        print(
'''
What has roots as nobody sees,
Is taller than trees,
Up, up it goes,
And yet never grows?''')
    answer = input("> ")
    clear_screen()
    check_answer(answer, gate, hero, loop)

def check_answer(answer, gate, hero, loop):
    correct = False
    while correct == False:
        if gate == 1 and (answer == "Time" or answer == "time"):
            correct = True
            print("That's correct. Clever Hobbit.")
        elif gate == 2 and (answer == "darkness" or answer == "Darkness" or answer == "the dark" or answer == "The darkness" or answer == "The Darkness"):
            correct = True
            print("That's correct. Clever Hobbit.")
        elif gate == 3 and (answer == "Mountain" or answer == "mountain" or answer == "a mountain" or answer == "A fish" or answer == "A Mountain"):
            correct = True
            print("That's correct. Clever Hobbit.")
        else:
            clear_screen()
            print("Try again...")
            correct = False
            loop += 1
            riddle(gate, hero, loop)
    if gate == 1:
        orc_room(hero)
    elif gate == 2:
        demon_room(hero)
    else:
        necro_room(hero)




def necro_room(hero):
    print(
'''The gate unlocks, and you walk through the portal...

Before you is a misty marshland. Rife with the smell of death, plague, and rot.
The very air seeks to suck your life force away.

There is a river, pitch black, not a life giving river
but one that takes life from all things who enter it.

A rope bridge crosses the distance, swaying slightly in the deathly wind.
Nearby is a pathway, leading onward into the clogged marshland.

1: Cross the bridge
2: Follow the path''')
    path = int(input('> '))
    clear_screen()
    confrontation_necro(hero, path)

def demon_room(hero):
    print(
'''The gate unlocks, and you walk through the portal...

Darkness surrounds you, save for a feint glow between cracks in the rocks.
You are deep below the earth, blistering heat radiates from the rocky walls, the air hums with raw, natural energy.
There's a torch on a wall mount, you pick it up and tap the bare rock with it.
It lights up and illuminates the immediate area around you.

There is a black, seemingly bottomless, pit before you.
To your left is an archway in the rock, with a staircase going down.

1: Jump into the abyss
2: Take the stairs''')
    path = int(input("> "))
    confrontation_demon(hero, path)

def orc_room(hero):
    print(
'''The gate unlocks, and you walk through the portal...

Defening silence...
You sense nothing. The air is empty. There is not even a gust of wind.
It's as if the area has been completely consumed and sucked dry.

A cold and lifeless mountain lies ahead, with a path leading into it.
1: Take the path
2: Go the long way around''')
    path = int(input("> "))
    confrontation_orc(hero, path)

def confrontation_necro(hero, path):
    clear_screen()

    def ogre_1(hero, path):
        print('''Your huge Ogre frame is too much for the bridge and it breaks under
your weight. You plunge into the black river.

You wade through the river and reach the other side.

The foe draws near, a Necromancer, wearing a long green garb.
A huge scythe in their left hand.
A ghostly glowing black book in their right.

They seem uneasy at the sight of the Ogre Chieftain even though they just
waded through the river of death and plague.

1. Fight
2. Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The necromancer panics and summons his army of the undead.
They are but small fry for the Ogre Chieftain and you demolish huge numbers of the undead with a single swing of your club.

"Weak! I smash them all strange wizard!"

The Necromancer tries to use spirit siphon but you.
It doesn't phase the Chief in the least, you run up to the Necromancer in three swift and powerful sprinting strides
and flatten the Necromancer with a single downward swing of your club.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Necromancer")
    def ogre_2(hero, path):
        print('''You make short work of the distance through the marsh. Huge Ogre feet provide
natural marshland shoes. The marsh, rife with plague and poison has no
effect on you. Your immense life force cannot be weakened by such things.

The foe draws near, a Necromancer, wearing a long green garb. The sight of the
Ogre Chieftain seems to make them uneasy.
A huge scythe in their left hand. A ghostly glowing black book in their right.

1. Fight
2. Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The necromancer panics and summons his army of the undead.
They are but small fry for the Ogre Chieftain and you demolish huge numbers of the undead with a single swing of your club.

"Weak! I smash them all strange wizard!"

The Necromancer tries to use spirit siphon but you.
It doesn't phase the Chief in the least, you run up to the Necromancer in three swift and powerful sprinting strides
and flatten the Necromancer with a single downward swing of your club.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Necromancer")

    def wizard_1(hero, path):
        print('''As a light, agile White Wizard, you flit across the bridge with ease, all the while shivering from
the overwhelming stench of death that flows beneath you. Your bones chill to the core.
On the other side of the river, a Necromancer awaits. They wear a long, tattered green garb.
A huge scythe in their left hand. A ghostly, glowing black book in their right.

1. Fight
2. Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The Necromancer summons their army of the undead. Weak skeleton warriors emerge
from below and start charging towards you. They are weak, you blast them back with simple magic.

The necromancer casts a spirit siphon spell upon you. The immortality magic that keeps you alive
begins to strain and you feel death creeping up on you.

1. Imbue your body with an agility spell, dash in towards the enemy and cut their head off with a flame sword
2. Start the incantation for your most powerful, ranged, magical attack''')
            attack_choice = int(input("> "))
            clear_screen()
            if attack_choice == 1:
                print('''The Necromancer is surprised, and reacts slowly. You dash in and slice their head off.
The spirit siphon ends and you breathe a sigh of relief. That was a close call.''')
                time.sleep(5)
                print("A swirling light starts surrounding your from the ground upwards.")
                time.sleep(1.5)
                print('.', end ='', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                victory(enemy = "Necromancer")
            else:
                print('''You start the incantation for your magical spell, which takes time. All the while
your life drains and your immortality magic all but ends. Your huge fireball is sent hurtling towards
your enemy. But they absord it and channel its energy into their skeleton warriors. Your spirit fades
as the last bits of life leave you. Skeleton warriors swamp you and you die.
1. God damn it, exit game
2. Lets go again''')
                lose_choice = int(input("> "))
                if lose_choice == 1:
                    close(0)
                else:
                    start(i = -1)
    def wizard_2(hero, path):
        print('''The overwhelming presence of death chills you to your core. You shiver, your spirit weakens.
The life-draining swamp rife with poison and plague weakens the magic that keeps you alive.
The magics that protect you from these effects strain and weaken.

The foe draws near, a Necromancer, wearing a long green garb. Eyes gleaming with vicious intent.
They sense your weakness.
A huge scythe in their left hand. A ghostly glowing black book in their right.

1: Steel yourself and fight
2. Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The Necromancer summons their army of the undead. Weak skeleton warriors emerge
from below and start charging towards you. You blast them back with simple magic, but they get up quickly and charge once more.
The necromancer casts a spirit siphon spell upon you. The immortality magic that keeps you alive crumbles,
you fall to you knees from weakness, and his skeleton army swamps you and kills you.
1. Let's go again
2. God damn, exit game''')
            death_choice = int(input('> '))
            clear_screen()
            if death_choice == 1:
                start(i = -1)
            else:
                exit(0)
    def elf_1(hero, path):
        print('''Flitting over the rope bridge was a breeze. You're a swift, light, Elf Mage
after all. Much time and energy is spared. The magical energies in this place are
powerful, tempting, but evil and corrupting.

The foe draws near, a Necromancer, wearing a long tattered green garb.
A huge scythe in their left hand. A ghostly, glowing black book in their right.

1. Fight them with magic
2. Teleport to safety
3. Fight them without magic''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        elif battle_choice == 1:
            print('''The Necromancer summons their undead skeleton army.
You channel the energies of the area. They are incredibly powerful and you demolish
all who stand on the battlefield in an instant, however the evil nature of the energy
corrupts you and you go insane. Your body rejects itself and you die!

1. Let's go again
2. God damn it, exit game''')
            death_choice = int(input('> '))
            if death_choice == 1:
                start(i = -1)
            else:
                exit(0)
        else:
            print('''The Necromancer summons their undead skeleton army. They are weak and slow compared to you.
An Elf who has trained for over 1000 years, with speed and incredible agility as well as infinite stamia.
You don't even break a sweat sweeping through the skeletons like a hot knife through butter.
The Necromancer starts a spirit siphon spell to try and drain your life force.
The Elven light is endless and cannot be drained dry, you reach your foe and swiftly cut their head off.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Necromancer")
    def elf_2(hero, path):
        print('''You wade through the life-draining swamp rife with poison and plague.
Luckily, Elf Mage bodies are soaked with magics that provide resistance to
such effects. The magical energies in this place are powerful, tempting, but
evil and corrupting.

The foe draws near, a Necromancer, wearing a long green garb.
A huge scythe in their left hand. A ghostly glowing black book in their right.

1: Fight them with magic
2: Teleport to safety
3: Fight them without magic''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        elif battle_choice == 1:
            print('''The Necromancer summons their undead skeleton army.
    You channel the energies of the area. They are incredibly powerful and you demolish
    all who stand on the battlefield in an instant, however the evil nature of the energy
    corrupts you and you go insane. Your body rejects itself and you die!

    1. Let's go again
    2. God damn it, exit game''')
            death_choice = int(input('> '))
            if death_choice == 1:
                start(i = -1)
            else:
                exit(0)
        else:
            print('''The Necromancer summons their undead skeleton army.
You channel the energies of the area. They are incredibly powerful and you demolish
all who stand on the battlefield in an instant, however the evil nature of the energy
corrupts you and you go insane. Your body rejects itself and you die!

1. Let's go again
2. God damn it, exit game''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Necromancer")


    if hero == 1 and path == 1:
        elf_1(hero, path)
    elif hero == 1 and path == 2:
        elf_2(hero, path)
    elif hero == 2 and path == 1:
        wizard_1(hero, path)
    elif hero == 2 and path == 2:
        wizard_2(hero, path)
    elif hero == 3 and path == 1:
        ogre_1(hero, path)
    elif hero == 3 and path == 2:
        ogre_2(hero, path)
def confrontation_orc(hero, path):

    clear_screen()

    def elf_1(hero, path):
        print('''On the mountain path, a cave comes into view. Deep into the mountain, hope
returns. The last ebbs of precious natural energy sleep here. You channel the
magic and fill your mana pool to half, leaving some of the energy so as not to
suck it all dry. The path leads through the mountain rock and out the other side.

The foe draws near. A genetically enhanced Orc! Thick armor. Powerful and quick.
1. Fight!
2. Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''You charge forward, and so does the Orc.
Both from Elven descent, you, a pure Elf, with the Elven light inside you. Your enemy, a line of Elves corrupted by dark magic.

The Orc is more powerful than you, and quick, but you are quicker.
You slice off a piece of armor with the little magic obtained in the mountain,
and stab into the Orc's flesh with your Elven blade.

"I shall rend you from this plane of existence foul beast!"

The blade burns the Orc from within.
The orc falls to their knees howling in pain.
You cut their head off.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Genetically Enhanced Orc")
    def elf_2(hero, path):
        print('''After going the long way around, all hope seems to fade.
Not a single drop of life energy is to be found in the surroundings.
Your mana pool runs empty.

The foe draws near. A genetically enhanced Orc! Thick armor. Powerful and quick.
1. Fight!
2. Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''You charge forward, and so does the Orc. Both from Elven descent, you, a pure Elf,
with the Elven light inside you. Your enemy, a line of Elves corrupted by dark magic.
The Orc is more powerful than you, and quick. You realise that you're usually quicker
but since there's no natural energy to fortify your body, you're a little slower than usual.
This realization cuases you to hesitate in the heat of battle for a second, and the orc
slams their hammer into the side of your head and you die.
1. Let's go again
2. God damn it, exit game''')
            death_choice = int(input('> '))
            if death_choice == 1:
                start(i =-1)
            else:
                exit(0)
    def ogre_2(hero, path):
        print('''An Ogre's large strides make short work of the distance around the mountain.
You use your club as a walking stick. Ogre like flat ground. Ogre smart.

The foe draws near. A genetically enhanced Orc! Thick armor. Powerful and quick.
A worthy opponent. The battle will be legendary.
1: Fight!
2: Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''You unleash your Ogre warcry, the Orc unleashes theirs.
Two manly men run forward and clash, steel against steel.
You are much slower than the Orc and they land blows on you one after another, however, their blows don't faze you much.
"You are but a fly, little Orc!"
The Orc parries your huge club with their hammer. Time and time again you swing your club until it breaks. Oh no.
1. Fight on
2. Teleport to safety''')
            run_or_fight = int(input('> '))
            clear_screen()
            if run_or_fight == 1:
                print('''You imbue your fists with your life force, go into a rage, and begin pummeling the orc with your bare hands.
Your attacks smash their thick armor to pieces and destroy their organs.
"Is that flimsy metal meant to protect you, weakling!?"
You then tear the limbs off your spent foe to fully respect their efforts.
Like a true Ogre Chieftain.''')
                time.sleep(15)
                print("A swirling light starts surrounding your from the ground upwards.")
                time.sleep(1.5)
                print('.', end ='', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                victory(enemy = "Genetically Enhanced Orc")
            else:
                teleported = True
                spawn_and_gate_choice(teleported, hero)
    def ogre_1(hero, path):
        print('''Your Ogre Chieftain goes up the mountain path and encounters the entrance
to a cave, but as fate would have it, an Ogre is too big to enter. You smack the
ground with your club in frustration and walk all the way down again.
Time for the long way around.
Ogre Chieftain now angry Ogre Cheiftain.

The foe draws near. A genetically enhanced Orc! Thick armor. Powerful and quick.
A worthy opponent. The battle will be legendary.
1: Fight
2: Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:

            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''You unleash your Ogre warcry, the Orc unleashes theirs.
Two manly men run forward and clash, steel against steel.
You are much slower than the Orc and they land blows on you one after another, however, their blows don't faze you much.
"You are but a fly, little Orc!"
The Orc parries your huge club with their hammer. Time and time again you swing your club until it breaks. Oh no.
1. Fight on
2. Teleport to safety''')
            run_or_fight = int(input('> '))
            clear_screen()
            if run_or_fight == 1:
                print('''You imbue your fists with your life force, go into a rage, and begin pummeling the orc with your bare hands.
Your attacks smash their thick armor to pieces and destroy their organs.
"Is that flimsy metal meant to protect you, weakling!?"
You then tear the limbs off your spent foe to fully respect their efforts.
Like a true Ogre Chieftain.''')
                time.sleep(15)
                print("A swirling light starts surrounding your from the ground upwards.")
                time.sleep(1.5)
                print('.', end ='', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                victory(enemy = "Genetically Enhanced Orc")
            else:
                teleported = True
                spawn_and_gate_choice(teleported, hero)
    def wizard_1(hero, path):
        print('''On the mountain path, a cave comes into view. Deep into the mountain, you
find what precious little remains of the life energy on the area. A White Wizard's
duty is to nurture the earth. You cast a spell that revitalizes the mountain's
core, setting in motion the rebirth of life.

The path leads through the mountain rock and out the other side.
The foe draws near. A genetically enhanced Orc! Thick armor. Powerful and quick.
1: Fight!
2: Teleport to safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''"Despicable Orc!" You shout.
"What have you done to the mountain, and the trees, the animals and the earth!
You've consumed them all. Scum. I shall rend you from this world heathen!"

The Orc laughs in your face and charges forward. Your rage summons the most ancient and primal magics you posses.
You lift the Orc into the air, chant an incantation so loudly that it could
be heard from a vast distance away.
You rend the Orc, in mid air, into tiny pieces and burn those pieces with a purifying flame.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Genetically Enhanced Orc")
    def wizard_2(hero, path):
        print('''You take the long way around, the journey is tiresome and nothing of
interest happens. You sense lost opportunity within the mountain core.

The foe draws near. A genetically enhanced Orc! Thick armor. Powerful and quick.
1: Fight!
2: To safety''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''"Despicable Orc!" You shout.
"What have you done to the mountain, and the trees, the animals and the earth!
You've consumed them all. Scum. I shall rend you from this world heathen!"

The Orc laughs in your face and charges forward. Your rage summons the most ancient and primal magics you posses.
You lift the Orc into the air, chant an incantation so loudly that it could
be heard from a vast distance away.
You rend the Orc, in mid air, into tiny pieces and burn those pieces with a purifying flame.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Genetically Enhanced Orc")

    if hero == 1 and path == 1:
        elf_1(hero, path)
    elif hero == 1 and path == 2:
        elf_2(hero, path)
    elif hero == 2 and path == 1:
        wizard_1(hero, path)
    elif hero == 2 and path == 2:
        wizard_2(hero, path)
    elif hero == 3 and path == 1:
        ogre_1(hero, path)
    elif hero == 3 and path == 2:
        ogre_2(hero, path)
def confrontation_demon(hero, path):

    clear_screen()

    def wizard_1(hero, path):
        print('''Falling down seems to last for hours. Yet truly it was 2 minutes.
A strong rising air current slows your fall and you land like a superhero. One hand holding
your Wizard hat to your head, the other hand holding your staff in a fist.

An Ancient Balrog illuminates the surroundings. Its power stems from the same
source as your own. Two mighty warriors, a standoff of the ages.
1. Draw your sword, and face your foe
2. Teleport to safety''')
        battle_choice = int(input("> "))
        if battle_choice == 2:

            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The battle is legendary. You fight on and on, defending yourself from flame and whip.

"I am a servant of the Secret Fire, wielder of the flame of Anor. The dark fire will not avail you, flame of Udûn! Go back to the shadow!"

Sending lightning bolts forth from your staff. Your strikes, and the strikes of the Balrog reverberate off the cavern walls.
Neither you nor your foe falters.

1. Wait for an opening
2. Lunge in for the kill''')
            battle_decision = int(input('> '))
            clear_screen()
            if battle_decision == 1:
                    print('''The Balrog lunges in to try and grab you, but you dodge and thrust forward with your sword
penetrating the thick black shell of the Balrog. You rend its insides with conjured lightning from your sword.
You stand over your defeated enemy.
"Foul Demon, back to the shadows with you."''')
                    time.sleep(15)
                    print("A swirling light starts surrounding your from the ground upwards.")
                    time.sleep(1.5)
                    print('.', end ='', flush = True)
                    time.sleep(1.5)
                    print('.', end = '', flush = True)
                    time.sleep(1.5)
                    print('.', end = '', flush = True)
                    time.sleep(1.5)
                    victory(enemy = "Balrog")
            else:
                print('''The Balrog grabs you as you make your desperate lunge and incants a flame spell.
You begin to burn in its grasp and you explode into a ball of flames. A nice crispy Wizard.
The Balrog throws you in its mouth and munches you for dinner.
1. Let's go again
2. God damn it, exit game''')
                death_choice = int(input('> '))
                if death_choice == 1:
                        start(i = -1)
                else:
                        exit(0)
    def wizard_2(hero, path):
        print('''The journey down the stairway takes over 2 hours. All the time in the world
to contemplate the meaning of life, why chickens don't fly, and how your dog
would sound if they could talk and what they would say. Finally, the stairway ends.
Your old Wizard legs sigh in delight.

An Ancient Balrog illuminates the surroundings. Its power stems from the same
source as your own. Two mighty warriors, a standoff of the ages.
1. Draw your sword, and face your foe
2. Teleport to safety''')
        battle_choice = int(input("> "))
        if battle_choice == 2:

            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The battle is legendary. You fight on and on, defending yourself from flame and whip.

"I am a servant of the Secret Fire, wielder of the flame of Anor. The dark fire will not avail you, flame of Udûn! Go back to the shadow!"

Sending lightning bolts forth from your staff. Your strikes, and the strikes of the Balrog reverberate off the cavern walls.
Neither you nor your foe falters.

1. Wait for an opening
2. Lunge in for the kill''')
            battle_decision = int(input('> '))
            clear_screen()
            if battle_decision == 1:
                print('''The Balrog lunges in to try and grab you, but you dodge and thrust forward with your sword
penetrating the thick black shell of the Balrog. You rend its insides with conjured lightning from your sword.
You stand over your defeated enemy.
"Foul Demon, back to the shadows with you."''')
                time.sleep(15)
                print("A swirling light starts surrounding your from the ground upwards.")
                time.sleep(1.5)
                print('.', end ='', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                print('.', end = '', flush = True)
                time.sleep(1.5)
                victory(enemy = "Balrog")
            else:
                    print('''The Balrog grabs you as you make your desperate lunge and incants a flame spell.
You begin to burn in its grasp and you explode into a ball of flames. A nice crispy Wizard.
The Balrog throws you in its mouth and munches you for dinner.
1. Let's go again
2. God damn it, exit game''')
                    death_choice = int(input('> '))
                    if death_choice == 1:
                        start(i = -1)
                    else:
                        exit(0)
    def elf_1(hero, path):
        print('''Falling down seems to last for hours. Yet truly it was 2 minutes.
A strong rising air current slows the fall. Your Elf Mage channels the energy
from this current and rides it into a superhero landing. Swift transportation!

An Ancient Balrog illuminates the surroundings. Your mana pool is bursting full
of rich energy.
1. Fight
2. Teleport to safety''')
        battle_choice = int(input("> "))
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The Balrog attacks with full force, but their movements are slow.
You taunt your foe "Is that all you can do, foul Demon from the depths?"

The Balrog is enraged and launches attack after attack.
Their attacks are slow and you dodge them easily.

You start incanting the most powerful and purifying spell known to the Elf Mages of old.
The Balrog begins to panic and starts trying to punch you.
"Foolish foul Demon!"
You jump up onto its fist, leap into the air, and release the magic attack that utterly destroys the Balrog, vaporizing it entirely.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Balrog")
    def elf_2(hero, path):
        print('''The journey down the stairway takes over 2 hours. All the time in the world
to contemplate the meaning of life, why chickens don't fly, and how your dog
would sounds if they could talk and what they would say. Finally, the stairway ends.

An Ancient Balrog illuminates the surroundings.
Your mana pool is bursting, full of rich energy.
1. Fight
2. Teleport to safety''')
        battle_choice = int(input("> "))
        if battle_choice == 2:

            teleported = True
            spawn_and_gate_choice(teleported, hero)
        else:
            print('''The Balrog attacks with full force, but their movements are slow.
You taunt your foe "Is that all you can do, foul Demon from the depths?"

The Balrog is enraged and launches attack after attack.
Their attacks are slow and you dodge them easily.

You start incanting the most powerful and purifying spell known to the Elf Mages of old.
The Balrog begins to panic and starts trying to punch you.
"Foolish foul Demon!"
You jump up onto its fist, leap into the air, and release the magic attack that utterly destroys the Balrog, vaporizing it entirely.''')
            time.sleep(15)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Balrog")
    def ogre_1(hero, path):
        print('''Falling down seems to last for hours. Yet truly it was 2 minutes.
The huge Ogre Chieftain breaks their fall by unleashing a
monstrous attack towards the ground and lands like a superhero in a cloud of epic dust.
Wicked.

An Ancient Balrog illuminates the surroundings. The Ogre's hair stands on end.
Never have they seen such a mighty foe. Even larger than themselves.
Wielding magical flame that sears even steel.

1. Fight on your own
2. Teleport to safety
3. Put away your pride and summon your best warriors with Ogre magic''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:
            teleported = True
            spawn_and_gate_choice(teleported, hero)
        elif battle_choice == 1:
            print('''You pound your chest a loose ferocious battle cry, the Balrog does the same and
completely dwarfs your battle cry. They attack with a mighty flaming whip
you block the attack with your club, which shatters, and you are sent flying sideways, crashing
into the cavern walls. Deep inside you, you know this foe is going to be the end for you.
You fight on and on until there's nothing left, and the Balrog rends your flesh with
its ancient flame.
1. Lets go again
2. God damn it, exit game''')
            death_choice = int(input('> '))
            if death_choice == 1:
                start(i = -1)
            else:
                exit(0)
        else:
            print('''You summon the 3 of the mightiest Ogre warriors of your clan to your side.
One of them say:
"You summoned, my Chief! What great foe stands before you that you summon us to you!?"
Then they gaze upon their foe, the Balrog, standing tall and huge, way bigger than any of you or your Ogre tribesmen.
You and your warriors go quiet and focus with extreme intensity on the mission at hand.

You then all let loose the mightiest battle cries, and the Balrog lets loose its own.
The battle rages on, you and your warriors imbue your fists with your own life force
and surround the Balrog, attacking over and over, slowly chipping away at the Balrog's life.

In the heat of battle, you witness your fellow warriors fall to the Balrog one by one. Your spirit rages.
As each one falls, your desperation grows and your anger festers.
You're the last man standing. The Balrog attacks recklessly and you grab onto its fangs.
You muster strength equal to that of the most vicious storm and rip its jaw apart, splitting its head in two.

You foe has been slain, but at what cost? You honor your fallen brethren with a victory cry filled
with pain and emotion.''')
            time.sleep(20)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Balrog")
    def ogre_2(hero, path):
        print('''The staircase is too small for a huge Ogre.
You walk over to the pit and leap in.
Falling down seems to last for hours. Yet truly it was 2 minutes.
The huge Ogre Chieftain breaks their fall by unleashing a
monstrous attack towards the ground. The Ogre lands like a superhero.
Wicked.
An Ancient Balrog illuminates the surroundings. The Ogre's hair stands on end.
Never have they seen such a mighty foe. Even larger than themselves.
Wielding magical flame that sears even steel.

1. Fight on your own
2. Teleport to safety
3. Put away your pride and summon your best warriors with Ogre magic''')
        battle_choice = int(input("> "))
        clear_screen()
        if battle_choice == 2:

            teleported = True
            spawn_and_gate_choice(teleported, hero)
        elif battle_choice == 1:
            print('''You pound your chest a loose ferocious battle cry, the Balrog does the same and
completely dwarfs your battle cry. They attack with a mighty flaming whip
you block the attack with your club, which shatters, and you are sent flying sideways, crashing
into the cavern walls. Deep inside you, you know this foe is going to be the end for you.
You fight on and on until there's nothing left, and the Balrog rends your flesh with
its ancient flame.
1. Lets go again
2. God damn it, exit game''')
            death_choice = int(input('> '))
            if death_choice == 1:
                start(i = -1)
            else:
                exit(0)
        else:
            print('''You summon the 3 of the mightiest Ogre warriors of your clan to your side.
One of them say:
"You summoned, my Chief! What great foe stands before you that you summon us to you!?"
Then they gaze upon their foe, the Balrog, standing tall and huge, way bigger than any of you or your Ogre tribesmen.
You and your warriors go quiet and focus with extreme intensity on the mission at hand.

You then all let loose the mightiest battle cries, and the Balrog lets loose its own.
The battle rages on, you and your warriors imbue your fists with your own life force
and surround the Balrog, attacking over and over, slowly chipping away at the Balrog's life.

In the heat of battle, you witness your fellow warriors fall the to Balrog one by one. Your spirit rages.
As each one falls, your desperation grows and your anger festers.
You're the last man standing. The Balrog attacks recklessly and you grab onto its fangs.
You muster strength equal to that of the most vicious storm and rip its jaw apart, splitting its head in two.

You foe has been slain, but at what cost? You honor your fallen brethren with a victory cry filled
with pain and emotion.''')
            time.sleep(22)
            print("A swirling light starts surrounding your from the ground upwards.")
            time.sleep(1.5)
            print('.', end ='', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            print('.', end = '', flush = True)
            time.sleep(1.5)
            victory(enemy = "Balrog")

    if hero == 1 and path == 1:
        elf_1(hero, path)
    elif hero == 1 and path == 2:
        elf_2(hero, path)
    elif hero == 2 and path == 1:
        wizard_1(hero, path)
    elif hero == 2 and path == 2:
        wizard_2(hero, path)
    elif hero == 3 and path == 1:
        ogre_1(hero, path)
    elif hero == 3 and path == 2:
        ogre_2(hero, path)

def victory(enemy):
    clear_screen()
    print(f'''You have slain the {enemy}!
You've been teleported into a grand hall.

There are long tables where your fellow kin feast gloriously.
You feast with them and celebrate your victory!
1. Play again
2. Exit''')
    choice = int(input('> '))
    clear_screen()
    if choice == 1:
        start(i)
    else:
        exit(0)

def elf():
    print(
'''High Elf Mage:
- Does not fear death
- Powerful magical spells charged with raw, magical energy from the surroundings
- Limited mana pool
- Quick, light, and infinite stamina
- Light leather armor. Shortbow. Two curved blades''')
def wizard():
    print(
'''White Wizard:
- Infinite mana pool. Draws upon the ancient energy of alternate dimensions
- Wise and brilliant, but fears death
- Quick and light on their feet
- Wields staff and magical sword''')
def ogre():
    print(
'''Ogre Chieftain:
- Huge, heavy, incredible physical power
- Limitless lifeforce and vitality
- Weilds a large club. Weak armor. If their weapon breaks, they imbue their fists
  with their own lifeforce and pummel their foe''')

start(i)
