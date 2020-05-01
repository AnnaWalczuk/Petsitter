from ConnectionManager import DBCOnnectManager
import pymysql

import os

import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import datetime


from functions import adjust_data
from functions import adj_price_kakadu
from functions import adj_price_fera
from functions import adj_price_maxizoo


class Dogs:

    def __init__(self, connection_manager):

        self.connection = connection_manager.connection
        self.logging_in()



    def logging_in(self):
        global login
        login = input("Enter you login: ")

        password=input("Enter your password: ")

        self.connection.cursor()
        self.cursor = self.connection.cursor()

        self.cursor.execute("select * from emp_login where user_name = %s  and password = %s", (login, password))

        result = self.cursor.fetchall()

        if(len(result) == 1 and login=="axo"):
            print("\nWelcome to Petsitter admin panel")
            self.admin_menu()
        elif(len(result) == 1 and login!="axo"):
            print("\nWelcome to Petsitter database")
            self.menu()
        else:
            print("The username or password is incorrect")
            self.logging_in()


    def menu(self):

        while(True):

            dec = input("\n1 - Show dogs \n2 - Show walks \n3 - Save dogs' details to txt file \n"
                        "4 - Plot: Number of dogs by age and by sex \n5 - Quit\n")

            if (dec == "1"):
                self.show_dogs()
            elif (dec == "4"):
                self.show_plot()
            elif (dec == "5"):
                print("Goodbye")
                exit()
            elif (dec == "2"):
                self.show_walks()
            elif (dec == "3"):
                self.save_to_file()
            else:
                print("incorrect input")


    def admin_menu(self):

        while(True):

            dec = input("\n1 - Show dogs \n2 - Show walks \n3 - Save dogs' details to txt file \n"
                        "4 - Plot: Number of dogs by age and by sex \n5 - Dog food prices check \n6 - Assign walks to employees \n7 - Insert dogs to database \n"
                                 "8 - Delete dogs from database \n9 - Quit\n")
            if (dec == "1"):
                self.show_dogs()
            elif (dec == "4"):
                self.show_plot()
            elif (dec == "9"):
                print("Goodbye")
                exit()
            elif (dec == "2"):
                self.show_walks()
            elif (dec == "3"):
                self.save_to_file()
            elif (dec == "7"):
                self.insert_dogs()
            elif (dec == "8"):
                self.delete_dogs()
            elif (dec == "5"):
                self.check_prices()
            elif (dec == "6"):
                self.organize_walks()
            else:
                print("incorrect input")



    def show_plot(self):

        self.cursor.execute("select age from dogs group by age asc")
        result = self.cursor.fetchall()
        d_list = list(result)
        age1 = []
        for tuple in d_list:
            age1.append(int(tuple[0]))

        self.cursor.execute("select age, count(id_dog) from dogs where male_female='f' group by age asc")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result)
        list_agef = df[0].tolist()
        list_dogsnbf = df[1].tolist()


        self.cursor.execute("select age, count(id_dog) from dogs where male_female='m' group by age asc")
        result = self.cursor.fetchall()
        df = pd.DataFrame(result)
        list_agem = df[0].tolist()
        list_dogsnbm = df[1].tolist()

        list_m_definitf = adjust_data(age1, list_agem, list_dogsnbm)
        list_f_definitf = adjust_data(age1, list_agef, list_dogsnbf)

        ages = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty"
        }

        labels = []
        for nb in age1:
            labels.append(ages.get(nb))

        x = np.arange(len(labels))
        width = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width / 2, list_f_definitf, width, label='Females')
        rects2 = ax.bar(x + width / 2, list_m_definitf, width, label='Males')

        ax.set_ylabel('Number of dogs', labelpad=5, color='#333333')
        ax.set_xlabel('Age (years)', labelpad=15, color='#333333')
        ax.set_title('Dogs by age and by sex', pad=20, color='#333333',
             weight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        plt.yticks([])

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),
                            textcoords="offset points", color=rects[0].get_facecolor(),
                            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_color('#DDDDDD')

        fig.tight_layout()
        plt.show()



    def organize_walks(self):
        global dog_id_list
        global emp_id_list
        self.cursor.execute("select * from v_walks_admin")
        result = self.cursor.fetchall()
        df_walks2 = pd.DataFrame(result)
        df_walks2.rename(columns={0: "Dog ID", 1: "Dog name", 2: "Employee ID", 3: "Employee name", 4:"Daily walk in minutes"}, inplace=True)
        print("\nCurrent list of walks")
        dog_id_list = df_walks2["Dog ID"].tolist()
        emp_id_list = df_walks2["Employee ID"].tolist()
        print(df_walks2)

        while True:
            dec3 = input("Do you want to make any changes to the list? (yes/no): ").lower()
            if dec3 == "no":
                print("Back to main menu")
                break
            if dec3 == "yes":
                while True:
                    w_dog = input("Enter dog's ID?: ")
                    if w_dog.isdigit() and int(w_dog) in dog_id_list:
                        w_dog2 = int(w_dog)
                        break
                    elif w_dog.isdigit()==False:
                        print("This must be a number")
                    else:
                        print("This ID is not in Dog ID list")

                while True:
                    w_emp = input("To which employee you want to assign this walk? Enter his/hers ID: ")
                    if w_emp.isdigit() and int(w_emp) in emp_id_list:
                        w_emp2 = int(w_emp)
                        break
                    elif w_emp.isdigit()==False:
                        print("This must be a number")
                    else:
                        print("This ID is not in Employee ID list")
                self.cursor.execute("update walks set id_emp = '%s' where id_dog = '%s'", (w_emp2, w_dog2))
                self.connection.commit()
                print("\nList of walks updated!")
                self.cursor.execute("select * from v_walks_admin where id_dog = '%s'", (w_dog2))
                result = self.cursor.fetchall()
                df_walks3 = pd.DataFrame(result)
                df_walks3.rename(columns={0: "Dog ID", 1: "Dog name", 2: "Employee ID", 3: "Employee name",
                                          4: "Daily walk(min)"}, inplace=True)

                print(df_walks3)






    def insert_dogs(self):
        global i_age
        global i_dog_name
        global i_breed
        global i_food
        global i_walk
        while True:
            i_dog_name = input("Dog name: ")
            if len(i_dog_name) == 0:
                print("Enter at least one letter")
            elif len(i_dog_name) > 20:
                print("Dog name too long")
            else:
                i_dog_name.capitalize()
                break
        while True:
            i_age = input("Dog age: ")
            if i_age.isdigit() and int(i_age) in range (1,21):
                break
            elif i_age.isdigit()==False:
                print("This must be a number")
            elif int(i_age) not in range(1, 16):
                print("Petsitter only accepts dogs from 1 to 20 years old")
        while True:
            i_male_female = input("Sex m/f: ").lower()
            if i_male_female =="m" or i_male_female=="f":
                break
        while True:
            i_breed = input("Dog breed: ")
            if i_breed.isdigit() == True:
                print("This cannot be a number")
            elif len(i_breed) == 0:
                print("This field cannot be empty")
            elif len(i_breed) > 46:
                print("Breed name too long")
            else:
                i_breed.capitalize()
                break
        while True:
            i_food = input("Brand of dog food: Chappi, Bosch Junior or Pedigree: ").capitalize()
            if i_food == ("Chappi") or i_food == ("Bosch Junior") or i_food == ("Pedigree"):
                break
        while True:
            i_walk = input("Length of daily walk in minutes: ")
            if i_walk.isdigit() == False:
                print("This must be a number")
            elif i_walk.isdigit() and len(i_walk) not in range (1,4):
                print("Enter a number in range 1-999")
            else:
                break
        try:
            self.cursor.execute("insert into dogs (dog_name, male_female, age, breed, food, walk_in_minutes) values "
                                "(%s, %s, %s, %s, %s, %s)", (i_dog_name, i_male_female, i_age, i_breed, i_food,
                                                             i_walk))
            self.connection.commit()
            print("\nNew dog successfully added to database: "+i_dog_name)


        except Exception as e:
            print (e)
            print("Couldn't insert record")




    def delete_dogs(self):

        global dog_to_be_removed
        global dogs_list
        self.cursor.execute("select dog_name from dogs")
        result = self.cursor.fetchall()
        df_dogs = pd.DataFrame(result)
        df_dogs.rename(columns={0: "Name"}, inplace=True)
        print("\nList of dogs currently in our pet hotel")
        print(df_dogs)
        dogs_list = df_dogs["Name"].to_list()

        while True:

            dog_to_be_removed = input("Name of dog to be removed from database: ")
            if dog_to_be_removed in dogs_list:
                break
            else:
                print("This dog is not in our database")


        while True:
            dec1 = input("Delete this record? yes/no: ")
            if dec1 == "yes":
                self.cursor.execute("delete from dogs where dog_name = %s", (dog_to_be_removed))
                self.connection.commit()
                print("Deleted from database")
                break
            elif dec1 == "no":
                print("Back to main menu")
                break



    def show_dogs(self):

        while True:

            letter = input("Enter a letter of a dog's name or leave empty to see all dogs: ")
            self.cursor.execute("select dog_name, male_female, age, breed, food, walk_in_minutes from dogs where dog_name "
                            "like '%s'" % ("%" + letter + "%",))
            result = self.cursor.fetchall()
            df_dogs = pd.DataFrame(result)
            if df_dogs.empty == False:
                df_dogs.rename(columns={0: "Name", 1: "Sex", 2: "Age", 3: "Breed",
                                        4: "Dog food", 5: "Daily walk(min)"}, inplace=True)
                print("\n")
                print(df_dogs)
                print("\n")
                break
            else:
                print("This dog is not in our pet hotel")



    def show_walks(self):

        while True:
            dec2 = input("\nDaily walks: \n1 - Show walks assigned to you \n2 - Show all walks\n")
            if (dec2 == "1"):
                user = login
                self.cursor.execute("select employee, dog_name, walk_length from v_walks where emp_user_name = %s", (user))
                result2 = self.cursor.fetchall()

                break
            elif (dec2 == "2"):
                self.cursor.execute("select employee, dog_name, walk_length from v_walks")
                result2 = self.cursor.fetchall()
                break

        df_walks = pd.DataFrame(result2)
        df_walks.rename(columns={0: "Employee", 1: "Dog", 2: "Daily walk(min)"}, inplace=True)
        print("\n")
        print(df_walks)



    def check_prices(self):

        self.cursor.execute("select count(id_dog) from dogs where food = 'Chappi'")
        result = self.cursor.fetchall()
        for tuple in result:
               print("\nUpdating Chappi prices... ", tuple[0], "dogs eat Chappi")

        page = requests.get(
            "https://e-sklep.kakadu.pl/produkt-20736/chappi.z.drobiem.i.warzywami.karma.dla.psa.135.kg.htm")

        html = BeautifulSoup(page.content, 'html.parser')
        kprice = adj_price_kakadu(html)
        self.cursor.execute("UPDATE food SET kakadu='%s' WHERE id_food=1", (kprice))
        self.connection.commit()


        page = requests.get("https://fera.pl/chappi-wolowina-kurczak-warzywa-13-5kg.html")
        html = BeautifulSoup(page.content, 'html.parser')
        fprice = adj_price_fera(html)
        self.cursor.execute("UPDATE food SET fera='%s' WHERE id_food=1", (fprice))
        self.connection.commit()



        self.cursor.execute("select count(id_dog) from dogs where food = 'Bosch Junior'")
        result = self.cursor.fetchall()
        for tuple in result:
               print("Updating Bosch Junior prices... ", tuple[0], "dogs eat Bosch Junior")


        page = requests.get("https://www.maxizoo.pl/p/bosch-junior-jagni-cina-i-ry-#15-kg")
        html = BeautifulSoup(page.content, 'html.parser')
        mzprice = adj_price_maxizoo(html)
        self.cursor.execute("UPDATE food SET maxizoo='%s' WHERE id_food=2", (mzprice))
        self.connection.commit()



        page = requests.get("https://fera.pl/bosch-junior-lamb-rice-15-kg.htmll")
        html = BeautifulSoup(page.content, 'html.parser')
        fprice = adj_price_fera(html)
        self.cursor.execute("UPDATE food SET fera='%s' WHERE id_food=2", (fprice))
        self.connection.commit()


        page = requests.get("https://e-sklep.kakadu.pl/produkt-23184/bosch.junior.z.jagniecina.i.ryzem.karma.dla.szczeniat.15.kg.htm")
        html = BeautifulSoup(page.content, 'html.parser')
        kprice = adj_price_kakadu(html)
        self.cursor.execute("UPDATE food SET kakadu='%s' WHERE id_food=2", (kprice))
        self.connection.commit()



        self.cursor.execute("select count(id_dog) from dogs where food = 'Pedigree'")
        result = self.cursor.fetchall()
        for tuple in result:
               print("Updating Pedigree prices... ", tuple[0], "dogs eat Pedigree")


        page = requests.get("https://e-sklep.kakadu.pl/produkt-1242/pedigree.adult.drob.i.warzywa.15.kg.htm")
        html = BeautifulSoup(page.content, 'html.parser')
        kprice = adj_price_kakadu(html)
        self.cursor.execute("UPDATE food SET kakadu='%s' WHERE id_food=3", (kprice))
        self.connection.commit()


        page = requests.get("https://www.maxizoo.pl/p/pedigree-adult#z-kurczakiem-i-warzywami15-kg")
        html = BeautifulSoup(page.content, 'html.parser')
        mzprice = adj_price_maxizoo(html)
        self.cursor.execute("UPDATE food SET maxizoo='%s' WHERE id_food=3", (mzprice))
        self.connection.commit()

        print("\nPrices updated!")

        self.cursor.execute("select food_brand, kakadu, fera, maxizoo from food")
        result = self.cursor.fetchall()
        df_food = pd.DataFrame(result)
        df_food.rename(columns={0: "Food brand", 1: "Kakadu(PLN)", 2: "Fera(PLN)", 3: "Maxizoo(PLN)"}, inplace=True)
        df_food = df_food.where(pd.notnull(df_food), None)
        print(df_food)


    def save_to_file(self):
        a_date = datetime.datetime.now()

        os.getcwd()
        file_name = "Dogs_"+str(a_date.date())
        self.file = open(file_name+".txt", 'w')

        self.cursor.execute("select id_dog, dog_name, male_female, age, breed, food, walk_in_minutes from dogs")
        result = self.cursor.fetchall()

        for dg in result:
            result_str = ""
            for elem in dg:
                result_str += str(elem)
                result_str += " "
            self.file.write(result_str + "\n")
        self.file.close()
        print("\nFile " + file_name +" has been saved here " + os.getcwd())




petsitter = Dogs(DBCOnnectManager())
