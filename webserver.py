from flask import Flask, render_template, request, jsonify, url_for,redirect, send_file
from flask_mail import Mail, Message
import os

print(os.getcwd())

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'mail.uhpae.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'welcome@uhpae.com'
app.config['MAIL_PASSWORD'] = 'ahmedrauf1'
app.config['MAIL_DEFAULT_SENDER'] = 'welcome@uhpae.com'
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/download')
def download():
    cwd = os.getcwd()
    path = cwd + "/saadiyat_brochure.pdf"
    return send_file(path, as_attachment=True)

@app.route('/offer')
def offer():
    return render_template("offer.html")

@app.route('/en_offer')
def en_offer():
    return render_template("en_offer.html")

@app.route('/sendmail',methods=['POST'])
def sendmail():
    email = request.form.get('email')
    name = request.form.get('name')
    phone = request.form.get('phone')
    msg = Message('I have registered', recipients=['bjarrah@uhpae.com'])
    msg.html = '<b>'+email+'<br>'+name+'<br>'+phone+'</b>'
    mail.send(msg)
    return redirect(request.referrer)


@app.route('/sendform',methods=['POST'])
def sendform():
    
    consultation =''
    mortgage =''
    land=''
    management =''
    design = ''
    
    email = request.form.get('email1')
    name = request.form.get('name1')
    phone = request.form.get('phone1')    
    construction = request.form.get('need_construction')
    if construction == None:
        construction =''
    consultation = request.form.get('need_consultation')
    if consultation == None:
        consultation =''
    mortgage = request.form.get('need_mortgage')
    if mortgage == None:
        mortgage =''

    land = request.form.get('need_land')
    if land == None:
        land =''
    management = request.form.get('need_management')
    if management== None:
        management =''
    design = request.form.get('need_design')
    if  design == None:
        design =''
    print(email + management)
    
    msg = Message('Hello, Im interested and my details are ... ', recipients=['bjarrah@uhpae.com'])
    msg.html = '<b>'+email+'<br>'+name+'<br>'+phone+'</b>'+'<br>'+construction+'<br>'+consultation+'<br>'+mortgage+'<br>'+land+'<br>'+management+'<br>'+design+'<br>'
    mail.send(msg)
    return redirect(request.referrer)

if __name__ == '__main__':
    app.run(debug=True)