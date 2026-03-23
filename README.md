# 🚀 Personal Portfolio Website - Flask Version

Selamat datang di repositori portofolio saya! Proyek ini adalah website personal yang saya bangun untuk menampilkan hasil karya di bidang **UI/UX Design**, **Informatics Engineering**, dan **Full-stack Development**.

## ✨ Fitur Utama

-   **Email Service:** Form kontak fungsional menggunakan `Flask-Mail` dan SMTP Gmail.
-   **Project Showcase:** Menampilkan daftar proyek (seperti SIAKAD, ECO Cleaner, dll).
-   **Responsive Design:** Tampilan yang optimal di perangkat mobile maupun desktop.
-   **Environment Safety:** Menggunakan `python-dotenv` untuk menjaga keamanan API keys/App Passwords.

## 🛠️ Tech Stack

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

-   **Backend:** [Python](https://www.python.org/) & [Flask Framework](https://flask.palletsprojects.com/)
-   **Frontend:** HTML5, CSS3, JavaScript (Aesthetic & Minimalist Style)
-   **Tools:** Figma (Prototyping), VS Code, Git/GitHub
-   **Environment:** Docker & Spark (Lab Experience)

## 📁 Struktur Proyek

-   `app.py`: Logika utama backend Flask.
-   `templates/`: File HTML (Jinja2).
-   `static/`: Asset CSS, JavaScript, dan gambar.
-   `.env.example`: Template konfigurasi environment.

## ⚙️ Cara Menjalankan Secara Lokal

Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1.  **Clone Repository:**
    ```bash
    git clone https://github.com/username-kamu/portfolio-flask.git
    cd portfolio-flask
    ```

2.  **Setup Virtual Environment:**
    ```bash
    python -m venv venv
    # Untuk Windows:
    venv\Scripts\activate
    # Untuk macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Konfigurasi Environment:**
    Salin file `.env.example` menjadi `.env` di root proyek Anda.
    ```bash
    cp .env.example .env
    ```
    Buka file `.env` dan masukkan `MAIL_USERNAME` (alamat email Anda) dan `MAIL_PASSWORD` (App Password Gmail Anda) yang diperlukan untuk fungsionalitas email service.

5.  **Run Application:**
    ```bash
    python app.py
    ```

6.  **Akses Aplikasi:**
    Buka browser Anda dan akses `http://127.0.0.1:5000/`.

## 👩‍💻 Tentang Saya

Saya Aulia, mahasiswi Semester 4 Teknik Informatika di Universitas Bale Bandung (UNIBBA). Berfokus pada pengembangan aplikasi web dan desain antarmuka yang bersih serta fungsional.

## Template web (ThemeWagon)

(https://themewagon.com/themes/free-bootstrap-4-html5-responsive-portfolio-website-template-clyde/)
