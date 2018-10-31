from flask import Flask, render_template, request
#request is used to read data from HMTL
from data import Faculties  # to import function
import os
portr = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

getfaculties = Faculties()

## Routing ##
@app.route('/')  #default route
def index():
    return render_template('home.html')   #picks file from template folders

@app.route('/about')
def about():
    # return '<h1> About Page </h1>'
    return render_template('about.html') 

@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method =='POST'):                #extract data from form
        getname=request.form['name']
        getemail=request.form['email']
        return render_template('contact.html',name=getname,email=getemail)       


@app.route('/faculties')
def faculties():
    return render_template('faculties.html',sendDat =getfaculties)

   ## debug=True turns on debug mode
if(__name__=='__main__'):
        app.run(port=portr)
        
