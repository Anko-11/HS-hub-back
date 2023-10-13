from app import creat_app
from flask_migrate import Migrate
from models import db

app = creat_app()
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
