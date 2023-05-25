import sqlite3
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog
from PyQt5 import QtWidgets
import login
import vxod
from Sotrydniki import Ui_Sotrydniki
from Tovar import Ui_Tovar
from Category_tovarov import Ui_Category_tovarov
from Postavshik import Ui_Postavshik
from Zakaz import Ui_Zakaz
from Clienti import Ui_Clienti
from Prodazhi import Ui_Prodazhi

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(login TEXT, password TEXT)''')
db.commit()

class Registration(QtWidgets.QMainWindow, login.Ui_login): #регистрация
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText('Введите логин')
        self.lineEdit_2.setPlaceholderText('Введите пароль')
        self.pushButton.pressed.connect(self.reg) #  регитрация
        self.pushButton_2.pressed.connect(self.login) #переход на вход
        

    def login(self): #показ класса логин (вход)
        self.login = Login()
        self.login.show()
        self.hide()


    def reg(self): #регистрация
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return
        if len(user_password) == 0:
            return
        cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}" ')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES("{user_login}","{user_password}")')
            self.label_2.setText(f'Аккаунт {user_login} успешно зарегистрирован')
            db.commit()
        else:
            self.label_2.setText('Такая запись уже имеется')

class Login(QtWidgets.QMainWindow, vxod.Ui_vxod):# вход
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText('Введите логин')
        self.lineEdit_2.setPlaceholderText('Введите пароль')


        self.pushButton_2.pressed.connect(self.login)
        self.pushButton.pressed.connect(self.reg)


    def reg(self):
        self.reg=Registration()
        self.reg.show()
        self.hide()


    def login(self):
        try:
           user_login = self.lineEdit.text()
           user_password = self.lineEdit_2.text()

           if len(user_login) == 0:
              return
           if len(user_password) == 0:
              return

           cursor.execute(f'SELECT password FROM users WHERE login = "{user_login}"')
           check_pass = cursor.fetchall()

           cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
           check_login = cursor.fetchall()
           print (check_login)
           print(check_pass)

           if check_pass[0][0] == user_password and check_login[0][0] == user_login:
              self.label_2.setText(f'Успешная авториазация')
              self.Sotrydniki = Form_Sotrydniki()
              self.Sotrydniki.show()
              self.hide()
           else:
            self.label_2.setText(f'Ошибка авторизации')
        except Exception as e:
            self.label_2.setText(f'Ошибка авторизации')


Poisk_Sotrydniki = ['ID_sotrydniki', 'Name', 'Familia', 'Dolzenost', 'Data_priema_na_raboty' 'Price', 'Pol', 'Seria', 'Nomer']
DOLZHNOST = ['Грузчик', 'Водитель', 'Менеджер', 'Товаровед', 'Сортирощик', 'Заведующая']
class Form_Sotrydniki(QWidget, Ui_Sotrydniki): #таблица вакансия
   def __init__(self):
       super(Form_Sotrydniki, self).__init__()
       self.setupUi(self)
       self.pbOpen.clicked.connect(self.open_Sotrydniki)#открыть таблицу
       self.pbAdd.clicked.connect(self.insert_Sotrydniki)#добавить строки
       self.lineID.setPlaceholderText('Введите ID')
       self.pbDelet.clicked.connect(self.delete_Sotrydniki)#удалить строку
       self.lineChange_4.setPlaceholderText('Введите ID')
       self.cbFind_4.addItems(Poisk_Sotrydniki)
       self.cbPost.addItems(DOLZHNOST)
       self.pbFind_4.clicked.connect(self.search_Sotrydniki)#поиск
       self.pdChange_4.clicked.connect(self.update_record)#изменить
       self.pbOpen_5.clicked.connect(self.show_Tovar)     
       self.pbOpen_6.clicked.connect(self.show_Category_tovarov)   
       self.pbOpen_7.clicked.connect(self.show_Postavshik)   
       self.pbOpen_8.clicked.connect(self.show_Zakaz)  
       self.pbOpen_10.clicked.connect(self.show_Clienti)  
       self.pbOpen_9.clicked.connect(self.show_Prodazhi)  

   def open_Sotrydniki(self): #кнопка открыть сотрудники
       try:
           self.conn = sqlite3.connect('Store.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Sotrydniki;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
           
       except Exception as e:
           print ("Ошибки с подключением к БД")
           return e
       self.twSotrydniki.setColumnCount(len(col_name))
       self.twSotrydniki.setHorizontalHeaderLabels(col_name)
       self.twSotrydniki.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.twSotrydniki.setRowCount(self.twSotrydniki.rowCount()+1)
           for j, elen in enumerate(row):
               self.twSotrydniki.setItem(i, j,QTableWidgetItem(str(elen)))
       self.twSotrydniki.resizeColumnsToContents()

   def update(self, query="select * from Sotrydniki"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.twSotrydniki.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.twSotrydniki.setRowCount(self.twSotrydniki.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twSotrydniki.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twSotrydniki.resizeColumnsToContents()

   def insert_Sotrydniki(self): #кнопка добавить
       row = [self.lineName.text(), self.lineFamilia.text(), self.cbPost.itemText(self.cbPost.currentIndex()), 
              self.lineDate.text(), self.linePrice.text(), 'м' if self.rbMan.isChecked() else 'ж', 
              self.lineSerias.text(), self.lineNamber.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Sotrydniki(Name, Familia, Dolzenost, Data_priema_na_raboty, 
           Price, Pol, Seria, Nomer)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Sotrydniki(self):
        id = self.lineID.text()
        conn = sqlite3.connect('Store.db')
        c = conn.cursor()
        c.execute("DELETE FROM Sotrydniki WHERE ID_sotrydniki=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Sotrydniki(self):
        column_name = self.cbFind_4.currentText()
        column_index = self.twSotrydniki.horizontalHeaderItem(self.twSotrydniki.currentColumn())
        search_text = self.lineFind_4.text()
        query = f"select * from Sotrydniki where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_record(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Store.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода 
       Name = self.lineName.text()
       Familia = self.lineFamilia.text()
       Dolzenost = self.cbPost.itemText(self.cbPost.currentIndex())
       Data_priema_na_raboty = self.lineDate.text()
       Price = self.linePrice.text()
       Pol = 'м' if self.rbMan.isChecked() else 'ж', self.lineSerias.text()
       Seria = self.lineSerias.text()
       Nomer = self.lineNamber.text()

       # Получаем ID_sotrydniki из поля ввода
       ID_sotrydniki = self.lineChange_4.text()

       # Обновляем запись в таблице Sotrydniki
       try:
           cursor.execute(
               """UPDATE Sotrydniki SET Name=?, Familia=?, Dolzenost=?, Data_priema_na_raboty=?,
                 Price=?, Pol=?, Seria=?, Nomer=? WHERE ID_sotrydniki=?""",
               (Name, Familia, Dolzenost, Data_priema_na_raboty, Price, Pol, Seria, Nomer, ID_sotrydniki))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице:", e)
       finally:
           cursor.close()
           conn.close()
       self.update()# Обновляем данные в таблице на форме

   def show_Tovar(self):
       self.SH_can = Form_Tovar()
       self.SH_can.show()

   def show_Category_tovarov(self):
       self.SH_can = Form_Category()
       self.SH_can.show()
    
   def show_Postavshik(self):
       self.SH_can = Form_Postavshik()
       self.SH_can.show()

   def show_Zakaz(self):
       self.SH_can = Form_Zakaz()
       self.SH_can.show()

   def show_Clienti(self):
       self.SH_can = Form_Clienti()
       self.SH_can.show()

   def show_Prodazhi(self):
       self.SH_can = Form_Prodazhi()
       self.SH_can.show()


POISK_Tovar = ['ID_tovara', 'Product_category', 'Name', 'Price_1sht', 'Kol-vo_na_sklade', 'Postavshik']
class Form_Tovar(QWidget, Ui_Tovar): #таблица вакансия
   def __init__(self):
       super(Form_Tovar, self).__init__()
       self.setupUi(self)
       self.pbOpen.clicked.connect(self.open_Tovar)
       self.pbAdd.clicked.connect(self.insert_Tovar)
       self.pbDelet.clicked.connect(self.delete_Tovar)
       self.cbFind.addItems(POISK_Tovar)
       self.pbFind.clicked.connect(self.search_Tovar)
       self.pdChange.clicked.connect(self.update_record)
       self.lineID.setPlaceholderText('Введите ID')
       self.lineChange.setPlaceholderText('Введите ID')
       
   
   def open_Tovar(self):  # кнопка добавить
       try:
           self.conn = sqlite3.connect('Store.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Tovar;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print("Ошибки с подключением к БД")
           return e
       self.twTovari.setColumnCount(len(col_name))
       self.twTovari.setHorizontalHeaderLabels(col_name)
       self.twTovari.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.twTovari.setRowCount(self.twTovari.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twTovari.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twTovari.resizeColumnsToContents()

   def update(self, query="select * from Tovar"):  # после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.twTovari.setRowCount(0)  # обнулмяем все данные из таблцы
       # заносим по новой
       for i, row in enumerate(data):
           self.twTovari.setRowCount(self.twTovari.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twTovari.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twTovari.resizeColumnsToContents()

   def insert_Tovar(self):  # кнопка добавить
       row = [self.spProduct.text(), self.lineName.text(), self.linePrice.text(),
              self.lineSclad.text(), self.spPostavshik.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Tovar(Product_category,Name,Price_1sht,Na_Sklade,Postavshik)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')""")
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("ошиб", r)
           return r
       self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Tovar(self):  # удалить агент
       id = self.lineID.text()
       conn = sqlite3.connect('Store.db')
       c = conn.cursor()
       c.execute("DELETE FROM Tovar WHERE ID_tovara=?", (id,))
       conn.commit()
       conn.close()
       self.update()

   def search_Tovar(self):
       column_name = self.cbFind.currentText()
       column_index = self.twTovari.horizontalHeaderItem(self.twTovari.currentColumn())
       search_text = self.lineFind.text()
       query = f"select * from Tovar where {column_name} like '%{search_text}%'"
       self.update(query)

   def update_record(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Store.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Product_category = self.spProduct.text()
       Price_1sht = self.linePrice.text()
       Na_Sklade = self.lineSclad.text()
       Postavshik = self.spPostavshik.text()
       
 # Получаем ID_emploee из поля ввода
       ID_tovara = self.lineChange.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Tovar SET Product_category=?, Price_1sht=?, Na_Sklade=?, Postavshik=? WHERE ID_tovara=?""",
               (Product_category, Price_1sht, Na_Sklade, Postavshik, ID_tovara))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Tovar:", e)
       finally:
           cursor.close()
           conn.close()
       # Обновляем данные в таблице на форме
       self.update()

POISK_Category = ['ID_category', 'Naimenovanie']

class Form_Category(QWidget, Ui_Category_tovarov): #таблица вакансия
   def __init__(self):
       super(Form_Category, self).__init__()
       self.setupUi(self)
       self.pbOpen.clicked.connect(self.open_Category)#открыть таблицу
       self.pbAdd.clicked.connect(self.insert_Category)#добавить строки
       self.lineChange.setPlaceholderText('Введите ID')
       self.pbDelet.clicked.connect(self.delete_Category)#удалить строку
       self.lineID.setPlaceholderText('Введите ID')
       self.cbFind.addItems(POISK_Category)
       self.pbFind.clicked.connect(self.search_Category)#поиск
       self.pdChange.clicked.connect(self.update_Category)#изменить


   def open_Category(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Store.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Category_tovarov;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ошибки с подключением к БД")
           return e
       self.twCategori.setColumnCount(len(col_name))
       self.twCategori.setHorizontalHeaderLabels(col_name)
       self.twCategori.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.twCategori.setRowCount(self.twCategori.rowCount()+1)
           for j, elen in enumerate(row):
               self.twCategori.setItem(i, j,QTableWidgetItem(str(elen)))
       self.twCategori.resizeColumnsToContents()

   def update(self, query="select * from Category_tovarov"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.twCategori.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.twCategori.setRowCount(self.twCategori.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twCategori.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twCategori.resizeColumnsToContents()


   def insert_Category(self): #кнопка добавить
       row = [self.lineName.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Category_tovarov(Naimenovanie)
           values('{row[0]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Category(self):
        id = self.lineID.text()
        conn = sqlite3.connect('Store.db')
        c = conn.cursor()
        c.execute("DELETE FROM Category_tovarov WHERE ID_category=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Category(self):
        column_name = self.cbFind.currentText()
        column_index = self.twCategori.horizontalHeaderItem(self.twCategori.currentColumn())
        search_text = self.lineFind.text()
        query = f"select * from Category_tovarov where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_Category(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Store.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Naimenovanie = self.lineName.text()

       # Получаем ID_emploee из поля ввода
       ID_category = self.lineChange.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Category_tovarov SET Naimenovanie=? WHERE ID_category=?""",
               (Naimenovanie, ID_category))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()

POISK_Postavshik = ['ID_postavshik', 'Naimenovanie', 'Adres', 'Telefon', 'Pochta']

class Form_Postavshik (QWidget, Ui_Postavshik): #таблица вакансия
   def __init__(self):
       super(Form_Postavshik, self).__init__()
       self.setupUi(self)
       self.pbOpen.clicked.connect(self.open_Postavshik)#открыть таблицу
       self.pbAdd.clicked.connect(self.insert_Postavshik)#добавить строки
       self.lineID.setPlaceholderText('Введите ID')
       self.pbDelet.clicked.connect(self.delete_Postavshik)#удалить строку
       self.lineChange.setPlaceholderText('Введите ID')
       self.cbFind.addItems(POISK_Postavshik)
       self.pbFind.clicked.connect(self.search_Postavshik)#поиск
       self.pdChange.clicked.connect(self.update_record)#изменить


   def open_Postavshik(self):  # кнопка добавить
       try:
           self.conn = sqlite3.connect('Store.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Postavshik;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print("Ошибки с подключением к БД")
           return e
       self.twPostavshik.setColumnCount(len(col_name))
       self.twPostavshik.setHorizontalHeaderLabels(col_name)
       self.twPostavshik.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.twPostavshik.setRowCount(self.twPostavshik.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twPostavshik.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twPostavshik.resizeColumnsToContents()

   def update(self, query="select * from Postavshik"):  # после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подключением {d}")
           return d
       self.twPostavshik.setRowCount(0)  # обнулмяем все данные из таблцы
       # заносим по новой
       for i, row in enumerate(data):
           self.twPostavshik.setRowCount(self.twPostavshik.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twPostavshik.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twPostavshik.resizeColumnsToContents()

   def insert_Postavshik(self):  # кнопка добавить
       row = [self.lineName.text(), self.lineAdress.text(), self.linePhone.text(), self.linePochta.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Postavshik(Naimenovanie,Adres,Telefon,Pochta)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}')""")
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("ошибка", r)
           return r
       self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Postavshik(self):  # удалить агент
       id = self.lineID.text()
       conn = sqlite3.connect('Store.db')
       c = conn.cursor()
       c.execute("DELETE FROM Postavshik WHERE ID_postavshik=?", (id,))
       conn.commit()
       conn.close()
       self.update()

   def search_Postavshik(self):
       column_name = self.cbFind.currentText()
       column_index = self.twPostavshik.horizontalHeaderItem(self.twPostavshik.currentColumn())
       search_text = self.lineFind.text()
       query = f"select * from Postavshik where {column_name} like '%{search_text}%'"
       self.update(query)

   def update_record(self):  # изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Store.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Naimenovanie = self.lineName.text()
       Adres = self.lineAdress.text()
       Telefon =  self.linePhone.text()
       Pochta = self.linePochta.text()

       # Получаем ID_emploee из поля ввода
       ID_postavshik = self.lineChange.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Postavshik SET Naimenovanie=?, Adres=?, Telefon=?, Pochta=? WHERE ID_postavshik=?""",
               (Naimenovanie, Adres, Telefon, Pochta, ID_postavshik))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице:", e)
       finally:
           cursor.close()
           conn.close()
       # Обновляем данные в таблице на форме
       self.update()

POISK_Zakaz = ['ID_zakaza', 'Data_zakaza', 'Data_otgryzki', 'Status']
STATUS = ['На сборке', 'Отгружен']
class Form_Zakaz(QWidget, Ui_Zakaz): #таблица вакансия
   def __init__(self):
       super(Form_Zakaz, self).__init__()
       self.setupUi(self)
       self.pbOpen.clicked.connect(self.open_Zakaz)#открыть таблицу
       self.pbAdd.clicked.connect(self.insert_Zakaz)#добавить строки
       self.lineChange.setPlaceholderText('Введите ID')
       self.pbDelet.clicked.connect(self.delete_Zakaz)#удалить строку
       self.lineID.setPlaceholderText('Введите ID')
       self.cbFind.addItems(POISK_Zakaz)
       self.pbFind.clicked.connect(self.search_Zakaz)#поиск
       self.pdChange.clicked.connect(self.update_Zakaz)#изменить
       self.cbStatys.addItems(STATUS)


   def open_Zakaz(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Store.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Zakaz;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ошибки с подключением к БД")
           return e
       self.twZakazi.setColumnCount(len(col_name))
       self.twZakazi.setHorizontalHeaderLabels(col_name)
       self.twZakazi.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.twZakazi.setRowCount(self.twZakazi.rowCount()+1)
           for j, elen in enumerate(row):
               self.twZakazi.setItem(i, j,QTableWidgetItem(str(elen)))
       self.twZakazi.resizeColumnsToContents()

   def update(self, query="select * from Zakaz"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.twZakazi.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.twZakazi.setRowCount(self.twZakazi.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twZakazi.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twZakazi.resizeColumnsToContents()


   def insert_Zakaz(self): #кнопка добавить
       row = [self.deZakaz.text(), self.deOtgryzka.text(), self.cbStatys.itemText(self.cbStatys.currentIndex())]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Zakaz(Data_zakaza, Data_otgryzki, Status)
           values('{row[0]}','{row[1]}','{row[2]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Zakaz(self):
        id = self.lineID.text()
        conn = sqlite3.connect('Store.db')
        c = conn.cursor()
        c.execute("DELETE FROM Zakaz WHERE ID_zakaza=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Zakaz(self):
        column_name = self.cbFind.currentText()
        column_index = self.twZakazi.horizontalHeaderItem(self.twZakazi.currentColumn())
        search_text = self.lineFind.text()
        query = f"select * from Zakaz where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_Zakaz(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Store.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Data_zakaza = self.deZakaz.text()
       Data_otgryzki = self.deOtgryzka.text()
       Status =  self.cbStatys.itemText (self.cbStatys.currentIndex())


       # Получаем ID_emploee из поля ввода
       ID_zakaza = self.lineChange.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Zakaz SET Data_zakaza=?, Data_otgryzki=?, Status=? WHERE ID_zakaza=?""",
               (Data_zakaza, Data_otgryzki, Status, ID_zakaza))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()

POISK_Clienti = ['ID_clienti', 'Name', 'Familia', 'Adres', 'Telefon', 'Pochta']
class Form_Clienti(QWidget, Ui_Clienti): #таблица вакансия
   def __init__(self):
       super(Form_Clienti, self).__init__()
       self.setupUi(self)
       self.pbOpen.clicked.connect(self.open_Clienti)#открыть таблицу
       self.pbAdd.clicked.connect(self.insert_Clienti)#добавить строки
       self.lineChange.setPlaceholderText('Введите ID')
       self.pbDelet.clicked.connect(self.delete_Clienti)#удалить строку
       self.lineID.setPlaceholderText('Введите ID')
       self.cbFind.addItems(POISK_Clienti)
       self.pbFind.clicked.connect(self.search_Clienti)#поиск
       self.pdChange.clicked.connect(self.update_Clienti)#изменить



   def open_Clienti(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Store.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Clienti;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ошибки с подключением к БД")
           return e
       self.twClient.setColumnCount(len(col_name))
       self.twClient.setHorizontalHeaderLabels(col_name)
       self.twClient.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.twClient.setRowCount(self.twClient.rowCount()+1)
           for j, elen in enumerate(row):
               self.twClient.setItem(i, j,QTableWidgetItem(str(elen)))
       self.twClient.resizeColumnsToContents()

   def update(self, query="select * from Clienti"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.twClient.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.twClient.setRowCount(self.twClient.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twClient.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twClient.resizeColumnsToContents()


   def insert_Clienti(self): #кнопка добавить
       row = [self.lineName.text(), self.lineFamilia.text(), self.lineAdress.text(), self.linePhone.text(), self.linePochta.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Clienti(Name, Familia, Adres, Telefon, Pochta)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Clienti(self):
        id = self.lineID.text()
        conn = sqlite3.connect('Store.db')
        c = conn.cursor()
        c.execute("DELETE FROM Clienti WHERE ID_clienti=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Clienti(self):
        column_name = self.cbFind.currentText()
        column_index = self.twClient.horizontalHeaderItem(self.twClient.currentColumn())
        search_text = self.lineFind.text()
        query = f"select * from Clienti where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_Clienti(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Store.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Name = self.lineName.text() 
       Familia = self.lineFamilia.text()
       Adres =  self.lineAdress.text()
       Telefon = self.linePhone.text()
       Pochta = self.linePochta.text()


       # Получаем ID_emploee из поля ввода
       ID_clienti = self.lineChange.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Clienti SET Name=?, Familia=?, Adres=?, Telefon=?, Pochta=? WHERE ID_clienti=?""",
               (Name, Familia, Adres, Telefon, Pochta, ID_clienti))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()

POISK_Prodazhi = ['ID_clienti', 'Name', 'Familia', 'Adres', 'Telefon', 'Pochta']
class Form_Prodazhi(QWidget, Ui_Prodazhi): #таблица вакансия
   def __init__(self):
       super(Form_Prodazhi, self).__init__()
       self.setupUi(self)
       self.pbOpen.clicked.connect(self.open_Prodazhi)#открыть таблицу
       self.pbAdd.clicked.connect(self.insert_Prodazhi)#добавить строки
       self.lineChange.setPlaceholderText('Введите ID')
       self.pbDelet.clicked.connect(self.delete_Prodazhi)#удалить строку
       self.lineID.setPlaceholderText('Введите ID')
       self.cbFind.addItems(POISK_Prodazhi)
       self.pbFind.clicked.connect(self.search_Prodazhi)#поиск
       self.pdChange.clicked.connect(self.update_Prodazhi)#изменить
       



   def open_Prodazhi(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Store.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Prodazhi;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ошибки с подключением к БД")
           return e
       self.twProdazhi.setColumnCount(len(col_name))
       self.twProdazhi.setHorizontalHeaderLabels(col_name)
       self.twProdazhi.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.twProdazhi.setRowCount(self.twProdazhi.rowCount()+1)
           for j, elen in enumerate(row):
               self.twProdazhi.setItem(i, j,QTableWidgetItem(str(elen)))
       self.twProdazhi.resizeColumnsToContents()

   def update(self, query="select * from Prodazhi"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.twProdazhi.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.twProdazhi.setRowCount(self.twProdazhi.rowCount() + 1)
           for j, elen in enumerate(row):
               self.twProdazhi.setItem(i, j, QTableWidgetItem(str(elen)))
       self.twProdazhi.resizeColumnsToContents()


   def insert_Prodazhi(self): #кнопка добавить
       row = [self.deProdazhi.text(), self.lineTovar.text(), self.linePrice.text(),  self.sbIDTovara.text(),  self.sbIDClienta.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Prodazhi(Data_prodazhi, Quantity_tovara, Price, ID_tovara, ID_clienti)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Prodazhi(self):
        id = self.lineID.text()
        conn = sqlite3.connect('Store.db')
        c = conn.cursor()
        c.execute("DELETE FROM Prodazhi WHERE ID_prodazhi=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Prodazhi(self):
        column_name = self.cbFind.currentText()
        column_index = self.twProdazhi.horizontalHeaderItem(self.twProdazhi.currentColumn())
        search_text = self.lineFind.text()
        query = f"select * from Prodazhi where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_Prodazhi(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Store.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Data_prodazhi = self.deProdazhi.text()
       Quantity_tovara =  self.lineTovar.text()
       Data_prodazhi =  self.linePrice.text()
       ID_tovara = self.sbIDTovara.text()
       ID_clienti =  self.sbIDClienta.text() 


       # Получаем ID_emploee из поля ввода
       ID_prodazhi = self.lineChange.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Prodazhi SET Data_prodazhi=?, Quantity_tovara=?, Data_prodazhi=?, ID_tovara=?, ID_clienti=? WHERE ID_prodazhi=?""",
               (Data_prodazhi, Quantity_tovara, Data_prodazhi, ID_tovara, ID_clienti, ID_prodazhi))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()

App = QtWidgets.QApplication([])
window = Login()
window.show()
App.exec()