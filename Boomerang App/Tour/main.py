# .withdraw() and .deiconify() to make frame hide and show respectively. NEVER use .destroy()

from tkinter import *
import mysql.connector
from mysql.connector import Error
import webbrowser
import smtplib

# Sample smtplib mailing format
"""sender = 'noreplymailboomerang@gmail.com'
receivers = ['mailaddress@anymail.com']"""
#message = """From: Boomerang <noreplymailboomerang@gmail.com>
#To: To Person <csecec.1802061@gmail.com>
#MIME-Version: 1.0
#Content-type: text/html
#Subject: Payment Successful
#<b>Your payment has been successful and approved</b>
#<br>
#<i>by Boomerang Tour and Travels</i>
#"""
"""
try:
   smtpObj = smtplib.SMTP('smtp.gmail.com:587')
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.login('noreplymailboomerang@gmail.com', '69420blaze')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")
"""

# Connection to Localhost
try:
    connection = mysql.connector.connect(host='localhost',database='boomerang', user='root', password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
"""
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
"""

# The code for login access of users
def click():
    username = textentry1.get()
    password = textentry2.get()
    print("Username= "+username)
    print("Password= "+password)
    mycursor = connection.cursor(buffered=True)
    finduser = ("SELECT * FROM login WHERE Username = %s AND Password= %s")
    mycursor.execute(finduser,[(username),(password)])
    results = mycursor.fetchall()
    connection.commit()
    if results:
        # Label(window, text="Login Successful", bg="white", fg="Red", font="times_new_roman 16").place(x=118, y=160)
        print("Connected")
        mainpart()
    else:
        Label(window, text="Invalid Username/Password", bg="white"
              , fg="Red", font="times_new_roman 10").place(x=180, y=202)
        print("Invalid Username or Password")

# What exit button does
def close_window():
    exit()

# This variable will be used for total amount to be paid (Trip + Hotel)
pay_total = 0
# This variable is used so a user cannot book more than one premium suite
pay_hotel = 0

# The central frame for whole app
def mainpart():

    mainframe = Tk()
    C = Canvas(mainframe, bg="blue", height=250, width=300)
    filename = PhotoImage(master=mainframe,file="specificbk.png")
    background_label = Label(mainframe, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    mainframe.title("Boomerang")
    mainframe.resizable(0, 0)

    def callback(url):
        webbrowser.open_new(url)

    # labels
    Label(mainframe, text="Please select an option", fg="black",bg="white",font="times_new_roman 14").place(x=151,y=140)
    link1 = Label(mainframe, text="or Try our website", fg="blue", font="times_new_roman 12",cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://roadtrippers.com/"))
    link1.place(x=189, y=170)
    Label(mainframe, text="Welcome ", bg="white", fg="Black", font="times_new_roman 16 bold").place(x=210, y=75)
    Label(mainframe, text=textentry1.get(), bg="white", fg="Black", font="times_new_roman 14 italic").place(x=320, y=75)

    # For Trip Packages

    def Trip_Packages():

        pack = Tk()
        pack.title("Boomerang")
        filename2 = PhotoImage(master=pack, file="trip_pack_a.png")
        background_label2 = Label(pack, image=filename2)
        background_label2.place(x=0, y=0, relwidth=1, relheight=1)
        # pack.configure(background="white")
        pack.resizable(0, 0)
        mainframe.withdraw()

        def actual_payment_portal():
            global pay_total
            print(pay_total)
            mainframe.withdraw()
            pay = Tk()
            pay.title("Boomerang")
            filename_south = PhotoImage(master=pay, file="actual_payments.png")
            background_label_south = Label(pay, image=filename_south)
            background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

            def add_hotel_cost():
                global pay_total
                global pay_hotel
                pay_hotel += 0
                if (pay_hotel==0):
                    pay_total = pay_total + 25000
                    pay_hotel+=1
                    pay.withdraw()
                    actual_payment_portal()
                else:
                    Label(pay, text="You can't book more than 1 suite (per person)", bg="white", fg="black", font="times_new_roman 9").place(x=118, y=347)

            def final_payment():
                pay.withdraw()
                final_pay = Tk()
                final_pay.title("Boomerang")
                filename_final_pay = PhotoImage(master=final_pay, file="final_payment.png")
                background_label_final_pay = Label(final_pay, image=filename_final_pay)
                background_label_final_pay.place(x=0, y=0, relwidth=1, relheight=1)

                def pay_back_final():
                    global pay_total
                    pay_total = 0
                    mainframe.deiconify()
                    final_pay.withdraw()

                textentry_card = Entry(final_pay, width=20, bg="white")
                textentry_card.place(x=60, y=150)
                textentry_email = Entry(final_pay, width=20, bg="white")
                textentry_email.place(x=270, y=150)
                textentry_num1 = Entry(final_pay, width=10, bg="white")
                textentry_num1.place(x=60, y=225)
                textentry_num2 = Entry(final_pay, width=10, bg="white")
                textentry_num2.place(x=130, y=225)
                textentry_num3 = Entry(final_pay, width=10, bg="white")
                textentry_num3.place(x=200, y=225)
                textentry_num4 = Entry(final_pay, width=10, bg="white")
                textentry_num4.place(x=270, y=225)
                textentry_exp_month = Entry(final_pay, width=10, bg="white")
                textentry_exp_month.place(x=60, y=305)
                textentry_exp_year = Entry(final_pay, width=10, bg="white")
                textentry_exp_year.place(x=130, y=305)
                textentry_cvv = Entry(final_pay, width=20, bg="white")
                textentry_cvv.place(x=60, y=385)

                def paid():

                    if ((int(textentry_num1.get()) > 9999 or len(textentry_num1.get()) < 4)):
                        print("Invalid card number")
                        final_pay.withdraw()
                        final_payment()
                    elif(len(textentry_email.get()) <= 0):
                        print("Invalid Emai ID")
                        final_pay.withdraw()
                        final_payment()
                    elif ((int(textentry_num2.get()) > 9999 or len(textentry_num2.get()) < 4)):
                        print("Invalid card number")
                        final_pay.withdraw()
                        final_payment()

                    elif ((int(textentry_num3.get()) > 9999 or len(textentry_num3.get()) < 4)):
                        print("Invalid card number")
                        final_pay.withdraw()
                        final_payment()

                    elif ((int(textentry_num4.get()) > 9999 or len(textentry_num4.get()) < 4)):
                        print("Invalid card number")
                        final_pay.withdraw()
                        final_payment()

                    elif (len(textentry_cvv.get()) != 3):
                        print("Invalid cvv")
                        final_pay.withdraw()
                        final_payment()

                    elif (textentry_card == ""):
                        print("invalid name")
                        final_pay.withdraw()
                        final_payment()

                    elif (int(textentry_exp_month.get()) > 12 or int(textentry_exp_month.get()) < 1):
                        print("Invalid month")
                        final_pay.withdraw()
                        final_payment()

                    elif (int(textentry_exp_year.get()) < 2020):
                        print("Invalid year")
                        final_pay.withdraw()
                        final_payment()

                    else:
                        card = textentry_card.get()

                        print(str(textentry_email.get()))
                        mycursor5 = connection.cursor(buffered=True)
                        insertusers = ("INSERT INTO payments (name,amount) VALUES (%s,%s)")
                        mycursor5.execute(insertusers, [(card), (pay_total)])
                        connection.commit()
                        sender = 'noreplymailboomerang@gmail.com'
                        receivers = ['']
                        receivers.append(str(textentry_email.get()))
                        print(receivers)
                        message = """From: Boomerang <noreplymailboomerang@gmail.com>
                        To: To Person
                        MIME-Version: 1.0
                        Content-type: text/html
                        Subject: Payment Successful

                        Your payment has been successful and approved
                        By Boomerang Tour and Travels
                        """

                        try:
                            smtpObj = smtplib.SMTP('smtp.gmail.com:587')
                            smtpObj.ehlo()
                            smtpObj.starttls()
                            smtpObj.login('yor mail id @ anymail.com goes here', 'your password goes here')
                            smtpObj.sendmail(sender, receivers, message)
                            print("Successfully sent email")
                        except smtplib.SMTPException:
                            print("Error: unable to send email")
                        webbrowser.open_new("https://roadtrippers.com/")
                        final_pay.withdraw()
                        mainpart()

                Button(final_pay, text="<< Back", width=6, command=pay_back_final).place(x=12, y=415)
                Button(final_pay, text="Pay", width=6, command=paid).place(x=222, y=415)
                Button(final_pay, text="Exit", width=6, command=close_window).place(x=435, y=415)

                final_pay.resizable(0, 0)
                final_pay.geometry("500x450+10+10")
                final_pay.mainloop()

            def pay_back():
                mainframe.deiconify()
                pay.withdraw()

            Label(pay, text="Amount:", bg="white", fg="red", font="times_new_roman 12").place(x=174, y=327)
            pay_str = str(pay_total)
            Label(pay, text="₹ "+pay_str, bg="white", fg="Black", font="times_new_roman 12").place(x=250, y=327)
            Button(pay, text="Add Premium Suite", width=15, bg="white", fg="Blue", borderwidth=0,
                   command=add_hotel_cost).place(x=196, y=375)
            Button(pay, text="<< Back", width=6, command=pay_back).place(x=12, y=415)
            Button(pay, text="Pay Now", width=6, command=final_payment).place(x=435, y=415)
            pay.resizable(0, 0)
            pay.geometry("500x450+10+10")
            pay.mainloop()

        def pack_back():
            mainframe.deiconify()
            pack.withdraw()

        def europe():
            pack.withdraw()
            pack2 = Tk()
            pack2.title("Boomerang")
            filenameA = PhotoImage(master=pack2, file="trip_pack_b.png")
            background_labelA = Label(pack2, image=filenameA)
            background_labelA.place(x=0, y=0, relwidth=1, relheight=1)
            pack2.resizable(0, 0)

            def america():
                pack2.withdraw()
                pack3 = Tk()
                pack3.title("Boomerang")
                filename3 = PhotoImage(master=pack3, file="trip_pack_c.png")
                background_label3 = Label(pack3, image=filename3)
                background_label3.place(x=0, y=0, relwidth=1, relheight=1)
                pack3.resizable(0, 0)

                def asia():
                    pack3.withdraw()
                    Trip_Packages()

                def explore_north():
                    pack3.withdraw()
                    pack_north = Tk()
                    pack_north.title("Boomerang")
                    filename_north = PhotoImage(master=pack_north, file="destination_north.png")
                    background_label_north = Label(pack_north, image=filename_north)
                    background_label_north.place(x=0, y=0, relwidth=1, relheight=1)

                    def pay_tripA():
                        pack_north.withdraw()
                        pack_south = Tk()
                        pack_south.title("Boomerang")
                        filename_south = PhotoImage(master=pack_south, file="specificbk - USA.png")
                        background_label_south = Label(pack_south, image=filename_south)
                        background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                        def money_pay():
                            global pay_total
                            pay_total = 159720
                            pack_south.withdraw()
                            actual_payment_portal()

                        def pay_A():
                            pack_south.withdraw()
                            america()

                        Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                        Button(pack_south, text="<< Back", width=6, command=pay_A).place(x=12, y=415)
                        pack_south.resizable(0, 0)
                        pack_south.geometry("500x450+10+10")
                        pack_south.mainloop()

                    def pay_tripB():
                        pack_north.withdraw()
                        pack_south = Tk()
                        pack_south.title("Boomerang")
                        filename_south = PhotoImage(master=pack_south, file="specificbk - Canada.png")
                        background_label_south = Label(pack_south, image=filename_south)
                        background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                        def money_pay():
                            global pay_total
                            pay_total = 167990
                            pack_south.withdraw()
                            actual_payment_portal()

                        def pay_B():
                            pack_south.withdraw()
                            america()

                        Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                        Button(pack_south, text="<< Back", width=6, command=pay_B).place(x=12, y=415)
                        pack_south.resizable(0, 0)
                        pack_south.geometry("500x450+10+10")
                        pack_south.mainloop()

                    def pay_tripC():
                        pack_north.withdraw()
                        pack_south = Tk()
                        pack_south.title("Boomerang")
                        filename_south = PhotoImage(master=pack_south, file="specificbk - Caribbean.png")
                        background_label_south = Label(pack_south, image=filename_south)
                        background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                        def money_pay():
                            global pay_total
                            pay_total = 130999
                            pack_south.withdraw()
                            actual_payment_portal()

                        def pay_C():
                            pack_south.withdraw()
                            america()

                        Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                        Button(pack_south, text="<< Back", width=6, command=pay_C).place(x=12, y=415)
                        pack_south.resizable(0, 0)
                        pack_south.geometry("500x450+10+10")
                        pack_south.mainloop()
                    Button(pack_north, text="USA (11 Days, 11 Nights)", width=20, bg="white",
                           font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripA).place(x=200, y=35)
                    Button(pack_north, text="Canada (15 Days, 14 Nights)", width=20, bg="white",
                           font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripB).place(x=68, y=176)
                    Button(pack_north, text="Caribbean (12 Days, 11 Nights)", width=23, bg="white",
                           font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripC).place(x=204, y=330)
                    pack_north.resizable(0, 0)
                    pack_north.geometry("500x450+10+10")
                    pack_north.mainloop()

                def explore_south():
                    pack3.withdraw()
                    pack_south = Tk()
                    pack_south.title("Boomerang")
                    filename_south = PhotoImage(master=pack_south, file="destination_south.png")
                    background_label_south = Label(pack_south, image=filename_south)
                    background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                    def pay_tripA():
                        pack_south.withdraw()
                        pack_southern = Tk()
                        pack_southern.title("Boomerang")
                        filename_southern = PhotoImage(master=pack_southern, file="specificbk - Peru.png")
                        background_label_south = Label(pack_southern, image=filename_southern)
                        background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                        def money_pay():
                            global pay_total
                            pay_total = 115099
                            pack_south.withdraw()
                            actual_payment_portal()

                        def pay_A():
                            pack_southern.withdraw()
                            america()

                        Button(pack_southern, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                        Button(pack_southern, text="<< Back", width=6, command=pay_A).place(x=12, y=415)
                        pack_southern.resizable(0, 0)
                        pack_southern.geometry("500x450+10+10")
                        pack_southern.mainloop()

                    def pay_tripB():
                        pack_south.withdraw()
                        pack_southern = Tk()
                        pack_southern.title("Boomerang")
                        filename_southern = PhotoImage(master=pack_southern, file="specificbk - Brazil.png")
                        background_label_southern = Label(pack_southern, image=filename_southern)
                        background_label_southern.place(x=0, y=0, relwidth=1, relheight=1)

                        def money_pay():
                            global pay_total
                            pay_total = 111099
                            pack_south.withdraw()
                            actual_payment_portal()

                        def pay_B():
                            pack_southern.withdraw()
                            america()

                        Button(pack_southern, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                        Button(pack_southern, text="<< Back", width=6, command=pay_B).place(x=12, y=415)
                        pack_southern.resizable(0, 0)
                        pack_southern.geometry("500x450+10+10")
                        pack_southern.mainloop()

                    def pay_tripC():
                        pack_south.withdraw()
                        pack_southern = Tk()
                        pack_southern.title("Boomerang")
                        filename_southern = PhotoImage(master=pack_southern, file="specificbk - Easter Island.png")
                        background_label_southern = Label(pack_southern, image=filename_southern)
                        background_label_southern.place(x=0, y=0, relwidth=1, relheight=1)

                        def money_pay():
                            global pay_total
                            pay_total = 120550
                            pack_south.withdraw()
                            actual_payment_portal()

                        def pay_C():
                            pack_southern.withdraw()
                            america()

                        Button(pack_southern, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                        Button(pack_southern, text="<< Back", width=6, command=pay_C).place(x=12, y=415)
                        pack_southern.resizable(0, 0)
                        pack_southern.geometry("500x450+10+10")
                        pack_southern.mainloop()

                    Button(pack_south, text="Peru (7 Days, 6 Nights)", width=26, bg="white",
                           font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripA).place(x=170, y=45)
                    Button(pack_south, text="Brazil (9 Days, 9 Nights)", width=20, bg="white",
                           font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripB).place(x=51, y=180)
                    Button(pack_south, text="Easter Island (7 Days, 6 Nights)", width=26, bg="white",
                           font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripC).place(x=179, y=332)

                    pack_south.resizable(0, 0)
                    pack_south.geometry("500x450+10+10")
                    pack_south.mainloop()

                # Button(pack3, text="<< Back", width=6, command=pack_back).place(x=12, y=415)
                Button(pack3, text="Explore More", width=10, bg="white", fg="Blue", borderwidth=0, command=explore_north).place(x=35, y=215)
                Button(pack3, text="Explore More", width=10, bg="white", fg="Blue", borderwidth=0, command=explore_south).place(x=187, y=390)
                Button(pack3, text="Next >>", width=6, command=asia).place(x=435, y=415)
                pack3.geometry("500x450+10+10")
                pack3.mainloop()

            def explore_europe():
                pack2.withdraw()
                pack_europe = Tk()
                pack_europe.title("Boomerang")
                filename_europe = PhotoImage(master=pack_europe, file="destination_europe.png")
                background_label_europe = Label(pack_europe, image=filename_europe)
                background_label_europe.place(x=0, y=0, relwidth=1, relheight=1)

                def pay_tripA():
                    pack_europe.withdraw()
                    pack_south = Tk()
                    pack_south.title("Boomerang")
                    filename_south = PhotoImage(master=pack_south, file="specificbk - Europe.png")
                    background_label_south = Label(pack_south, image=filename_south)
                    background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                    def money_pay():
                        global pay_total
                        pay_total = 124990
                        pack_south.withdraw()
                        actual_payment_portal()

                    def pay_A():
                        pack_south.withdraw()
                        europe()

                    Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                    Button(pack_south, text="<< Back", width=6, command=pay_A).place(x=12, y=415)
                    pack_south.resizable(0, 0)
                    pack_south.geometry("500x450+10+10")
                    pack_south.mainloop()

                def pay_tripB():
                    pack_europe.withdraw()
                    pack_south = Tk()
                    pack_south.title("Boomerang")
                    filename_south = PhotoImage(master=pack_south, file="specificbk - Russia.png")
                    background_label_south = Label(pack_south, image=filename_south)
                    background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                    def money_pay():
                        global pay_total
                        pay_total = 900599
                        pack_south.withdraw()
                        actual_payment_portal()

                    def pay_B():
                        pack_south.withdraw()
                        europe()

                    Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                    Button(pack_south, text="<< Back", width=6, command=pay_B).place(x=12, y=415)
                    pack_south.resizable(0, 0)
                    pack_south.geometry("500x450+10+10")
                    pack_south.mainloop()

                def pay_tripC():
                    pack_europe.withdraw()
                    pack_south = Tk()
                    pack_south.title("Boomerang")
                    filename_south = PhotoImage(master=pack_south, file="specificbk - Scandinavia.png")
                    background_label_south = Label(pack_south, image=filename_south)
                    background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                    def money_pay():
                        global pay_total
                        pay_total = 150999
                        pack_south.withdraw()
                        actual_payment_portal()

                    def pay_C():
                        pack_south.withdraw()
                        europe()

                    Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                    Button(pack_south, text="<< Back", width=6, command=pay_C).place(x=12, y=415)
                    pack_south.resizable(0, 0)
                    pack_south.geometry("500x450+10+10")
                    pack_south.mainloop()

                Button(pack_europe, text="Europe (9 Days, 8 Nights)", width=20, bg="white",
                       font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripA).place(x=184, y=37)
                Button(pack_europe, text="Russia (10 Days, 9 Nights)", width=20, bg="white",
                       font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripB).place(x=66, y=177)
                Button(pack_europe, text="Scandinavia (9 Days, 9 Nights)", width=22, bg="white",
                       font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripC).place(x=181, y=330)
                pack_europe.resizable(0, 0)
                pack_europe.geometry("500x450+10+10")
                pack_europe.mainloop()

            def explore_africa():
                pack2.withdraw()
                pack_africa = Tk()
                pack_africa.title("Boomerang")
                filename_africa = PhotoImage(master=pack_africa, file="destination_africa.png")
                background_label_africa = Label(pack_africa, image=filename_africa)
                background_label_africa.place(x=0, y=0, relwidth=1, relheight=1)

                def pay_tripA():
                    pack_africa.withdraw()
                    pack_south = Tk()
                    pack_south.title("Boomerang")
                    filename_south = PhotoImage(master=pack_south, file="specificbk - Egpyt.png")
                    background_label_south = Label(pack_south, image=filename_south)
                    background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                    def money_pay():
                        global pay_total
                        pay_total = 90550
                        pack_south.withdraw()
                        actual_payment_portal()

                    def pay_A():
                        pack_south.withdraw()
                        europe()

                    Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                    Button(pack_south, text="<< Back", width=6, command=pay_A).place(x=12, y=415)
                    pack_south.resizable(0, 0)
                    pack_south.geometry("500x450+10+10")
                    pack_south.mainloop()

                def pay_tripB():
                    pack_africa.withdraw()
                    pack_south = Tk()
                    pack_south.title("Boomerang")
                    filename_south = PhotoImage(master=pack_south, file="specificbk - Tanzania.png")
                    background_label_south = Label(pack_south, image=filename_south)
                    background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                    def money_pay():
                        global pay_total
                        pay_total = 135099
                        pack_south.withdraw()
                        actual_payment_portal()

                    def pay_B():
                        pack_south.withdraw()
                        europe()

                    Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                    Button(pack_south, text="<< Back", width=6, command=pay_B).place(x=12, y=415)
                    pack_south.resizable(0, 0)
                    pack_south.geometry("500x450+10+10")
                    pack_south.mainloop()

                def pay_tripC():
                    pack_africa.withdraw()
                    pack_south = Tk()
                    pack_south.title("Boomerang")
                    filename_south = PhotoImage(master=pack_south, file="specificbk - South Africa.png")
                    background_label_south = Label(pack_south, image=filename_south)
                    background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                    def money_pay():
                        global pay_total
                        pay_total = 120990
                        pack_south.withdraw()
                        actual_payment_portal()

                    def pay_C():
                        pack_south.withdraw()
                        europe()

                    Button(pack_south, text="Pay Now", font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                    Button(pack_south, text="<< Back", width=6, command=pay_C).place(x=12, y=415)
                    pack_south.resizable(0, 0)
                    pack_south.geometry("500x450+10+10")
                    pack_south.mainloop()

                Button(pack_africa, text="Egypt (8 Days, 8 Nights)", width=25, bg="white",
                       font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripA).place(x=169, y=45)
                Button(pack_africa, text="Tanzania (6 Days, 6 Nights)", width=20, bg="white",
                       font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripB).place(x=64, y=175)
                Button(pack_africa, text="South Africa (9 Days, 8 Nights)", width=25, bg="white",
                       font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripC).place(x=201, y=335)
                pack_africa.resizable(0, 0)
                pack_africa.geometry("500x450+10+10")
                pack_africa.mainloop()

            # Button(pack2, text="<< Back", width=6, command=pack_back).place(x=12, y=415)
            Button(pack2, text="Next >>", width=6, command=america).place(x=435, y=415)
            Button(pack2, text="Explore More", width=10, bg="white", fg="Blue", borderwidth=0, command=explore_europe).place(x=34, y=205)
            Button(pack2, text="Explore More", width=10, bg="white", fg="Blue", borderwidth=0, command=explore_africa).place(x=162, y=390)
            pack2.geometry("500x450+10+10")
            pack2.mainloop()

        def explore_asia():
            pack.withdraw()
            pack_asia = Tk()
            pack_asia.title("Boomerang")
            filename_asia = PhotoImage(master=pack_asia, file="destination_asia.png")
            background_label_asia = Label(pack_asia, image=filename_asia)
            background_label_asia.place(x=0, y=0, relwidth=1, relheight=1)

            def pay_tripA():
                pack_asia.withdraw()
                pack_south = Tk()
                pack_south.title("Boomerang")
                filename_south = PhotoImage(master=pack_south, file="specificbk - Japan-Korea.png")
                background_label_south = Label(pack_south, image=filename_south)
                background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                def money_pay():
                    global pay_total
                    pay_total = 136000
                    pack_south.withdraw()
                    actual_payment_portal()

                def pay_A():
                    pack_south.withdraw()
                    Trip_Packages()
                Button(pack_south, text="Pay Now",font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                Button(pack_south, text="<< Back", width=6, command=pay_A).place(x=12, y=415)
                pack_south.resizable(0, 0)
                pack_south.geometry("500x450+10+10")
                pack_south.mainloop()

            def pay_tripB():
                pack_asia.withdraw()
                pack_south = Tk()
                pack_south.title("Boomerang")
                filename_south = PhotoImage(master=pack_south, file="specificbk - India.png")
                background_label_south = Label(pack_south, image=filename_south)
                background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                def money_pay():
                    global pay_total
                    pay_total = 40599
                    pack_south.withdraw()
                    actual_payment_portal()

                def pay_B():
                    pack_south.withdraw()
                    Trip_Packages()
                Button(pack_south, text="Pay Now",font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                Button(pack_south, text="<< Back", width=6, command=pay_B).place(x=12, y=415)
                pack_south.resizable(0, 0)
                pack_south.geometry("500x450+10+10")
                pack_south.mainloop()

            def pay_tripC():
                pack_asia.withdraw()
                pack_south = Tk()
                pack_south.title("Boomerang")
                filename_south = PhotoImage(master=pack_south, file="specificbk - Singapore-Malaysia.png")
                background_label_south = Label(pack_south, image=filename_south)
                background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                def money_pay():
                    global pay_total
                    pay_total = 69999
                    pack_south.withdraw()
                    actual_payment_portal()

                def pay_C():
                    pack_south.withdraw()
                    Trip_Packages()
                Button(pack_south, text="Pay Now",font="times_new_roman 9", width=6, command=money_pay).place(x=435, y=415)
                Button(pack_south, text="<< Back", width=6, command=pay_C).place(x=12, y=415)
                pack_south.resizable(0, 0)
                pack_south.geometry("500x450+10+10")
                pack_south.mainloop()

            Button(pack_asia, text="Japan-Korea (9 Days, 8 Nights)", width=30, bg="white",
                   font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripA).place(x=162, y=45)
            Button(pack_asia, text="India (10 Days, 9 Nights)", width=20, bg="white",
                   font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripB).place(x=54, y=180)
            Button(pack_asia, text="Singapore-Malaysia (9 Days, 9 Nights)", width=30, bg="white",
                   font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripC).place(x=182, y=335)
            pack_asia.resizable(0, 0)
            pack_asia.geometry("500x450+10+10")
            pack_asia.mainloop()

        def explore_oceania():
            pack.withdraw()
            pack_oceania = Tk()
            pack_oceania.title("Boomerang")
            filename_oceania = PhotoImage(master=pack_oceania, file="destination_australia.png")
            background_label_oceania = Label(pack_oceania, image=filename_oceania)
            background_label_oceania.place(x=0, y=0, relwidth=1, relheight=1)

            def pay_tripA():
                pack_oceania.withdraw()
                pack_south = Tk()
                pack_south.title("Boomerang")
                filename_south = PhotoImage(master=pack_south, file="specificbk - Australia.png")
                background_label_south = Label(pack_south, image=filename_south)
                background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                def money_pay():
                    global pay_total
                    pay_total = 108990
                    pack_south.withdraw()
                    actual_payment_portal()

                def pay_A():
                    pack_south.withdraw()
                    Trip_Packages()
                Button(pack_south, text="Pay Now",font="times_new_roman 9", width=6, command = money_pay).place(x=435, y=415)
                Button(pack_south, text="<< Back", width=6, command=pay_A).place(x=12, y=415)
                pack_south.resizable(0, 0)
                pack_south.geometry("500x450+10+10")
                pack_south.mainloop()

            def pay_tripB():
                pack_oceania.withdraw()
                pack_south = Tk()
                pack_south.title("Boomerang")
                filename_south = PhotoImage(master=pack_south, file="specificbk - New Zealand.png")
                background_label_south = Label(pack_south, image=filename_south)
                background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                def money_pay():
                    global pay_total
                    pay_total = 98990
                    pack_south.withdraw()
                    actual_payment_portal()

                def pay_B():
                    pack_south.withdraw()
                    Trip_Packages()

                Button(pack_south, text="Pay Now",font="times_new_roman 9", width=6, command = money_pay).place(x=435, y=415)
                Button(pack_south, text="<< Back", width=6, command=pay_B).place(x=12, y=415)
                pack_south.resizable(0, 0)
                pack_south.geometry("500x450+10+10")
                pack_south.mainloop()

            def pay_tripC():
                pack_oceania.withdraw()
                pack_south = Tk()
                pack_south.title("Boomerang")
                filename_south = PhotoImage(master=pack_south, file="specificbk - Fiji.png")
                background_label_south = Label(pack_south, image=filename_south)
                background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

                def money_pay():
                    global pay_total
                    pay_total = 110090
                    pack_south.withdraw()
                    actual_payment_portal()

                def pay_C():
                    pack_south.withdraw()
                    Trip_Packages()
                Button(pack_south, text="Pay Now",font="times_new_roman 9", width=6, command = money_pay).place(x=435, y=415)
                Button(pack_south, text="<< Back", width=6, command=pay_C).place(x=12, y=415)
                pack_south.resizable(0, 0)
                pack_south.geometry("500x450+10+10")
                pack_south.mainloop()

            Button(pack_oceania, text="Australia (12 Days, 11 Nights)", width=30, bg="white",
                   font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripA).place(x=159, y=45)
            Button(pack_oceania, text="New Zealand (10 Days, 10 Nights)", width=25, bg="white",
                   font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripB).place(x=63, y=177)
            Button(pack_oceania, text="Fiji (9 Days, 8 Nights)", width=16, bg="white",
                   font="times_new_roman 10 underline", fg="Blue", borderwidth=0, command=pay_tripC).place(x=190, y=335)
            pack_oceania.resizable(0, 0)
            pack_oceania.geometry("500x450+10+10")
            pack_oceania.mainloop()

        # button
        Button(pack, text="Explore More", width=10, bg="white", fg="Blue", borderwidth=0, command=explore_asia).place(x=32, y=205)
        Button(pack, text="Explore More", width=10, bg="white", fg="Blue", borderwidth=0, command=explore_oceania).place(x=204, y=390)
        Button(pack, text="<< Back", width=6, command=pack_back).place(x=12, y=415)
        Button(pack, text="Next >>", width=6, command=europe).place(x=435, y=415)

        # run main loop
        pack.geometry("500x450+10+10")
        pack.mainloop()

    # End of Trip Module

    def tag_search():

        search = Tk()
        search.title("Boomerang")
        search.configure(background="white")
        search.resizable(0, 0)
        mainframe.withdraw()
        # image
        filename5 = PhotoImage(master=search, file="tag_search.png")
        background_label5 = Label(search, image=filename5)
        background_label5.place(x=0, y=0, relwidth=1, relheight=1)

        # text box
        textentryA1 = Entry(search, width=20, bg="white")
        textentryA1.place(x=95, y=225)

        textentryA2 = Entry(search, width=20, bg="white")
        textentryA2.place(x=342, y=225)

        textentryA3 = Entry(search, width=20, bg="white")
        textentryA3.place(x=95, y=275)

        textentryA4 = Entry(search, width=20, bg="white")
        textentryA4.place(x=342, y=275)

        textentryA5 = Entry(search, width=20, bg="white")
        textentryA5.place(x=95, y=325)

        textentryA6 = Entry(search, width=20, bg="white")
        textentryA6.place(x=342, y=325)

        def search_work():
            myconnect = connection.cursor(buffered=True)
            findloc = ("SELECT Country, Count(*) FROM locationsearch WHERE Tags LIKE %s LIMIT 1")

            tag1 = textentryA1.get()
            tag2 = textentryA2.get()
            tag3 = textentryA3.get()
            tag4 = textentryA4.get()
            tag5 = textentryA5.get()
            tag6 = textentryA6.get()

            if (tag1 == "" or tag2=="" or tag3=="" or tag4=="" or tag5=="" or tag6==""):
                Label(search, text="Enter valid tags or NULL", bg="white", fg="red", font="times_new_roman 10 ").place(x=180, y=350)

            else:
                # 1
                myconnect.execute(findloc, [("%"+tag1+"%")])
                result1 = myconnect.fetchall()
                for i in result1:
                    j1 = i[1]
                # 2
                myconnect.execute(findloc, [("%"+tag2+"%")])
                result2 = myconnect.fetchall()
                for i in result2:
                    j2 = i[1]
                # 3
                myconnect.execute(findloc, [("%"+tag3+"%")])
                result3 = myconnect.fetchall()
                for i in result3:
                    j3 = i[1]
                # 4
                myconnect.execute(findloc, [("%"+tag4+"%")])
                result4 = myconnect.fetchall()
                for i in result4:
                    j4 = i[1]
                # 5
                myconnect.execute(findloc, [("%"+tag5+"%")])
                result5 = myconnect.fetchall()
                for i in result5:
                    j5 = i[1]
                # 6
                myconnect.execute(findloc, [("%"+tag6+"%")])
                result6 = myconnect.fetchall()
                for i in result6:
                    j6 = i[1]

                print(j1,j2,j3,j4,j5,j6)
                connection.commit()

                j = j1+j2+j3+j4+j5+j6
                print("Score", j)
                if (j) == 6:
                    for i in result1:
                        print("Locaton is:", i[0])
                        loc_print = str(i[0])
                        Label(search, text="Location Recommended:  "+loc_print, bg="white", fg="#d966ff",
                              font="times_new_roman 10 ").place(x=170, y=180)
                        link5 = Label(search, text="Check out this place here", fg="blue", font="times_new_roman 10",
                                      cursor="hand2")
                        link5.pack()
                        link5.bind("<Button-1>", lambda e: callback("https://roadtrippers.com/"))
                        link5.place(x=184, y=200)
                elif (j) >= 5:
                    for i in result1:
                        print("Location is:",i[0])
                        loc_print = str(i[0])
                        Label(search, text="Location Recommended:  "+loc_print, bg="white", fg="#d966ff",
                              font="times_new_roman 10 ").place(x=170, y=180)
                        link5 = Label(search, text="Check out this place here", fg="blue", font="times_new_roman 10",
                                      cursor="hand2")
                        link5.pack()
                        link5.bind("<Button-1>", lambda e: callback("https://roadtrippers.com/"))
                        link5.place(x=184, y=200)
                elif (j) >= 4:
                    for i in result1:
                        print("Location is:",i[0])
                        loc_print = str(i[0])
                        Label(search, text="Location Recommended:  "+loc_print, bg="white", fg="#d966ff",
                              font="times_new_roman 10 ").place(x=170, y=180)
                        link5 = Label(search, text="Check out this place here", fg="blue", font="times_new_roman 10",
                                      cursor="hand2")
                        link5.pack()
                        link5.bind("<Button-1>", lambda e: callback("https://roadtrippers.com/"))
                        link5.place(x=184, y=200)
                elif (j) >= 3:
                    for i in result1:
                        print("Location is:",i[0])
                        loc_print = str(i[0])
                        Label(search, text="Location Recommended:  "+loc_print, bg="white", fg="#d966ff",
                              font="times_new_roman 10 ").place(x=170, y=180)
                        link5 = Label(search, text="Check out this place here", fg="blue", font="times_new_roman 10",
                                      cursor="hand2")
                        link5.pack()
                        link5.bind("<Button-1>", lambda e: callback("https://roadtrippers.com/"))
                        link5.place(x=184, y=200)

                else:
                    Label(search, text="Please enter some other tags", bg="white", fg="red",
                          font="times_new_roman 10 ").place(x=180, y=350)

        def recommend_back():
            mainframe.deiconify()
            search.withdraw()

        # button
        Button(search, text="Search", width=6, command=search_work).place(x=223, y=375)
        Button(search, text="<< Back", width=6, command=recommend_back).place(x=12, y=415)
        Button(search, text="Exit", width=6, command=close_window).place(x=435, y=415)

        # run main loop
        search.geometry("500x450+10+10")
        search.mainloop()

    def hotel_book():
        mainframe.withdraw()
        hotel = Tk()
        hotel.title("Boomerang")
        hotel_bg = PhotoImage(master=hotel, file="hotel_bk.png")
        hotel_label = Label(hotel, image=hotel_bg)
        hotel_label.place(x=0, y=0, relwidth=1, relheight=1)

        def hotel_back():
            mainframe.deiconify()
            hotel.withdraw()

        Button(hotel, text="<< Back", width=6, command=hotel_back).place(x=12, y=415)
        Button(hotel, text="Post", width=6).place(x=435, y=415)
        hotel.resizable(0, 0)
        hotel.geometry("500x450+10+10")
        hotel.mainloop()

    def settings():

        sett = Tk()
        sett.title("Boomerang")
        sett.configure(background="white")
        sett.resizable(0, 0)
        mainframe.withdraw()
        # image
        photoA1 = PhotoImage(master=sett, file="settings.png")
        setting_label = Label(sett, image=photoA1)
        setting_label.place(x=0, y=0, relwidth=1, relheight=1)

        def setting_pass_work():
            username = textentryA.get()
            new_pass = textentryB.get()
            mycursor = connection.cursor(buffered=True)

            sql = "UPDATE login SET Password = %s WHERE Username = %s"
            mycursor.execute(sql, [(new_pass),(username)])
            connection.commit()
            print("Record Updated")

        def setting_user_work():
            password = textentryC.get()
            new_name = textentryD.get()
            mycursor = connection.cursor(buffered=True)

            sqli = "UPDATE login SET Username = %s WHERE Password = %s"
            mycursor.execute(sqli, [(new_name),(password)])
            connection.commit()
            print("Record Updated")

        # text box
        Button(sett, text="Change", width=6, bg="white",fg="red", borderwidth=0, command=setting_pass_work).place(x=30, y=209)

        textentryA = Entry(sett, width=15, bg="white")
        textentryA.place(x=121, y=247)

        textentryB = Entry(sett, width=15, bg="white")
        textentryB.place(x=375, y=247)

        Button(sett, text="Change", width=6, bg="white",fg="red", borderwidth=0, command=setting_user_work).place(x=30, y=309)

        textentryC = Entry(sett, width=15, bg="white")
        textentryC.place(x=121, y=347)

        textentryD = Entry(sett, width=15, bg="white")
        textentryD.place(x=375, y=347)

        def setting_back():
            mainframe.deiconify()
            sett.withdraw()

        Button(sett, text="<< Back", width=6, command=setting_back).place(x=12, y=415)
        Button(sett, text="Exit", width=6, command=close_window).place(x=435, y=415)
        # run main loop
        sett.geometry("500x450+10+10")
        sett.mainloop()

    # Module for payment options visual purpose
    def payment_options():
        mainframe.withdraw()
        pay = Tk()
        pay.title("Boomerang")
        filename_south = PhotoImage(master=pay, file="payments.png")
        background_label_south = Label(pay, image=filename_south)
        background_label_south.place(x=0, y=0, relwidth=1, relheight=1)

        def pay_back():
            mainframe.deiconify()
            pay.withdraw()

        Button(pay, text="<< Back", width=6, command=pay_back).place(x=12, y=415)
        pay.resizable(0, 0)
        pay.geometry("500x450+10+10")
        pay.mainloop()

    # function for user complaints. Goes to website
    def complaints():
        mainframe.withdraw()
        complain = Tk()
        complain.title("Boomerang")
        complain_bg = PhotoImage(master=complain, file="complaints.png")
        complain_label = Label(complain, image=complain_bg)
        complain_label.place(x=0, y=0, relwidth=1, relheight=1)

        textentryName = Entry(complain, width=40, bg="white")
        Label(complain, text="Name", bg="white", fg="Black", font="times_new_roman 12").place(x=23, y=247)
        textentryName.place(x=111, y=245)

        textentryEmail = Entry(complain, width=40, bg="white")
        Label(complain, text="Email", bg="white", fg="Black", font="times_new_roman 12").place(x=23, y=297)
        textentryEmail.place(x=111, y=295)

        textentryMessage = Text(complain, height=4, width=30, bg="white")
        Label(complain, text="Message", bg="white", fg="Black", font="times_new_roman 12").place(x=23, y=347)
        textentryMessage.place(x=111, y=345)

        def complaint_post():
            name = textentryName.get()
            email = textentryEmail.get()
            # This is how we get entry from Text type
            message = textentryMessage.get("1.0",END)

            if (name == "" or email == ""):
                print("Invalid name/email")
            else:
                mycursor = connection.cursor(buffered=True)
                insertuser = ("INSERT INTO complaint (name,email,message) VALUES (%s,%s,%s)")
                mycursor.execute(insertuser, [(name), (email),(message)])
                connection.commit()
                callbackC()

        def complain_back():
            mainframe.deiconify()
            complain.withdraw()

        def callbackC():
            webbrowser.open_new("https://roadtrippers.com/")

        Button(complain, text="<< Back", width=6, command=complain_back).place(x=12, y=415)
        Button(complain, text="Post", width=6, command=complaint_post).place(x=435, y=415)
        complain.resizable(0, 0)
        complain.geometry("500x450+10+10")
        complain.mainloop()


    # text box
    Button(mainframe, text="Recommendations", width=14, command=tag_search, font="times_new_roman 10").place(x=24, y=227)
    Button(mainframe, text="Hotel Booking", width=14, command=hotel_book, font="times_new_roman 10").place(x=355,y=227)
    Button(mainframe, text="Trip Packages", width=14, command=Trip_Packages, font="times_new_roman 10").place(x=24,y=277)
    Button(mainframe, text="Complaints", width=14, command=complaints, font="times_new_roman 10").place(x=355,y=277)
    Button(mainframe, text="Payments", width=14, command=payment_options, font="times_new_roman 10").place(x=24,y=327)
    Button(mainframe, text="Settings", width=14, command=settings, font="times_new_roman 10").place(x=355,y=327)

    # button
    Button(mainframe, text="Exit", width=6, command=close_window).place(x=435, y=415)

    # run mainframe loop
    window.withdraw()
    mainframe.geometry("500x450+10+10")
    mainframe.mainloop()

# For entry of users into table 'Login', database 'Boomerang'
def sign_in():
    # main
    sign = Tk()
    sign.title("Boomerang")
    sign.configure(background="white")
    sign.resizable(0, 0)
    window.withdraw()

    # display
    photo2 = PhotoImage(master=sign, file="LongMile.png")
    Label(sign, image=photo2).place(x=10,y=0)
    Label(sign, text="Sign~Up", bg="white", fg="Black", font="papyrus 28 bold").place(x=215,y=10)
    Label(sign, text="Enter your credentials", bg="white", fg="Black", font="papyrus 16 bold").place(x=200,y=75)
    Label(sign, text="Please don't use a password that is\n same as your email account", bg="white", fg="Red",
          font="times_new_roman 14").place(x=98, y=160)

    textentryA = Entry(sign, width=20, bg="white")
    Label(sign, text="First Name", bg="white", fg="Black", font="times_new_roman 12").place(x=21, y=227)
    textentryA.place(x=111, y=230)

    textentryB = Entry(sign, width=20, bg="white")
    Label(sign, text="Last Name", bg="white", fg="Black", font="times_new_roman 12").place(x=258, y=227)
    textentryB.place(x=348, y=230)

    textentryC = Entry(sign, width=20, bg="white")
    Label(sign, text="Email", bg="white", fg="Black", font="times_new_roman 12").place(x=21, y=277)
    textentryC.place(x=111, y=280)

    textentryD = Entry(sign, width=20, bg="white")
    Label(sign, text="Location", bg="white", fg="Black", font="times_new_roman 12").place(x=258, y=277)
    textentryD.place(x=348, y=280)

    textentryE = Entry(sign, width=20, bg="white")
    Label(sign, text="PIN/ZIP", bg="white", fg="Black", font="times_new_roman 12").place(x=21, y=327)
    textentryE.place(x=111, y=330)

    textentryF = Entry(sign, width=20, bg="white")
    Label(sign, text="Phone", bg="white", fg="Black", font="times_new_roman 12").place(x=258, y=327)
    textentryF.place(x=348, y=330)

    textentryG = Entry(sign, width=20, bg="white")
    Label(sign, text="Username", bg="white", fg="Black", font="times_new_roman 12").place(x=21, y=377)
    textentryG.place(x=111, y=380)

    textentryH = Entry(sign, width=20, bg="white")
    Label(sign, text="Password", bg="white", fg="Black", font="times_new_roman 12").place(x=258, y=377)
    textentryH.place(x=348, y=380)

    # Main code for table entry
    def table_ent():
        mycursor = connection.cursor()
        sql = "INSERT INTO Login (First,Last,Email,Location,PIN,Phone,Username, Password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (textentryA.get(),textentryB.get(),textentryC.get(),textentryD.get(),textentryE.get(),textentryF.get(),
                textentryG.get(),textentryH.get())
        mycursor.execute(sql, args)
        connection.commit()
        print(mycursor.rowcount, "record inserted.")
        sign.withdraw()
        mainpart()

    Button(sign, text="Enter", width=6, command=table_ent).place(x=21, y=415)
    Button(sign, text="Exit", width=6, command=close_window).place(x=435, y=415)

    # run sign frame
    sign.geometry("500x450+10+10")
    sign.mainloop()


# main
window = Tk()

# Background Image
C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file="bkground.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

window.title("Boomerang")
window.configure(background="white")
window.resizable(0, 0)

# text box
textentry1 = Entry(window, width=20, bg="white")
Label(window, text="Username:", bg="white", fg="Black", font="times_new_roman 12").place(x=154,y=227)
textentry1.place(x=238, y=230)

textentry2 = Entry(window, width=20, bg="white")
Label(window, text="Password:", bg="white", fg="Black", font="times_new_roman 12").place(x=154,y=277)
textentry2.place(x=238, y=280)

Button(window, text="Login", width=6, command=click).place(x=234,y=327)

Button(window, text="Sign-up", width=6, bg="white", fg="Blue", borderwidth=0, command=sign_in).place(x=221,y=375)
# button
Button(window, text="Exit", width=6, command=close_window).place(x=435, y=415)

# run main loop
window.geometry("500x450+10+10")
window.mainloop()
