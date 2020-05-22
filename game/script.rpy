# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Ruby Ray", image="ruby")

define p = Character("Phil Phaser", image="phil")

define a = Character("Arthur", image="arthur")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg outside

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ruby outside at left

    # These display lines of dialogue.

    r "Here we are. On Ganymede. Far away from the city, as you wanted."

    show phil outside at right

    p "Call me a madman, but I still have bad feeling about this. I'll bring my gun, just to be sure."

    r "Who would have thought?"

    p "What?"

    r "Nothing. Let's get going. Thanks to you we have a long walk ahead of us."

    scene bg city

    show phil inside at right

    p "See? I told you! Something happened here. The city is empty. Everyone is gone."

    show ruby inside at left

    r "Calm down! Maybe they are just on a large gathering or something."

    p "Yeah, sure..."

    r "Look! Hotel Quantum. I bet we'll find someone there who can explain what is going on."

    scene bg lobby
    
    show phil inside at right

    p "Empty, just like the whole city."

    show ruby inside at left
    
    r "Wait! Someone is coming."

    show arthur
    
    a "Oh! New guests? Or the same old ones with new faces? Should I introduce myself or just let you shoot me down?"

    r "Why would we shoot you down? And where is everybody?"

    a "Ah, so you really are new guests. Poor souls. At the wrong time in the wrong place."

    p "I told you! I told you! We are doomed!"

    r "Phil, calm down already, and let him explain what is going on."

    a "An invasion. That's what going on. Monsters from outer space diguised as decent human beings are decimating the population."

    p "Then where is the resistance? Who is fighting this war?"

    a "They are nowhere. We are alone. Locked up in this hotel, and in all the other houses."

    r "Um... I mean, nothing has stopped us to come in. The city gates and the doors of the hotel were wide open."

    a "Hah, great. Your friend was right, we are doomed. Only the manager had a key to the front door. If the door is open, then they took it from him. So they are here. We are doomed."

    p "Not me! I'm leaving! I don't trust you. You can be one of them. Don't even try to follow me. I have a gun, and I'm not afraid to use it."

    hide phil

    r "Phil, don't be a kid!"

    show phil inside at right

    p "The door is locked!"

    a "Hah, told you. They are here. And you two fell into their trap for good."

    p "No! Never! There has to be a way out. And I'll find it."

    hide phil

    a "Well, good luck! And you, young lady, feel free to find yourself a room! At least you can spend your last days comfortable."

    r "Thank you, I guess."

    a "You are welcome. Tomorrow morning I'll hold a meeting here in the lobby with all the guests and inform them about the new situation. You should come as well. If you are still able to."

    r "I'll be here."

    scene bg room

    "Next morning..."

    show ruby room at left

    r "A new day. A new chance to survive..."

    # This ends the game.

    return
