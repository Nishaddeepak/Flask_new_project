from appone import app, db
from appone.models.item_model import Registertable


if __name__=="__main__":
    with app.app_context():
        Registertable()
    app.run(debug=True)

