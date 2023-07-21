import random
import os
import re

class Scene(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.choices = {}

    def choose(self, choice):
        return self.choices.get(choice, None)
    
    def add_choices(self, choices):
        self.choices.update(choices)



""" class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        #  print("Engine play called")
        current_scene = self.scene_map.opening_scene()
        # print(f"Current scene is {current_scene}")
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter() """

def thesaurus(input):

    synonyms = {
        'beam': 'beam',
        'kamehameha': 'beam',
        'tail': 'tail',
        'swim': 'swim',
        'jump': 'swim',
        'water': 'swim',
        'nimbus': 'nimbus',
        'kinto': 'nimbus',
        'cloud': 'nimbus',
        'pole': 'pole',
        'staff': 'pole',
        'power': 'pole',
        'nyoibo': 'pole',
        'image': 'image',
        'after': 'image',
        'afterimage': 'image',
        'zanzoken': 'image',
        'crone': 'crone',
        'woman': 'crone',
        'lady': 'crone',
        'joan': 'crone',
        'hint': 'hint',
        'help': 'hint',
        'fight': 'fight',
        'punch': 'fight',
        'kick': 'fight',
        'whoop': 'fight',
        'next': 'next',
        'back': 'back',
    }

    lower = input.lower()
    list = lower.split(' ')
        
    for item in list:
        try:
            s = synonyms[item]
            return s
        except:
            pass

    return 'error'
    

def fail():

    quip = [
        "\nWanna try that one again, chief?",
        "\nBut what if Goku did something else?",
        "\nHmm, let's try something different this time.",
        "\nThat didn't go as planned.",
        "\nNah, that doesn\'t work.",
        "\nOpe."
    ]

    print(quip.random())

green_list = [
    'red',
    'yellow',
    'blue',
    'orange',
    'purple',
    'pink',
    'white',
    'gray',
    'brown',
]
green = random.choice(green_list)

intro = Scene('Intro', 
"""
You have been fighting your way through the Red Ribbon Army,
Slowly but surely.
With a rare moment to relax, you realize you are hungry.
There's a river down below next to a small town.
You decide to land and catch a fish.
You land on the ground and an old crone nearby offers you a sad smile.
The river roars by, rushing quickly.
              
So, how are you going to catch this fish?
              """)

intro_tail = Scene('intro_tail', 
"""You dip your tail into the water.
Before long, a fish twice your size bites.
You yank it up out of the water and begin to eat it.
The Crone gasps in surprise

"Goodness child, I didn't realize you were so strong.
Do you think you could help my village?
My name is Joan, and the Red Ribbon army has been terrorizing us.
They say they're looking for a Dragonball.
But mostly they just bully us and steal our stuff."

You agree to help her and walk with her to the village.""")

intro_beam = Scene('intro_beam', """
You charge up a kamehameha wave, and blast it at the water.
Dozens of tiny fish come raining down.
You laugh and pick a few up off the ground to eat.
The Crone gasps in surprise.
                   
"Goodness child, I didn't realize you were so strong.
Do you think you could help my village?
My name is Joan, and the Red Ribbon army has been terrorizing us.
They say they're looking for a Dragonball.
But mostly they just bully us and steal our stuff."

You agree to help her and walk with her to the village.
""")

intro_swim = Scene('intro_swim', """
You jump into the water.
The current is too strong.
It sends you downstream, bouncing off rocks.              
""")

intro_nimbus = Scene('intro_nimbus', """
You hop up on your cloud.
Now you are hungry a few feet above the ground.
""")

intro_pole = Scene('intro_pole', """
You fish in the water with your power pole, but the fish don't bite.             
""")
        
intro_image = Scene('intro_image', """
You leave an afterimage in your place and then...
Try to sneak up on the fish?
It doesn't work.
""")

intro_crone = Scene('intro_crone', """
The Crone smiles sadly, but doesn't talk to you.                   
""")

intro_hint = Scene('intro_hint', """
Maybe use something the fish could mistake for a worm?                   
""")


        
goons = Scene('Goons',
"""
You come across two Red Ribbon goons bullying a shopkeeper.
The tall, skinny one speaks first, in a nasal voice.
"Give us the Dragonball, old man. We know you're hiding it!"

"Please," the elderly man says "I don't know what that is!"

The short fat one chimes in with his gravelly voice.
"Then you're going to give us all your money.
That should make up for inconveniencing us"

What do you do?
""")

goons_fight = Scene('goons_fight', """
You jump through the air and kick one.
WHOOMPF!
Then you punch the other.
POW!
They go down in one hit each.
That was easy.                   
""")

goons_pole = Scene('goons_pole', """
"Power pole, extend!"
You smack them with the power pole.
THWACK!
They each go down in one hit.                
""")

goons_beam = Scene('goons_beam', """
You begin chanting...
"KAA- MEE-"
An orb of energy begins to glow in your hands.
"What\'s happening?!" shouts the tall one.
"HAAA- MEEE-"')
"Wait!" shouts the short one. "Stop!!"
"We give up! Don't hurt us!"
You stop charging the kamehameha wave and chuckle.               
""")

goons_image = Scene('goons_image', """
"Hey, what gives?" says the tall one, who moves forward to hit you with his gun.
But you appear behind them and kick both of them to the ground.                  
""")

goons_hint = Scene('goons_hint', """
Really? You want a hint?
These guys suck, just do whatever.                
""")

goons_win = Scene('goons_win', """
"You\'ll regret this!" says the short one.
He pulls out his radio.
"Colonel Chartreuse, you have to get over here! This kid is beating us up!"

A cool alto voice replies over the radio.
"You are losing to what?"

"A kid," says the tall one, "but he\'s really strong!"

"Hold position," the woman says with a sigh, "I\'m on the way."
A moment later, a woman shows up on a motorcycle.                  
""")

chartreuse = Scene('chartreuse', f"""
Colonel Chartreuse\'s {green} motorcycle rolls to a stop.
She steps onto the ground with her {green} boots.
She reaches her hands, nails painted sparkling {green}, up to her head.
She pulls off her {green} helmet, and waves of {green} hair billow out.
Her {green} eyes look coolly at you.

Wait, that doesn\'t sound right.
What color is Chartreuse again?
""")

# Need to redo the green input method
# maybe don't call the thesaurus and just take input

chartreuse_green = Scene('chartreuse_green', f"""
Colonel Chartreuse\'s {green} motorcycle rolls to a stop.
She steps onto the ground with her {green} boots.
She reaches her hands, nails painted sparkling {green}, up to her head.
She pulls off her {green} helmet, and waves of {green} hair billow out.
Her {green} eyes look coolly at you.

"You," she says slowly "are responsible for injuring my soldiers?"
"No matter," she says, "I\'ll take you out myself"
Curiously, she doesn't even get into a fighting stance as she says it.

What do you do now?
""")

round1 = Scene('chartreuse_power', """
Before you can do that, her eyes glow brightly.
She says "Why don\'t you walk into the river instead?"
Seemingly without your control, your body turns around and walks into the river')
The current sweeps you away, and you bang into a few rocks.
OW!

Joan catches up to you and fishes you out with a stick
"I think we\'re going to have to outsmart her, sonny."

You make it back to town.

"Colonel, we\'ve located the Dragonball!" exlaims a mook.

"Excellent." she says, walking over to inspect it.
She holds it up to the light and sees that it is the six star ball.
She then notices you.
"Oh, You\'re back for round 2? Bring it on!" she says with a smirk.
A crowd gathers around you to watch the two of you fight.                       
""")

adverb_list = [
            'boisterously',
            'loudly',
            'hysterically',
            'vigorously',
            'ferociously',
            'fiercely',
            'heartily',
            'rowdily',
            'savagely',
            'spitefully',
            'viciously',
            'violently'
        ]
# see if we can skip this by declaring it each time the list is loaded
# adverb = random.choice(adverb_list)

round2 = Scene('round2', 'How are you going to beat her this time?')

round2_fight = Scene('round2_fight', f"""
You start to lunge at her to strike.
Her eyes glow bright green and she says:
"Punch yourself instead."
You punch yourself instead, and she laughs {random.choice(adverb_list)} at you.               
""")

round2_beam = Scene('round2_beam', f"""
You begin charging up a powerful Kamehameha wave.
"KAAA-
MEEE-"

She does not wait for you to finish.
Her eyes glow bright green, and she tells you to punch yourself instead.
'When you do, she laughs {random.choice(adverb_list)}.                 
""")

round2_pole = Scene('round2_pole', f"""
"Power pole, extend!" you shout.
Her eyes flash bright green, and she tells you to hit yourself with it instead.
'You do, and she laughs {random.choice(adverb_list)}.        
""")

round2_nimbus = Scene('round2_nimbus', f"""
"Flying nimbus!" you shout
The cloud zooms to your feet, and you hop on.
Her eyes flash bright green.
"Fall down instead." she says.
Your body freezes stiff, and falls off the nimbus.
The impact hurts, and she laughs {random.choice(adverb_list)}.                   
""")

round2_image = Scene('round2_image', """
Imperceptively, you zip away, leaving an afterimage in your place.
Her eyes glow bright green.
                     
"Punch yourself." she says to your afterimage.
When nothing happens, she quickly becomes alarmed and confused.

"I said- punch yourself!" she repeats, a little more angrily.

"Here I am!" you shout as you jump at her with a flying kick from behind.
She turns around just in time to drop her jaw in surprise as your foot connects with her face.
She goes tumbling down to the ground.

"This. Isn\'t. Over." she says as she climbs back to her feet.

"All of you!" she bellows, turning and addressing the crowd,
"Go walk into the river!"
                     
"But they\'ll get hurt!" you shout.
"That sounds like your problem, brat.
With that, she shoves the Dragonball into a cargo pocket, hops onto her bike, and speeds away.                   
""")

round2_hint = Scene('round2_hint', 'maybe do something where she can\'t see you?')

piper = Scene('piper', """
This is bad.
The villagers are walking towards the rushing river. 
Chartreuse is speeding away on her bike.

What do you do?""")                                       

piper_fight = Scene('piper_fight', """
You start fighting villagers, trying to knock them down.
Many of them still get around you and walk into the current.                   
""")

piper_beam = Scene('piper_beam', """
You charge up a Kamehameha wave to scare the villagers.
They don\'t even notice you, and walk straight into the water.              
""")

piper_pole = Scene('piper_pole', """
You jump past all of them to block their way.
                   
"Power pole, Extend!"
The Power pole extends in both directions, blocking the villagers from walking past.
They push hard, but after a few moments some of them come to, and start helping you push the other way.
Soon, everyone has come to their senses.

"Thank you for saving us", Joan says,
"but what are you going to do about the Colonel?"                
""")

piper_nimbus = Scene('piper_nimbus', """
You hop up on your cloud and fly above the villagers.

"Stop!" you shout, "It\'s not safe!"
But they keeping walking into the river.                
""")

piper_image = Scene('piper_image', """
You use a bunch of afterimages to make it look like there are 10 Gokus stopping the crowd.
But the hypnotized villagers just walk right through them into the water.        
""")

piper_hint = Scene('piepr_hint', 'Maybe something that can block a long area at once?')

chase = Scene('chase', """
Colonel Chartreuse is speeding away on her bike.

What do you do?""")

chase_fight = Scene('chase_fight', 'Punch what? She\'s not here.')

chase_beam = Scene('chase_beam', """
You start to charge a Kamehameha wave...
But she is driving too erratically, you\'d never be able to hit her at this distance.                
""")

chase_pole = Scene('chase_pole', 'You pull out your power pole, but she is moving too fast for it to catch up to her.')

chase_nimbus = Scene('chase_nimbus', """
"Flying Nimubs!" you shout, and hop onto the cloud.
                     
You speed off, catching up to her quickly.
You fly up next to her.

"Don\'t you ever stay down, kid!?" she yells.                   
""")

chase_image = Scene('chase_image', """
You leave an afterimage in your spot, and start running towards her.
Meanwhile, she speeds away faster.
""")

chase_hint = Scene('chase_hint', """
What can you use to fly fast?
Maybe something from the very beginning of this story?                
""")

chase2 = Scene('chase2', """
You are flying through the air on a cloud.
Next to you, Colonel Chartreuse is speeding on a bike.

How do you finish this?
""")

chase2_fight = Scene('chase2_fight', """
You fly over to strike, but she pulls out her handgun and shoots at you.
OW!                  
""")

chase2_beam = Scene('chase2_beam', """
You glide the cloud a little further away from her.
                    
"KAAA-" you begin.
A ball of blue energy begins to form in your hands.

"MEEEEEEE-"

"What are you doing?" Chartreuse shouts.

"HAAAAAAAAAA-"

"Stop it! We\'re both moving too fast for that to be safe!"

"MEEEEEEEEEEEEE-"

She starts firing her handgun wildly at you.
"HAAAAAAAAAA!!!!

With a mighty shout, a beam of brilliant blue light leaves your hands.
It connects with the Engine of the bike, causing an explosion!

"NOOOOOOOoooooo!!..." Chartreuse shouts, as she goes flying into the distance.

Momentarily worried for her safety, you faintly see a parachute pop open in the distance.
"Well", you say, I guess she won\'t be bothering this village any more.
You reach out a hand, and catch the falling Dragonball.
Nice!                  
""")

chase2_pole = Scene('chase2_pole', """
"Power pole, extend!"
You stretch the power pole out at her.
She grabs it, and almost pulls you off the cloud.                  
""")

chase2_nimbus = Scene('chase2_nimbus', """
But... you\'re already on the nimbus...                      
""")

chase2_image = Scene('chase2_image', """
You leave an afterimage and sneak up on her from the other side.
She easily catches you every time.
turns out, the after images don\'t have a cloud under them.
She tracks the real cloud, and kicks you away.                 
""")

chase2_hint = Scene('chase2_hint', """
What would be the coolest, most anime way for Goku to end this fight?                    
""")

ending = Scene('ending', """
You fly back into town on the nimbus, Dragonball in hand.
"Ah!" Screams one of the soldiers, "He defeated the Colonel!"
"Run away! Every man for himself!" says another
They all quickly hop into vehicles and speed away...
Except for the short one from earlier, who is left behind and has to run.

"Oh Goku, Thank you!" says Joan. "How can we repay you?"
"That's ok, I just wanted to fight the bad guys" you say.
Your stomach growls in loud protest.
"Actually, do you have anything to eat?"

And so, the day is saved!
You thwarted the red ribbon army yet again.
You made new friends, and got to eat some tasty food!""")

error = Scene('error', 'sorry, I don\'t know what that means.')

crash = Scene('crash', 'Something went wrong.')

intro.add_choices({
    'tail': intro_tail,
    'beam': intro_beam,
    'swim': intro_swim,
    'nimbus': intro_nimbus,
    'pole': intro_pole,
    'image': intro_image,
    'crone': intro_crone,
    'hint': intro_hint,
    'error': error,
})

intro_tail.add_choices({
    'next': goons
})

intro_beam.add_choices({
    'next': goons
})

intro_swim.add_choices({
    'back': intro
})

intro_nimbus.add_choices({
    'back': intro
})

intro_pole.add_choices({
    'back': intro
})

intro_image.add_choices({
    'back': intro
})

intro_crone.add_choices({
    'back': intro
})

intro_hint.add_choices({
    'back': intro
})

goons.add_choices({
    'fight': goons_fight,
    'pole': goons_pole,
    'beam': goons_beam,
    'image': goons_image,
    'hint': goons_hint,
    'error': error,
})

goons_fight.add_choices({
    'next': goons_win
})

goons_pole.add_choices({
    'next': goons_win
})

goons_beam.add_choices({
    'next': goons_win
})

goons_image.add_choices({
    'next': goons_win
})

goons_hint.add_choices({
    'back': goons
})

goons_win.add_choices({
    'next_col': chartreuse
})

chartreuse.add_choices({
    'green': chartreuse_green,
    '*': chartreuse
})

chartreuse_green.add_choices({
    '*': round1
})

round1.add_choices({
    'next': round2
})

round2.add_choices({
    'fight': round2_fight,
    'beam': round2_beam,
    'pole': round2_pole,
    'nimbus': round2_nimbus,
    'image': round2_image,
    'hint': round2_hint,
    'error': error,
})

round2_fight.add_choices({
    'back': round2
})

round2_beam.add_choices({
    'back': round2
})

round2_pole.add_choices({
    'back': round2
})

round2_nimbus.add_choices({
    'back': round2
})

round2_image.add_choices({
    'next': piper
})

round2_hint.add_choices({
    'back': round2
})

piper.add_choices({
    'fight': piper_fight,
    'beam': piper_beam,
    'pole': piper_pole,
    'nimbus': piper_nimbus,
    'image': piper_image,
    'hint': piper_hint,
    'error': error,
})

piper_fight.add_choices({
    'back': piper
})

piper_beam.add_choices({
    'back': piper
})

piper_pole.add_choices({
    'next': chase
})

piper_nimbus.add_choices({
    'back': piper
})

piper_image.add_choices({
    'back': piper
})

piper_hint.add_choices({
    'back': piper
})

chase.add_choices({
    'fight': chase_fight,
    'beam': chase_beam,
    'nimbus': chase_nimbus,
    'image': chase_image,
    'hint': chase_hint,
    'error': error,
})

chase_fight.add_choices({
    'back': chase
})

chase_beam.add_choices({
    'back': chase
})

chase_nimbus.add_choices({
    'next': chase2
})

chase_image.add_choices({
    'back': chase
})

chase_hint.add_choices({
    'back': chase
})

chase2.add_choices({
    'fight': chase2_fight,
    'beam': chase2_beam,
    'pole': chase2_pole,
    'nimbus': chase2_nimbus,
    'image': chase2_image,
    'hint': chase2_hint,
    'error': error,
})

chase2_fight.add_choices({
    'back': chase2
})

chase2_beam.add_choices({
    'next': ending
})

chase2_pole.add_choices({
    'back': chase2
})

chase2_nimbus.add_choices({
    'back': chase2
})

chase2_image.add_choices({
    'back': chase2
})

chase2_hint.add_choices({
    'back': chase2
})

crash.add_choices({
    'restart': intro
})

START = 'intro'

def load_scene(name):
    """Security problem.
    Who gets to set name?
    Can that expose a variable?
    """
    return globals().get(name)

def name_scene(scene):
    """Same possible security problem.
    Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == scene:
            return key

""" class Map(object):

    scenes = {
        'intro': intro,
        'goons': goons,
        'chartreuse': chartreuse,
        'round2': round2,
        'piper': piper,
        'chase': chase,
        'chase2': chase2,
        'ending': ending
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        # print(self.next_scene(self.start_scene))
        return self.next_scene(self.start_scene)



da_map = Map('intro')
da_game = Engine(da_map)
da_game.play() """

