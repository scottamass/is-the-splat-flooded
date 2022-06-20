from flask import Flask
from flask import request, jsonify
import datetime as dt



app = Flask(__name__)
app.config["DEBUG"] = True

status = [{'Status':'no',"timestamp":"2015-10-21T09:47:50-04:00"}]

@app.route('/', methods=['GET'])
def home():
    return '''<h2>Has the Splat Flooded</h2>
<h1>No</h1>'''

@app.route('/api/flood', methods=['GET'])
def flood():
    return jsonify(status)


@app.route('/api/flood', methods=['POST'])
def update_status():
    data= request.json
    yes={'Status': 'yes'}
    no ={'Status': 'no'}
    print(data)
    result = data['Status']
    out={"Status": result,'timestamp':dt.datetime.now()}
    if "yes" or "no" in result:
        status.append(out)
        return out
    else: return "error"
  


if __name__ == '__main__':
    app.run(debug=True)
