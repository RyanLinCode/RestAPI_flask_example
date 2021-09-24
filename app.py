from flask import Flask

app = Flask(__name__)


store = [
    {
        'name': 'My Wonderful Store',
        'items':[
            {
                'name':'My Item',
                'price': 15.99
            }
        ]
    }
]

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass
# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name
def get_store(name):
    pass
# GET /store
@app.route('/store')
def get_store():
    pass

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_in_store():
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


def home():
    return "Hello, world"