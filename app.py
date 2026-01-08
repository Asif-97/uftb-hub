from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

# Flask অ্যাপ শুরু করুন
app = Flask(__name__)

# কনফিগারেশন
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

# এক্সটেনশনগুলো শুরু করুন
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# --- ডাটাবেস মডেল (User Table) ---
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student') # 'student' or 'supervisor'

    def __repr__(self):
        return f"User('{self.username}', '{self.role}')"

# --- লগইন এবং লগআউট রুট ---
@app.route("/", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.role == 'supervisor':
            return redirect(url_for('supervisor_dashboard'))
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            if user.role == 'supervisor':
                return redirect(url_for('supervisor_dashboard'))
            else:
                return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


# --- পেইজ রুট ---
@app.route("/dashboard")
@login_required 
def dashboard():
    return render_template("dashboard.html")

@app.route("/slides")
@login_required
def slides():
    return render_template("slides.html")

@app.route("/course_details")
@login_required
def course_details():
    return render_template("course_details.html")

@app.route("/slide_viewer")
@login_required
def slide_viewer():
    return render_template("slide_viewer.html")

@app.route("/question_bank")
@login_required
def question_bank():
    return render_template("question_bank.html")

@app.route("/practice_test")
@login_required
def practice_test():
    return render_template("practice_test.html")

@app.route("/repository")
@login_required
def repository():
    return render_template("repository.html")

@app.route("/project_details")
@login_required
def project_details():
    return render_template("project_details.html")

@app.route("/my_project")
@login_required
def my_project():
    return render_template("my_project.html")

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

# Supervisor Panel Pages
@app.route("/supervisor_dashboard")
@login_required
def supervisor_dashboard():
    return render_template("supervisor_dashboard.html")

@app.route("/manage_student")
@login_required
def manage_student():
    return render_template("manage_student.html")

@app.route("/upload_slides")
@login_required
def upload_slides():
    return render_template("upload_slides.html")

@app.route("/add_questions")
@login_required
def add_questions():
    return render_template("add_questions.html")

@app.route("/analytics")
@login_required
def analytics():
    return render_template("analytics.html")

@app.route("/announcements")
@login_required
def announcements():
    return render_template("announcements.html")

# সার্ভারটি রান করার জন্য
if __name__ == "__main__":
    app.run(debug=True)