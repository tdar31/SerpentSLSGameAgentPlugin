# SerpentSLSGameAgent (Migrated Repo)

This project is a machine learning game agent for the game Slay The Spire using the SerpentAI framework with DDQN (Reinforced Learning) and a trained CNN supervised image classifier (~3500 images for 9 classes).

Additionally this project also utilizes a second repository found [here](https://github.com/tdar31/SerpentSLSGamePlugin) but 90% of the project's code is found in this repo.

- Uses Tensorflow 1.8 + Keras, Tesseract-ocr 4.00, CUDA + CUDNN 9.1 and Anaconda
- Uses a slightly modded version of the SerpentAI framework
    - Updating deprecated methods in Keras
    - Updating Tensorflow to prevent it from allocating all of GPU's memory by default which causes crashes

![still](images/STSstill.jpg)

## Setup
- Game is launched through the Steam client at 1280x720 utilizing the BaseMod Mod which enables the command console
- Always uses ‘the Silent’ class and starts a new game
- Resets the default deck to a new deck, removes all relics and launches an encounter with the enemy 'Cultist'
    - Strike x4,  Defend x4, Poisoned Stab, Neutralize, Dodge and Roll is the deck
- Game resets when either the player or enemy die.  When this happens the encounter is reset via the command console automatically

## How it works
- The image classifier is trained to return which stages the game is in (battle, death, reward etc.) by capturing the entire game screen (once every second) then return which trained class it falls under.  Depending on the stage it's in it will execute different automated commands to return the game back to controlled battle stage in order to train the agent.
- Player and enemy stats are captured via the usage of Tesseract from both predefined and dynamic regions of the screen. 
- Decision making (DDQN) revolves around which of the five cards drawn to play each turn
- The enemy will always project its next move (attack, buff, defend etc) so the idea is that based on certain player stats, what the enemy plans on doing and the cards available to the player; a decision is made.

![webp](images/STSgif.webp)

## Reward Structure
The reward structure has been tweaked a ton and probably will be part of the project I will mess with the most.  Ultimately the goal is:
    - Encourage the bot to play cards and use all the energy it has available before ending the turn
    - Try to avoid taking as much damage as possible

The hope is that it chooses cards that buff defense to negate enemy damage then play attack cards.  The rewards structure isn't designed to be overly specific in an effort to allow the agent to actually learn through its actions.  I also want to try and allow flexibility for different cards and enemy encounters later down the road.

The actual values are somewhat arbitrary and it's more about encouraging certain behaviors

- Penalties (-)
    - Take 1 to 9 damage in one turn = -5
    - Take over 10 or more damage in one turn = -10
    - Go a turn without using energy (playing a card) = -3
- Rewards (+)
    - Use energy to play a card regardless of what it does = +10
    - If enemy is poisoned = +5

## Expanding on the project
- API
    - So clearly the much more efficient way to do this is to interact with the game via some sort of API that can pass the info to the game agent instead of using primarily OCR.  While this is true for this project I mostly wanted to focus on just building an agent that worked.  SerpentAI is built around the usage of Tesseract as a means to capture data and this method also allows for more flexibility in which types of games I can pick.  I would also need to actually make an API or restrict myself to game that have existing API's that work in this manner.  Going forward this is almost certainly be the route I would go but for this project I'll stick with this method of data capture.
- Tesseract
    - Tesseract doesn't capture single character values by default.  Had to make some weird workarounds to parse out captured values (i.e. enemy attack value).  Figuring out a better way to do this would probably help clean up the code a bit.  Need to spend some more time digging through the tesseract + skimage docs.
- Cards
    - Building out the hardcoded deck to include different cards or interactions.  For example seeing if the bot can learn to execute certain combinations of cards played in sequence
- Enemy types
    - Introducing different types of enemies with varied attack patterns etc.  Cultist is one of the easier enemies in the game to fight
- Navigating the map
    - The map menu allows for the passage
- Adding cards via reward menu and Merchant shop
    - Dynamically selecting cards to build out a deck
    - Would be pretty far down the road but I think this is by far the most interesting thing to build out as the decisions around deck building effect all other decisions made in the game
