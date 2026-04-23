🚀 Deployment Guide (FastAPI API with Custom Domain & HTTPS)

This guide explains how to deploy the FastAPI application on a server and connect it to a custom domain with HTTPS.

---

📦 Prerequisites

- A cloud server (AWS EC2 / DigitalOcean / VPS)
- A domain name (e.g. from GoDaddy / Namecheap)
- SSH access to the server
- Python 3 installed
- Git installed

---

🖥️ Step 1: Connect to Server

ssh username@your-server-ip

---

📥 Step 2: Clone the Repository

git clone https://github.com/your-username/your-repo.git
cd your-repo

---

🧪 Step 3: Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

---

📦 Step 4: Install Dependencies

pip install -r requirements.txt

---

⚙️ Step 5: Run API (Testing)

uvicorn app.main:app --host 0.0.0.0 --port 8000

Open in browser:

http://your-server-ip:8000/docs

---

🔁 Step 6: Run in Production (Gunicorn)

pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app

---

🌐 Step 7: Setup Nginx

Install Nginx

sudo apt update
sudo apt install nginx

Create Config File

sudo nano /etc/nginx/sites-available/api

Add Configuration

server {
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

Enable Config

sudo ln -s /etc/nginx/sites-available/api /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

---

🌍 Step 8: Connect Domain to Server

Go to your domain provider DNS settings:

- Add an A Record
  - Host: @
  - Value: your-server-ip

---

🔒 Step 9: Enable HTTPS (SSL Certificate)

Install Certbot

sudo apt install certbot python3-certbot-nginx

Generate SSL Certificate

sudo certbot --nginx -d yourdomain.com

Follow the prompts to complete setup.

---

🔄 Step 10: Auto Renew SSL

sudo certbot renew --dry-run

---

🔥 Optional: Run App in Background (Recommended)

Using systemd

Create service file:

sudo nano /etc/systemd/system/api.service

Paste:

[Unit]
Description=FastAPI App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/your-repo
ExecStart=/home/ubuntu/your-repo/venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
Restart=always

[Install]
WantedBy=multi-user.target

Run:

sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl start api
sudo systemctl enable api

---

✅ Final Check

Open:

https://yourdomain.com

---

🎯 Notes

- Ensure ports 80 and 443 are open in firewall
- Keep environment variables secure
- Use ".env" file for secrets (optional improvement)

---

🎉 Deployment Complete!

Your FastAPI API is now live with a custom domain and HTTPS 🚀