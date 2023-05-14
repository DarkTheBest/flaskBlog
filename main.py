from application import create_app, db
from authentication import models


app = create_app()

if __name__ == '__main__':
    db.create_all()
    app.run()

