# CodeQuest-Cyberia
CodeQuest, learn C++ while playing a game!

CodeQuest: Cyberia

CodeQuest: Cyberia is an interactive coding adventure game designed to teach you the fundamentals of C++ programming while exploring a dynamic, cyber-themed universe. As a young coder, you discover a hidden virtual world known as Cyberia, where regions are locked by puzzles that can only be solved by writing and debugging C++ code.

Features
- Interactive tutorials and coding challenges designed for beginners.
- Split-screen interface with a code editor and real-time output display.
- Progress through levels, each introducing new C++ concepts.
- Earn badges, points, and customization options for your avatar.
- Explore different regions of Cyberia and defeat the rogue AI.
- Accessible via web browsers, ensuring availability on multiple devices.

Game Description
Join the quest, solve the puzzles, and become a coding hero in Cyberia! "CodeQuest: Cyberia" offers a fun and engaging way to learn and practice C++ programming. Whether you are a beginner or looking to sharpen your coding skills, this game is designed to make learning enjoyable.

Getting Started

Prerequisites
- Python 3.8 or higher
- Flask
- Gunicorn
- Node.js (for frontend dependencies, optional)

Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

2. Set up the backend:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Ensure you have Node.js and npm installed (optional, if you plan to use additional frontend tools).

4. Create necessary files:
   - Add a `Procfile` to your project directory:
     ```plaintext
     web: gunicorn app:app
     ```
   - Create `runtime.txt` to specify the Python version:
     ```plaintext
     python-3.8.10
     ```

Running the Application

1. Run the Flask application locally:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

Deployment

Deploying to Heroku

1. Login to Heroku:
   ```bash
   heroku login
   ```

2. Create a Heroku app:
   ```bash
   heroku create
   ```

3. Push your code to Heroku:
   ```bash
   git push heroku master
   ```

4. Open your Heroku app:
   ```bash
   heroku open
   ```

Contributing
Contributions are welcome! Please fork this repository and submit pull requests with improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or feedback, feel free to contact me at manicjax99@gmail.com.

---

Join the quest, solve the puzzles, and become a coding hero in CodeQuest: Cyberia!

