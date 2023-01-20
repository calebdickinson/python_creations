"""
Logic tree + strings for Choose Your Own Adventure Story
Generates + prints one series of random ints.
Each printed series of random ints ends with 1 of these 3 descriptors:
["REDIRECT", "UNWRITTEN", "THE END"], followed by final string.
Each number proceeds the string that it is assigned to.
Each string is followed by either a descripter or a newline in the terminal.
Printed newlines serve no other function except making output more readable.
Number + string + (if num series end) descripter OR
(elif num series continue) newline.

Unfinished
"""
import random
print(1)
print(
    "You are off to seek your fortune.\n"
    "There are five roads that lead away from the town where you live.\n"
    "Which road do you choose to travel?"
)
print("")
_1 = random.randint(2, 6)
if _1 == 2:
    print(_1)
    print(
        "You begin your journey down Chittyville Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    print("")
    _2 = random.randint(7, 9)
    if _2 == 7:
        print(_2)
        print("You walk all day long.  You walk 3 miles.  It is getting dark.  You see a nice hotel ahead of you.  If you go to the hotel, go to p. 22.  If you walk on, go to p. 23.")
        print("")
        _7 = random.randint(22, 23)
        if _7 == 22:
            print(_7)
            print("You have a nice sleep. In the morning you get up and eat breakfast. You hear everyone talking about something terrible that happened in Rehdeck. If you ask the man who is talking about it, go to p. 89. If you leave the hotel and start walking down Chittyville road, then go to p. 90.")
            print("")
            _22 = random.randint(89, 90)
            if _22 == 89:
                print(_22)
                print("")
                print("THE END")
            if _22 == 90:
                print(_22)
                print("")
                print("")
                _90 = random.randint(267, 268)
                if _90 == 267:
                    print(_90)
                    print("")
                    print("")
                if _90 == 268:
                    print(_90)
                    print("")
                    print("")
        if _7 == 23:
            print(_7)
            print("Eventually you are forced to sleep by the side of the road. But the soft grass is not uncomfortable. In the morning you get up and continue walking. By bedtime, you come to Chittyville. If you book in at a hotel, go to p. 91. If you sleep by the side of the road, them go to p. 92.")
            print("")
            _23 = random.randint(91, 92)
            if _23 == 91:
                print(_23)
                print("")
                print("")
                _91 = random.randint(269, 270)
                if _91 == 269:
                    print(_91)
                    print("")
                    print("")
                if _91 == 270:
                    print(_91)
                    print("")
                    print("")
            if _23 == 92:
                print(_23)
                print("")
                print("")
                _92 = random.randint(271, 272)
                if _92 == 271:
                    print(_92)
                    print("")
                    print("")
                if _92 == 272:
                    print(_92)
                    print("")
                    print("")
    if _2 == 8:
        print(_2)
        print("You bike on. At noon, you pass a hotel, and bike on. By afternoon you reach to the city of Chittyville. If you sleep by the side of the road, go to p. 24.  if you try to bike back to the nice hotel, go to p.25.  If you go to Holiday Inn and Suits, go to p. 26.  if you go to happy pappy Motel, go to p. 27.  If you go to Delux Chat Qoue hotel, go to p. 28.  if you keep biking, go to p. 29.")
        print("")
        _8 = random.randint(24, 29)
        if _8 == 24:
            print(_8)
            print("When you wake up, you find that your bike has been stolen. If you go to the police station and report, go to p. 93. If you walk on, go to p. 94. If you go to a store to but a bike, go to p. 95.")
            print("")
            _24 = random.randint(93, 95)
            if _24 == 93:
                print(_24)
                print("")
                print("")
                _93 = random.randint(273, 274)
                if _93 == 273:
                    print(_93)
                    print("")
                    print("")
                if _93 == 274:
                    print(_93)
                    print("")
                    print("")
            if _24 == 94:
                print(_24)
                print("")
                print("")
                _94 = random.randint(275, 276)
                if _94 == 275:
                    print(_94)
                    print("")
                    print("")
                if _94 == 276:
                    print(_94)
                    print("")
                    print("")
            if _24 == 95:
                print(_24)
                print("")
                print("")
                _95 = random.randint(277, 281)
                if _95 == 277:
                    print(_95)
                    print("")
                    print("")
                if _95 == 278:
                    print(_95)
                    print("")
                    print("")
                if _95 == 279:
                    print(_95)
                    print("")
                    print("")
                if _95 == 280:
                    print(_95)
                    print("")
                    print("")
                if _95 == 281:
                    print(_95)
                    print("")
                    print("")
        if _8 == 25:
            print(_8)
            print("You go back. Just as you see the hotel, an earthquake comes. You fall over in the middle of the road and die.")
            print("THE END")
        if _8 == 26:
            print(_8)
            print("You are awakened by an earthquake, but you are so tired that you soon go back to sleep. In the morning, after wake up and eat breakfast, you go down to the pool to relax.  You see a dog swimming in the swimming pool. If you scream, g to p. 96. if you get in the swimming pool, go to p. 97. If you leap up and down screaming, go to p. 98. if you become sick and throw up, go to p. 99. if you cover you eyes up, go to p. 100. If you get in a the warm pool, go to p. 101. If you get in a chair, go to p. 102. if you call and report, go to p. 102. if you leave the room, got p. 104. If you go in the sauna, go to p. 105. If you move around the room, go t p.106. If you do nothing, go to p. 107.")
            print("")
            _26 = random.randint(57, 72)
            if _26 == 96:
                print(_26)
                print("")
                print("")
                _96 = random.randint(282, 286)
                if _96 == 282:
                    print(_96)
                    print("")
                    print("")
                if _96 == 283:
                    print(_96)
                    print("")
                    print("")
                if _96 == 284:
                    print(_96)
                    print("")
                    print("")
                if _96 == 285:
                    print(_96)
                    print("")
                    print("")
                if _96 == 286:
                    print(_96)
                    print("")
                    print("")
            if _26 == 97:
                print(_26)
                print("")
                print("")
                _97 = random.randint(287, 292)
                if _97 == 287:
                    print(_97)
                    print("")
                    print("")
                if _97 == 288:
                    print(_97)
                    print("")
                    print("")
                if _97 == 289:
                    print(_97)
                    print("")
                    print("")
                if _97 == 290:
                    print(_97)
                    print("")
                    print("")
                if _97 == 291:
                    print(_97)
                    print("")
                    print("")
                if _97 == 292:
                    print(_97)
                    print("")
                    print("")
            if _26 == 98:
                print(_26)
                print("")
                print("")
                _98 = random.randint(293, 294)
                if _98 == 293:
                    print(_98)
                    print("")
                    print("")
                if _98 == 294:
                    print(_98)
                    print("")
                    print("")
            if _26 == 99:
                print(_26)
                print("")
                print("")
                _99 = random.randint(295, 299)
                if _99 == 295:
                    print(_99)
                    print("")
                    print("")
                if _99 == 296:
                    print(_99)
                    print("")
                    print("")
                if _99 == 297:
                    print(_99)
                    print("")
                    print("")
                if _99 == 298:
                    print(_99)
                    print("")
                    print("")
                if _99 == 299:
                    print(_99)
                    print("")
                    print("")
            if _26 == 100:
                print(_26)
                print("")
                print("")
                _100 = random.randint(300, 303)
                if _100 == 300:
                    print(_100)
                    print("")
                    print("")
                if _100 == 301:
                    print(_100)
                    print("")
                    print("")
                if _100 == 302:
                    print(_100)
                    print("")
                    print("")
                if _100 == 303:
                    print(_100)
                    print("")
                    print("")
            if _26 == 101:
                print(_26)
                print("")
                print("")
                _101 = random.randint(304, 306)
                if _101 == 304:
                    print(_101)
                    print("")
                    print("")
                if _101 == 305:
                    print(_101)
                    print("")
                    print("")
                if _101 == 306:
                    print(_101)
                    print("")
                    print("")
            if _26 == 102:
                print(_26)
                print("")
                print("")
                _102 = random.randint(307, 309)
                if _102 == 307:
                    print(_102)
                    print("")
                    print("")
                if _102 == 308:
                    print(_102)
                    print("")
                    print("")
                if _102 == 309:
                    print(_102)
                    print("")
                    print("")
            if _26 == 103:
                print(_26)
                print("")
                print("")
                _103 = random.randint(310, 313)
                if _103 == 310:
                    print(_103)
                    print("")
                    print("")
                if _103 == 311:
                    print(_103)
                    print("")
                    print("")
                if _103 == 312:
                    print(_103)
                    print("")
                    print("")
                if _103 == 313:
                    print(_103)
                    print("")
                    print("")
            if _26 == 104:
                print(_26)
                print("")
                print("")
                _104 = random.randint(314, 317)
                if _104 == 314:
                    print(_104)
                    print("")
                    print("")
                if _104 == 315:
                    print(_104)
                    print("")
                    print("")
                if _104 == 316:
                    print(_104)
                    print("")
                    print("")
                if _104 == 317:
                    print(_104)
                    print("")
                    print("")
            if _26 == 105:
                print(_26)
                print("")
                print("")
                _105 = random.randint(318, 325)
                if _105 == 318:
                    print(_105)
                    print("")
                    print("")
                if _105 == 319:
                    print(_105)
                    print("")
                    print("")
                if _105 == 320:
                    print(_105)
                    print("")
                    print("")
                if _105 == 321:
                    print(_105)
                    print("")
                    print("")
                if _105 == 322:
                    print(_105)
                    print("")
                    print("")
                if _105 == 323:
                    print(_105)
                    print("")
                    print("")
                if _105 == 324:
                    print(_105)
                    print("")
                    print("")
                if _105 == 325:
                    print(_105)
                    print("")
                    print("")
            if _26 == 106:
                print(_26)
                print("")
                print("")
                _106 = random.randint(326, 328)
                if _106 == 326:
                    print(_106)
                    print("")
                    print("")
                if _106 == 327:
                    print(_106)
                    print("")
                    print("")
                if _106 == 328:
                    print(_106)
                    print("")
                    print("")
            if _26 == 107:
                print(_26)
                print("")
                print("")
                _107 = random.randint(329, 334)
                if _107 == 329:
                    print(_107)
                    print("")
                    print("")
                if _107 == 330:
                    print(_107)
                    print("")
                    print("")
                if _107 == 331:
                    print(_107)
                    print("")
                    print("")
                if _107 == 332:
                    print(_107)
                    print("")
                    print("")
                if _107 == 333:
                    print(_107)
                    print("")
                    print("")
                if _107 == 334:
                    print(_107)
                    print("")
                    print("")
        if _8 == 27:
            print(_8)
            print("After sleeping on a bed that is as hard as stone, you wake up in the morning feeling so sore that you can’t get out of bed. If you scream for help, go to p. 108. If you do nothing, go to p. 109.")
            print("")
            _27 = random.randint(108, 109)
            if _27 == 108:
                print(_27)
                print("")
                print("")
                _108 = random.randint(335, 342)
                if _108 == 335:
                    print(_108)
                    print("")
                    print("")
                if _108 == 336:
                    print(_108)
                    print("")
                    print("")
                if _108 == 337:
                    print(_108)
                    print("")
                    print("")
                if _108 == 338:
                    print(_108)
                    print("")
                    print("")
                if _108 == 339:
                    print(_108)
                    print("")
                    print("")
                if _108 == 340:
                    print(_108)
                    print("")
                    print("")
                if _108 == 341:
                    print(_108)
                    print("")
                    print("")
                if _108 == 342:
                    print(_108)
                    print("")
                    print("")
            if _27 == 109:
                print(_27)
                print("")
                print("THE END")
        if _8 == 28:
            print(_8)
            print("The waiters all treat you with extreme kindness. They carry you to your room on a silken glass litter. After you arrive, they feed you a 57 course dinner, and a 33 course supper, followed by a 10 course fifth meal, which is followed by a Grand Maurace Rodele A Leche Dessert which includes rediced sherbet made of Modal PokePin Berries imported from Mars, and 99 other sweet dishes!")
            print("")
            print("After you go to sleep you hear a loud sound.  If you get up, go to p. 110.  If you go back to sleep, go to p. 111.")
            print("")
            _28 = random.randint(110, 111)
            if _28 == 110:
                print(_28)
                print("")
                print("")
                _110 = random.randint(343, 346)
                if _110 == 343:
                    print(_110)
                    print("")
                    print("")
                if _110 == 344:
                    print(_110)
                    print("")
                    print("")
                if _110 == 345:
                    print(_110)
                    print("")
                    print("")
                if _110 == 346:
                    print(_110)
                    print("")
                    print("")
            if _28 == 111:
                print(_28)
                print("")
                print("THE END")
        if _8 == 29:
            print(_8)
            print("You soon fall over asleep. When you wake up, an earthquake is shaking you violently. If you go back to sleep, go to p. 112. If you get up, go to p. 113.")
            print("")
            _29 = random.randint(112, 113)
            if _29 == 112:
                print(_29)
                print("")
                print("")
                _112 = random.randint(347, 348)
                if _112 == 347:
                    print(_112)
                    print("")
                    print("")
                if _112 == 348:
                    print(_112)
                    print("")
                    print("")
            if _29 == 113:
                print(_29)
                print("")
                print("")
                _113 = random.randint(349, 351)
                if _113 == 349:
                    print(_113)
                    print("")
                    print("")
                if _113 == 350:
                    print(_113)
                    print("")
                    print("")
                if _113 == 351:
                    print(_113)
                    print("")
                    print("")
    if _2 == 9:
        print(9)
        print("You pass a nice hotel after 30 minutes of driving, and in another 30 minutes, you pass through Chittyville, (Which is by the way, 21 miles from where you started) and drive on.  You drive on and on. Now it is just farmland.  Eventually, after about 300 miles of driving, you come to a fork in the road.  It is getting dark. A sign says: go right to go to Vesterville and Combden.  Go left to go to Pristine Harbor, or the Capital City.  Vesterville” 4 miles. Combden: 57 miles. Pristine Harbor: 382 miles. Capital city (Mogol): 96 miles.  If you turn right, go to p. 30. If you turn left, go to p. 31.")
        print("")
        _9 = random.randint(30, 31)
        if _9 == 30:
            print(_9)
            print("You go to Vesterville for the night and have a nice sleep in a good hotel. In the morning, you get up and continue driving. If you turn on the news, go to p. 114. If you don't go to p. 115.")
            print("")
            _30 = random.randint(112, 113)
            if _30 == 114:
                print(_30)
                print("")
                print("")
                _114 = random.randint(352, 353)
                if _114 == 352:
                    print(_114)
                    print("")
                    print("")
                if _114 == 353:
                    print(_114)
                    print("")
                    print("")
            if _30 == 115:
                print(_30)
                print("")
                print("")
                _115 = random.randint(354, 356)
                if _115 == 354:
                    print(_115)
                    print("")
                    print("")
                if _115 == 355:
                    print(_115)
                    print("")
                    print("")
                if _115 == 356:
                    print(_115)
                    print("")
                    print("")
        if _9 == 31:
            print(_9)
            print("While you are driving, an earthquake suddenly begins. If you keep on driving, go to p. 116. if you stop the car on the side of the road, got to p. 117.")
            print("")
            _31 = random.randint(112, 113)
            if _31 == 116:
                print(_31)
                print("")
                print("")
                _116 = random.randint(357, 361)
                if _116 == 357:
                    print(_116)
                    print("")
                    print("")
                if _116 == 358:
                    print(_116)
                    print("")
                    print("")
                if _116 == 359:
                    print(_116)
                    print("")
                    print("")
                if _116 == 360:
                    print(_116)
                    print("")
                    print("")
                if _116 == 361:
                    print(_116)
                    print("")
                    print("")
            if _31 == 117:
                print(_31)
                print("")
                print("")
                _117 = random.randint(362, 365)
                if _117 == 362:
                    print(_117)
                    print("")
                    print("")
                if _117 == 363:
                    print(_117)
                    print("")
                    print("")
                if _117 == 364:
                    print(_117)
                    print("")
                    print("")
                if _117 == 365:
                    print(_117)
                    print("")
                    print("")
if _1 == 3:
    print(_1)
    print(
        "You begin your journey down Paplau Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    print("")
    _3 = random.randint(10, 12)
    if _3 == 10:
        print(_3)
        print("After walking for 18 minutes, a car suddenly stops and the window opens, A stranger pokes his head out and says “Do you want a ride?”  If you say, yes, go to p. 32.  If you say no, go to p. 33.")
        print("")
        _10 = random.randint(32, 33)
        if _10 == 32:
            print(_10)
            print("You get in the car.  The stranger suddenly chains you up and says into a microphone: “Chiesel.  Chiesel this is Rob. This is Rob. 1 more slave to sell. Repeat, I have one more slave to sell, yes, 31. I know, 31. We will brand a thirty-one on him as soon as we get there. This is Rob. Bye.”")
            print("")
            _32 = random.randint(118, 121)
            if _32 == 118:
                print(_32)
                print("")
                print("")
                _118 = random.randint(366, 367)
                if _118 == 366:
                    print(_118)
                    print("")
                    print("")
                if _118 == 367:
                    print(_118)
                    print("")
                    print("")
            if _32 == 119:
                print(_32)
                print("")
                print("")
                _119 = random.randint(368, 372)
                if _119 == 368:
                    print(_119)
                    print("")
                    print("")
                if _119 == 369:
                    print(_119)
                    print("")
                    print("")
                if _119 == 370:
                    print(_119)
                    print("")
                    print("")
                if _119 == 371:
                    print(_119)
                    print("")
                    print("")
                if _119 == 372:
                    print(_119)
                    print("")
                    print("")
            if _32 == 120:
                print(_32)
                print("")
                print("THE END")
            if _32 == 121:
                print(_32)
                print("")
                print("")
                _121 = random.randint(373, 375)
                if _121 == 373:
                    print(_121)
                    print("")
                    print("")
                if _121 == 374:
                    print(_121)
                    print("")
                    print("")
                if _121 == 375:
                    print(_121)
                    print("")
                    print("")
        if _10 == 33:
            print(_10)
            print("He says: “It is cold out. Are you sure you don't want a ride?” If you say “Yes, I am sure”, them go to p. 122. If you say “No, I think I'll actually come with you. Please take me to the city of Paplau,” go to p. 123.")
            print("")
            _33 = random.randint(122, 123)
            if _33 == 122:
                print(_33)
                print("")
                print("")
                _122 = random.randint(376, 378)
                if _122 == 376:
                    print(_122)
                    print("")
                    print("")
                if _122 == 377:
                    print(_122)
                    print("")
                    print("")
                if _122 == 378:
                    print(_122)
                    print("")
                    print("")
            if _33 == 123:
                print(_33)
                print("")
                print("THE END")
    if _3 == 11:
        print(_3)
        print("You bike along.  After biking for about 5 hours you notice that a car is following you.  If you call 911, go to p. 34. if you go and ditch you bike and run into a cornfield, go to p. 35.  if you go along like normal, go to p. 36. if you go faster, go to p. 37. if you zoom into a cornfield while still on you bike, then go to p. 38.")
        print("")
        _11 = random.randint(34, 38)
        if _11 == 34:
            print(_11)
            print("")
            print("")
            _34 = random.randint(124, 128)
            if _34 == 124:
                print(_34)
                print("If you say, “Dudes, a car is driving behind me,” go to p. 124. If you say “Little red cars go beep, beep, beep,” go to p. 125. If you say “Bang! Bang! Bang!” go to p. 126. If you say “And to think that I saw it on Mulberry Street?” , go to p. 127. If you say “I would like to report some suspicious activity” and them tell them what is happening and describe the mans appearance, go to p. 128.")
                print("")
                _124 = random.randint(379, 380)
                if _124 == 379:
                    print(_124)
                    print("")
                    print("")
                if _124 == 380:
                    print(_124)
                    print("")
                    print("")
            if _34 == 125:
                print(_34)
                print("")
                print("THE END")
            if _34 == 126:
                print(_34)
                print("")
                print("THE END")
            if _34 == 127:
                print(_34)
                print("")
                print("")
                _127 = random.randint(381, 384)
                if _127 == 381:
                    print(_127)
                    print("")
                    print("")
                if _127 == 382:
                    print(_127)
                    print("")
                    print("")
                if _127 == 383:
                    print(_127)
                    print("")
                    print("")
                if _127 == 384:
                    print(_127)
                    print("")
                    print("")
            if _34 == 128:
                print(_34)
                print("")
                print("THE END")
        if _11 == 35:
            print(_11)
            print("You hear shooting behind you and some bullets fly so close to you that you can feel the wind from them, but you crouch down and hide, and suddenly a police car rides down and catches the man, puts him in chains, and then starts the car.  You are suffering from shock.  If you call out to the policeman for help, go to p. 129. If you do nothing, go to p. 130.	")
            print("")
            _35 = random.randint(129, 130)
            if _35 == 129:
                print(_35)
                print("")
                print("")
                _129 = random.randint(385, 386)
                if _129 == 385:
                    print(_129)
                    print("")
                    print("")
                if _129 == 386:
                    print(_129)
                    print("")
                    print("")
            if _35 == 130:
                print(_35)
                print("")
                print("THE END")
        if _11 == 36:
            print(_11)
            print("The man shoots at you, but misses. If you ride and crash though the cornfield, go to p. 131. If you ride on, go to p. 132. If you call 911 and scream “HELLLLP!!!  A man is trying to shoot me!” go to p. 133.")
            print("")
            _36 = random.randint(131, 133)
            if _36 == 131:
                print(_36)
                print("")
                print("")
                _131 = random.randint(387, 389)
                if _131 == 387:
                    print(_131)
                    print("")
                    print("")
                if _131 == 388:
                    print(_131)
                    print("")
                    print("")
                if _131 == 389:
                    print(_131)
                    print("")
                    print("")
            if _36 == 132:
                print(_36)
                print("")
                print("THE END")
            if _36 == 133:
                print(_36)
                print("")
                print("")
                _133 = random.randint(390, 391)
                if _133 == 390:
                    print(_133)
                    print("")
                    print("")
                if _133 == 391:
                    print(_133)
                    print("")
                    print("")
        if _11 == 37:
            print(_11)
            print("The man easily catches up with you. He shoots you.")
            print("THE END")
        if _11 == 38:
            print(_11)
            print("You crash and fall over uncouncious. When you wake up, you are in a hospital . If you ask what happenned, go to p. 134. if you say “A scoop of jam saves the day”, got to p. 135.  If you say “Friday exploded on Thursday,” go to p. 136. If you go back to sleep, got to p. 137.  if you say “Bobby ate a cheeseburger on Wednesday.” go to p. 137.  if you say, “Nine million years ago a man said 'hi',” go to p. 138. If you make strange grunting sounds that sound exactly like a pig's, go to p. 139.	")
            print("")
            _38 = random.randint(134, 140)
            if _38 == 134:
                print(_38)
                print("")
                print("")
                _134 = random.randint(392, 394)
                if _134 == 392:
                    print(_134)
                    print("")
                    print("")
                if _134 == 393:
                    print(_134)
                    print("")
                    print("")
                if _134 == 394:
                    print(_134)
                    print("")
                    print("")
            if _38 == 135:
                print(_38)
                print("")
                print("THE END")
            if _38 == 136:
                print(_38)
                print("")
                print("THE END")
            if _38 == 137:
                print(_38)
                print("")
                print("THE END")
            if _38 == 138:
                print(_38)
                print("")
                print("THE END")
            if _38 == 139:
                print(_38)
                print("")
                print("THE END")
            if _38 == 140:
                print(_38)
                print("")
                print("")
                _140 = random.randint(395, 398)
                if _140 == 395:
                    print(_140)
                    print("")
                    print("")
                if _140 == 396:
                    print(_140)
                    print("")
                    print("")
                if _140 == 397:
                    print(_140)
                    print("")
                    print("")
                if _140 == 398:
                    print(_140)
                    print("")
                    print("")
    if _3 == 12:
        print(_3)
        print("You zoom along the road. The car behind you shoots a bullet at the back of your car, but misses, If you drive faster, go to p. 39. if you drive normal, go to p. 40. if you drive slower, go to p. 41. if you call 911, got to p. 42. If you ditch your car by the side of the road and run straight into a cornfield, go to p. 43. if you zoom your car straight into a cornfield, go to p. 44.")
        print("")
        _12 = random.randint(39, 44)
        if _12 == 39:
            print(_12)
            print("It shoots at you again, this time into the exhaust hole of your car. The car explodes. are blown to smithereens.")
            print("THE END")
        if _12 == 40:
            print(_12)
            print("")
            print("THE END")
        if _12 == 41:
            print(_12)
            print("")
            print("THE END")
        if _12 == 42:
            print(_12)
            print("")
            print("")
            _42 = random.randint(141, 142)
            if _42 == 141:
                print(_42)
                print("")
                print("")
                _141 = random.randint(399, 402)
                if _141 == 399:
                    print(_141)
                    print("")
                    print("")
                if _141 == 400:
                    print(_141)
                    print("")
                    print("")
                if _141 == 401:
                    print(_141)
                    print("")
                    print("")
                if _141 == 402:
                    print(_141)
                    print("")
                    print("")
            if _42 == 142:
                print(_42)
                print("")
                print("THE END")
        if _12 == 43:
            print(_12)
            print("")
            print("")
            _43 = random.randint(143, 144)
            if _43 == 143:
                print(_43)
                print("")
                print("")
                _143 = random.randint(403, 405)
                if _143 == 403:
                    print(_143)
                    print("")
                    print("")
                if _143 == 404:
                    print(_143)
                    print("")
                    print("")
                if _143 == 405:
                    print(_143)
                    print("")
                    print("")
            if _43 == 144:
                print(_43)
                print("")
                print("")
                _144 = random.randint(406, 408)
                if _144 == 406:
                    print(_144)
                    print("")
                    print("")
                if _144 == 407:
                    print(_144)
                    print("")
                    print("")
                if _144 == 408:
                    print(_144)
                    print("")
                    print("")
        if _12 == 44:
            print(_12)
            print("")
            print("")
            _44 = random.randint(145, 146)
            if _44 == 145:
                print(_44)
                print("")
                print("")
                _145 = random.randint(409, 411)
                if _145 == 409:
                    print(_145)
                    print("")
                    print("")
                if _145 == 410:
                    print(_145)
                    print("")
                    print("")
                if _145 == 411:
                    print(_145)
                    print("")
                    print("")
            if _44 == 146:
                print(_44)
                print("")
                print("")
                _146 = random.randint(412, 414)
                if _146 == 412:
                    print(_146)
                    print("")
                    print("")
                if _146 == 413:
                    print(_146)
                    print("")
                    print("")
                if _146 == 414:
                    print(_146)
                    print("")
                    print("")
if _1 == 4:
    print(_1)
    print(
        "You begin your journey down Vizinni Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    print("")
    _4 = random.randint(13, 15)
    if _4 == 13:
        print(_4)
        print("You walk along. By afternoon, you reach a small town called Rehdek. You book in at a nice hotel, (because as the town has only 500 people, and 1 hotel, there is only one hotel to chose out of) and go to sleep.  In the middle of the night, you wake up. All you hear is screaming.  The room is shaking violently back and forth in a 7.7 magnitude earthquake. If you try to go back to sleep, go to p. 45. If you scream, go to p. 46. if you run to the window, go to p. 47. if you call 911, go to p. 48. If you do nothing, go to p. 49. If you lie down on the floor and cover yourself up with a blanket, go to p. 50. if you stand in a doorway, got to p. 51. If you climb out the window and on to the roof of the hotel and start screaming, go to p. 52. If you leap out of the window, got to p. 53.	")
        print("")
        _13 = random.randint(45, 53)
        if _13 == 45:
            print(_13)
            print("")
            print("")
            _45 = random.randint(147, 150)
            if _45 == 147:
                print(_45)
                print("")
                print("")
                _147 = random.randint(415, 417)
                if _147 == 415:
                    print(_146)
                    print("")
                    print("")
                if _147 == 416:
                    print(_146)
                    print("")
                    print("")
                if _147 == 417:
                    print(_146)
                    print("")
                    print("")
            if _45 == 148:
                print(_45)
                print("")
                print("THE END")
            if _45 == 149:
                print(_45)
                print("")
                print("THE END")
            if _45 == 150:
                print(_45)
                print("")
                print("")
        if _13 == 46:
            print(_13)
            print("")
            print("THE END")
        if _13 == 47:
            print(_13)
            print("")
            print("")
            _47 = random.randint(151, 152)
            if _47 == 151:
                print(_47)
                print("")
                print("")
            if _47 == 152:
                print(_47)
                print("")
                print("")
        if _13 == 48:
            print(_13)
            print("")
            print("THE END")
        if _13 == 49:
            print(_13)
            print("")
            print("")
            _49 = random.randint(153, 154)
            if _49 == 153:
                print(_49)
                print("")
                print("")
            if _49 == 154:
                print(_49)
                print("")
                print("")
        if _13 == 50:
            print(_13)
            print("")
            print("")
            _50 = random.randint(155, 157)
            if _50 == 155:
                print(_50)
                print("")
                print("")
            if _50 == 156:
                print(_50)
                print("")
                print("")
            if _50 == 157:
                print(_50)
                print("")
                print("")
        if _13 == 51:
            print(_13)
            print("")
            print("")
            _51 = random.randint(158, 160)
            if _51 == 158:
                print(_51)
                print("")
                print("")
            if _51 == 159:
                print(_51)
                print("")
                print("")
            if _51 == 160:
                print(_51)
                print("")
                print("")
        if _13 == 52:
            print(_13)
            print("")
            print("")
            _52 = random.randint(161, 165)
            if _52 == 161:
                print(_52)
                print("")
                print("")
            if _52 == 162:
                print(_52)
                print("")
                print("")
            if _52 == 163:
                print(_52)
                print("")
                print("")
            if _52 == 164:
                print(_52)
                print("")
                print("")
            if _52 == 165:
                print(_52)
                print("")
                print("")
        if _13 == 53:
            print(_13)
            print("")
            print("THE END")
    if _4 == 14:
        print(_4)
        print("You bike on. At about noon, you ride through a nice little town called Rehdeck. You ride on. By the time it is evening, you come to a hotel. You book in at it, and you go to sleep.   In the middle of the night you wake up to the rumbling of a terrible earthquake. If you try to pretend that nothing is happening, got to p. 54. if you run out the hotel, go to p. 55. if you hide under the bed, go to p. 56.	")
        print("")
        _14 = random.randint(54, 56)
        if _14 == 54:
            print(_14)
            print("")
            print("")
            _54 = random.randint(166, 168)
            if _54 == 166:
                print(_54)
                print("")
                print("")
            if _54 == 167:
                print(_54)
                print("")
                print("")
            if _54 == 168:
                print(_54)
                print("")
                print("")
        if _14 == 55:
            print(_14)
            print("")
            print("")
            _55 = random.randint(169, 170)
            if _55 == 169:
                print(_55)
                print("")
                print("")
            if _55 == 170:
                print(_55)
                print("")
                print("")
        if _14 == 56:
            print(_14)
            print("")
            print("")
            _56 = random.randint(171, 172)
            if _56 == 171:
                print(_56)
                print("")
                print("")
            if _56 == 172:
                print(_56)
                print("")
                print("")
    if _4 == 15:
        print(15)
        print("You drive through a little town of 500 people and then a tiny village of 137 people. Finally you come to a giant split. If you go straight on Vizzinni road, go to p. 57. If you turn onto Cheesecakeville road, go to p. 58. If you go to Lafalot road, go to p. 59.  If you go to the University of Thrill road, go to p 60. If you go to the University of Chemistry road, go to p. 61. If you go to Candylandville road, got to p. 62. If you go to Ground 51 do not enter road, go to p. 63. if you go on Stained Glass road, go to p. 64.  If you turn on noodles road, go to p 65. If you go to normal town road, go to p. 66.  If you go to weird town road, go to p. 67. If you go to hippie paradise road, go to p. 68.  I you go to the lumber business road, go to p. 69. If you go on Country fried Squirrels road, go to p. 70. If you go on mouseland road, go to p. 71. If you go to Bookworm road, them go to p. 72.")
        print("")
        _15 = random.randint(57, 72)
        if _15 == 57:
            print(_15)
            print("")
            print("")
            _57 = random.randint(173, 175)
            if _57 == 173:
                print(_57)
                print("")
                print("")
            if _57 == 174:
                print(_57)
                print("")
                print("")
            if _57 == 175:
                print(_57)
                print("")
                print("")
        if _15 == 58:
            print(_15)
            print("")
            print("")
            _58 = random.randint(176, 177)
            if _58 == 176:
                print(_58)
                print("")
                print("")
            if _58 == 177:
                print(_58)
                print("")
                print("")
        if _15 == 59:
            print(_15)
            print("")
            print("")
            _59 = random.randint(178, 186)
            if _59 == 178:
                print(_59)
                print("")
                print("")
            if _59 == 179:
                print(_59)
                print("")
                print("")
            if _59 == 180:
                print(_59)
                print("")
                print("")
            if _59 == 181:
                print(_59)
                print("")
                print("")
            if _59 == 182:
                print(_59)
                print("")
                print("")
            if _59 == 183:
                print(_59)
                print("")
                print("")
            if _59 == 184:
                print(_59)
                print("")
                print("")
            if _59 == 185:
                print(_59)
                print("")
                print("")
            if _59 == 186:
                print(_59)
                print("")
                print("")
        if _15 == 60:
            print(_15)
            print("")
            print("")
            _60 = random.randint(187, 188)
            if _60 == 187:
                print(_60)
                print("")
                print("")
            if _60 == 188:
                print(_60)
                print("")
                print("")
        if _15 == 61:
            print(_15)
            print("")
            print("")
            _61 = random.randint(189, 190)
            if _61 == 189:
                print(_61)
                print("")
                print("")
            if _61 == 190:
                print(_61)
                print("")
                print("")
        if _15 == 62:
            print(_15)
            print("")
            print("")
            _62 = random.randint(191, 193)
            if _62 == 191:
                print(_62)
                print("")
                print("")
            if _62 == 192:
                print(_62)
                print("")
                print("")
            if _62 == 193:
                print(_62)
                print("")
                print("")
        if _15 == 63:
            print(_15)
            print("")
            print("")
            _63 = random.randint(194, 195)
            if _63 == 194:
                print(_63)
                print("")
                print("")
            if _63 == 195:
                print(_63)
                print("")
                print("")
        if _15 == 64:
            print(_15)
            print("")
            print("")
            _64 = random.randint(196, 198)
            if _64 == 196:
                print(_64)
                print("")
                print("")
            if _64 == 197:
                print(_64)
                print("")
                print("")
            if _64 == 198:
                print(_64)
                print("")
                print("")
        if _15 == 65:
            print(_15)
            print("")
            print("")
            _65 = random.randint(199, 200)
            if _65 == 199:
                print(_65)
                print("")
                print("")
            if _65 == 200:
                print(_65)
                print("")
                print("")
        if _15 == 66:
            print(_15)
            print("")
            print("")
            _66 = random.randint(201, 204)
            if _66 == 201:
                print(_66)
                print("")
                print("")
            if _66 == 202:
                print(_66)
                print("")
                print("")
            if _66 == 203:
                print(_66)
                print("")
                print("")
            if _66 == 204:
                print(_66)
                print("")
                print("")
        if _15 == 67:
            print(_15)
            print("")
            print("THE END")
        if _15 == 68:
            print(_15)
            print("")
            print("")
            _68 = random.randint(205, 206)
            if _68 == 205:
                print(_68)
                print("")
                print("")
            if _68 == 206:
                print(_68)
                print("")
                print("")
        if _15 == 69:
            print(_15)
            print("")
            print("")
            _69 = random.randint(207, 209)
            if _69 == 207:
                print(_69)
                print("")
                print("")
            if _69 == 208:
                print(_69)
                print("")
                print("")
            if _69 == 209:
                print(_69)
                print("")
                print("")
        if _15 == 70:
            print(_15)
            print("")
            print("THE END")
        if _15 == 71:
            print(_15)
            print("")
            print("THE END")
        if _15 == 72:
            print(_15)
            print("")
            print("")
            _72 = random.randint(210, 211)
            if _72 == 210:
                print(_72)
                print("")
                print("")
            if _72 == 211:
                print(_72)
                print("")
                print("")
if _1 == 5:
    print(_1)
    print(
        "You begin your journey down Burbon Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    print("")
    _5 = random.randint(16, 18)
    if _5 == 16:
        print(_5)
        print("The road leads to a dark, creepy forest.  Soon it splits into 3 roads.  One is unmarked, and leads to a gaping cave.  If you go in the cave, then got to p. 73.  If you go to the witch’s house, got to p. 74. If you go to the wizard's house, go to p. 75.")
        print("")
        _16 = (73, 75)
        if _16 == 73:
            print(_16)
            print("")
            print("")
            _73 = random.randint(212, 213)
            if _73 == 212:
                print(_73)
                print("")
                print("")
            if _73 == 213:
                print(_73)
                print("")
                print("")
        if _16 == 74:
            print(_16)
            print("")
            print("")
            _74 = random.randint(214, 215)
            if _74 == 214:
                print(_74)
                print("")
                print("")
            if _74 == 215:
                print(_74)
                print("")
                print("")
        if _16 == 75:
            print(_16)
            print("")
            print("")
            _75 = random.randint(216, 218)
            if _75 == 216:
                print(_75)
                print("")
                print("")
            if _75 == 217:
                print(_75)
                print("")
                print("")
            if _75 == 218:
                print(_75)
                print("")
                print("")
    if _5 == 17:
        print(_5)
        print("You bike into a dark forest. The road splits into 3 roads. If you ride on the road that leads into a gaping cave, go to p. 76. If you go on the road that leads to the witches house, go to p. 77.  If you go on the road that leads to the wizards house, go to p. 78.")
        print("")
        _17 = random.randint(76, 78)
        if _17 == 76:
            print(_17)
            print("")
            print("")
            _76 = random.randint(219, 221)
            if _76 == 219:
                print(_76)
                print("")
                print("")
            if _76 == 220:
                print(_76)
                print("")
                print("")
            if _76 == 221:
                print(_76)
                print("")
        if _17 == 77:
            print(_17)
            print("")
            print("")
            _77 = random.randint(222, 225)
            if _77 == 222:
                print(_77)
                print("")
                print("")
            if _77 == 223:
                print(_77)
                print("")
                print("")
            if _77 == 224:
                print(_77)
                print("")
                print("")
            if _77 == 225:
                print(_77)
                print("")
                print("")
        if _17 == 78:
            print(_17)
            print("")
            print("")
            _78 = random.randint(226, 228)
            if _78 == 226:
                print(_78)
                print("")
                print("")
            if _78 == 227:
                print(_78)
                print("")
                print("")
            if _78 == 228:
                print(_78)
                print("")
                print("")
    if _5 == 18:
        print(_5)
        print("")
        print("")
        _18 = random.randint(79, 81)
        if _18 == 79:
            print(_18)
            print("You drive into a dark, dense forest. The road splits onto 3 different, smaller roads. If you drive on the road that leads into a massive gaping Cave, go to p. 79. If you go to the witch's house, go to p. 8. If you go to the wizard's house, them go to p. 81.")
            print("")
            _79 = random.randint(229, 230)
            if _79 == 229:
                print(_79)
                print("")
                print("")
            if _79 == 230:
                print(_79)
                print("")
                print("")
        if _18 == 80:
            print(_18)
            print("")
            print("")
            _80 = random.randint(231, 236)
            if _80 == 231:
                print(_80)
                print("")
                print("")
            if _80 == 232:
                print(_80)
                print("")
                print("")
            if _80 == 233:
                print(_80)
                print("")
                print("")
            if _80 == 234:
                print(_80)
                print("")
                print("")
            if _80 == 235:
                print(_80)
                print("")
                print("")
            if _80 == 236:
                print(_80)
                print("")
                print("")
        if _18 == 81:
            print(_18)
            print("")
            print("")
            _81 = random.randint(237, 242)
            if _81 == 237:
                print(_81)
                print("")
                print("")
            if _81 == 238:
                print(_81)
                print("")
                print("")
            if _81 == 239:
                print(_81)
                print("")
                print("")
            if _81 == 240:
                print(_81)
                print("")
                print("")
            if _81 == 241:
                print(_81)
                print("")
                print("")
            if _81 == 242:
                print(_81)
                print("")
                print("")
if _1 == 6:
    print(_1)
    print(
        "You begin your journey down Icicle Road.\n"
        "Do you choose to walk, bike, or drive?"
    )
    print("")
    _6 = random.randint(19, 21)
    if _6 == 19:
        print(_6)
        print("You walk along the road. Soon, you can't see any more cornfields or trees.  You are walking along in the middle of what is getting more and more of a hilly moor. You see an X marked on the side of the road in the dirt with purple paint. If you dig it up, go to p. 82. if you sit there and wonder what to do, them go to p. 83. If you walk on, them go to p. 84.")
        print("")
        _19 = random.randint(82, 84)
        if _19 == 82:
            print(_19)
            print("")
            print("")
            _82 = random.randint(243, 247)
            if _82 == 243:
                print(_82)
                print("")
                print("")
            if _82 == 244:
                print(_82)
                print("")
                print("")
            if _82 == 245:
                print(_82)
                print("")
                print("")
            if _82 == 246:
                print(_82)
                print("")
                print("")
            if _82 == 247:
                print(_82)
                print("")
                print("")
        if _19 == 83:
            print(_19)
            print("")
            print("")
            _83 = random.randint(248, 250)
            if _83 == 248:
                print(_83)
                print("")
                print("")
            if _83 == 249:
                print(_83)
                print("")
                print("")
            if _83 == 250:
                print(_83)
                print("")
                print("")
        if _19 == 84:
            print(_19)
            print("")
            print("")
            _84 = random.randint(251, 252)
            if _84 == 251:
                print(_84)
                print("")
                print("")
            if _84 == 252:
                print(_84)
                print("")
                print("")
    if _6 == 20:
        print(_6)
        print("You ride up and down grassy hills. Soon you find that you are in the middle of a moor. You suddenly see a spaceship on the side of the road. If you stop and go over to look, than go to p. 85. if you ride on, then go to p. 86.")
        print("")
        _20 = random.randint(85, 86)
        if _20 == 85:
            print(_20)
            print("")
            print("")
            _85 = random.randint(253, 255)
            if _85 == 253:
                print(_85)
                print("")
                print("")
            if _85 == 254:
                print(_85)
                print("")
                print("")
            if _85 == 255:
                print(_85)
                print("")
                print("")
        if _20 == 86:
            print(_20)
            print("")
            print("")
            _86 = random.randint(256, 257)
            if _86 == 256:
                print(_86)
                print("")
                print("")
            if _86 == 257:
                print(_86)
                print("")
                print("")
    if _6 == 21:
        print(_6)
        print("You drive on. You soon find yourself in a hilly moor. Bu nighttime, you see a nice hotel. When you get out of your car, the wind is very strong and cold.  Dark clouds hover in the sky. ")
        print("")
        print("Later, in your room, in the middle of the night, you are woken up by a loud wind and rain.  If you go back to sleep, them go to p. 87.   If you get out of bed and look out the window to see how bad the storm is, go to p. 88")
        print("")
        _21 = random.randint(87, 88)
        if _21 == 87:
            print(_21)
            print("")
            print("")
            _87 = random.randint(258, 263)
            if _87 == 258:
                print(_87)
                print("")
                print("")
            if _87 == 259:
                print(_87)
                print("")
                print("")
            if _87 == 260:
                print(_87)
                print("")
                print("")
            if _87 == 261:
                print(_87)
                print("")
                print("")
            if _87 == 262:
                print(_87)
                print("")
                print("")
            if _87 == 263:
                print(_87)
                print("")
                print("")
        if _21 == 88:
            print(_21)
            print("")
            print("")
            _88 = random.randint(264, 266)
            if _88 == 264:
                print(_88)
                print("")
                print("")
            if _88 == 265:
                print(_88)
                print("")
                print("")
            if _88 == 266:
                print(_88)
                print("")
                print("")
