#  Late Show API Challenge

A RESTful API built with Flask to manage guest appearances on a fictional late-night talk show. The app supports user authentication, and provides endpoints to view and manage episodes, guests, and appearances.

## 🚀 Tech Stack

- Python 3.11
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-Migrate
- SQLAlchemy
- PostgreSQL
- Postman (for API testing)

---

## 📁 Project Structure

late_show_api_challenge/
├── server/
│ ├── app.py
│ ├── extension.py
│ ├── models/
│ │ ├── guest.py
│ │ ├── episode.py
│ │ ├── appearance.py
│ │ └── user.py
│ ├── controllers/
│ │ ├── auth_controller.py
│ │ └── appearance_controller.py
│ └── seed.py
├── migrations/
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/late_show_api_challenge.git
   cd late_show_api_challenge
Create a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables (e.g. in .env):

ini
Copy
Edit
FLASK_APP=server.app
FLASK_ENV=development
JWT_SECRET_KEY=your_secret_key
Set up the database:

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed the database:

bash
Copy
Edit
python server/seed.py
Run the app:

bash
Copy
Edit
flask run
🔐 Authentication
Register a User
POST /register
Body:

json
Copy
Edit
{
  "username": "yourname",
  "password": "yourpassword"
}
Login to get a JWT Token
POST /login
Body:

json
Copy
Edit
{
  "username": "yourname",
  "password": "yourpassword"
}
Response:

json
Copy
Edit
{
  "access_token": "your.jwt.token"
}
Using the Token in Protected Routes
Add the token in Postman under Headers:

makefile
Copy
Edit
Key: Authorization
Value: Bearer your.jwt.token
📌 Key Endpoints
Endpoint	Method	Description
/register	POST	Register a new user
/login	POST	Login and get access token
/appearances	GET	View all appearances (Protected)
/appearances	POST	Create an appearance (Protected)
/episodes	GET	View all episodes
/guests	GET	View all guests

