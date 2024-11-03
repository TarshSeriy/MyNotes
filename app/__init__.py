from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Создаем экземпляр SQLAlchemy и Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///note.db'

    # Инициализируем SQLAlchemy и Migrate с приложением
    db.init_app(app)
    migrate.init_app(app, db)

    # Создаем все таблицы
    with app.app_context():
        db.create_all()

    # Регистрируем блюпринты
    from app.blueprints import register_blueprints
    register_blueprints(app)

    return app


