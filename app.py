import requests
from flask import make_response, jsonify, Response
from flask_restful import Resource
from flask import Flask, request, render_template
from flask_restful import Api
import json
app = Flask(__name__, template_folder='templates')
api = Api(app)


@app.route("/")
def index():
    return render_template("c_o_w.html", message="Hello Flask!")


@app.route("/our_globe", methods=['POST', 'GET'])
def our_globe():
    response = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events').json()
    if request.method == 'GET':
        categories = []
        for data in response["events"]:
            for items in data["categories"]:
                categories.append(items["title"])
        categories = list(set(categories))
        return render_template("globe.html", categories=categories)
    else:
        metadata = []
        category = request.values.get("category", "")
        for data in response["events"]:
            for items in data["categories"]:
                if items["title"] == category:
                    metadata.append(data)
        return json.dumps(metadata)


class SmallBusinessAddressAPIView(Resource):
    """
        Api for creating address instance for small business relationship
    """

    def post(self):
        pass

    def put(self, obj_id):
        pass

    def delete(self, obj_id):
        pass


api.add_resource(SmallBusinessAddressAPIView, '/small_business/address', endpoint='create_address')
api.add_resource(SmallBusinessAddressAPIView, '/small_business/address/<int:obj_id>', endpoint='update_address')


if __name__ == '__main__':
    app.run(debug=True)
