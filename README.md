# 📝 To-Do API with Flask + Firebase

A secure and scalable **To-Do List API** built with [Flask](https://flask.palletsprojects.com/), [Firebase](https://firebase.google.com/), and [Firestore](https://firebase.google.com/docs/firestore).  
Supports **Google Authentication** 🔑, **CORS** 🌍, and **RESTful endpoints** ⚡.

---

## ✨ Features
- 🔒 **Firebase Authentication** (Google Sign-In tokens verification)
- 📦 **Firestore Database** for storing todos per user
- 🌐 **CORS enabled** for frontend integration
- ⚡ **Simple REST API** (GET & POST for todos)
- 🐍 Lightweight Flask backend

---

## 📂 Project Structure
```
.
├── app.py                # Flask app with routes
├── firebase_config.json  # Firebase Admin SDK service account key
├── requirements.txt      # Dependencies
└── README.md             # This file 😄
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/itz-Harsh/ToDo-API.git
cd ToDo-API
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv .venv
# On Windows:
.\.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add Firebase config
- Go to [Firebase Console](https://console.firebase.google.com/)  
- Create a project → Add **Firestore Database**  
- Generate a **Service Account Key** (JSON)  
- Save it as `firebase_config.json` in the root folder.

---

## 📌 API Endpoints

- Running on http://127.0.0.1:5000
<br>
 or
- Deployed Link of your Own Backend

### 🔐 Authentication
All requests require a **Bearer Token** from Firebase Authentication.  
Example:
```
Authorization: Bearer <your-firebase-id-token>
```

### 📖 Get Todos
**Endpoint**: `GET /todos`  
**Response**:
```json
[
  {
    "id": "abcd1234",
    "title": "Learn Flask",
    "done": false
  },
  {
    "id": "efgh5678",
    "title": "Build ToDo API",
    "done": true
  }
]
```

### ➕ Add Todo
**Endpoint**: `POST /todos`  
**Body**:
```json
{
  "title": "Finish project",
  "done": false
}
```

**Response**:
```json
{
  "message": "task added !"
}
```

---

## 🛠️ Tech Stack
- **Backend**: [Flask](https://flask.palletsprojects.com/) 🐍
- **Database**: [Firestore](https://firebase.google.com/docs/firestore) ☁️
- **Auth**: [Firebase Authentication](https://firebase.google.com/docs/auth) 🔑
- **Hosting (optional)**: [Render](https://render.com/), [Vercel](https://vercel.com/), or [Heroku](https://www.heroku.com/)

---

## 📦 requirements.txt
```txt
flask
flask-cors
firebase-admin
```

---

## 🎯 Future Improvements
- ✅ Update & Delete Todos
- ✅ Add user profile support
- ✅ Deploy on Render/Heroku
- ✅ Unit testing with Pytest

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to fork the repo and submit a PR ✨

---

## 📜 License
This project is licensed under the **MIT License**.

---

### 💡 Pro Tip
Pair this API with a **React / Next.js frontend** and build your own **full-stack ToDo App** 🚀
