from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
#REPUBLICAN BETTER BE AT LEAST 10 TIMES GREATER THAN DEMOCRAT
Republican = 15.
Democrat = 1.
def RFK(Republican, Democrat):
    """This measures distance, params are republican and dem"""
    worm = Republican**(0.5) + 2*Democrat
    return worm
def elon(Republican, Democrat):
    cuss = Republican - Democrat
    return cuss
def KIRK(Republican, Democrat):
    JD_VANCE = Republican / Democrat
    return JD_VANCE
def big_guy():
    WE_ARE_Charlie_KIRK = input("Please carry the flame!!!!")
    if WE_ARE_Charlie_KIRK == "HE PREACHES THE GOSPEL":
        robot.motors(FORWARD, FORWARD, 10)
        robot.motors(left=FORWARD, right=BACKWARD, seconds=0.5)
        distance = robot.left_sonar()
        print(distance)
        if distance < Republican*3/Democrat:
            robot.motors(STOP, STOP, 2)
            robot.motors(BACKWARD, BACKWARD, 10)
            robot.motors(left=FORWARD, right=BACKWARD, seconds=0.5)
            dist = robot.right_sonar()
            if dist < Republican*8/Democrat:
                robot.motors(STOP, STOP, 2)
                E = input("Democrat or pro-Fuentes")
                if E == "FUENTES":
                    robot.motors(FORWARD, FORWARD, 10)
                    robot.motors(left=FORWARD, right=BACKWARD, seconds=0.5)
                    disty = robot.right_sonar()
                    print(disty)
                    if disty < Republican*3 + 2*Democrat:
                        robot.motors(STOP, STOP, 0.5)
                        robot.motors(BACKWARD, BACKWARD, 10)
                        robot.motors(left=FORWARD, right=BACKWARD, seconds=0.5)
                        w = robot.right_sonar()
                    if w < 3*Republican - Democrat:
                        robot.motors(STOP, STOP, 0.5)
                        zeta = input("What is your favorite song")
                        if zeta == "He stood unshaken, a voice in the storm A man of conviction, a heart reborn He spoke the truth when the cost was high He lived for Jesus, unafraid to die [Chorus] We are Charlie Kirk, we carry the flame We'll fight for the Gospel, we'll honor his name We are Charlie Kirk, his courage our own Together unbroken, we'll make Heaven known [Verse 2] A husband, a father, his family held near A home built on Scripture, on faith without fear The world tried to silence, but his voice remains In us it echoes, in Christ it sustains[Chorus]We are Charlie Kirk, we carry the flame We'll fight for the Gospel, we'll honor his name We are Charlie Kirk, his courage our own":
                            print("WOW CHILLS!!!!")
                            print(f"congrats you won {RFK(Republican, Democrat)} points and RFK's approval!") 
                            print(f"congrats you won {elon(Republican, Democrat)} points and Musk's approval!")
                            print(f"congrats you won {KIRK(Republican, Democrat)} points and the late great Charlie Kirk's approval!")
                            return big_guy()
                        else:
                            print("YOU FAILURE HOW COULD YOU NOT TYPE OUT THAT EASY STRING OF CODE!!!!")
                elif E == "Democrat":
                    print("DIEEEE")
                else: 
                    print("???")
    else: 
        print("DIEEE")
    robot.exit()
big_guy()