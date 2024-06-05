#Now this looks like a lot of code but don't worry, these comments will (hopefully) tell you everything about what is happening in the code.
import time
#Importing time is added so whenever I create dialogue, there is a pause so the player has time to read.
import random
#Importing random is added so the player doesn't get the same questions repeated to them and rng will give different questions and answers. It will also be used to generate unique dialogue and random hosts for fun.
import climage
#Importing climage is added so I can use images for the host and images for picture-based questions.
points = 0
#This is the points system. Each question answered correctly will give you 10 points. When points is at 100, the game will end.
text = random.randint(1, 4)
#This will generate unique dialogue used once as the opening message at the start of the game from the announcer.
text2 = "normal"
categories = ["1) Computer Science", "2) Quick Maths", "3) Nonsensical Nonsense", "4) Science & Chemistry", "5) English Languages", "6) Historical Events", "7) Food & Beverages", "8) Tourist Attractions", "9) Randomly Generated", "10) Horror & Creepypastas", "11) Host's Special", "12) What does that mean?"]
#These are our categories.
host = climage.convert("DancingBanana.png", is_unicode=True)
btext = random.randint(1, 4)
host2 = 1
if text == 2:
  print("Announcer: Amazon... PlayStation 5... checkout... oh wait we're live? *ahem*")
  time.sleep(4)
elif text == 3:
  print("...")
  time.sleep(3)
  print("...")
  time.sleep(3)
  print("Game: Where's the announcer?")
  time.sleep(3)
  print("*The announcer left a note*")
  time.sleep(3)
  print("Announcer's note: Hey, I'm currently getting a haircut and I might be a little bit late. If you can, please try to cover my schedule. Thanks! - From Announcer")
  time.sleep(7)
  print("Game: No, the show needs to begin and the player is about to get impatient!")
  time.sleep(4)
  print("*Announcer is somehow teleported in magically*")
  time.sleep(3)
  print("Announcer: O-oh I wasn't ready yet!!!")
  time.sleep(3)
  print("Game: Now the show can finally begin...")
  time.sleep(3)
elif text == 4:
  print("Announcer on the phone: Yeah everything is going good...")
  time.sleep(3)
  print("Announcer: I really would like a raise tho-- oh my bad sorry, uhhhh")
  time.sleep(3)
print("Announcer: HELLO EVERYBODY!!! Welcome to the game created in Python, inside of repl.it...")
time.sleep(3)
print("Announcer: The one... and only...")
time.sleep(2)
print("Announcer: The Python Gameshow!")
time.sleep(2)
print("Announcer: And your host for this show is...")
time.sleep(3)
print("Announcer: The banana with a planana who loves to dance... the DANCCCCIIING BANANAAAAAAA!!!")
time.sleep(2)
print(host)
time.sleep(3)
if btext == 1:
  print("Banana: Thank you, thank you, I have successfully been imported into Python!")
  time.sleep(3)
  print("Banana: How exciting! But, we have a show to do so let's get along with it!")
  time.sleep(3)
elif btext == 2:
  print("Banana: Let's get this show on the road!")
  time.sleep(3)
elif btext == 3:
  print("Banana: Welcome to the Python Gameshow where most of our questions were created from ChatGPT!")
elif btext == 4:
  print("Banana: If I catch you looking up the answers, then just know...")
  time.sleep(3)
  print("Banana: I will be outside your house in 3 minutes regarding a 'special experiment' :D.")
