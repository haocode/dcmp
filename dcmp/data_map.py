from flask import Flask,request,redirect,render_template
from flask import Response
import pandas as pd
import pymysql
import json
from flask import jsonify
app = Flask(__name__)

dbcon = pymysql.connect(
  host="",
    user="",
    password="",
    db="",
    port="",
    charset='',
  )

app.config['SECRET_KEY'] = "adddddddd"
@app.route("/")
def index():
    return render_template("data-map.html")



@app.route("/datamap",methods=['GET'])
def get_data_map():
    t_table = request.args.get('table_name')
    sql=""
    try:
        data = pd.read_sql(sql,dbcon)
    except:
        print "read data error"
    finally:
        pass
    if data is None:
        return "没有此表"
    else:
        data_list = (data.to_dict('records'))
        result_json = json.dump(data_list)
        resp = Response(result_json)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

