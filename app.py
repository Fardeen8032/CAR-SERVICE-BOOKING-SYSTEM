
from flask import Flask, render_template,request;
import sqlite3 as sql
import os
from os import path
currentsirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('Index.html')

@app.route("/" ,methods=['POST'])
def Contact():
    if request.method == 'POST':
      try:
         fname = request.form['fname']
         lname2 = request.form['lname2']
         ename2 = request.form['ename2']
         text = request.form['text']
         con = sql.connect(currentsirectory + "\Carservice.db")
         cur = con.cursor()
         cur.execute("INSERT INTO User (fname, lname2, ename2, text) VALUES (?,?,?,?)",(fname, lname2, ename2, text) )
         con.commit()
         print("Record successfully added")

      except:
         con.rollback()
         print("error in insert operation")



    return render_template('Index.html');



@app.route('/book' ,methods=['POST'])
def Book():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            Phone2 = request.form["Phone2"]
            cars = request.form["cars"]
            if(cars == 'Preventive Maintenance Service'):
                cars = "Preventive Maintenance Service"
            elif(cars =="Body Repair Service"):
                cars = "Body Repair Service"
            else:
                cars ="Car Care Service"
            Car2 = request.form["Car2"]
            model2 = request.form["model2"]
            FuelType = request.form["FuelType"]
            if(FuelType == 'Petrol'):
                FuelType = "Petrol"
            elif(FuelType =="Diesel"):
                FuelType = "Diesel"
            else:
                FuelType ="CNG"
            Kilo2 = request.form["Kilo2"]
            with sql.connect("Carservice.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Booking (name, email, Phone2,cars,Car2, model2, FuelType,Kilo2) values (?,?,?,?,?,?,?,?)",(name, email, Phone2,cars,Car2, model2, FuelType,Kilo2))
                con.commit()
                msg = "Booking is done successfully"

        except:
            con.rollback()
            print("We can not book")

        finally:
            return render_template("Booking.html")
            con.close()






@app.route('/service1' ,methods=['POST'])
def Service1():
    return render_template('Service1.html');

@app.route('/service2' ,methods=['POST'])
def Service2():
    return render_template('Service2.html');

@app.route('/service3' ,methods=['POST'])
def Service3():
    return render_template('Service3.html');
if __name__=='__main__':
    app.run(debug=True);