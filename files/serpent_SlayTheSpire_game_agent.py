from serpent.game_agent import GameAgent
from serpent.machine_learning.context_classification.context_classifiers.cnn_inception_v3_context_classifier import CNNInceptionV3ContextClassifier

from serpent.input_controller import KeyboardKey
from serpent.input_controller import MouseButton
from serpent.frame_grabber import FrameGrabber

from serpent.machine_learning.reinforcement_learning.ddqn import DDQN
from serpent.machine_learning.reinforcement_learning.keyboard_mouse_action_space import KeyboardMouseActionSpace

import serpent.cv
import serpent.utilities
import serpent.ocr

from serpent.sprite import Sprite
from serpent.sprite_locator import SpriteLocator

import sklearn
import skimage.io

import time
import numpy as np
import offshoot
import random
import os
import gc

from datetime import datetime

class SerpentSlayTheSpireGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        global prevContext
        prevContext = "None"

        self.game_state = None
        self._reset_game_state()

        serpent.utilities.clear_terminal()
        print("------------------------------------")
        print("Starting up . . . ")

        self.frame_handlers["PLAY"] = self.handle_play
        self.frame_handler_setups["PLAY"] = self.setup_play
        
    def setup_play(self):
        global input_mapping

        print("------------------------------------")
        print("Loading Image Classifer . . . ")
        print("------------------------------------")

        plugin_path = offshoot.config["file_paths"]["plugins"]

        context_classifier_path = f"{plugin_path}/SerpentSlayTheSpireGameAgentPlugin/files/ml_models/context_classifier.model"

        context_classifier = CNNInceptionV3ContextClassifier(input_shape=(384, 512, 3))  # Replace with the shape (rows, cols, channels) of your captured context frames

        context_classifier.prepare_generators()
        context_classifier.load_classifier(context_classifier_path)

        self.machine_learning_models["context_classifier"] = context_classifier

        input_mapping = {
            1: [KeyboardKey.KEY_1],
            2: [KeyboardKey.KEY_2],
            3: [KeyboardKey.KEY_3],
            4: [KeyboardKey.KEY_4],
            5: [KeyboardKey.KEY_5],      
            "E": [KeyboardKey.KEY_E]                                   
        }

        action_space = KeyboardMouseActionSpace(
            card_inputs=[1, 2, 3, 4, 5, "E"]
        )

        # card_selection_model_file_path = "datasets/tdar31_slaythespire_dqn_0.9981189999999986_.h5".replace("/", os.sep)

        # DDQN setup
        self.dqn_card_selection = DDQN(
            model_file_path=card_selection_model_file_path if os.path.isfile(card_selection_model_file_path) else None,
            input_shape=(90, 160, 4),
            input_mapping=input_mapping,
            action_space=action_space,
            replay_memory_size=1000,
            max_steps=1000,
            observe_steps=100,
            batch_size=64,
            model_learning_rate=1e-4,
            initial_epsilon=1,
            final_epsilon=0.01,
            override_epsilon=True
        )

    def find_index(self):
        return print("TEST")

    def handle_play(self, game_frame):
        global prevContext
        context = self.machine_learning_models["context_classifier"].predict(game_frame.frame)
        print(context)

        if context != prevContext:
            prevContext = context
            time.sleep(1)
            return print("context doesn't match prevContext")

        if context == "DEATH_MENU":
            self.handle_DEATH_MENU(game_frame, context)

        elif context == "BATTLE_STAGE":
            self.handle_BATTLE_STAGE(game_frame, context)

        elif context == "REWARD_STAGE":
            self.handle_REWARD_STAGE(game_frame, context)

        # While these classes aren't used; the image classifer is trained to check for them
        # and maybe prove useful/important as I expand on the project.  So even though they
        # currently do nothing I am going to leave them for now

        elif context == "START_RUN":
            self.handle_START_RUN(game_frame, context)

        elif context == "MAP_MENU":
            self.handle_MAP_MENU(game_frame, context)

        elif context == "MERCHANT_MENU":
            self.handle_MERCHANT_MENU(game_frame, context)

        elif context == "MERCHANT_PRE_MENU":
            self.handle_MERCHANT_PRE_MENU(game_frame, context)

        elif context == "REST_STAGE":
            self.handle_REST_STAGE(game_frame, context)

        elif context == "SMITH_DECK_LIST":
            self.handle_SMITH_DECK_LIST(game_frame, context)

    def _reset_game_state(self):
        self.game_state = {
            "current_run": 0,
            "current_run_steps": 0,
            "last_run_duration": 0,
            "record_time_alive": dict(),
            "random_time_alive": None,
            "random_time_alives": list(),
            "run_timestamp": datetime.utcnow(),
            "masterCardList": ["Strike_G", "Strike_G", "Strike_G", "Strike_G", "Defend_G", "Defend_G", "Defend_G", "Defend_G", "Poisoned Stab", "Neutralize", "Dodge and Roll"],
            "player_energy_available": [3],
            "player_energy_total": [3],
            "player_health": [70],
            "final_cultist_attack": [0],
            "poison_check": [False],
            "run_reward_selection": 0,
            "run_predicted_selection": 0,
        }
       
    def handle_DEATH_MENU(self, game_frame, context):
        print("INSIDE DEATH_MENU function")
        global prevContext
        prevContext = "DEATH_STAGE"

        time.sleep(1)

        death_menuing_Xcoords = [639, 644, 104, 344, 634, 1207]
        death_menuing_Ycoords = [622, 637, 440, 376, 579, 593]

        menuing_delays = [1, 2, 1, 1, 1, 1]

        for elem in range(6):
            self.input_controller.move(x=death_menuing_Xcoords[elem], y=death_menuing_Ycoords[elem], duration=0.25, absolute=True)
            self.input_controller.click(button=MouseButton.LEFT, duration=0.25)

            time.sleep(menuing_delays[elem])

        time.sleep(1)
                
        self.fight_setup()

    # Remove relic and reset deck
    def fight_setup(self):
        console_commands = ["relic remove r", "deck remove a", "fight cu"]

        self.input_controller.type_string("~", 0.05)

        for elem in range(3):
            self.input_controller.type_string(console_commands[elem], 0.05)
            self.input_controller.tap_key(KeyboardKey.KEY_TAB)
            self.input_controller.tap_key(KeyboardKey.KEY_ENTER)

            time.sleep(1)

        self.input_controller.type_string("~", 0.05)

        time.sleep(1)

        self.game_state["current_run"] += 1

        print("self.dqn_card_selection.mode: --- ", self.dqn_card_selection.mode)

        if self.dqn_card_selection.mode in ["TRAIN", "RUN"]:
            print("if self.dqn_card_selection.mode in ['TRAIN', 'RUN']:")
            print("----------------------------------------------------")
            time.sleep(2)
            if self.game_state["current_run"] > 0 and self.game_state["current_run"] % 100 == 0:
                if self.dqn_card_selection.type == "DDQN":
                    self.dqn_card_selection.update_target_model()
                    
            if self.game_state["current_run"] > 0 and self.game_state["current_run"] % 20 == 0:
                self.dqn_card_selection.enter_run_mode()
                
            else:
                self.dqn_card_selection.enter_train_mode()

        # NOW INSIDE BATTLE STAGE BUT FUNCTION HASN'T BEEN TRIGGERED BY IMAGE CONTEXT CLASSIFER
        self.populating_deck()

    def populating_deck(self):
        masterCardList = self.game_state["masterCardList"]

        time.sleep(1)

        self.input_controller.type_string("~", 0.05)
        
        time.sleep(1)

        prefixCmd = "hand add "
        for elem in range(len(masterCardList)):
            print(masterCardList[elem])
            tempCard = ""
            tempCardSelection = ""

            tempCard = masterCardList[elem]
            tempCardSelection = prefixCmd + tempCard

            self.input_controller.type_string(tempCardSelection, 0.05)
            self.input_controller.tap_key(KeyboardKey.KEY_ENTER)
            time.sleep(1)

        # Closes console
        self.input_controller.type_string("~", 0.05)
        
        # Ends turn
        self.input_controller.tap_key(KeyboardKey.KEY_E)
        
        time.sleep(1.5)

    def handle_BATTLE_STAGE(self, game_frame, context):
        print("INSIDE BATTLE_STAGE function")
        global prevContext
        prevContext = "BATTLE_STAGE"

        # Player Energy
        player_energy = serpent.cv.extract_region_from_image(game_frame.frame, self.game.screen_regions["PLAYER_ENERGY"])
        player_energy_grayscale = np.array(skimage.color.rgb2gray(player_energy) * 255, dtype="uint8")

        player_energy = serpent.ocr.perform_ocr(image=player_energy_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)
        
        print("player_energy")
        print(player_energy)

        # Parses returned value from tesseract for grabbing current energy
        # Issue is that because of the swirling animation behind the numbers the OCR isn't 100% at returning this value correctly
        # The '/' is by far the most consistant value returned and it's the char that the energy values revolve around so if it's not found we force the program to refresh and grab a new game_image and try again
        if '/' in player_energy:
            print("player_energy INSIDE IF STATEMENT")
            finalArr = []

            ## Examples of type of values returned by OCR when grabbing energy
            # 3/3 <- correct
            # '3/3
            # "3 /3
            # 53 /3
            # 27/ 3
            # "3/3'
            # 3/3.
            # .3 /3
            # *3/3

            for elem in player_energy:
                # Next layer of parsing
                # If the value isn't '/' or an integer it isn't pushed into finalArr
                if (elem == "/") or (elem.isdigit() == True):
                    finalArr.append(elem)

            # Final check
            # if the length of the list is greater 3 or '/' isn't in the second position
            # Techincally this fails if the player has 10 or more energy but due to how infrequently this happens I don't have a conditional check for it
            if len(finalArr) < 3 or (finalArr[1] != "/"):
                return print("Failed to capture energy successfully // len(finalArr) < 3) or finalArr[1] != '/'")

            # Capture available and total player energy
            player_energy_available = finalArr[0]
            player_energy_total = finalArr[2]

            print("------------------------------------")
            print(player_energy_available, "/", player_energy_total)
            print("------------------------------------")

            time.sleep(1)

            self.game_state["player_energy_available"].insert(0, player_energy_available)
            self.game_state["player_energy_total"].insert(0, player_energy_total)

        else:
            print(player_energy)
            return print("Failed to capture energy successfully // captured energy value doesn't have '/'")

        # Player Health
        player_total_health = serpent.cv.extract_region_from_image(game_frame.frame, self.game.screen_regions["PLAYER_HEALTH"])
        player_total_health_grayscale = np.array(skimage.color.rgb2gray(player_total_health) * 255, dtype="uint8")

        player_health = serpent.ocr.perform_ocr(image=player_total_health_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)    

        tempArr = []

        for elem in player_health:
            if (elem.isdigit() == True):
                tempArr.append(elem)
            
            if (elem == "/"):
                break

        player_health = ''.join(tempArr)    

        print("player_health", player_health)   

        self.game_state["player_health"].insert(0, player_health)

        time.sleep(.5)

        self.enemy_action_capture(game_frame)

    def enemy_action_capture(self, game_frame):
        final_cultist_attack = []
        attack_cultist_temp_list= []

        # Unselect anything just incase
        self.input_controller.click(button=MouseButton.RIGHT, duration=0.25)
        time.sleep(.5)

        # Home hover
        self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        time.sleep(1)

        # Enemy hover
        self.input_controller.move(x=959, y=410, duration=0.25, absolute=True)

        time.sleep(.75)

        image_data = skimage.io.imread("plugins/SerpentSlayTheSpireGamePlugin/files/data/sprites/sprite_Attack_for_0.png")[..., np.newaxis]

        attack_for_cultist = Sprite("attack_for_cultist", image_data=image_data)

        # Full game frame capture
        # print("-----------Full game frame capture-----------")
        # full_game_frame = FrameGrabber.get_frames(
        #     [0],
        #     frame_shape=(self.game.frame_height, self.game.frame_width),
        #     frame_type="PIPELINE"
        # ).frames[0]

        # Allows for dynamic capture of enemy attack
        sprite_locator = SpriteLocator()
        
        attack_for_cultist_location = sprite_locator.locate(sprite=attack_for_cultist, game_frame=game_frame)
        
        print("attack_for_cultist_location: ", attack_for_cultist_location)

        # Tuples are immutable :(
        if (attack_for_cultist_location != None):
            attack_cultist_temp_list = list(attack_for_cultist_location)

            attack_cultist_temp_list[1] = attack_cultist_temp_list[1] + 45
            attack_cultist_temp_list[3] = attack_cultist_temp_list[3] + 15

            attack_for_cultist_location = tuple(attack_cultist_temp_list)

            print("Updated - attack_for_cultist_location: ", attack_for_cultist_location)
            time.sleep(1)

            cultist_attack = serpent.cv.extract_region_from_image(game_frame.frame, attack_for_cultist_location)
            cultist_attack_grayscale = np.array(skimage.color.rgb2gray(cultist_attack) * 255, dtype="uint8")

            cultist_attack = serpent.ocr.perform_ocr(image=cultist_attack_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)
            
            # This is actually an awkward work around for limitations in how tesseract works.  By default it doesn't capture single char values so when dynamically 
            # searching and capturing the enemy attack the region it's looking for the region that includes the word "for " + attack value (i.e. "for 6").  There 
            # are ways of swapping the mode of tesseract to do a capture for single char values but because the attack values are dynamic it sometimes is 
            # less than 10 or much greater than 10 which is now multiple char's and messes with the capture. For the sake of just getting it working I did this

            # TLDR: Awkward workaround for limitation in tesseract when capturing single char values.  Likely easier way to capture then parse attack value
            for elem in cultist_attack:
                if (elem.isdigit() == True):
                    final_cultist_attack.append(elem)
                    print("final_cultist_attack", final_cultist_attack)

            final_cultist_attack = ''.join(final_cultist_attack)

            print("final_cultist_attack: ", final_cultist_attack)
            print("------------------------------------")
        
            self.game_state["final_cultist_attack"].insert(0, final_cultist_attack)

            self.poison_check(game_frame)

        else:
            return print("Failed to capture enemy attack")


    def poison_check(self, game_frame):
        image_data = skimage.io.imread("plugins/SerpentSlayTheSpireGamePlugin/files/data/sprites/sprite_poison_check_0.png")[..., np.newaxis]

        poison_check = Sprite("poison_check", image_data=image_data)

        # # Full game frame capture
        # print("-----------Full game frame capture-----------")
        # full_game_frame = FrameGrabber.get_frames(
        #     [0],
        #     frame_shape=(self.game.frame_height, self.game.frame_width),
        #     frame_type="PIPELINE"
        # ).frames[0]

        sprite_locator = SpriteLocator()

        poison_check_location = sprite_locator.locate(sprite=poison_check, game_frame=game_frame)
        
        print("poison_check_location: ", poison_check_location)

        if (poison_check_location != None):
            self.game_state["poison_check"].insert(0, True)
            print("POISON_CHECK == TRUE")

        else:
            self.game_state["poison_check"].insert(0, False)
            print("POISON_CHECK == FALSE")

        self.ddqn_setup(game_frame)

    def ddqn_setup(self, game_frame):

        gc.disable()           
        
        if self.dqn_card_selection.first_run:		
            self.dqn_card_selection.first_run = False
            print("---------------first_run---------------")

            return None

        timestamp_now = datetime.utcnow()
        runtime_total = timestamp_now - self.game_state["run_timestamp"]
              
        time.sleep(1)
        print("self.dqn_card_selection.mode", self.dqn_card_selection.mode)

        if self.dqn_card_selection.frame_stack is None:
            full_game_frame = FrameGrabber.get_frames(
                [0],
                frame_shape=(self.game.frame_height, self.game.frame_width),
                frame_type="PIPELINE"
            ).frames[0]
            print("self.dqn_card_selection.frame_stack is None")

            self.dqn_card_selection.build_frame_stack(full_game_frame.frame)

            self.dqn_card_selection.frame_stack = self.dqn_card_selection.frame_stack

        else:
            print("ELSE -- self.dqn_card_selection.frame_stack is None // game_frame_buffer")
            print("INSIDE ELSE self.dqn_card_selection.mode", self.dqn_card_selection.mode)

            game_frame_buffer = FrameGrabber.get_frames(
                [0, 4, 8, 12],
                frame_shape=(self.game.frame_height, self.game.frame_width),
                frame_type="PIPELINE"
            )

            if self.dqn_card_selection.mode == "TRAIN":
                print("self.dqn_card_selection.mode == TRAIN", self.dqn_card_selection.mode)
                time.sleep(2)
        
                # calculates reward then appends it to replay memory
                reward_selection = self.calculate_reward()

                self.game_state["run_reward_selection"] += reward_selection

                self.dqn_card_selection.append_to_replay_memory(
                    game_frame_buffer,
                    reward_selection,
                    terminal=self.game_state["player_health"] == 0
                )

                if self.dqn_card_selection.current_step % 100 == 0:
                    self.dqn_card_selection.save_model_weights(
                        file_path_prefix=f"datasets/tdar31_slaythespire_selection"
                    )

                if self.dqn_card_selection.current_step % 500 == 0:
                    self.dqn_card_selection.save_model_weights(
                        file_path_prefix=f"datasets/tdar31_slaythespire_selection"
                    )

                if self.dqn_card_selection.current_step % 5000 == 0:
                    self.dqn_card_selection.save_model_weights(
                        file_path_prefix=f"datasets/tdar31_slaythespire_selection",
                        is_checkpoint=True
                    )

            elif self.dqn_card_selection.mode == "RUN":
                self.dqn_card_selection.update_frame_stack(game_frame_buffer)

            run_time = datetime.now() - self.started_at

            serpent.utilities.clear_terminal()

            print(f"SESSION RUN TIME: {run_time.days} days, {run_time.seconds // 3600} hours, {(run_time.seconds // 60) % 60} minutes, {run_time.seconds % 60} seconds")
            print("")

            print("Selection NN:\n")
            self.dqn_card_selection.output_step_data()

            print("")
            print(f"RUN: {self.game_state['current_run']}")
            print(f"RUN REWARD: {round(self.game_state['run_reward_selection'], 2)}")
            print(f"RUN PREDICTED ACTIONS: {self.game_state['run_predicted_selection']}")
            print(f"PLAYER HEALTH: {self.game_state['player_health'][0]}")                                    
            print(f"PLAYER ENERGY AVAILABLE: {self.game_state['player_energy_available'][0]}")                          
            print(f"PLAYER ENERGY TOTAL: {self.game_state['player_energy_total'][0]}")                          
            print(f"PLAYER ENERGY AVAILABLE: {self.game_state['player_energy_available'][0]}")                          
            print(f"POISON CHECK: {self.game_state['poison_check'][0]}")                          
            print(f"RUN TIME: {runtime_total.seconds} seconds")           
            print(f"LAST RUN DURATION: {self.game_state['last_run_duration']} seconds")

        self.dqn_card_selection.pick_action()
        self.dqn_card_selection.generate_action()
        card_selection_keys = self.dqn_card_selection.get_input_values()

        print("card_selection_keys", card_selection_keys)

        ddqnInputSelection = card_selection_keys[0]

        print("ddqnInputSelection", ddqnInputSelection)

        print("self.dqn_card_selection.current_action_type", self.dqn_card_selection.current_action_type)                                             
        # Starts as random?  Once frame stack is built out swaps to PREDICTED? as in delibrate choice when running .action
        # appending to memory + setting up reward calucation?

        if self.dqn_card_selection.current_action_type == "PREDICTED":
            self.game_state["run_predicted_selection"] += 1

        self.dqn_card_selection.erode_epsilon(factor=2)

        self.dqn_card_selection.next_step()

        self.ddqn_action_output(ddqnInputSelection)

    def ddqn_action_output(self, ddqnInputSelection):
        print(ddqnInputSelection)

        # Unselects anything just incase
        self.input_controller.click(button=MouseButton.RIGHT, duration=0.25)            

        if ddqnInputSelection == "KeyboardKey.KEY_E":
            print("ddqnInputSelection = E // End turn")

            self.input_controller.tap_key(ddqnInputSelection)
            time.sleep(.5)

        else:
            # This is where the chosen card is actually selected then played
            self.input_controller.tap_key(ddqnInputSelection)

            time.sleep(.5)

            play_card_Xcoords = [636, 959]
            play_card_Ycoords = [375, 410]

            for elem in range(2):
                self.input_controller.move(x=play_card_Xcoords[elem], y=play_card_Ycoords[elem], duration=0.25, absolute=True)
                time.sleep(1)

            self.input_controller.click(button=MouseButton.LEFT, duration=0.25)
            time.sleep(.5)

    def calculate_reward(self):
        reward = 0

        # 1 to 9 damage taken that turn // -5
        reward -= (5 if (int(self.game_state["player_health"][1])) - (int(self.game_state["player_health"][0])) <= 9 else 0)
        # 10 or more damage taken that turn // -10
        reward -= (10 if (int(self.game_state["player_health"][1])) - (int(self.game_state["player_health"][0])) >= 10 else 0)

        # Slight penalty if no card is played aka no energy used // -3
        reward -= (3 if (int(self.game_state["player_energy_available"][0])) == (int(self.game_state["player_energy_total"][0])) else 0)
        # Energy used to play card regardless of what it does // +10
        reward += (10 if (int(self.game_state["player_energy_available"][0])) < (int(self.game_state["player_energy_total"][1])) else 0)

        # If enemy poisoned // +5
        reward += (5 if (self.game_state["poison_check"][0] == True) else 0)

        return reward

    def handle_REWARD_STAGE(self, game_frame, context):
        print("INSIDE REWARD_STAGE function")
        global prevContext
        prevContext = "REWARD_STAGE"
        
        time.sleep(.5)

        play_card_Xcoords = [1249, 952, 563]
        play_card_Ycoords = [26, 146, 456]

        for elem in range(3):
            self.input_controller.move(x=play_card_Xcoords[elem], y=play_card_Ycoords[elem], duration=0.25, absolute=True)
            time.sleep(.75)
            self.input_controller.click(button=MouseButton.LEFT, duration=0.25)

        time.sleep(.5)

    # def handle_MERCHANT_PRE_MENU(self, game_frame, context):
    #     print("INSIDE MERCHANT_PRE_MENU function")
    #     global prevContext
    #     prevContext = "MERCHANT_PRE_MENU"
    #     time.sleep(1) 

    # def handle_MERCHANT_MENU(self, game_frame, context):
    #     print("INSIDE MERCHANT_MENU function")
    #     global prevContext
    #     prevContext = "MERCHANT_MENU"

    # def handle_MAP_MENU(self, game_frame, context):
    #     print("INSIDE MAP_MENU function")
    #     global prevContext
    #     prevContext = "MAP_MENU"
    #     time.sleep(1)

    # def handle_REST_STAGE(self, game_frame, context):
    #     print("INSIDE REST_STAGE function")
    #     global prevContext
    #     prevContext = "REST_STAGE"
    #     time.sleep(1)

    # def handle_SMITH_DECK_LIST(self, game_frame, context):
    #     print("INSIDE SMITH_DECK_LIST function")
    #     global prevContext
    #     prevContext = "SMITH_DECK_LIST"
    #     time.sleep(1)