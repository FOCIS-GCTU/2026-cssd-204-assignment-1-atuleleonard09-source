# File: initials.py
# Description: Print out my initials in stylized large block letters.
# Assignment Number: 1
#
# Name: Leonard Awindoleti Atule
# STUDENT ID:  <YOUR SID>
# Email: <YOUR EMAIL>
# Grader: <YOUR GRADER'S NAME Carolyn OR Emma or Ahmad>
#
# On my honor, Leonard Awindoleti Atule, this programming assignment is my own work
# and I have not provided this code to any other student.


def main():
    # Print initials L, A, A in small form then as large 12x10 block letters
    # made of the corresponding letter and periods. Each letter is 12 chars wide
    # by 10 chars high, followed by a 4-char asterisk period block on the last 2
    # rows. Three dots border each side of each letter+period pair.
    # Total output: 10 rows high x 60 chars wide. No trailing spaces.

    print()
    print("...LAA")
    print()

    # Row 0
    print("..." + "LL.........." + "...." + "..." + "....AAAA...." + "...." + "..." + "....AAAA...." + "...." + "...")
    # Row 1
    print("..." + "LL.........." + "...." + "..." + "...AAAAAA..." + "...." + "..." + "...AAAAAA..." + "...." + "...")
    # Row 2
    print("..." + "LL.........." + "...." + "..." + "..AA....AA.." + "...." + "..." + "..AA....AA.." + "...." + "...")
    # Row 3
    print("..." + "LL.........." + "...." + "..." + ".AA......AA." + "...." + "..." + ".AA......AA." + "...." + "...")
    # Row 4
    print("..." + "LL.........." + "...." + "..." + "AAAAAAAAAAAA" + "...." + "..." + "AAAAAAAAAAAA" + "...." + "...")
    # Row 5
    print("..." + "LL.........." + "...." + "..." + "AAAAAAAAAAAA" + "...." + "..." + "AAAAAAAAAAAA" + "...." + "...")
    # Row 6
    print("..." + "LL.........." + "...." + "..." + "AA........AA" + "...." + "..." + "AA........AA" + "...." + "...")
    # Row 7
    print("..." + "LL.........." + "...." + "..." + ".AA......AA." + "...." + "..." + ".AA......AA." + "...." + "...")
    # Row 8
    print("..." + "LL.........." + "****" + "..." + ".AA......AA." + "****" + "..." + ".AA......AA." + "****" + "...")
    # Row 9
    print("..." + "LLLLLLLLLLLL" + "****" + "..." + ".AA......AA." + "****" + "..." + ".AA......AA." + "****" + "...")

    print()


main()
