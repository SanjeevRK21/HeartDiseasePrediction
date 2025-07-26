from app import db, app  # Import db and app

# Create database tables
with app.app_context():
    db.create_all()
    print("Database initialized successfully!")
