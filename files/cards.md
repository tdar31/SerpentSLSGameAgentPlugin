Defend -> +5 player block
Neutralize -> +3 player damage +1 weak
Strike -> +6 player damage
Survivor -> Survivor +8 player block + discard call
Backflip -> +5 player block + draw two cards
Bane -> +7 player damage, +14 player damage if enemy has poison
Dagger Spray -> +4 damage to all enemies twice
Deflect -> +4 player block
Dagger Throw -> +9 player damage draw 1 card discard 1 card
Deadly Poison -> +5 poison damage
Poisoned Stab -> +6 player damage +3 poison damage
Quick Slash -> +8 player damage + draw 1 card
Flying Knee -> +8 player damage + 1 energy next turn
Dash -> +10 player block + +10 player damage

Home hover x=636, y=375
Five Card One hover     x=388, y=663
Five Card Two hover     x=512, y=651
Five Card Three hover   x=639, y=637
Five Card Four hover    x=767, y=648
Five Card Five hover    x=881, y=676

"FIVE_CARD_ONE": (454, 336, 474, 472),
"FIVE_CARD_TWO": (453, 452, 474, 578),
"FIVE_CARD_THREE": (454, 574, 474, 710),
"FIVE_CARD_FOUR": (454, 700, 474, 836),
"FIVE_CARD_FIVE": (454, 813, 474, 948),

***Death Menu***

continue =    x=639, y=622
main menu =   x=644, y=637
play          x=104, y=440
standard      x=344, y=376
class select  x=634, y=579
embark        x=1207, y=593
talk          x=207, y=649
1 hp          x=291, y=600

menuing_delays = [1, 1.5, 1, 1, 1.5, 1, 1.5, 1]


Five Cards
health
enemy attack

identifies sprites of cards
specific cards more benefical depending on situation
numbers align to cards
can output numbers based on selection of which card "makes" the most sense

rewards

-- die
-- fail to play a card when there is energy available
-- fail to make a selection? (not sure if this is needed)
- take damage (scaled to the amount of damage)
- None selection in DDQN for card_inputs

+ use all energy
+ use as many cards as possible (this requires extra info passed in)
++ end turn when there is no energy left
++ no damage taken
++ attack enemy
+++ kill enemy

//////

basically set it up where it out puts the 1,2,3,4,5 + enter

Min/Max time inbetween training!!! basically done

No card capture at all now!!!

Hardcoded deck passed in each time and entered

Pass in Keys to excute commands (1, 2, 3, 4, 5, 6, 7, 8) and Enter

Hopefully it uses sprites from cards to grab?  Not sure how this part will work but cards are easily large enough it should hopefully be ok

Enemy attack capture probably should be hardcoded?  Not sure if the sprite is large enough it make it viewable

enemy health via the bar which could be captured? Or at least is more likely

//

https://stackoverflow.com/questions/22397289/finding-the-values-of-the-arrow-keys-in-python-why-are-they-triples

Always press one of the arrow keys left or right at start of turn

Mouse always hovers the enemy after playing card each time.  Solve issues regarding card selection for attacks versus defences

