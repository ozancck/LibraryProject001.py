

while True:

    books = []
    books1 = []
    with open("Books.txt", "r") as f:
        for x in f:
            books1 = x.split(",")
            books1[3] = books1[3].replace("\n", "")
            books.append(books1)

    students = []
    student1 = []
    with open("students.txt", "r") as f:
        for x in f:
            student1 = x.split(" ")
            student1[2] = student1[2].replace("\n", "")
            students.append(student1)

    checkList = []
    check1 = []
    with open("CheckList.txt", "r") as f:
        for x in f:
            check1 = x.split(",")
            check1[1] = check1[1].replace("\n", "")
            checkList.append(check1)

    anaInput1 = str(input("PRESS A FOR STUDENTS PROCEDURES.\nPRESS B FOR BOOKS PROCEDURES.\n"))

    if anaInput1 == "A":

            print("")
            print(".....................................................................")
            anaInput2 = str(input("LIST ALL THE STUDENTS PRESS G \n"
                                  "RETURN MAIN MENU PRESS Q"))
            print(".....................................................................")
            print("")

            if anaInput2 == "G":

                for x in students:
                    print("{}, {}, {}".format(x[0], x[1], x[2]), end="")
                    for y in checkList:
                        if x[0] == y[0]:
                            print(y[1], end="|")
                    print("\n")

            elif anaInput2 == "Q":
                break
            else:
                print("WRONG KEY :(")

    elif anaInput1 == "B":






            anaInput = str(input(
                "LIST ALL THE BOOKS PRESS K \n"
                "LIST ALL CHECKED BOOKS PRESS L \n"
                "ADD A NEW BOOK PRESS M \n"
                "SEARCH A BOOK BY ISBN NUMBER PRESS N \n"
                "SEARCH A BOOK BY NAME PRESS O \n"
                "CHECKED OUT A BOOK TO A STUDENT PRESS P \n"
                "RETURN MAIN MENU PRESS QQ \n"))

            if anaInput == "K":

                print(".....................................................................")
                for x in books:
                    print("{}, {}, {}, {}\n".format(x[0], x[1], x[2], x[3]))

            elif anaInput == "L":
                print(".....................................................................")
                for x in books:
                    if x[3] == "T":
                        print("{},{},{},{}\n".format(x[0], x[1], x[2], x[3]))


                print(".....................................................................")
                print("")

            elif anaInput == "M":

                print(".....................................................................")

                name = input("Book name: ")
                writer = input("Book's writer Name: ")
                ısbn = input("ISBN: ")

                bookTxt = open("books.txt", "a")
                bookTxt.write("{},{},{},F\n".format(ısbn, name, writer))
                bookTxt.close()
                print("Book Added")
                print(".....................................................................")

            elif anaInput == "N":

                print(".....................................................................")
                isbnSearch = 0
                isbn1 = int(input("ISBN : "))
                for x in books:
                    if x[0] == str(isbn1):
                        print("{}, {}, {}, {}\n".format(x[0], x[1], x[2], x[3]))
                        isbnSearch = 1
                if isbnSearch == 0:
                    print("Book not found")
                print(".....................................................................")

            elif anaInput == "O":
                print("")
                print(".....................................................................")
                arananKitap = []
                bookName = input("Book's Name : ")
                for x in books:
                    if x[1].find(str(bookName)) == -1:
                        continue
                    else:
                        arananKitap.append(x)
                if len(arananKitap) != 0:
                    for x in arananKitap:
                        print("{}, {}, {}, {}\n".format(x[0], x[1], x[2], x[3]))
                else:
                    print("The Book not found.")

                arananKitap.clear()

                print(".....................................................................")

            elif anaInput == "P":

                bookIsbnC = 0
                bookStudentC = 0
                print("Enter book ISBN and student ID,")
                bCI = input("ISBN : ")
                bCS = input("STUDENT ID : ")
                for x in books:
                    if x[0] == str(bCI):
                        x[3] = "T"
                        bookTxt = open("Books.txt", "w")
                        for x in books:
                            bookTxt.write("{},{},{},{}\n".format(x[0], x[1], x[2], x[3]))
                        bookTxt.close()
                        bookIsbnC = 1

                if bookIsbnC == 0:
                    print("THE BOOK NOT FOUND.")

                for x in students:
                    if x[0] == str(bCS):
                        bookStudentC = 1
                if bookStudentC == 0:
                    print("STUDENT NOT FOUND.")

                check_txt = open("CheckList.txt", "a")
                check_txt.write("{},{}\n".format(bCS, bCI))
                check_txt.close()

            else:
                print("")
                print(".....................................................................")
                print("WRONG KEY")
                print(".....................................................................")
                print("")

    else:
        print("")
        print(".....................................................................")
        print("WRONG KEY")
        print(".....................................................................")
        print("")


