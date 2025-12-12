from simulator import robot, FORWARD, BACKWARD, STOP

# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles
#REPUBLICAN BETTER BE AT LEAST 10 TIMES GREATER THAN DEMOCRAT
Republican = 10
Democrat = 1
def RFK(Republican, Democrat):
    """This measures distance, params are republican and dem"""
    worm = Republican^(0.5) + 2*Democrat
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
        robot.motor(FORWARD)
        distance = robot.left_sonar
        if distance < KIRK:
            robot.motor(STOP)
            robot.motor(BACKWARD)
            dist = robot.right_sonar
            if dist < KIRK/2:
                robot.motor(STOP)
                E = input("Democrat or pro-Fuentes")
                if E == "FUENTES":
                    robot.motor(FORWARD)
                    disty = robot.right_sonar
                    if disty < RFK:
                        robot.motor(STOP)
                        robot.motor(BACKWARD)
                    if disty < elon:
                        robot.motor(STOP)
                        zeta = input("What is your favorite song")
                        if zeta == "He stood unshaken, a voice in the storm A man of conviction, a heart reborn He spoke the truth when the cost was high He lived for Jesus, unafraid to die [Chorus] We are Charlie Kirk, we carry the flame We'll fight for the Gospel, we'll honor his name We are Charlie Kirk, his courage our own Together unbroken, we'll make Heaven known [Verse 2] A husband, a father, his family held near A home built on Scripture, on faith without fear The world tried to silence, but his voice remains In us it echoes, in Christ it sustains[Chorus]We are Charlie Kirk, we carry the flame We'll fight for the Gospel, we'll honor his name We are Charlie Kirk, his courage our own"
                            print("WOW CHILLS!!!")
                            return big_guy()
                        else:
                            print("YOU FAILURE!!!!")
                else:
                    print("DIEEEE")
    else: 
        print("DIEEE")
    robot.exit()