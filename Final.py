import json
import datetime
import random


def exit_program():
    print("Thanks for using our service!")
    exit()

def load_q():
    try:
        with open ("quiz.json")as infile:
            return json.load(infile)
    except:
        return []
def save_q(quiz):
    with open("quiz.json", "w")as outfile:
        json.dump(quiz, outfile, indent=4)

def load4():
    try:
        with open ("math.json")as infile:
            return json.load(infile)
    except:
        return []
def save4(math):
    with open("math.json", "w")as outfile:
        json.dump(math, outfile, indent=4)

def load3():
    try:
        with open ("programming.json")as infile:
            return json.load(infile)
    except:
        return []
def save3(programming):
    with open("programming.json", "w")as outfile:
        json.dump(programming, outfile, indent=4)

def load2():
    try:
        with open ("ml.json")as infile:
            return json.load(infile)
    except:
        return []
def save2(ml):
    with open("ml.json", "w")as outfile:
        json.dump(ml, outfile, indent=4)

def load():
    try:
        with open ("db.json")as infile:
            return json.load(infile)
    except:
        return []
def save(db):
    with open("db.json", "w")as outfile:
        json.dump(db, outfile, indent=4)

print()
print("🔻🔺" * 40)
class Signup:

            @staticmethod
            def get_password():
                    while True:
                        password = input("enter your password🔑 or (forgot): ".title())
                        if password.lower() == "forgot":
                            color = "red"
                            car = "demon"
                            question_1 = input("what is your favorite color ? ")
                            while question_1.lower() != color:
                                print("try again....❌".title())
                                question_1 = input("what is your favorite color ? ")
                            question_2 = input("what is your favorite car ? ")
                            while question_2.lower() != car:
                                print("try again....❌".title())
                                question_2 = input("what is your favorite car ? ")

                            password = input("enter your password🔑 : ".title())
                        if len(password) < 8:
                            print("least 8 character".title())
                        elif not any(char.islower() for char in password):
                            print("least on lower character".title())
                        elif not any(char.isupper() for char in password):
                            print("least on upper character".title())
                        elif not any(char.isdigit() for char in password):  # بررسی وجود حداقل یک عدد
                            print("At least one digit (number) is required".title())
                        else:
                            print("valid password...✅".title())
                            return password

            @staticmethod
            def email():
                # email section
                email = input("enter your email address📧: ".title())
                while not email.endswith("@gmail.com") and not email.endswith("@email.com"):
                    email = input("enter your email address📧: ".title())
                if email.endswith("@gmail.com") or email.endswith("@email.com"):
                        print("email valid 📧✅".title())
                        return email

            @staticmethod
            def birth():
                birth = int(input("enter your birth year🎂 : ".title()))
                birth_2 = datetime.datetime.now().year - birth
                if birth_2 < 18 or birth_2 > 50:
                    print("call to our office --> 347067".title())
                else:
                    return birth_2

            @staticmethod
            def signup():
                # username section
                db = load()
                time = datetime.datetime.now().strftime("%Y : %B : %d : %H : %M : %S")
                username = input("enter your username👨‍💻 : ".title())
                for i in db:
                    while i["username"] == username:
                        print("we have this one❌".title())
                        username = input("enter your username👨‍💻 : ".title())
                # password section
                password = Signup.get_password()

                # email section
                email = Signup.email()

                # id_code section
                id_code = random.randint(100000, 999999)

                # birthday section
                birth_2 = Signup.birth()
                print()
                print("🔻🔺" * 40)
                print()

                # info section
                info = {
                        "login time" : time,
                        "username" : username,
                        "password" : password,
                        "email" : email,
                        "birth year" : birth_2,
                        "id_code" : id_code
                }
                db.append(info)
                save(db)

