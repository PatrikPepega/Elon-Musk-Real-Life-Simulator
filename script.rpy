# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define elonmusk = Character('Elon Musk', color="#FF0000")
define andrewtate = Character('Andrew Tate', color="#FFA500")

# The game starts here.

label splashscreen:

    $ renpy.movie_cutscene('intro.ogv')

    return

label start:
    "A one sussy day..."
    show elonmusk happy
    "elonmusk" "Welcome to my villa! You sussy boy."

label background:
    play music "audio/chinesetalking.mp3" fadein 1.0 volume 0.5
    show elonmusk happy
    "elonmusk" "My villa name is Super Ultra Chad Villa 2023."
    scene bg elonmuskvilla
    with fade
    show andrewtate happy
    play sound "audio/fard.mp3"
    "andrewtate" "I JUST FARDED LOL!"

label sprites:
    show elonmusk angry
    "elonmusk" "Oh, this is our bodyguard Andrew Tate."
    show elonmusk happy
    show andrewtate happy at right
    "elonmusk" "So, now i will show you everything."
    "elonmusk" "Wait, are you the sussy boy from tv?"
    show elonmusk angry
    "elonmusk" "Oh no. You aren't. Sorry."
    show elonmusk happy
    show andrewtate happy at right
    "andrewtate" "No he's not that guy. His name was Zdena."
label choices:
    default worked = False
    "elonmusk" "Well, did you worked in cotton factory before?"
menu:
    "Yes":
        jump choices1_a
    "No":
        jump choices1_b
label choices1_a:
    "elonmusk" "OK, here is 69 dabloons."
    $ worked = True
    jump choices1_common

label choices1_b:
    "elonmusk" "You will get your first money tommorow."
    jump choices1_common

label choices1_common:
    "elonmusk" "Now, i will show you our sussy factory."
    "elonmusk" "Come with me."

label second:
    play music "audio/bingchilling.mp3" fadein 1.0 volume 0.5
    scene bg elonmuskfactory
    with fade
    show elonmusk happy
    "elonmusk" "Welcome to our Super Sussy Chad Factory!"
    "elonmusk" "Our black people are crafting Pringles and cotton here."
    show elonmusk angry
    "elonmusk" "You will work here for 69 years."
    show andrewtate happy at right
    "andrewtate" "I will show you my bedroom soon."
    show elonmusk happy
    scene bg elonmuskfactoryinside
    show elonmusk happy
    "elonmusk" "This is our main Pringles line."
    show elonmusk angry
    "elonmusk" "I hope you like it."
    "elonmusk" "Now, let's go back to my villa."
    show andrewtate happy at right
    "andrewtate" "Time to see my bedroom!"

label third:
    play music "audio/chinesetalking.mp3" fadein 1.0 volume 0.5
    scene bg elonmuskvillainside
    with fade
    show elonmusk happy
    "elonmusk" "So, this is my villa."
    show andrewtate happy at right
    "andrewtate" "vrrrrrr"

label choices2:
    default think = False
    "elonmusk" "What do you think about my villa?"
menu:
    "OMG MEGA CHAD VILLA!":
        jump choices2_a
    "BRUH that's mid villa. My dragon have better.":
        jump choices2_b

label choices2_a:
    "elonmusk" "Thanks! Here is 6969 dabloons."
    $ think = True
    jump choices2_common

label choices2_b:
    "elonmusk" "WHAT!"
    "Game Narrator" "Well, Andrew Tate killed you, so your game end here. There are more endings, so play again to see all of them."
    return

label choices2_common:
    "elonmusk" "I need to go."
    "elonmusk" "Andrew Tate will show remaining places."

label fourth:
    play music "audio/fortnitebedroom.mp3" fadein 1.0 volume 0.5
    scene bg andrewtatebedroom
    with fade
    show andrewtate happy at right
    "andrewtate" "This is my bedroom."
    show elonmusk happy
    "elonmusk" "ANDREW TATE!"
    "elonmusk" "OH MY GOD!"
    "elonmusk" "What are you doing with our sussy worker?!?!"
    "andrewtate" "I'm just showing him my bedroom."
    "elonmusk" "Stop right now Andrew."
    "elonmusk" "Come sussy worker with me. You need to go work."

label choices3:
    default go = False
    "elonmusk" "What are you waiting for? Come with me!"
menu:
    "Sure. Im coming.":
        jump choices3_a
    "WTF!!! I wanna be with Andrew in his bedroom.":
        jump choices3_b
    
label choices3_a:
    "elonmusk" "OK, now move out from this place."
    $ go = True
    jump choices3_common

label choices3_b:
    "elonmusk" "WHAT ARE YOU THINKING YOU ARE???"
    "Game Narrator" "Elon Musk killed you with his cactus magic. There are more endings, so play again to see all of them."
    return

label choices3_common:
    play music "audio/bingchilling.mp3" fadein 1.0 volume 0.5
    scene bg elonmuskfactoryinside
    with fade
    show elonmusk angry
    "elonmusk" "Now work."
    show elonmusk happy
    "elonmusk" "I will watch you."
    "Unspecified Game Sounds without Sound" "*intense working*"
    "Unspecified Game Sounds without Sound" "*very hard working*"
    "Unspecified Game Sounds without Sound" "*Fortnite victory royale*"
    "elonmusk" "CALM DOWN!"
    "elonmusk" "You are working so much"
    "elonmusk" "Go to Andrews bedroom and sleep"

label fifth:
    play music "audio/fortnitebedroom.mp3" fadein 1.0 volume 0.5
    scene bg andrewtatebedroom
    with fade
    "Your deep voice" "It was a hard day at work"
    "Your deep voice" "Let's go sleep"
    "Game narrator" "You survived your first day at work!"
    "Game narrator" "Game ends here for now. Wait for more updates."


    
    
    
    return
