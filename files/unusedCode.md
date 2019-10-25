# Full game frame capture
        print("-----------Full game frame capture-----------")
        full_game_frame = FrameGrabber.get_frames(
            [0],
            frame_shape=(self.game.frame_height, self.game.frame_width),
            frame_type="PIPELINE"
        ).frames[0]

        print("-----------Capture Drawpile----------")
        time.sleep(1)

        draw_pile_ONE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_ONE"])
        draw_pile_ONE_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_ONE_NAME) * 255, dtype="uint8")

        draw_pile_ONE_NAME = serpent.ocr.perform_ocr(image=draw_pile_ONE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        print("draw_pile_ONE_NAME")
        print(draw_pile_ONE_NAME)
        print("-----------")

        temp = []
        temp = draw_pile_ONE_NAME.split()

        # If OCR returns nothing stops looking for cards in draw pile
        if temp != []:

            draw_pile_total.append(int(temp[0]))
            print("draw_pile_total")
            print(draw_pile_total)
            print("-----------")
            time.sleep(1)

            # Used because of duplicate cards in deck
            for temp[0] in range(int(temp[0])):
                print(temp[1])
                captureCards.append(temp[1])

            print("captureCards")
            print(captureCards)
            print("-----------")
            time.sleep(1)
        
            # Full game frame capture
            print("-----------Full game frame capture-----------")
            full_game_frame = FrameGrabber.get_frames(
                [0],
                frame_shape=(self.game.frame_height, self.game.frame_width),
                frame_type="PIPELINE"
            ).frames[0]

            print("-----------Capture Drawpile----------")
            time.sleep(1)

            draw_pile_TWO_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_TWO"])
            draw_pile_TWO_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_TWO_NAME) * 255, dtype="uint8")

            draw_pile_TWO_NAME = serpent.ocr.perform_ocr(image=draw_pile_TWO_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

            print("draw_pile_TWO_NAME")
            print(draw_pile_TWO_NAME)
            print("-----------")
            time.sleep(1)

            temp = []
            temp = draw_pile_TWO_NAME.split()

            if temp != []:

                draw_pile_total.append(int(temp[0]))
                print("draw_pile_total")
                print(draw_pile_total)
                print("-----------")
                time.sleep(1)

                for temp[0] in range(int(temp[0])):
                    print(temp[1])
                    captureCards.append(temp[1])

                print("captureCards")
                print(captureCards)
                print("-----------")
                time.sleep(1)

                # Full game frame capture
                print("-----------Full game frame capture-----------")
                full_game_frame = FrameGrabber.get_frames(
                    [0],
                    frame_shape=(self.game.frame_height, self.game.frame_width),
                    frame_type="PIPELINE"
                ).frames[0]

                print("-----------Capture Drawpile----------")
                time.sleep(1)

                draw_pile_THREE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_THREE"])
                draw_pile_THREE_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_THREE_NAME) * 255, dtype="uint8")

                draw_pile_THREE_NAME = serpent.ocr.perform_ocr(image=draw_pile_THREE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                print("draw_pile_THREE_NAME")
                print(draw_pile_THREE_NAME)
                print("-----------")
                time.sleep(1)

                temp = []
                temp = draw_pile_THREE_NAME.split()

                if temp != []:

                    draw_pile_total.append(int(temp[0]))
                    print("draw_pile_total")
                    print(draw_pile_total)
                    print("-----------")
                    time.sleep(1)

                    for temp[0] in range(int(temp[0])):
                        print(temp[1])
                        captureCards.append(temp[1])

                    print("captureCards")
                    print(captureCards)
                    print("-----------")
                    time.sleep(1)

                    # Full game frame capture
                    print("-----------Full game frame capture-----------")
                    full_game_frame = FrameGrabber.get_frames(
                        [0],
                        frame_shape=(self.game.frame_height, self.game.frame_width),
                        frame_type="PIPELINE"
                    ).frames[0]

                    print("-----------Capture Drawpile----------")
                    time.sleep(1)

                    draw_pile_FOUR_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_FOUR"])
                    draw_pile_FOUR_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_FOUR_NAME) * 255, dtype="uint8")

                    draw_pile_FOUR_NAME = serpent.ocr.perform_ocr(image=draw_pile_FOUR_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                    print("draw_pile_FOUR_NAME")
                    print(draw_pile_FOUR_NAME)
                    print("-----------")
                    time.sleep(1)

                    temp = []
                    temp = draw_pile_FOUR_NAME.split()

                    if temp != []:

                        draw_pile_total.append(int(temp[0]))
                        print("draw_pile_total")
                        print(draw_pile_total)
                        print("-----------")
                        time.sleep(1)

                        for temp[0] in range(int(temp[0])):
                            print(temp[1])
                            captureCards.append(temp[1])

                        print("captureCards")
                        print(captureCards)
                        print("-----------")
                        time.sleep(1)

                        # Full game frame capture
                        print("-----------Full game frame capture-----------")
                        full_game_frame = FrameGrabber.get_frames(
                            [0],
                            frame_shape=(self.game.frame_height, self.game.frame_width),
                            frame_type="PIPELINE"
                        ).frames[0]

                        print("-----------Capture Drawpile----------")
                        time.sleep(1)

                        draw_pile_FIVE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_FIVE"])
                        draw_pile_FIVE_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_FIVE_NAME) * 255, dtype="uint8")

                        draw_pile_FIVE_NAME = serpent.ocr.perform_ocr(image=draw_pile_FIVE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                        print("draw_pile_FIVE_NAME")
                        print(draw_pile_FIVE_NAME)
                        print("-----------")
                        time.sleep(1)

                        temp = []
                        temp = draw_pile_FIVE_NAME.split()

                        if temp != []:

                            draw_pile_total.append(int(temp[0]))
                            print("draw_pile_total")
                            print(draw_pile_total)
                            print("-----------")
                            time.sleep(1)

                            for temp[0] in range(int(temp[0])):
                                print(temp[1])
                                captureCards.append(temp[1])

                            print("captureCards")
                            print(captureCards)
                            print("-----------")
                            time.sleep(1)


                            # Full game frame capture
                            print("-----------Full game frame capture-----------")
                            full_game_frame = FrameGrabber.get_frames(
                                [0],
                                frame_shape=(self.game.frame_height, self.game.frame_width),
                                frame_type="PIPELINE"
                            ).frames[0]

                            print("-----------Capture Drawpile----------")
                            time.sleep(1)

                            draw_pile_SIX_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_SIX"])
                            draw_pile_SIX_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_SIX_NAME) * 255, dtype="uint8")

                            draw_pile_SIX_NAME = serpent.ocr.perform_ocr(image=draw_pile_SIX_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                            print("draw_pile_SIX_NAME")
                            print(draw_pile_SIX_NAME)
                            print("-----------")
                            time.sleep(1)

                            temp = []
                            temp = draw_pile_SIX_NAME.split()

                            if temp != []:

                                draw_pile_total.append(int(temp[0]))
                                print("draw_pile_total")
                                print(draw_pile_total)
                                print("-----------")
                                time.sleep(1)

                                for temp[0] in range(int(temp[0])):
                                    print(temp[1])
                                    captureCards.append(temp[1])

                                print("captureCards")
                                print(captureCards)
                                print("-----------")
                                time.sleep(1)


                                # Full game frame capture
                                print("-----------Full game frame capture-----------")
                                full_game_frame = FrameGrabber.get_frames(
                                    [0],
                                    frame_shape=(self.game.frame_height, self.game.frame_width),
                                    frame_type="PIPELINE"
                                ).frames[0]

                                print("-----------Capture Drawpile----------")
                                time.sleep(1)

                                draw_pile_SEVEN_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_SEVEN"])
                                draw_pile_SEVEN_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_SEVEN_NAME) * 255, dtype="uint8")

                                draw_pile_SEVEN_NAME = serpent.ocr.perform_ocr(image=draw_pile_SEVEN_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                                print("draw_pile_SEVEN_NAME")
                                print(draw_pile_SEVEN_NAME)
                                print("-----------")
                                time.sleep(1)

                                temp = []
                                temp = draw_pile_SEVEN_NAME.split()

                                if temp != []:

                                    draw_pile_total.append(int(temp[0]))
                                    print("draw_pile_total")
                                    print(draw_pile_total)
                                    print("-----------")
                                    time.sleep(1)

                                    for temp[0] in range(int(temp[0])):
                                        print(temp[1])
                                        captureCards.append(temp[1])

                                    print("captureCards")
                                    print(captureCards)
                                    print("-----------")
                                    time.sleep(1)

                                    # Full game frame capture
                                    print("-----------Full game frame capture-----------")
                                    full_game_frame = FrameGrabber.get_frames(
                                        [0],
                                        frame_shape=(self.game.frame_height, self.game.frame_width),
                                        frame_type="PIPELINE"
                                    ).frames[0]

                                    print("-----------Capture Drawpile----------")
                                    time.sleep(1)

                                    draw_pile_EIGHT_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_EIGHT"])
                                    draw_pile_EIGHT_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_EIGHT_NAME) * 255, dtype="uint8")

                                    draw_pile_EIGHT_NAME = serpent.ocr.perform_ocr(image=draw_pile_EIGHT_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                                    print("draw_pile_EIGHT_NAME")
                                    print(draw_pile_EIGHT_NAME)
                                    print("-----------")
                                    time.sleep(1)

                                    temp = []
                                    temp = draw_pile_EIGHT_NAME.split()

                                    if temp != []:

                                        draw_pile_total.append(int(temp[0]))
                                        print("draw_pile_total")
                                        print(draw_pile_total)
                                        print("-----------")
                                        time.sleep(1)

                                        for temp[0] in range(int(temp[0])):
                                            print(temp[1])
                                            captureCards.append(temp[1])

                                        print("captureCards")
                                        print(captureCards)
                                        print("-----------")
                                        time.sleep(1)

                                        # Full game frame capture
                                        print("-----------Full game frame capture-----------")
                                        full_game_frame = FrameGrabber.get_frames(
                                            [0],
                                            frame_shape=(self.game.frame_height, self.game.frame_width),
                                            frame_type="PIPELINE"
                                        ).frames[0]

                                        print("-----------Capture Drawpile----------")
                                        time.sleep(1)

                                        draw_pile_NINE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DRAW_PILE_NINE"])
                                        draw_pile_NINE_NAME_grayscale = np.array(skimage.color.rgb2gray(draw_pile_NINE_NAME) * 255, dtype="uint8")

                                        draw_pile_NINE_NAME = serpent.ocr.perform_ocr(image=draw_pile_NINE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                                        print("draw_pile_NINE_NAME")
                                        print(draw_pile_NINE_NAME)
                                        print("-----------")
                                        time.sleep(1)

                                        temp = []
                                        temp = draw_pile_NINE_NAME.split()

                                        if temp != []:

                                            draw_pile_total.append(int(temp[0]))
                                            print("draw_pile_total")
                                            print(draw_pile_total)
                                            print("-----------")
                                            time.sleep(1)

                                            for temp[0] in range(int(temp[0])):
                                                print(temp[1])
                                                captureCards.append(temp[1])

                                            print("captureCards")
                                            print(captureCards)
                                            print("-----------")
                                            time.sleep(1)

                                        else:
                                            time.sleep(1)
                                            prevContext = "BATTLE_STAGE"
                                            print("----DONE-----")
                                            print("captureCards")
                                            print(captureCards)
                                            print("-----------")
                                            print("draw_pile_total")
                                            print(draw_pile_total)
                                            print("-----------")
                                            time.sleep(1)

                                    else:
                                        time.sleep(1)
                                        prevContext = "BATTLE_STAGE"
                                        print("----DONE-----")
                                        print("captureCards")
                                        print(captureCards)
                                        print("-----------")
                                        print("draw_pile_total")
                                        print(draw_pile_total)
                                        print("-----------")
                                        time.sleep(1)

                                else:
                                    time.sleep(1)
                                    prevContext = "BATTLE_STAGE"
                                    print("----DONE-----")
                                    print("captureCards")
                                    print(captureCards)
                                    print("-----------")
                                    print("draw_pile_total")
                                    print(draw_pile_total)
                                    print("-----------")
                                    time.sleep(1)

                            else:
                                time.sleep(1)
                                prevContext = "BATTLE_STAGE"
                                print("----DONE-----")
                                print("captureCards")
                                print(captureCards)
                                print("-----------")
                                print("draw_pile_total")
                                print(draw_pile_total)
                                print("-----------")
                                time.sleep(1)    

                        else:
                            time.sleep(1)
                            prevContext = "BATTLE_STAGE"
                            print("----DONE-----")
                            print("captureCards")
                            print(captureCards)
                            print("-----------")
                            print("draw_pile_total")
                            print(draw_pile_total)
                            print("-----------")
                            time.sleep(1)

                    else:
                        time.sleep(1)
                        prevContext = "BATTLE_STAGE"
                        print("----DONE-----")
                        print("captureCards")
                        print(captureCards)
                        print("-----------")
                        print("draw_pile_total")
                        print(draw_pile_total)
                        print("-----------")
                        time.sleep(1)

                else:
                    time.sleep(1)
                    prevContext = "BATTLE_STAGE"
                    print("----DONE-----")
                    print("captureCards")
                    print(captureCards)
                    print("-----------")
                    print("draw_pile_total")
                    print(draw_pile_total)
                    print("-----------")
                    time.sleep(1)

            else:
                time.sleep(1)
                prevContext = "BATTLE_STAGE"
                print("----DONE-----")
                print("captureCards")
                print(captureCards)
                print("-----------")
                print("draw_pile_total")
                print(draw_pile_total)
                print("-----------")
                time.sleep(1)            
                        
        else:
            time.sleep(1)
            prevContext = "BATTLE_STAGE"
            print("----DONE-----")
            print("captureCards")
            print(captureCards)
            print("-----------")
            print("draw_pile_total")
            print(draw_pile_total)
            print("-----------")
            time.sleep(1)

        # DISCARD/////////////////////////////////////////////////////////////////////////

        time.sleep(1)  
        print("DISCARD PILE")
        print("------------")
        time.sleep(1)  

        # Full game frame capture
        print("-----------Full game frame capture-----------")
        full_game_frame = FrameGrabber.get_frames(
            [0],
            frame_shape=(self.game.frame_height, self.game.frame_width),
            frame_type="PIPELINE"
        ).frames[0]

        print("-----------Capture Drawpile----------")
        time.sleep(1)

        discard_pile_ONE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_ONE"])
        discard_pile_ONE_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_ONE_NAME) * 255, dtype="uint8")

        discard_pile_ONE_NAME = serpent.ocr.perform_ocr(image=discard_pile_ONE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        print("discard_pile_ONE_NAME")
        print(discard_pile_ONE_NAME)
        print("-----------")

        temp = []
        temp = discard_pile_ONE_NAME.split()

        if temp != []:

            discard_pile_total.append(int(temp[0]))
            print("discard_pile_total")
            print(discard_pile_total)
            print("-----------")
            time.sleep(1)

            for temp[0] in range(int(temp[0])):
                print(temp[1])
                captureCards.append(temp[1])

            print("captureCards")
            print(captureCards)
            print("-----------")
            time.sleep(1)
        
            # Full game frame capture
            print("-----------Full game frame capture-----------")
            full_game_frame = FrameGrabber.get_frames(
                [0],
                frame_shape=(self.game.frame_height, self.game.frame_width),
                frame_type="PIPELINE"
            ).frames[0]

            print("-----------Capture Drawpile----------")
            time.sleep(1)

            discard_pile_TWO_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_TWO"])
            discard_pile_TWO_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_TWO_NAME) * 255, dtype="uint8")

            discard_pile_TWO_NAME = serpent.ocr.perform_ocr(image=discard_pile_TWO_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

            print("discard_pile_TWO_NAME")
            print(discard_pile_TWO_NAME)
            print("-----------")
            time.sleep(1)

            temp = []
            temp = discard_pile_TWO_NAME.split()

            if temp != []:

                discard_pile_total.append(int(temp[0]))
                print("discard_pile_total")
                print(discard_pile_total)
                print("-----------")
                time.sleep(1)

                for temp[0] in range(int(temp[0])):
                    print(temp[1])
                    captureCards.append(temp[1])

                print("captureCards")
                print(captureCards)
                print("-----------")
                time.sleep(1)

                # Full game frame capture
                print("-----------Full game frame capture-----------")
                full_game_frame = FrameGrabber.get_frames(
                    [0],
                    frame_shape=(self.game.frame_height, self.game.frame_width),
                    frame_type="PIPELINE"
                ).frames[0]

                print("-----------Capture Drawpile----------")
                time.sleep(1)

                discard_pile_THREE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_THREE"])
                discard_pile_THREE_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_THREE_NAME) * 255, dtype="uint8")

                discard_pile_THREE_NAME = serpent.ocr.perform_ocr(image=discard_pile_THREE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                print("discard_pile_THREE_NAME")
                print(discard_pile_THREE_NAME)
                print("-----------")
                time.sleep(1)

                temp = []
                temp = discard_pile_THREE_NAME.split()

                if temp != []:

                    discard_pile_total.append(int(temp[0]))
                    print("discard_pile_total")
                    print(discard_pile_total)
                    print("-----------")
                    time.sleep(1)

                    for temp[0] in range(int(temp[0])):
                        print(temp[1])
                        captureCards.append(temp[1])

                    print("captureCards")
                    print(captureCards)
                    print("-----------")
                    time.sleep(1)

                    # Full game frame capture
                    print("-----------Full game frame capture-----------")
                    full_game_frame = FrameGrabber.get_frames(
                        [0],
                        frame_shape=(self.game.frame_height, self.game.frame_width),
                        frame_type="PIPELINE"
                    ).frames[0]

                    print("-----------Capture Drawpile----------")
                    time.sleep(1)

                    discard_pile_FOUR_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_FOUR"])
                    discard_pile_FOUR_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_FOUR_NAME) * 255, dtype="uint8")

                    discard_pile_FOUR_NAME = serpent.ocr.perform_ocr(image=discard_pile_FOUR_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                    print("discard_pile_FOUR_NAME")
                    print(discard_pile_FOUR_NAME)
                    print("-----------")
                    time.sleep(1)

                    temp = []
                    temp = discard_pile_FOUR_NAME.split()

                    if temp != []:

                        discard_pile_total.append(int(temp[0]))
                        print("discard_pile_total")
                        print(discard_pile_total)
                        print("-----------")
                        time.sleep(1)

                        for temp[0] in range(int(temp[0])):
                            print(temp[1])
                            captureCards.append(temp[1])

                        print("captureCards")
                        print(captureCards)
                        print("-----------")
                        time.sleep(1)

                        # Full game frame capture
                        print("-----------Full game frame capture-----------")
                        full_game_frame = FrameGrabber.get_frames(
                            [0],
                            frame_shape=(self.game.frame_height, self.game.frame_width),
                            frame_type="PIPELINE"
                        ).frames[0]

                        print("-----------Capture Drawpile----------")
                        time.sleep(1)

                        discard_pile_FIVE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_FIVE"])
                        discard_pile_FIVE_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_FIVE_NAME) * 255, dtype="uint8")

                        discard_pile_FIVE_NAME = serpent.ocr.perform_ocr(image=discard_pile_FIVE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                        print("discard_pile_FIVE_NAME")
                        print(discard_pile_FIVE_NAME)
                        print("-----------")
                        time.sleep(1)

                        temp = []
                        temp = discard_pile_FIVE_NAME.split()

                        if temp != []:

                            discard_pile_total.append(int(temp[0]))
                            print("discard_pile_total")
                            print(discard_pile_total)
                            print("-----------")
                            time.sleep(1)

                            for temp[0] in range(int(temp[0])):
                                print(temp[1])
                                captureCards.append(temp[1])

                            print("captureCards")
                            print(captureCards)
                            print("-----------")
                            time.sleep(1)


                            # Full game frame capture
                            print("-----------Full game frame capture-----------")
                            full_game_frame = FrameGrabber.get_frames(
                                [0],
                                frame_shape=(self.game.frame_height, self.game.frame_width),
                                frame_type="PIPELINE"
                            ).frames[0]

                            print("-----------Capture Drawpile----------")
                            time.sleep(1)

                            discard_pile_SIX_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_SIX"])
                            discard_pile_SIX_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_SIX_NAME) * 255, dtype="uint8")

                            discard_pile_SIX_NAME = serpent.ocr.perform_ocr(image=discard_pile_SIX_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                            print("discard_pile_SIX_NAME")
                            print(discard_pile_SIX_NAME)
                            print("-----------")
                            time.sleep(1)

                            temp = []
                            temp = discard_pile_SIX_NAME.split()

                            if temp != []:

                                discard_pile_total.append(int(temp[0]))
                                print("discard_pile_total")
                                print(discard_pile_total)
                                print("-----------")
                                time.sleep(1)

                                for temp[0] in range(int(temp[0])):
                                    print(temp[1])
                                    captureCards.append(temp[1])

                                print("captureCards")
                                print(captureCards)
                                print("-----------")
                                time.sleep(1)


                                # Full game frame capture
                                print("-----------Full game frame capture-----------")
                                full_game_frame = FrameGrabber.get_frames(
                                    [0],
                                    frame_shape=(self.game.frame_height, self.game.frame_width),
                                    frame_type="PIPELINE"
                                ).frames[0]

                                print("-----------Capture Drawpile----------")
                                time.sleep(1)

                                discard_pile_SEVEN_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_SEVEN"])
                                discard_pile_SEVEN_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_SEVEN_NAME) * 255, dtype="uint8")

                                discard_pile_SEVEN_NAME = serpent.ocr.perform_ocr(image=discard_pile_SEVEN_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                                print("discard_pile_SEVEN_NAME")
                                print(discard_pile_SEVEN_NAME)
                                print("-----------")
                                time.sleep(1)

                                temp = []
                                temp = discard_pile_SEVEN_NAME.split()

                                if temp != []:

                                    discard_pile_total.append(int(temp[0]))
                                    print("discard_pile_total")
                                    print(discard_pile_total)
                                    print("-----------")
                                    time.sleep(1)

                                    for temp[0] in range(int(temp[0])):
                                        print(temp[1])
                                        captureCards.append(temp[1])

                                    print("captureCards")
                                    print(captureCards)
                                    print("-----------")
                                    time.sleep(1)

                                    # Full game frame capture
                                    print("-----------Full game frame capture-----------")
                                    full_game_frame = FrameGrabber.get_frames(
                                        [0],
                                        frame_shape=(self.game.frame_height, self.game.frame_width),
                                        frame_type="PIPELINE"
                                    ).frames[0]

                                    print("-----------Capture Drawpile----------")
                                    time.sleep(1)

                                    discard_pile_EIGHT_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_EIGHT"])
                                    discard_pile_EIGHT_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_EIGHT_NAME) * 255, dtype="uint8")

                                    discard_pile_EIGHT_NAME = serpent.ocr.perform_ocr(image=discard_pile_EIGHT_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                                    print("discard_pile_EIGHT_NAME")
                                    print(discard_pile_EIGHT_NAME)
                                    print("-----------")
                                    time.sleep(1)

                                    temp = []
                                    temp = discard_pile_EIGHT_NAME.split()

                                    if temp != []:

                                        discard_pile_total.append(int(temp[0]))
                                        print("discard_pile_total")
                                        print(discard_pile_total)
                                        print("-----------")
                                        time.sleep(1)

                                        for temp[0] in range(int(temp[0])):
                                            print(temp[1])
                                            captureCards.append(temp[1])

                                        print("captureCards")
                                        print(captureCards)
                                        print("-----------")
                                        time.sleep(1)

                                        # Full game frame capture
                                        print("-----------Full game frame capture-----------")
                                        full_game_frame = FrameGrabber.get_frames(
                                            [0],
                                            frame_shape=(self.game.frame_height, self.game.frame_width),
                                            frame_type="PIPELINE"
                                        ).frames[0]

                                        print("-----------Capture Drawpile----------")
                                        time.sleep(1)

                                        discard_pile_NINE_NAME = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["DISCARD_PILE_NINE"])
                                        discard_pile_NINE_NAME_grayscale = np.array(skimage.color.rgb2gray(discard_pile_NINE_NAME) * 255, dtype="uint8")

                                        discard_pile_NINE_NAME = serpent.ocr.perform_ocr(image=discard_pile_NINE_NAME_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

                                        print("discard_pile_NINE_NAME")
                                        print(discard_pile_NINE_NAME)
                                        print("-----------")
                                        time.sleep(1)

                                        temp = []
                                        temp = discard_pile_NINE_NAME.split()

                                        if temp != []:

                                            discard_pile_total.append(int(temp[0]))
                                            print("discard_pile_total")
                                            print(discard_pile_total)
                                            print("-----------")
                                            time.sleep(1)

                                            for temp[0] in range(int(temp[0])):
                                                print(temp[1])
                                                captureCards.append(temp[1])

                                            print("captureCards")
                                            print(captureCards)
                                            print("-----------")
                                            time.sleep(1)

                                        else:
                                            time.sleep(1)
                                            prevContext = "BATTLE_STAGE"
                                            print("----DONE-----")
                                            print("captureCards")
                                            print(captureCards)
                                            print("-----------")
                                            print("discard_pile_total")
                                            print(discard_pile_total)
                                            print("-----------")
                                            time.sleep(1)

                                    else:
                                        time.sleep(1)
                                        prevContext = "BATTLE_STAGE"
                                        print("----DONE-----")
                                        print("captureCards")
                                        print(captureCards)
                                        print("-----------")
                                        print("discard_pile_total")
                                        print(discard_pile_total)
                                        print("-----------")
                                        time.sleep(1)

                                else:
                                    time.sleep(1)
                                    prevContext = "BATTLE_STAGE"
                                    print("----DONE-----")
                                    print("captureCards")
                                    print(captureCards)
                                    print("-----------")
                                    print("discard_pile_total")
                                    print(discard_pile_total)
                                    print("-----------")
                                    time.sleep(1)

                            else:
                                time.sleep(1)
                                prevContext = "BATTLE_STAGE"
                                print("----DONE-----")
                                print("captureCards")
                                print(captureCards)
                                print("-----------")
                                print("discard_pile_total")
                                print(discard_pile_total)
                                print("-----------")
                                time.sleep(1)    

                        else:
                            time.sleep(1)
                            prevContext = "BATTLE_STAGE"
                            print("----DONE-----")
                            print("captureCards")
                            print(captureCards)
                            print("-----------")
                            print("discard_pile_total")
                            print(discard_pile_total)
                            print("-----------")
                            time.sleep(1)

                    else:
                        time.sleep(1)
                        prevContext = "BATTLE_STAGE"
                        print("----DONE-----")
                        print("captureCards")
                        print(captureCards)
                        print("-----------")
                        print("discard_pile_total")
                        print(discard_pile_total)
                        print("-----------")
                        time.sleep(1)

                else:
                    time.sleep(1)
                    prevContext = "BATTLE_STAGE"
                    print("----DONE-----")
                    print("captureCards")
                    print(captureCards)
                    print("-----------")
                    print("discard_pile_total")
                    print(discard_pile_total)
                    print("-----------")
                    time.sleep(1)

            else:
                time.sleep(1)
                prevContext = "BATTLE_STAGE"
                print("----DONE-----")
                print("captureCards")
                print(captureCards)
                print("-----------")
                print("discard_pile_total")
                print(discard_pile_total)
                print("-----------")
                time.sleep(1)            
                        
        else:
            time.sleep(1)
            prevContext = "BATTLE_STAGE"
            print("----DONE-----")
            print("captureCards")
            print(captureCards)
            print("-----------")
            print("discard_pile_total")
            print(discard_pile_total)
            print("-----------")
            time.sleep(1)

        print("---------------")
        print("FINAL CARD CAPTURE")
        print("---------------")
        time.sleep(1)
        print("FINAL captureCards")
        print(captureCards)
        print("-----------")
        print("FINAL discard_pile_total")
        print(discard_pile_total)
        print("-----------")
        print("FINAL draw_pile_total")
        print(draw_pile_total)
        print("-----------")
        time.sleep(1)

        discardSum = sum(discard_pile_total)
        print("discardSum")
        print(discardSum)
        print("-----------")
        time.sleep(1)

        drawSum = sum(draw_pile_total)
        print("drawSum")
        print(drawSum)
        print("-----------")
        time.sleep(1)

        totalPileSum = (int(discardSum) + int(drawSum))
        print("totalPileSum")
        print(totalPileSum)
        print("-----------")
        time.sleep(1)

        remainingCards = masterDeckList[:]
        print("remainingCards COPY", remainingCards)
        time.sleep(1)
 
        for x in captureCards:
            print("captureCards -> x:", x)
            if (x in remainingCards):
                remainingCards.remove(x)
        
        print("remainingCards", remainingCards)
        time.sleep(1)

        /
        /
        /
        /
        /
        /
        /
        /
        /
        /
        /


        # if sevenCard == True:   
        #     prevContext = "BATTLE_STAGE"
        #     print("sevenCard TRUE")
        #     print("-----------")
        #     print("sevenCard selection SET TO FALSE")
        #     sevenCard = False
        #     time.sleep(1)

        #     ## Seven Card One hover
        #     self.input_controller.move(x=286, y=642, duration=0.25, absolute=True)
        #     time.sleep(1.5)

        #     # Full game frame capture
        #     print("-----------Full game frame capture-----------")

        #     full_game_frame = FrameGrabber.get_frames(
        #         [0],
        #         frame_shape=(self.game.frame_height, self.game.frame_width),
        #         frame_type="PIPELINE"
        #     ).frames[0]

        #     print("-----------Capture seven_card_one----------")
        #     time.sleep(1)

        #     seven_card_one = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["SEVEN_CARD_ONE"])
        #     seven_card_one_grayscale = np.array(skimage.color.rgb2gray(seven_card_one) * 255, dtype="uint8")

        #     seven_card_one = serpent.ocr.perform_ocr(image=seven_card_one_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        #     print("seven_card_one")
        #     print(seven_card_one)
        #     print("-----------")
        #     captureCards.append(seven_card_one)
        #     time.sleep(1)

        #     # Home hover
        #     self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        #     time.sleep(1)

        #     ## Seven Card Two hover
        #     self.input_controller.move(x=389, y=669, duration=0.25, absolute=True)
        #     time.sleep(1.5)

        #     # Full game frame capture
        #     print("-----------Full game frame capture-----------")

        #     full_game_frame = FrameGrabber.get_frames(
        #         [0],
        #         frame_shape=(self.game.frame_height, self.game.frame_width),
        #         frame_type="PIPELINE"
        #     ).frames[0]

        #     print("-----------Capture seven_card_two-----------")

        #     seven_card_two = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["SEVEN_CARD_TWO"])
        #     seven_card_two_grayscale = np.array(skimage.color.rgb2gray(seven_card_two) * 255, dtype="uint8")

        #     seven_card_two = serpent.ocr.perform_ocr(image=seven_card_two_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        #     print("seven_card_two")
        #     print(seven_card_two)
        #     print("-----------")
        #     captureCards.append(seven_card_two)
        #     time.sleep(1)

        #     # Home hover
        #     self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        #     time.sleep(1)

        #     ## Seven Card Three hover
        #     self.input_controller.move(x=502, y=659, duration=0.25, absolute=True)
        #     time.sleep(1.5)

        #     # Full game frame capture
        #     print("-----------Full game frame capture-----------")

        #     full_game_frame = FrameGrabber.get_frames(
        #         [0],
        #         frame_shape=(self.game.frame_height, self.game.frame_width),
        #         frame_type="PIPELINE"
        #     ).frames[0]

        #     print("-----------Capture seven_card_three-----------")

        #     seven_card_three = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["SEVEN_CARD_THREE"])
        #     seven_card_three_grayscale = np.array(skimage.color.rgb2gray(seven_card_three) * 255, dtype="uint8")

        #     seven_card_three = serpent.ocr.perform_ocr(image=seven_card_three_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        #     print("seven_card_three")
        #     print(seven_card_three)
        #     print("-----------")
        #     captureCards.append(seven_card_three)
        #     time.sleep(1)

        #     # Home hover
        #     self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        #     time.sleep(1)

        #     ## Seven Card Four hover
        #     self.input_controller.move(x=631, y=650, duration=0.25, absolute=True)
        #     time.sleep(1.5)

        #     # Full game frame capture
        #     print("-----------Full game frame capture-----------")

        #     full_game_frame = FrameGrabber.get_frames(
        #         [0],
        #         frame_shape=(self.game.frame_height, self.game.frame_width),
        #         frame_type="PIPELINE"
        #     ).frames[0]

        #     print("-----------Capture seven_card_four-----------")

        #     seven_card_four = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["SEVEN_CARD_FOUR"])
        #     seven_card_four_grayscale = np.array(skimage.color.rgb2gray(seven_card_four) * 255, dtype="uint8")

        #     seven_card_four = serpent.ocr.perform_ocr(image=seven_card_four_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        #     print("seven_card_four")
        #     print(seven_card_four)
        #     print("-----------")
        #     captureCards.append(seven_card_four)
        #     time.sleep(1)

        #     # Home hover
        #     self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        #     time.sleep(1)

        #     ## Seven Card Five hover
        #     self.input_controller.move(x=760, y=645, duration=0.25, absolute=True)
        #     time.sleep(1.5)

        #     # Full game frame capture
        #     print("-----------Full game frame capture-----------")

        #     full_game_frame = FrameGrabber.get_frames(
        #         [0],
        #         frame_shape=(self.game.frame_height, self.game.frame_width),
        #         frame_type="PIPELINE"
        #     ).frames[0]

        #     print("-----------Capture seven_card_five-----------")

        #     seven_card_five = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["SEVEN_CARD_FIVE"])
        #     seven_card_five_grayscale = np.array(skimage.color.rgb2gray(seven_card_five) * 255, dtype="uint8")

        #     seven_card_five = serpent.ocr.perform_ocr(image=seven_card_five_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        #     print("seven_card_five")
        #     print(seven_card_five)
        #     print("-----------")
        #     captureCards.append(seven_card_five)
        #     time.sleep(1)

        #     # Home hover
        #     self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        #     time.sleep(1)

        #     ## Seven Card Six hover
        #     self.input_controller.move(x=867, y=670, duration=0.25, absolute=True)
        #     time.sleep(1.5)

        #     # Full game frame capture
        #     print("-----------Full game frame capture-----------")

        #     full_game_frame = FrameGrabber.get_frames(
        #         [0],
        #         frame_shape=(self.game.frame_height, self.game.frame_width),
        #         frame_type="PIPELINE"
        #     ).frames[0]

        #     print("-----------Capture seven_card_six-----------")

        #     seven_card_six = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["SEVEN_CARD_SIX"])
        #     seven_card_six_grayscale = np.array(skimage.color.rgb2gray(seven_card_six) * 255, dtype="uint8")

        #     seven_card_six = serpent.ocr.perform_ocr(image=seven_card_six_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        #     print("seven_card_six")
        #     print(seven_card_six)
        #     print("-----------")
        #     captureCards.append(seven_card_six)
        #     time.sleep(1)

        #     # Home hover
        #     self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        #     time.sleep(1)

        #     ## Seven Card Seven hover
        #     self.input_controller.move(x=1010, y=682, duration=0.25, absolute=True)
        #     time.sleep(1.5)

        #     # Full game frame capture
        #     print("-----------Full game frame capture-----------")

        #     full_game_frame = FrameGrabber.get_frames(
        #         [0],
        #         frame_shape=(self.game.frame_height, self.game.frame_width),
        #         frame_type="PIPELINE"
        #     ).frames[0]

        #     print("-----------Capture seven_card_seven-----------")

        #     seven_card_seven = serpent.cv.extract_region_from_image(full_game_frame.frame, self.game.screen_regions["SEVEN_CARD_SEVEN"])
        #     seven_card_seven_grayscale = np.array(skimage.color.rgb2gray(seven_card_seven) * 255, dtype="uint8")

        #     seven_card_seven = serpent.ocr.perform_ocr(image=seven_card_seven_grayscale, scale=15, order=5, horizontal_closing=2, vertical_closing=1)

        #     print("seven_card_seven")
        #     print(seven_card_seven)
        #     print("-----------")
        #     captureCards.append(seven_card_seven)
        #     time.sleep(1)

        #     # Home hover
        #     self.input_controller.move(x=636, y=375, duration=0.25, absolute=True)
        #     time.sleep(1)

        #     print(captureCards)
        #     print("-----------CaptureCards--------------")
        #     time.sleep(2)

        # else

            # Well Laid Plans = . "el'l-Laid 13m in FIVE_CARD_FOUR