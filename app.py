from flask import Flask



app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "chair", "price": 15.99}]}]


@app.get("/store")  # localhost:5000/store
def get_stores():
    pass


@app.get("/item")  # localhost:5000/item
def get_all_items():
    pass


@app.post("/store")  # localhost:5000/stores
def create_stores():

    pass


@app.post("/item")
def create_item():
    pass


@app.get("/store/<string:store_id>")
def get_store(store_id):
    pass


@app.get("/item/<string:item_id>")
def get_item(item_id):
    pass


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    pass


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    pass


@app.put("/item/<string:item_id>")
def update_item(item_id):
    pass