time.sleep(4)
while points < 100:
  QCorrect = random.randint(1, 6)
  QWrong = random.randint(1, 6)
  print("Banana: You need " + str(100 - points) + " points to complete this gameshow! With that being said...")
  time.sleep(4)
  print("Banana: Pick a category!")
  time.sleep(2)
  print(categories)
  question = int(input(""))
  if question == 1:
    CS = random.randint(1, 2)
    if CS == 1:
      CSopening = random.randint(1, 2)
      print("Announcer: Computer Science!")
      time.sleep(2)
      if CSopening == 1:
        print("Banana: We're about to dive into science...")
        time.sleep(3)
        print("Banana: That is based around computers, Computer Science!")
      if CSopening == 2:
        print("Banana: Computer Science! Is it better than regular Science?")
      time.sleep(4)
      print("Announcer: Python programming is a high-level, general-purpose, object-oriented programming language that can be used to make applications and websites.")
      time.sleep(5)
      print("Announcer: Which function should I use to send a specified message on-screen or to any output device?")
      time.sleep(5)
      print("1) str()" + " 2) char()" + " 3) print()" + " 4) float()")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: print()! It's what we're using right now to speak to you!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: print()! It's what we're using right now to speak to you!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 3:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yes! We use the print() function to send messages in code, which is what we're doing right now!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: print()! It's what we're using right now to speak to you!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
    if CS == 2:
      CSopening = random.randint(1, 2)
      print("Announcer: Computer Science!")
      time.sleep(2)
      if CSopening == 1:
        print("Banana: We're about to dive into science...")
        time.sleep(3)
        print("Banana: That is based around computers, Computer Science!")
      if CSopening == 2:
        print("Banana: Computer Science! Is it better than regular Science?")
      time.sleep(4)
      print("Announcer: A bit is the smallest increment of data that can only hold 2 values, 0 being off and 1 being on.")
      time.sleep(5)
      print("Announcer: Bit can also be used to express numbers, for example, these are 8 bits which make up a byte -> 00000000. From right to left, the maximum number for that bit is 2^0, 2^1, 2^2, and so on.")
      time.sleep(7)
      print("Announcer: Following those rules... What does this binary value represent? 01000110")
      print("1) 64" + " 2) 68" + " 3) 72" + " 4) 70")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 70! 01000110 -> 128, 64, 32, 16, 8, 4, 2, 1 -> off, on, off, off, off, on, on, off -> 64 + 4 + 2 = 70")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 70! 01000110 -> 128, 64, 32, 16, 8, 4, 2, 1 -> off, on, off, off, off, on, on, off -> 64 + 4 + 2 = 70")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 70! 01000110 -> 128, 64, 32, 16, 8, 4, 2, 1 -> off, on, off, off, off, on, on, off -> 64 + 4 + 2 = 70")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 4:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yes! 01000110 -> 128, 64, 32, 16, 8, 4, 2, 1 -> off, on, off, off, off, on, on, off -> 64 + 4 + 2 = 70")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
  if question == 2:
    QM = random.randint(1, 2)
    if QM == 1:
      QMopening = random.randint(1, 2)
      print("Announcer: Quick Maths!")
      time.sleep(2)
      if QMopening == 1:
        print("Banana: Math is everywhere!")
        time.sleep(3)
        print("Banana: There's no escaping this topic!")
      if QMopening == 2:
        print("Banana: Quick Maffs! Let's see how fast you can solve this!")
      time.sleep(4)
      print("Announcer: What is 7 multiplied by 8?")
      time.sleep(5)
      print("1) 56" + " 2) 57" + " 3) 15" + " 4) 54")
      QA = int(input(""))
      if QA == 1:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: 7 multiplied by 8 does indeed equal 56! It's also equivilant to adding 7, 8 times (7+7+7+7+7+7+7+7)")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 56! Add 7, 8 times in a row!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 56! Add 7, 8 times in a row!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 56! Add 7, 8 times in a row!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
    if QM == 2:
      QMopening = random.randint(1, 2)
      print("Announcer: Quick Maths!")
      time.sleep(2)
      if QMopening == 1:
        print("Banana: Math is everywhere!")
        time.sleep(3)
        print("Banana: There's no escaping this topic!")
      if QMopening == 2:
        print("Banana: Quick Maffs! Let's see how fast you can solve this!")
      time.sleep(4)
      print("Announcer: A store is offering a 20% discount on all items. If a customer buys a $50 item, how much will they pay after the discount?")
      time.sleep(5)
      print("1) $10" + " 2) $20" + " 3) $30" + " 4) $40")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: $40! 20% of $50 = 0.2 * 50 = $10. So the discount is $10 and the customer will pay $50 - $10 = $40 after the discount.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: $40! 20% of $50 = 0.2 * 50 = $10. So the discount is $10 and the customer will pay $50 - $10 = $40 after the discount.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: $40! 20% of $50 = 0.2 * 50 = $10. So the discount is $10 and the customer will pay $50 - $10 = $40 after the discount.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yes! 20% of $50 is $40!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
  if question == 3:
    NN = random.randint(1, 2)
    if NN == 1:
      NNopening = random.randint(1, 2)
      print("Announcer: Nonsensical Nonsense!")
      time.sleep(2)
      if NNopening == 1:
        print("Banana: I'm so ready for whatever this category is supposed to mean!")
      if NNopening == 2:
        print("Banana: Get ready for an extremely goofy question!")
      time.sleep(4)
      print("Announcer: How many holes are in a polo?")
      time.sleep(5)
      print("1) 1" + " 2) 2" + " 3) 3" + " 4) 4")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 4! We we're talking about the holes in the letters of this line 'a polo'!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 4! We we're talking about the holes in the letters of this line 'a polo'!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 4! We we're talking about the holes in the letters of this line 'a polo'!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 4:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct! The answer is 4! How did you get past our trick by reading 'a polo'? Or did you just guess?")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
    if NN == 2:
      NNopening = random.randint(1, 2)
      print("Announcer: Nonsensical Nonsense!")
      time.sleep(2)
      if NNopening == 1:
        print("Banana: I'm so ready for whatever this category is supposed to mean!")
      if NNopening == 2:
        print("Banana: Get ready for an extremely goofy question!")
      time.sleep(4)
      print("Announcer: Can a match box?")
      time.sleep(5)
      print("1) Yes" + " 2) No" + " 3) No, but a tin can" + " 4) Yes, one beat Mike Tyson")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No, but a tin can! It's a pun, meaning tin is able to box!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No, but a tin can! It's a pun, meaning tin is able to box!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
      if QA == 3:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct! Tin is able to box! Did you like our pun?")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No, but a tin can! It's a pun, meaning tin is able to box!")
        time.sleep(2)
        print("Total points: " + str(points))
        time.sleep(2)
  if question == 4:
    SC = random.randint(1, 2)
    if SC == 1:
      SCopening = random.randint(1, 3)
      print("Announcer: Science & Chemistry!")
      time.sleep(2)
      if SCopening == 1:
        print("Banana: We're about to dive into science...")
        time.sleep(3)
        print("Banana: That is NOT based around computers, just regular Science!")
      if SCopening == 2:
        print("Banana: Chemistry or Science? I would like to know!")
      if SCopening == 3:
        print("Banana: Would you prefer Science or Chemistry?")
      time.sleep(4)
      print("Announcer: What is the chemical formula for sodium bicorbonate?")
      time.sleep(5)
      print("1) NaCHO" + " 2) NaHCO" + " 3) NaHCO3" + " 4) NaCHO3")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: NaHCO3! It's sodium bicarbonate's chemical formula!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: NaHCO3! It's sodium bicarbonate's chemical formula!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yes! NaHCO3 is the correct chemical formula!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: NaHCO3! It's sodium bicarbonate's chemical formula!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if SC == 2:
      SCopening = random.randint(1, 3)
      print("Announcer: Science & Chemistry!")
      time.sleep(2)
      if SCopening == 1:
        print("Banana: We're about to dive into science...")
        time.sleep(3)
        print("Banana: That is NOT based around computers, just regular Science!")
      if SCopening == 2:
        print("Banana: Chemistry or Science? I would like to know!")
      if SCopening == 3:
        print("Banana: Would you prefer Science or Chemistry?")
      time.sleep(4)
      print(climage.convert('Californium.png', is_unicode=True))
      time.sleep(2)
      print("Announcer: What is this element called? (Cf)")
      time.sleep(5)
      print("1) Caesium" + " 2) Californium" + " 3) Chromium" + " 4) Copernicium")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Californium. Did California make this element?")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yes! Californium is the correct element! And yes, California did create this element!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Californium. Did California make this element?")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Californium. Did California make this element?")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 5:
    EL = random.randint(1, 2)
    if EL == 1:
      ELopening = random.randint(1, 2)
      print("Announcer: English Languages")
      time.sleep(2)
      if ELopening == 1:
        print("Banana: Ready to learn about English related topics?")
      if ELopening == 2:
        print("Banana: Why is it named English anyways? Isn't it just a language?")
      time.sleep(4)
      print("Announcer: What literary device is used in the following sentence: ... ")
      time.sleep(5)
      print(" ... 'The wind howled like a pack of wolves in the distance' ?")
      time.sleep(5)
      print("1) Metaphor" + " 2) Simile" + " 3) Personification" + " 4) Hyperbole")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Simile! A simile compares two things using the words like or as. The sentence included the word 'like'!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yes! Similes use the words like or as when comparing two things! This sentence has the word like.")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Simile! A simile compares two things using the words like or as. The sentence included the word 'like'!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Simile! A simile compares two things using the words like or as. The sentence included the word 'like'!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if EL == 2:
      ELopening = random.randint(1, 2)
      print("Announcer: English Language")
      time.sleep(2)
      if ELopening == 1:
        print("Banana: Ready to learn about English related topics?")
      if ELopening == 2:
        print("Banana: Why is it named English anyways? Isn't it just a language?")
      time.sleep(4)
      print("What is the difference between an allusion and a metaphor?")
      time.sleep(5)
      print("1) Allusion references famous people or events & Metaphor compares 2 unlike things" + " 2) Allusion compares 2 unlike things & Metaphor references famous people or events" + " 3) They are the same" + " 4) Allusion adds imagery & Metaphor is used for humor")
      QA = int(input(""))
      if QA == 1:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct! Can you think of any Allusions?")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No. 1! Allusion references famous people or events while metaphors are comparing two unlike things.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No. 1! Allusion references famous people or events while metaphors are comparing two unlike things.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No. 1! Allusion references famous people or events while metaphors are comparing two unlike things.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 6:
    HE = random.randint(1, 2)
    if HE == 1:
      HEopening = random.randint(1, 2)
      print("Announcer: Historical Events")
      time.sleep(2)
      if HEopening == 1:
        print("Banana: Time to travel backwards to the past!")
      if HEopening == 2:
        print("Banana: Would you prefer the past, present, or future?")
      time.sleep(4)
      print("Announcer: When did the French Revolution begin?")
      time.sleep(5)
      print("1) January 1793" + " 2) November 1791" + " 3) June 1789" + " 4) May 1789")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: May 1789!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: May 1789!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: May 1789!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
    if HE == 2:
      HEopening = random.randint(1, 2)
      print("Announcer: Historical Events")
      time.sleep(2)
      if HEopening == 1:
        print("Banana: Time to travel backwards to the past!")
      if HEopening == 2:
        print("Banana: Would you prefer the past, present, or future?")
      time.sleep(4)
      print("Announcer: When was the Silk Road established?")
      time.sleep(5)
      print("1) 130 B.C" + " 2) 114 B.C" + " 3) 1450 A.D" + " 4) 1453 A.D")
      QA = int(input(""))
      if QA == 1:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: May 1789!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: May 1789!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: May 1789!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 7:
    FB = random.randint(1, 2)
    if FB == 1:
      FBopening = random.randint(1, 3)
      print("Announcer: Food & Beverages")
      time.sleep(2)
      if FBopening == 1:
        print("Banana: Hope you're not too hungry when getting these questions!")
      if FBopening == 2:
        print("Banana: Will these questions quench your thirst?")
      if FBopening == 3:
        print("Banana: Don't think about eating me! Because then who will continue the game?")
      time.sleep(4)
      print("Announcer: What is the only fruit that has its seeds on the outside?")
      time.sleep(5)
      print("1) Lemon" + " 2) Watermelon" + " 3) Strawberry" + " 4) Pineapple")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Strawberry! They are the only fruit that has seeds on the outside. Unless if you want to count a watermelon *slice* instead of the whole watermelon fruit.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Strawberry! They are the only fruit that has seeds on the outside. Unless if you want to count a watermelon *slice* instead of the whole watermelon fruit.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct! For the watermelon, it's the *slices* that have seeds on the outside, but we're counting the entire fruit, not slices or chunks.")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Strawberry! They are the only fruit that has seeds on the outside. Unless if you want to count a watermelon *slice* instead of the whole watermelon fruit.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if FB == 2:
      FBopening = random.randint(1, 2)
      print("Announcer: Food & Beverages")
      time.sleep(2)
      if FBopening == 1:
        print("Banana: Hope you're not too hungry when getting these questions!")
      if FBopening == 2:
        print("Banana: Will these questions quench your thirst?")
      if FBopening == 3:
        print("Banana: Don't think about eating me! Because then who will continue the game?")
      time.sleep(4)
      print("Announcer: What is the core ingedient to the Shirley Temple drink?")
      time.sleep(5)
      print("1) Lemonade soda" + " 2) Ginger ale w/ grenadine" + " 3) Orange juice" + " 4) A cherry")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Ginger ale w/ grenadine! Sometimes people substitute ginger ale with lemon-lime soda but it's more common seeing ginger ale.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct! I wonder what other popular drinks taste like without the main ingredients.")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Ginger ale w/ grenadine! Sometimes people substitute ginger ale with lemon-lime soda but it's more common seeing ginger ale.")
        time.sleep(3)
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Ginger ale w/ grenadine! Sometimes people substitute ginger ale with lemon-lime soda but it's more common seeing ginger ale.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 8:
    TA = random.randint(1, 2)
    if TA == 1:
      TAopening = random.randint(1, 2)
      print("Announcer: Tourist Attractions")
      time.sleep(2)
      if TAopening == 1:
        print("Banana: Let's travel around the world!")
      if TAopening == 2:
        print("Banana: Get ready to see big objects!")
      time.sleep(4)
      print("Announcer: What world-famous tourist attraction was built for the 1889 World's Fair in Paris and was intended to be a temporary installation, but still stands today as an iconic symbol of the city?")
      time.sleep(5)
      print("1) Eiffel Tower" + " 2) Palace of Versailles" + " 3) Louvre Museum" + " 4) Musée d'Orsay")
      QA = int(input(""))
      if QA == 1:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct! Did you know, the Eiffel Tower's construction began in January 28th 1887?.")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Eiffel Tower. Paris is the city of love!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Eiffel Tower. Paris is the city of love!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Eiffel Tower. Paris is the city of love!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if TA == 2:
      TAopening = random.randint(1, 2)
      print("Announcer: Tourist Attractions")
      time.sleep(2)
      if TAopening == 1:
        print("Banana: Let's travel around the world!")
      if TAopening == 2:
        print("Banana: Get ready to see big objects!")
      time.sleep(4)
      print("Announcer: The Statue of Liberty was a gift to the United States from which country?")
      time.sleep(5)
      print("1) New York" + " 2) United Kingdom" + " 3) France" + " 4) Italy")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: France.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: France.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct! France's gift was The Statue of Liberty for the United States.")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: France.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 9:
    RG = random.randint(1, 2)
    if RG == 1:
      RGopening = random.randint(1, 2)
      print("Announcer: Randomly Generated")
      time.sleep(2)
      if RGopening == 1:
        print("Banana: Take it away ChatGPT!")
      if RGopening == 2:
        print("Banana: ChatGPT, you're on!")
      if RGopening == 3:
        print("Banana: It's time for ChatGPT to rise!")
      time.sleep(4)
      print("ChatGPT: Sure, here's your randomly generated trivia question")
      time.sleep(3)
      print("ChatGPT: What American state is known as the Land of 'Enchantment'?")
      time.sleep(5)
      print("1) Arizona" + " 2) New Mexico" + " 3) Kansas" + " 4) Louisiana")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: New Mexico!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: New Mexico!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: New Mexico!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if RG == 2:
      RGopening = random.randint(1, 2)
      print("Announcer: Randomly Generated")
      time.sleep(2)
      if RGopening == 1:
        print("Banana: Take it away ChatGPT!")
      if RGopening == 2:
        print("Banana: ChatGPT, you're on!")
      if RGopening == 3:
        print("Banana: It's time for ChatGPT to rise!")
      time.sleep(4)
      print("ChatGPT: Sure, here's your randomly generated trivia question")
      time.sleep(3)
      print("ChatGPT: What is the smallest planet in our solar system?")
      time.sleep(5)
      print("1) Mercury" + " 2) Moon" + " 3) Pluto" + " 4) Venus")
      QA = int(input(""))
      if QA == 1:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Mercury! The Moon belongs to Earth as it's Moon.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Mercury! Pluto is a dwark planet in our solar system.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Mercury! Venus is the 2nd smallest planet just smaller than Earth.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 10:
    HC = random.randint(1, 2)
    if HC == 1:
      HCopening = random.randint(1, 2)
      print("Announcer: Horror & Creepypastas")
      time.sleep(2)
      if HCopening == 1:
        print("Banana: I hope it isn't 3:00 A.M. for you!")
      if HCopening == 2:
        print("Banana: Are you ready for some spooky stuff?")
      if HCopening == 3:
        print("Banana: Try not to get scared!")
      time.sleep(4)
      print(climage.convert('RedMistSquidward.png', is_unicode=True))
      time.sleep(3)
      print("Announcer: What is the name of this creepypasta?")
      time.sleep(5)
      print("1) Faceless" + " 2) Rock Motto" + " 3) Bootleg" + " 4) Red Mist")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Red Mist! Full name: Red Mist Squidward! The actual name would be considered way to mature for this gameshow.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Red Mist! Full name: Red Mist Squidward! The actual name would be considered way to mature for this gameshow.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Red Mist! Full name: Red Mist Squidward! The actual name would be considered way to mature for this gameshow.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Good job to all of those die-hard creepypasta fans out there!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
    if HC == 2:
      HCopening = random.randint(1, 2)
      print("Announcer: Horror & Creepypastas")
      time.sleep(2)
      if HCopening == 1:
        print("Banana: I hope it isn't 3:00 A.M. for you!")
      if HCopening == 2:
        print("Banana: Are you ready for some spooky stuff?")
      if HCopening == 3:
        print("Banana: Try not to get scared!")
      time.sleep(4)
      print(climage.convert('Mouse.avi.png', is_unicode=True))
      time.sleep(3)
      print("Announcer: What is the name of this creepypasta?")
      time.sleep(5)
      print("1) Mouse" + " 2) Mouse.avi" + " 3) Mickey's Best Friend" + " 4) ???")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Mouse.avi! The actual name would be considered way to mature for this gameshow.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Good job to all of those die-hard creepypasta fans out there!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Mouse.avi! The actual name would be considered way to mature for this gameshow.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Mouse.avi! The actual name would be considered way to mature for this gameshow.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 11:
    HS = random.randint(1, 5)
    if HS == 1:
      HSopening = random.randint(1, 4)
      print("Announcer: Host's Special")
      time.sleep(2)
      if HSopening == 1:
        print("Banana: Welcome to our behind-the-scenes look of the program!")
      if HSopening == 2:
        print("Banana: Look at all of these things that got scrapped n' trashed")
      if HSopening == 3:
        print("Banana: Woah! Content!")
      if HSopening == 4:
        print("Banana: Hello scrapped items that are placed here due to syntax errors!")
      time.sleep(4)
      print(climage.convert('FakeMrBeast.png', is_unicode=True))
      time.sleep(3)
      print("???: ##########################")
      time.sleep(3)
      print("Announcer: What is the name of this scrapped host?")
      time.sleep(5)
      print("1) Mr. Beast" + " 2) Real Mr. Beast" + " 3) THE Mr. Beast" + " 4) Fake Mr. Beast")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Fake Mr. Beast.")
        time.sleep(3)
        print("*Mr. Beast is angrily staring at you*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Fake Mr. Beast.")
        time.sleep(3)
        print("*Mr. Beast is angrily staring at you*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Fake Mr. Beast.")
        time.sleep(3)
        print("*Mr. Beast is angrily staring at you*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yay! You got it right!")
        time.sleep(3)
        print("Fake Mr. Beast: MR BEEEEEEEEEEEAAAAAAAAASSSSSSSSSSTTTT")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
    if HS == 2:
      HSopening = random.randint(1, 4)
      print("Announcer: Host's Special")
      time.sleep(2)
      if HSopening == 1:
        print("Banana: Welcome to our behind-the-scenes look of the program!")
      if HSopening == 2:
        print("Banana: Look at all of these things that got scrapped n' trashed")
      if HSopening == 3:
        print("Banana: Woah! Content!")
      if HSopening == 4:
        print("Banana: Hello scrapped items that are placed here due to syntax errors!")
      time.sleep(4)
      print(climage.convert('MetalPipe.png', is_unicode=True))
      time.sleep(3)
      print("???")
      time.sleep(3)
      print("Announcer: What is the name of this scrapped host?")
      time.sleep(5)
      print("1) Pipe" + " 2) Metal" + " 3) MetalPipe" + " 4) xX_MetalPipe_Xx")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: MetalPipe.")
        time.sleep(3)
        print("MetalPipe: *MetalPipe noises*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: MetalPipe.")
        time.sleep(3)
        print("MetalPipe: *MetalPipe noises*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yay! You got it right!")
        time.sleep(3)
        print("MetalPipe: *MetalPipe noises*")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: MetalPipe.")
        time.sleep(3)
        print("MetalPipe: *MetalPipe noises*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if HS == 3:
      HSopening = random.randint(1, 4)
      print("Announcer: Host's Special")
      time.sleep(2)
      if HSopening == 1:
        print("Banana: Welcome to our behind-the-scenes look of the program!")
      if HSopening == 2:
        print("Banana: Look at all of these things that got scrapped n' trashed")
      if HSopening == 3:
        print("Banana: Woah! Content!")
      if HSopening == 4:
        print("Banana: Hello scrapped items that are placed here due to syntax errors!")
      time.sleep(4)
      print(climage.convert('Paul.png', is_unicode=True))
      time.sleep(3)
      print("???: ") #Need Paul to say something that doesn't give away the answer
      time.sleep(3)
      print("Announcer: What is the name of this scrapped host?")
      time.sleep(5)
      print("1) Paul" + " 2) Paool" + " 3) Pull" + " 4) Poul")
      QA = int(input(""))
      if QA == 1:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yay! You got it right!")
        time.sleep(3)
        print("Paul: ") #Need a positive comment from Paul
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Paul.")
        time.sleep(3)
        print("Paul: ")#Need a negative comment from paul
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Paul.")
        time.sleep(3)
        print("Paul: ")#Need a negative comment from paul
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Paul.")
        time.sleep(3)
        print("Paul: ")#Need a negative comment from paul
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if HS == 4:
      HSopening = random.randint(1, 4)
      print("Announcer: Host's Special")
      time.sleep(2)
      if HSopening == 1:
        print("Banana: Welcome to our behind-the-scenes look of the program!")
      if HSopening == 2:
        print("Banana: Look at all of these things that got scrapped n' trashed")
      if HSopening == 3:
        print("Banana: Woah! Content!")
      if HSopening == 4:
        print("Banana: Hello scrapped items that are placed here due to syntax errors!")
      time.sleep(4)
      print(climage.convert('Slowpoke.png', is_unicode=True))
      time.sleep(3)
      print("This unknown creature seems to be minding its own business") 
      time.sleep(3)
      print("Announcer: What is the name of this scrapped host?")
      time.sleep(5)
      print("1) Slowking" + " 2) Slowpoke" + " 3) Slowbro" + " 4) Mega Slowbro")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Slowpoke.")
        time.sleep(3)
        print("*Slowpoke proceeds to ignore you*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yay! You got it right!")
        time.sleep(3)
        print("Slowpoke: *Proceeds to do nothing*")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Slowpoke.")
        time.sleep(3)
        print("*Slowpoke proceeds to ignore you*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: Slowpoke.")
        time.sleep(3)
        print("*Slowpoke proceeds to ignore you*")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
    if HS == 5:
      HSopening = random.randint(1, 4)
      print("Announcer: Host's Special")
      time.sleep(2)
      if HSopening == 1:
        print("Banana: Welcome to our behind-the-scenes look of the program!")
      if HSopening == 2:
        print("Banana: Look at all of these things that got scrapped n' trashed")
      if HSopening == 3:
        print("Banana: Woah! Content!")
      if HSopening == 4:
        print("Banana: Hello scrapped items that are placed here due to syntax errors!")
      time.sleep(4)
      print(climage.convert('Roblox.png', is_unicode=True))
      time.sleep(3)
      print("Announcer: Why did this host end up getting deleted?")
      time.sleep(5)
      print("1) Because he is stupid" + " 2) Because the owner had no comments for him" + " 3) Because the owner thought some comments wouldn't make any sense" + " 4) Because there was already too many host ideas and he was clogging up space")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No. 2! We couldn't think of any responses to give this poor fella.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Yay! You got it right!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 3:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No. 2! We couldn't think of any responses to give this poor fella.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: No. 2! We couldn't think of any responses to give this poor fella.")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
  if question == 12:
    WDTM = 1 #random.randint(1, 2)
    if WDTM == 1:
      WDTMopening = random.randint(1, 4)
      print("Announcer: What does that mean?")
      time.sleep(2)
      if WDTMopening == 1:
        print("Banana: I don't know! You tell me!")
      if WDTMopening == 2:
        print("Banana: No seriously, what does that mean?")
      if WDTMopening == 3:
        print("Banana: Can you tell me what that meant?")
      if WDTMopening == 4:
        print("Banana: Does he know?")
      time.sleep(4)
      print("Announcer: What is the verb meaning of the word 'Gross'?")
      time.sleep(5)
      print("1) Very obvious; Unacceptable" + " 2) Twelve dozen (144)" + " 3) Produce or earn an amount of income" + " 4) Very unpleasant; Unattractive")
      QA = int(input(""))
      if QA == 1:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 3! For example: Avengers: Endgame grossed $2.7 billion!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 2:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 3! For example: Avengers: Endgame grossed $2.7 billion!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
      if QA == 3:
        if QCorrect == 1:
          print("Announcer: Hey! That's correct!")
        elif QCorrect == 2:
          print("Announcer: Correct!")
        elif QCorrect == 3:
          print("Announcer: Good job!")
        elif QCorrect == 4:
          print("Announcer: That's pretty based!")
        elif QCorrect == 5:
          print("Announcer: Yup!")
        elif QCorrect == 6:
          print("Announcer: Well done!")
        time.sleep(1)
        print("*DING*")
        time.sleep(2)
        print("Banana: Correct!")
        time.sleep(3)
        points = points + 10
        print("Total points: " + str(points))
      if QA == 4:
        if QWrong == 1:
          print("Announcer: NOPE!")
        elif QWrong == 2:
          print("Announcer: Sorry buddy.")
        elif QWrong == 3:
          print("Annoucner: Uh, no!")
        elif QWrong == 4:
          print("Announcer: You've just posted cringe!")
        elif QWrong == 5:
          print("Announcer: That's incorrect.")
        elif QWrong == 6:
          print("Announcer: Not happening.")
        time.sleep(1)
        print("*BUZZER* X")
        time.sleep(2)
        print("Banana: The correct answer...")
        time.sleep(3)
        print("Banana: 3! For example: Avengers: Endgame grossed $2.7 billion!")
        time.sleep(3)
        print("Total points: " + str(points))
        time.sleep(3)
print("Banana: Looks like you got 100 points!")
time.sleep(3)
print("Banana: Congratulations! You've won the gameshow!")
time.sleep(3)
print("Banana: The prize?... Well... uh... oh! bragging rights!")
time.sleep(3)
print("Banana: I hope you enjoyed this gameshow because it took a lot and I mean A LOT of time to get this working right!")
time.sleep(4)
print("Banana: Our owner had to keep repeatedly working on us on and off just to make sure everything is right and every single detail is added")
time.sleep(5)
print("Banana: With all of that out of the way, I hope to see you again in the near future!")
time.sleep(3)
print("Banana: Maybe try running the code again for a Round 2 for more questions? Round 3? Who knows?")
time.sleep(3)
print("Banana: But I keep stalling and I need this code to end so... bye-bye!")
time.sleep(3)
print("Announcer: Ok bye lol.")
time.sleep(3)
print("Announcer: Please rate this experience: 1) Very bad 2) Bad 3) Average) 4) Good 5) Very Good")
rating = int(input(""))
if rating == 1:
  print("Announcer: Oh, I see :(")
elif rating == 2:
  print("Announcer: Hey, I mean it's at least better than a one.")
elif rating == 3:
  print("Announcer: Ah, I see you're mixed and wanted to choose the middle option.")
elif rating == 4:
  print("Announcer: Hey, thanks!")
elif rating == 5:
  print("Announcer: WOW! You must've really enjoyed this game. You should run the code again to get even more fun.")
else:
  print("Announcer: I guess you didn't listen to me. But that's alright, mistakes happen sometimes and we have to accept that.")
time.sleep(5)
print("Announcer: Well, I'll be here waiting for you...whenever you want to play the code again.")