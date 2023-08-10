from flask import Flask, render_template, request, redirect, send_file, url_for
import smtplib

app = Flask(__name__)

@app.route("/")
def LandingPage():
    return render_template('home.html')

@app.route("/home")
def HomePage():
    return render_template('home.html')

@app.route("/about")
def AboutPage():
    return render_template('about.html')

@app.route("/project")
def ProjectsPage():
    return render_template('projects.html')

@app.route("/contact")
def ContactPage():
    return render_template('contact.html', flash_message = "False")

@app.route("/redirect")
def AfterMessage():
    return render_template('contact.html', flash_message = "True")

@app.route('/download')
def DowloadManager():
    path = "Resume.pdf"
    return send_file(path, as_attachment= True)

@app.route('/SendMessage', methods = ['GET','POST'])
def NotifyMe():
    if request.method == 'POST':
        subject = 'Message from Portfolio website'
        First_name = request.form['first_name']
        Last_name = request.form['last_name']
        Contact_to = request.form['email_id']
        Body = request.form['message']
        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('ownerwebsite14@gmail.com','nypcnfpmowyyuvcj')
            
            message = f'Subject: {subject} \n\n {Body} \n message from: {First_name} \t {Last_name} \n message to: {Contact_to}'
            print(type(message))
            smtp.sendmail('ownerwebsite14@gmail.com','nikunjsaini37@gmail.com',message)
        
    return redirect("/redirect")

if __name__ == "main":
    app.run(debug=True, host="0.0.0.0",port=5000)