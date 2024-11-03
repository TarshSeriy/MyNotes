from app.routes.notes import note_bp
from app.routes.categories import category_bp


def register_blueprints(app):
    app.register_blueprint(note_bp, url_prefix='/')
    app.register_blueprint(category_bp, url_prefix='/categories')

