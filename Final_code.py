import pyttsx3
import speech_recognition as sr
import time
import datetime
import random
import pandas as pd

def otp():
    otp = random.randrange(1000,10000)
    print("pass code",otp)
    return otp


def dt():
    datetime_object = datetime.datetime.now()
    print("Date And time",datetime_object)
    return datetime_object


def recognition(a):
    print()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(a)
        print("Listening....")
        time.sleep(1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if(text == "mail"):
                text = "male"
                print("You said : {}".format(text.upper()))
                return text
            elif (text == "be positive"):
                text = "b positive"
                print("You said : {}".format(text.upper()))
                return text
            elif (text == 2):
                newtext = r.recognize_google(audio)
                print("You said : {}".format(newtext.upper()))
                newtext = text.replace(text, newtext)
                return newtext
            else:
                print("You said : {}".format(text.upper()))
                return text
        except:
            print("Sorry could not recognize what you said")
            return False


def recognition1(b):
    print()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(b)
        print("ऐकत आहे")
        time.sleep(1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if (text == "mail"):
                text = "male"
                print("आपण सांगितले: : {}".format(text.upper()))
                return text
            elif (text == "be positive"):
                text = "B POSITIVE"
                print("You said : {}".format(text.upper()))
                return text
            elif (text == 2):
                newtext = r.recognize_google(audio)
                print("आपण सांगितले: : {}".format(newtext.upper()))
                newtext = text.replace(text, newtext)
                return newtext
            else:
                print("आपण सांगितले: : {}".format(text.upper()))
                return text
        except:
            print("क्षमस्व, आपण काय म्हटले ते ओळखणे शक्य नाही")
            return False

def func1(p, q, r, s, t, u, w):
    reader = pd.read_excel(r"./Registered Members.xlsx")
    df = pd.DataFrame({"Date":[datetime.date.today()], "Time":[time.strftime("%H:%M:%S")], "Name": [str(p.upper())], "Age": [q], "Gender": [str(u.upper())], "BloodGroup": [str(t.upper())], "Area": [str(s.upper())], "ContactNumber": [r], "Passcode":[str(w)]})
    df1 = pd.concat([reader, df])
    writer = pd.ExcelWriter("./Registered Members.xlsx")
    df1.to_excel(writer, index=False)
    writer.close()
    print("---------------------------------------------------------------------------------------")
    print("Enrollment Successful !")
    print("---------------------------------------------------------------------------------------")


def func2():
    df = open("Registered Members.xlsx")
    content = df.read()
    print(content)
    df.close()



def func3(g, h, i, j, k, x, y, z):
    print("|| Name:" + str(g.upper()))
    print("|| Age:" + str(h))
    print("|| Contact number:" + str(i))
    print("|| Locality:" + str(j.upper()))
    print("|| Blood Group:" + str(k.upper()))
    print("|| Gender:" + str(x.upper()))
    print("|| Date and time:" + str(y))
    print("|| Pass Code:" + str(z))


def func4(k):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    # print(rate)
    engine.setProperty('rate', 120)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id)
    engine.say(k)
    engine.runAndWait()


def func5():
    func4("Please say your name")
    e11 = recognition("Please say your name")
    while True:
        if(e11 == False):
            func4("Please say your name")
            e11 = recognition("Please say your name")
        else:
            break
    func4("\nIf your name is correct press 1\nIf your name is incorrect press 2")
    print("\nIf your name is correct press 1\nIf your name is incorrect press 2")
    repeat = int(input("Your choice.."))
    while True:
       if(repeat == 2):
           func4("Please say your name")
           c11 = recognition("Please say your name")
           while True:
               if (c11 == False):
                   func4("Please say your name")
                   c11 = recognition("Please say your name")
               else:
                   break
           c11 =e11.replace(e11, c11)
           e11 = c11
           func4("\nIf your name is correct press 1\nIf your name is incorrect press 2")
           print("\nIf your name is correct press 1\nIf your name is incorrect press 2")
           repeat = int(input("Your choice.."))
       elif(repeat == 1):
           print(" ")
           break
       else:
           func4("\nIf your name is correct press 1\nIf your name is incorrect press 2")
           print("\nIf your name is correct press 1\nIf your name is incorrect press 2")
           repeat = int(input("Your choice.."))


    func4("Please say your age")
    e12 = recognition("Please say your age")
    while True:
        if(e12 == False):
            func4("Please say your age")
            e12 = recognition("Please say your age")
        else:
            break
    func4("\nIf your age is correct press 1\nIf your age is incorrect press 2")
    print("\nIf your age is correct press 1\nIf your age is incorrect press 2")
    repeat = int(input("Your choice.."))
    while True:
        if(repeat == 2):
            func4("Please say your age")
            c12 = recognition("Please say your age")
            while True:
                if (c12 == False):
                    func4("Please say your age")
                    c12 = recognition("Please say your age")
                else:
                    break
            c12 = e12.replace(e12, c12)
            e12 = c12
            func4("\nIf your age is correct press 1\nIf your age is incorrect press 2")
            print("\nIf your age is correct press 1\nIf your age is incorrect press 2")
            repeat = int(input("Your choice.."))
        elif(repeat == 1):
            print(" ")
            break
        else:
            func4("\nIf your age is correct press 1\nIf your age is incorrect press 2")
            print("\nIf your age is correct press 1\nIf your age is incorrect press 2")
            repeat = int(input("Your choice.."))


    func4("Please say your phone number")
    e13 = recognition("Please say your phone number")
    while True:
        if(e13 == False):
            func4("Please say your phone number")
            e13 = recognition("Please say your phone number")
        else:
            break
    func4("\nIf your Phone Number is correct press 1\nIf your Phone Number is incorrect press 2")
    print("\nIf your Phone Number is correct press 1\nIf your Phone Number is incorrect press 2")
    repeat = int(input("Your choice.."))
    while True:
        if (repeat == 2):
            func4("Please say your phone number")
            c13 = recognition("Please say your phone number")
            while True:
                if (c13 == False):
                    func4("Please say your phone number")
                    c13 = recognition("Please say your phone number")
                else:
                    break
            c13 = e13.replace(e13, c13)
            e13 = c13
            func4("\nIf your Phone Number is correct press 1\nIf your Phone Number is incorrect press 2")
            print("\nIf your Phone Number is correct press 1\nIf your Phone Number is incorrect press 2")
            repeat = int(input("Your choice.."))
        elif (repeat == 1):
            print("  ")
            break
        else:
            func4("\nIf your Phone Number is correct press 1\nIf your Phone Number is incorrect press 2")
            print("\nIf your Phone Number is correct press 1\nIf your Phone Number is incorrect press 2")
            repeat = int(input("Your choice.."))


    func4("Please say your Area or Locality")
    e14 = recognition("Please say your Area or Locality")
    while True:
        if(e14 == False):
            func4("Please say your Area or Locality")
            e14 = recognition("Please say your Area or Locality")
        else:
            break
    func4("\nIf your Locality is correct press 1\nIf your locality is incorrect press 2")
    print("\nIf your Locality is correct press 1\nIf your locality is incorrect press 2")
    repeat = int(input("Your choice.."))
    while True:
        if (repeat == 2):
            func4("Please say your Area or Locality")
            c14 = recognition("Please say your Area or Locality")
            while True:
                if (c14 == False):
                    func4("Please say your Area or Locality")
                    c14 = recognition("Please say your Area or Locality")
                else:
                    break
            c14 = e14.replace(e14, c14)
            e14 = c14
            func4("\nIf your Locality is correct press 1\nIf your locality is incorrect press 2")
            print("\nIf your Locality is correct press 1\nIf your locality is incorrect press 2")
            repeat = int(input("Your choice.."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            func4("\nIf your Locality is correct press 1\nIf your locality is incorrect press 2")
            print("\nIf your Locality is correct press 1\nIf your locality is incorrect press 2")
            repeat = int(input("Your choice.."))


    func4("Please say your blood group")
    e15 = recognition("Please say your blood group")
    while True:
        if(e15 == False):
            func4("Please say your blood group")
            e15 = recognition("Please say your blood group")
        else:
            break
    func4("\nIf your Blood Group is correct press 1\nIf your Blood Group is incorrect press 2")
    print("\nIf your Blood Group is correct press 1\nIf your Blood Group is incorrect press 2")
    repeat = int(input("Your choice.."))
    while True:
        if (repeat == 2):
            func4("Please say your blood group")
            c15 = recognition("Please say your blood group")
            while True:
                if (c15 == False):
                    func4("Please say your blood group")
                    c15 = recognition("Please say your blood group")
                else:
                    break
            c15 = e15.replace(e15, c15)
            e15 = c15
            func4("\nIf your Blood Group is correct press 1\nIf your Blood Group is incorrect press 2")
            print("\nIf your Blood Group is correct press 1\nIf your Blood Group is incorrect press 2")
            repeat = int(input("Your choice.."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            func4("\nIf your Blood Group is correct press 1\nIf your Blood Group is incorrect press 2")
            print("\nIf your Blood Group is correct press 1\nIf your Blood Group is incorrect press 2")
            repeat = int(input("Your choice.."))


    func4("Please say your gender")
    e16 = recognition("Please say your gender")
    while True:
        if(e16 == False):
            func4("Please say your gender")
            e16 = recognition("Please say your gender")
        else:
            break
    func4("\nIf your Gender is correct press 1\nIf your Gender is incorrect press 2")
    print("\nIf your Gender is correct press 1\nIf your Gender is incorrect press 2")
    repeat = int(input("Your choice.."))
    while True:
        if (repeat == 2):
            func4("Please say your gender")
            c16 = recognition("Please say your gender")
            while True:
                if (c16 == False):
                    func4("Please say your gender")
                    c16 = recognition("Please say your gender")
                else:
                    break
            c16 = e16.replace(e16, c16)
            e16 = c16
            func4("\nIf your Gender is correct press 1\nIf your Gender is incorrect press 2")
            print("\nIf your Gender is correct press 1\nIf your Gender is incorrect press 2")
            repeat = int(input("Your choice.."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            func4("\nIf your Gender is correct press 1\nIf your Gender is incorrect press 2")
            print("\nIf your Gender is correct press 1\nIf your Gender is incorrect press 2")
            repeat = int(input("Your choice.."))

    e17 = dt()
    func4("Note Down Your Passcode\nIts important")
    e18 = otp()
    func1(e11, e12, e13, e14, e15, e16, e18)
    func4("Please confirm your details shown below")
    func3(e11, e12, e13, e14, e15, e16, e17, e18)



def func7():
    func4("krupaaya aaple naav saanga")
    m11 = recognition1("कृपया आपले नाव सांगा:")
    while True:
        if (m11 == False):
            func4("krupaaya aaple naav saanga")
            m11 = recognition1("कृपया आपले नाव सांगा:")
        else:
            break
    print("आपले नाव बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
    repeat = int(input("पर्याय निवडा..."))
    while True:
        if (repeat == 2):
            func4("krupaaya aaple naav saanga")
            c11 = recognition1("कृपया आपले नाव सांगा:")
            while True:
                if (c11 == False):
                    func4("krupaaya aaple naav saanga")
                    c11 = recognition1("कृपया आपले नाव सांगा:")
                else:
                    break
            c11 = m11.replace(m11, c11)
            m11 = c11
            print("आपले नाव बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            print("आपले नाव बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा"))


    func4("krupaaya aaple vaya saanga")
    m12 = recognition1("कृपया आपले वय सांगा:")
    while True:
        if (m12 == False):
            func4("krupaaya aaple vaya saanga")
            m12 = recognition1("कृपया आपले वय सांगा:")
        else:
            break
    print("आपले वय बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
    repeat = int(input("पर्याय निवडा..."))
    while True:
        if (repeat == 2):
            func4("krupaaya aaple vaya saanga")
            c12 = recognition1("कृपया आपले वय सांगा:")
            while True:
                if (c12 == False):
                    func4("krupaaya aaple vaya saanga")
                    c12 = recognition1("कृपया आपले वय सांगा:")
                else:
                    break
            c12 = m12.replace(m12, c12)
            m12 = c12
            print("आपले वय बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            print("आपले वय बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))


    func4("krupaaya aapla Mōbā'īla kraamaanka saanga")
    m13 = recognition1("कृपया तुमचा संपर्क क्रमांक सांगा:")
    while True:
        if (m13 == False):
            func4("krupaaya aapla Mōbā'īla kraamaanka saanga")
            m13 = recognition1("कृपया तुमचा संपर्क क्रमांक सांगा:")
        else:
            break
    print("आपला मोबाईल नंबर बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
    repeat = int(input("पर्याय निवडा..."))
    while True:
        if (repeat == 2):
            func4("krupaaya aapla Mōbā'īla kraamaanka saanga")
            c13 = recognition1("कृपया तुमचा संपर्क क्रमांक सांगा:")
            while True:
                if (c13 == False):
                    func4("krupaaya aapla Mōbā'īla kraamaanka saanga")
                    c13 = recognition1("कृपया तुमचा संपर्क क्रमांक सांगा:")
                else:
                    break
            c13 = m13.replace(m13, c13)
            m13 = c13
            print("आपला मोबाईल नंबर बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            print("आपला मोबाईल नंबर बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))


    func4("krupaaya aaple parisara saanga")
    m14 = recognition1("कृपया आपला परिसर सांगा:")
    while True:
        if (m14 == False):
            func4("krupaaya aaple parisara saanga")
            m14 = recognition("कृपया आपला परिसर सांगा:")
        else:
            break
    print("आपला परिसर बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
    repeat = int(input("पर्याय निवडा..."))
    while True:
        if (repeat == 2):
            func4("krupaaya aaple parisara saanga")
            c14 = recognition1("कृपया आपला परिसर सांगा:")
            while True:
                if (c14 == False):
                    func4("krupaaya aaple parisara saanga")
                    c14 = recognition1("कृपया आपला परिसर सांगा:")
                else:
                    break
            c14 = m14.replace(m14, c14)
            m14 = c14
            print("आपला परिसर बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            print("आपला परिसर बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))


    func4("krupaaya aaple Blood group saanga")
    m15 = recognition1("कृपया आपल्या रक्तगट सांगा:")
    while True:
        if (m15 == False):
            func4("krupaaya aaple Blood group saanga")
            m15 = recognition("कृपया आपल्या रक्तगट सांगा:")
        else:
            break
    print("आपला ब्लड ग्रुप बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
    repeat = int(input("पर्याय निवडा..."))
    while True:
        if (repeat == 2):
            func4("krupaaya aaple Blood group saanga")
            c15 = recognition1("कृपया आपल्या रक्तगटास सांगा:")
            while True:
                if (c15 == False):
                    func4("krupaaya aaple Blood group saanga")
                    c15 = recognition1("कृपया आपल्या रक्तगटास सांगा:")
                else:
                    break
            c15 = m15.replace(m15, c15)
            m15 = c15
            print("आपला ब्लड ग्रुप बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            print("आपला ब्लड ग्रुप बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))


    func4("krupaaya aaple leenga sanga")
    m16 = recognition1("कृपया आपले लिंग सांगा:")
    while True:
        if (m16 == False):
            func4("krupaaya aaple leenga sanga")
            m16 = recognition("कृपया आपले लिंग सांगा:")
        else:
            break
    print("आपले लिंग बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
    repeat = int(input("पर्याय निवडा..."))
    while True:
        if (repeat == 2):
            func4("krupaaya aaple leenga sanga")
            c16 = recognition1("कृपया आपले लिंग सांगा:")
            while True:
                if (c16 == False):
                    func4("krupaaya aaple leenga sanga")
                    c16 = recognition1("कृपया आपले लिंग सांगा:")
                else:
                    break
            c16 = m16.replace(m16, c16)
            m16 = c16
            print("आपले लिंग बरोबर असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))
        elif (repeat == 1):
            print(" ")
            break
        else:
            print("आपले लिंग असल्यास 1 दाबा अथवा 2 दाबा")
            repeat = int(input("पर्याय निवडा..."))


    m17 = dt()
    print("कृपया आपला पासकोड लक्षात ठेवा")
    m18 = otp()
    func1(m11, m12, m13, m14, m15, m16, m18)
    func4("krupaaya apalya maaheeteechee pushti kaara")
    print("आपली माहिती बरोबर असल्याची खात्री करा")
    func3(m11, m12, m13, m14, m15, m16, m17, m18)


while True:
    print("=====================================================================================")
    print("|                              WELCOME TO THE SYSTEM                                |")
    print("=====================================================================================")
    print("---------------------------------------------------------------------------------------")
    print("Press 1 to continue in English.\nमराठी मध्ये पुढे जाण्यासाठी 2दाबा.\nPress b to go back")
    print("---------------------------------------------------------------------------------------")
    choice5 = input("Enter your choice:")
    print("---------------------------------------------------------------------------------------")
    print("** WELCOME TO REGISTRATION PROCESS **")
    print("---------------------------------------------------------------------------------------")
    if choice5 == '1':
        func5()
        continue

    elif choice5 == '2':
        func7()
        continue

    else:
        print("* Invalid Input. Try Again ! *")
        continue
