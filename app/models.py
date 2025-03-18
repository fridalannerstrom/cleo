from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from your_database_module import db  # Ersätt med din databasmodul
from flask_login import login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'  # Tabellnamn i din databas
    
    id = db.Column(db.Integer, primary_key=True)  # Primärnyckel för användaren
    username = db.Column(db.String(150), unique=True, nullable=False)  # Unikt användarnamn
    email = db.Column(db.String(150), unique=True, nullable=False)  # Unik email
    password = db.Column(db.String(200), nullable=False)  # Användarens lösenord
    
    def set_password(self, password):
        """Hashar lösenordet innan det sparas i databasen."""
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        """Kontrollerar om det angivna lösenordet matchar det lagrade hashade lösenordet."""
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Hämtar användaren från databasen baserat på ID
