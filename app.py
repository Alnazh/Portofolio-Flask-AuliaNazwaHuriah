import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv

# Load variabel dari file .env
load_dotenv()

app = Flask(__name__)
# Mengambil secret key dari .env atau gunakan default jika tidak ada
app.secret_key = os.getenv('SECRET_KEY', 'dev_key_123')

# Konfigurasi SMTP Gmail menggunakan Environment Variables
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog-single')
def single():
    return render_template('single.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Alamat email penerima diambil dari .env (biasanya emailmu sendiri)
    recipient_email = os.getenv('MAIL_USERNAME')

    msg = Message(subject=f"New Message from Portfolio: {subject}",
                  recipients=[recipient_email],
                  body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    try:
        mail.send(msg)
        return "<script>alert('Pesan terkirim! Terima kasih, Aulia akan segera membalas.'); window.location.href='/';</script>"
    except Exception as e:
        # Error log tetap muncul di terminal tapi tidak membocorkan password ke user
        print(f"Error: {e}")
        return "<script>alert('Gagal mengirim pesan. Silakan coba lagi nanti.'); window.history.back();</script>"

if __name__ == '__main__':
    app.run(debug=True)