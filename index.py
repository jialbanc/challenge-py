from flask import Flask, Blueprint
from flask import request, jsonify,abort

from challenge import CountryChallenge

challenge = CountryChallenge("csv/countries.csv")

api = Blueprint('api', __name__)


@api.route('/countries', methods=['GET'])
def countries():
    response = []
    if len(request.args) > 0:
        for arg in request.args:
            value = request.args.get(arg)
            if not challenge.isfloat(value):
                abort(400)
                
            if challenge.validateParams(arg):
                response = challenge.filter(arg, value)[['LOCATION','Country']].to_dict('records')
                break
    else:
        response = challenge.getAllCountries()[['LOCATION','Country']].to_dict('records')
    return jsonify(response)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/')

    app.run()
