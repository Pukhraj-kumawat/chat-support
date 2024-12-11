# WhatsApp Messaging System

This project demonstrates the integration of WhatsApp with a Django application. Follow the steps below to set it up and start receiving messages in the Django admin panel.

---

## Prerequisites
- Node.js installed on your system
- Python 3.x installed
- Django installed
- pip (Python package manager)
- Git installed

---

## Step 1: Clone the WhatsApp Integration Repository
    	1.  git clone https://github.com/Pukhraj-kumawat/whatsapp
	2. switch to main branch
	3. cd whatsapp
	4. npm install
	5. nodemon server.js


## Step 2: Link WhatsApp Account
	1.	Open your browser and go to: http://localhost:3000/scanqr
	2.	A QR code will be displayed on the screen.
	3.	Open the WhatsApp app on your phone.
	4.	Go to Settings > Linked Devices > Link a Device.
	5.	Scan the QR code displayed in the browser.

Your WhatsApp account is now linked to the application.


## Step 3: Clone the Current Project

	1. git clone https://github.com/Pukhraj-kumawat/chat-support
	2. cd chatSupport
	3. pip install -r requirements.txt
	4. python3 manage.py migrate
	5. python3 manage.py runserver


## Step 4: Send Messages to the Linked WhatsApp Account
	1.	Use any other device to send a message to the linked WhatsApp account.
	2.	These messages will be captured by the application.



## Step 5: View Messages in the Admin Panel
	1.	Open the Django admin panel in your browser: http://localhost:8000/admin.
	2.	Log in using your admin credentials.
	3.	Navigate to the WhatsAppMessage model to view the stored messages.
