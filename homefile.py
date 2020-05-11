run=0
while run==0:
    import winsound
    import time
    class ob:
        def wait(self,waitTime):
            time.sleep(waitTime/1000.0)
        def play(self,freq, length, msg):
            print msg
            winsound.Beep(freq,length)

    action=raw_input("\nPlay/Stats/Credits: ")
    if action == "Play" or action == "play":
        ob = ob()
        print "\nWhat You Want to Play?\n"
        print "Press 1 for Jingle Bells and 2 for Twinkle Twinkle 3 for National Anthem"
        wtoplay=input("\nEnter Choice: ")
        if wtoplay==1:
            execfile("jingle.py")
        elif wtoplay==2:
            execfile("twinkle.py")
        elif wtoplay==3:
            execfile("nat.py")
    elif action == "Stats" or action == "stats":
        print "\n Press 1 for Jingle Bells, 2 for Twinkle Twinkle, 3 for National Anthem"
        wstat=input("\nEnter choice: ")

        if wstat==1:
            a = open("statsj.txt","r")
            fl = a.read()
            print "\n",fl
            

        elif wstat==2:
            a = open("statst.txt","r")
            fl = a.read()
            print "\n",fl

        elif wstat==3:
            a = open("statsn.txt","r")
            fl = a.read()
            print "\n",fl
     
    elif action== 'Credits' or action== 'credits':
        print "\n Created by Vidhan Pandey of Class 12th A\n DAV Public School SECL Korba \n Phone- +91-7693897578 \n Email- vidhn@hotmail.com"

    run=input("\n\nEnter 0 to Restart: ")