class Login:
    @staticmethod
    def login():
        while True:
            db = load()
            ml = load2()
            programming = load3()
            math = load4()
            quiz = load_q()
            username = input("Enter your username👨‍💻 : ".title())
            password = input("Enter your password🔑 : ".title())
            founder = False
            for i in db:
                if username == i["username"]:
                    if password == i["password"]:
                        founder = True
                        print("Login successfully...✅")
                        while True:
                            ask = input("🔷 1) Request for registration in the course\n🔷 2) Request to participate in the placement test\n🔷 3) Forgot your password🔑 ? \n".title())

                            # حلقه برای انتخاب دوره که در صورت انتخاب دوره تکراری، به کاربر اجازه می‌دهد دوباره دوره دیگری انتخاب کند.

                            if ask == "1":
                                while True:  # حلقه برای انتخاب دوره
                                    menu = input(
                                        "🔷 Choose your course :\n🔷 1) Learning ML\n🔷 2) Learning Programming\n🔷 3) Learning Math\n".title())

                                    if menu == "1":
                                        # Check if the user has already chosen this course (ML)
                                        for j in ml:
                                            if j["username"] == username:
                                                print(
                                                    "You have already signed up for this course❌, please try again with a different course.".title())
                                                break
                                        else:  # Only add user to the course if they are not already in the list
                                            print("You chose to learn ML. Well done! ✅".title())
                                            for _ in db:
                                                i["course"] = "ML"
                                            print(
                                                f"Your course will begin ---> {datetime.datetime.now().strftime('%Y : %B : %d : %H : %M : %S')}")
                                            info_ml = {"username": username}
                                            ml.append(info_ml)
                                            save2(ml)
                                            save(db)
                                            break  # پس از ثبت‌نام موفق، از حلقه بیرون می‌آید

                                    elif menu == "2":
                                        # Check if the user has already chosen this course (Programming)
                                        for j in programming:
                                            if j["username"] == username:
                                                print(
                                                    "You have already signed up for this course❌, please try again with a different course.".title())
                                                break
                                        else:
                                            print("You chose to learn Programming. Well done! ✅".title())
                                            for _ in db:
                                                i["course"] = "Programming"
                                            print(
                                                f"Your course will begin ---> {datetime.datetime.now().strftime('%Y : %B : %d : %H : %M : %S')}")
                                            info_pro = {"username": username}
                                            programming.append(info_pro)
                                            save3(programming)
                                            save(db)
                                            break

                                    elif menu == "3":
                                        # Check if the user has already chosen this course (Math)
                                        for j in math:
                                            if j["username"] == username:
                                                print(
                                                    "You have already signed up for this course❌, please try again with a different course.".title())
                                                break
                                        else:
                                            print("You chose to learn Math. Well done! ✅".title())
                                            for _ in db:
                                                i["course"] = "Math"
                                            print(
                                                f"Your course will begin ---> {datetime.datetime.now().strftime('%Y : %B : %d : %H : %M : %S')}")
                                            info_math = {"username": username}
                                            math.append(info_math)
                                            save4(math)
                                            save(db)
                                            break

                            elif ask == "2":
                                grade = 0
                                while True:

                                    print("your test is going to start...✅".title())
                                    print()
                                    print("🔻🔺" * 40)
                                    print()
                                    q_1 = input("where is the capital of Nigeria ?\n1)tehran\n2)milan\n3)baghdad\n4)abaju\ntype answer : ".title())
                                    for q in quiz:
                                        if q_1.lower() == q["q_1"]:
                                            print("well done...✅")
                                            grade += 1
                                        else:
                                            print("incorrect...❌")

                                    q_2 = input("where is the capital of italy ?\n1)rome\n2)milan\n3)baghdad\n4)abaju\ntype answer :  ".title())
                                    for q in quiz:
                                        if q_2.lower() == q["q_2"]:
                                            print("well done...✅")
                                            grade += 1
                                        else:
                                            print("incorrect...❌")

                                    q_3 = input("what is the largest river in europe ?\n1)forat\n2)nil\n3)amazon\n4)volga\ntype answer :  ".title())
                                    for q in quiz:
                                        if q_3.lower() == q["q_3"]:
                                            print("well done...✅")
                                            grade += 1
                                        else:
                                            print("incorrect...❌")

                                    q_4 = input("where is the biggest church in europe ?\n1)esphahan\n2)vatican\n3)milan\n4)tehran\ntype answer : ".title())
                                    for q in quiz:
                                        if q_4.lower() == q["q_4"]:
                                            print("well done...✅")
                                            grade += 1
                                        else:
                                            print("incorrect...❌")

                                    q_5 = input("what is the name of hitlers army ?\n1)People's Liberation Army Ground Force\n2)United States Army\n3)wehrmacht\n4)French Army\ntype answer : ".title())
                                    for q in quiz:
                                        if q_5.lower() == q["q_5"]:
                                            print("well done...✅")
                                            grade += 1
                                        else:
                                            print("incorrect...❌")
                                    for _ in db:
                                        i["grade"] = grade
                                    save(db)

                                    # در اینجا برنامه به طور کامل تمام می‌شود
                                    exit_program()


                            elif ask == "3":
                                color = "red"
                                car = "demon"
                                question_1 = input("What is your favorite color? ")
                                while question_1.lower() != color:
                                    print("Try again....❌".title())
                                    question_1 = input("What is your favorite color? ")
                                question_2 = input("What is your favorite car? ")
                                while question_2.lower() != car:
                                    print("Try again....❌".title())
                                    question_2 = input("What is your favorite car? ")
                                print("You've answered correctly✅")
                                new_password = Signup.get_password()  # Ask for a new password

                                # Update password in database
                                i["password"] = new_password
                                save(db)  # Save changes

                                print("Your password has been updated successfully. Please login again.".title())
                                break


                            else:
                                print("wrong input...❌".title())
                                continue
                        break
            if not founder:
                print("User not found...❌".title())
            else:
                return founder


print("🔷hello and welcome to our final project🔷".title())

while True:
    base_q = input("🔷enter your choice 🔷:\n🔷 1) signup\n🔷 2) login\n ".title())
    if base_q == "1":
        Signup.signup()

    elif base_q == "2":
        Login.login()

    else:
        print("Try Again...❌")