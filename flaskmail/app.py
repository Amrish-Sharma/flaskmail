from flask import Flask, request, render_template, url_for,redirect
from flask_mail import Mail, Message


app = Flask(__name__)
#app.config to be updated with your username and password
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'your@gmail.com',
	MAIL_PASSWORD='yourpassword',
    MAIL_ASCII_ATTACHMENTS=True
	)
#created object of Mail
mail=Mail(app)
#when the app is started, we are in this default page index.html having link of more info to download page
@app.route('/')
def index():
    return render_template('index.html')

# After we are redirected from the index.html and download.html appears we need to input the email address and click on submit button

@app.route('/download')
def download():
    return render_template('download.html')

# When submit button is clicked as method post below function is called to take the value of receiveremail and create
@app.route('/download', methods=['POST'])
def mail_send():
    receiveremail = request.form['rec_mail']
    
    msg = Message( 'Hello', 
                sender ='yourId@gmail.com', 
                recipients = receiveremail 
               )
    #You can change the content of the mailbody as per your requirement
    msg.body = 'Please find attached the pdf'
    # Change the filename to attach
    msg.attach(filename='filetobesent.pdf', content_type="application/pdf")
    mail.send(msg)
    return "Mail sent successfully"


if __name__ == "__main__":
    app.run(debug=True)

