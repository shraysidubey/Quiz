Q1 = """1. What do you call a computer on a network that requests files from another computer ?
a. A client
b. A host
c. A router
d. web server"""

Q2 = """2. Hardware devices that are not part of the main computer system and are often added later to the system ?
a. Peripheral
b. Clip art
c. Highlight
d. Execute"""

Q3 = """3. The main computer that stores the files that can be sent to computers that are networked together is:
a. Clip art
b. Mother board
c. Peripheral
d. File server"""

Q4 = """4. How can you catch a computer virus?
a. Sending e-mail messages
b. Using a laptop during the winter
c. Opening e-mail attachments
d. Shopping on-line"""

Q5 = """5. Google (www.google.com) is a:
a. Search Engine
b. Number in Math
c. Directory of images
d. Chat service on the web"""

Q6 = """6. Which is not an Internet protocol?
a. HTTP
b. FTP
c. STP
d. IP"""

Q7 = """7. Which of the following is not a valid domain name ?
a. www.yahoo.com
b. www.yahoo.co.uk
c. www.com.yahoo
d. www.yahoo.co.in"""

Q8 = """8. AOL stands for:
a. Arranged Outer Line
b. America Over LAN
c. Audio Over LAN
d. America On-line"""

Q9 = """9. Another name for a computer chip is:
a. Execute
b. Micro chip
c. Microprocessor
d. Select"""

Q10 = """10. "www" stands for:
a. World Wide Web
b. World Wide Wares
c. World Wide Wait
d. World Wide War"""


input_from_user = input("Do you want to play quiz (yes/no)").lower()
if input_from_user != "yes":
    exit()
else:
    user_name = input("Please Enter your name :")

    print("Hi, " + user_name + " let's start the quiz ")

questions = {Q1:"a", Q2:"a", Q3:"d", Q4:"c", Q5:"a", Q6:"c", Q7:"c", Q8:"d", Q9:"b", Q10:"a"}

score = 0
for key in questions:
    print()
    print(key)
    print()
    ans = input("please select any one answer(a/b/c/d): ").lower()
    if ans == questions[key]:
        score += 1
        print()
        print("Hi " + user_name + " your score is: " + str(score))
    else:
        print("oop's selected wrong answer")
print()
print("Your total score is: " + str(score))

if int(score) > 7:
    print("Wohhoo!! You passed the quiz.")
else:
    print("Not achieved good score, please play again.") 


