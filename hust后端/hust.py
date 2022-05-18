
from flask_cors import CORS
from flask import Flask, render_template, url_for, request, json,jsonify

app = Flask(__name__)
CORS(app)
data = {}
with open("hust_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

@app.route('/data',methods=["GET"])
def getdata():
    return data

@app.route('/userlistselect', methods=["GET", 'POST'])
def userlistselect():
    if request.method == 'GET':
        return """<form method='post'>
        姓名<input type='text' name='name'>
        学号<input type='text' name='snumber'>
        专业<input type='text' name='academy'>
        资质通过情况<input type='text' name='qualify'>
        <input type='submit' value="查询">
        </form>
    """
    else:
        a=request.form.get("name")
        b=request.form.get("snumber")
        c=request.form.get("academy")
        d=request.form.get("qualify")
        lenth=len(data["user_info"])
        selectdata=[{
            "name":"",
            "snumber":"",
            "academy":"",
            "qualify":""
            }
        ]
        for i in range[0,lenth-1]:
            if a==data["user_info"][i]["name"] and data["user_info"][i]["snumber"]==b and data["user_info"][i]["academy"]==c and data["user_info"][i]["qualify"]==d:
                selectdata.append({"name":data["user_info"][i]["name"],"snumber":data["user_info"][i]["snumber"],"academy":data["user_info"][i]["academy"],"qualify":data["user_info"][i]["qualify"]})
        return selectdata

@app.route('/del_userinfo')
def data_del():
    lenth=len(data["user_info"])
    for i in range(0,lenth-1):
        if data["user_info"][i]["id"]==1:
            data["user_info"][i].clear()
    return data

@app.route('/userlogintest', methods=["GET", 'POST'])
def userlogintest():
    if request.method == 'GET':
        return """<form method='post'>
        用户名<input type='text' name='username'>
        密码<input type='password' name='password'>
        <input type='submit'>
        </form>
    """
    else:
        lenth=len(data["user_info"])
        a=request.form.get("username")
        b=request.form.get("password")
        for i in range(0,lenth-1):
            if data["user_info"][i]["username"]==a:
                if data["user_info"][i]["password"]==b:
                    return "登陆成功"
                else:
                    return "登陆失败"
        return "用户名不存在"

@app.route('/userlogin', methods=['GET','POST'])
def userlogin():
    if request.method == 'GET':
        lenth=len(data["user_info"])
        a=request.args.get("username","")
        b=request.args.get("password","")
        for i in range(0,lenth-1):
            if data["user_info"][i]["username"]==a:
                if data["user_info"][i]["password"]==b:
                    return "登陆成功！"
                else:
                    return "密码错误！"
        return "用户名不存在！"

@app.route('/adminlogintest', methods=["GET", 'POST'])
def adminlogintest():
    if request.method == 'GET':
        return """<form method='post'>
        用户名<input type='text' name='username'>
        密码<input type='password' name='password'>
        <input type='submit'>
        </form>
    """
    else:
        lenth=len(data["admin_info"])
        a=request.form.get("username")
        b=request.form.get("password")
        for i in range(0,lenth-1):
            if data["admin_info"][i]["username"]==a:
                if data["admin_info"][i]["password"]==b:
                    return "登陆成功"
                else:
                    return "登陆失败"
        return "用户名不存在"

@app.route('/adminlogin', methods=["GET", 'POST'])
def adminlogin():
    if request.method == 'GET':
        lenth=len(data["admin_info"])
        a=request.args.get("username")
        b=request.args.get("password")
        for i in range(0,lenth-1):
            if data["admin_info"][i]["username"]==a:
                if data["admin_info"][i]["password"]==b:
                    return "登陆成功！"
                else:
                    return "密码错误！"
        return "用户名不存在！"

@app.route('/registertest', methods=["GET", 'POST'])
def registertest():
    if request.method == 'GET':
        return """<form method='post'>
        用户名<input type='text' name='username'><br>
        密码<input type='password' name='password'><br>
        姓名<input type='text' name='name'><br>
        性别<input type='text' name='sex'><br>
        学院<input type='text' name='college'><br>
        班级<input type='text' name='class'><br>
        学号<input type='text' name='snumber'><br>
        专业<input type='text' name='academy'><br>
        生日<input type='text' name='birthdate'><br>
        QQ号<input type='text' name='qqnum'><br>
        联系方式<input type='text' name='contact'><br>
        <input type='submit'>
        </form>
    """
    else:
        i=len(data["user_info"])
        i=i+1
        data["user_info"].append({"id": i, "username": request.form.get("username"), "password": request.form.get("password"), "name":request.form.get("name"),"sex":request.form.get("sex"),"college":request.form.get("college"),"class":request.form.get("class"),"snumber":request.form.get("snumber"),"academy":request.form.get("academy"),"birthdate":request.form.get("birthdate"),"qqnum":request.form.get("qqnum"),"contact": request.form.get("contact")})
        with open("hust_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return "注册成功"

@app.route('/register', methods=["GET", 'POST'])
def register():
    if request.method == 'GET':
        a1=request.args.get("username")
        a2=request.args.get("password")
        a3=request.args.get("name")
        a4=request.args.get("sex")
        a5=request.args.get("birthdate")
        a6=request.args.get("snumber")
        a7=request.args.get("college")
        a8=request.args.get("academy")
        a9=request.args.get("class")
        a10=request.args.get("qqnum")
        a11=request.args.get("contact")
        i=len(data["user_info"])
        i=i+1
        data["user_info"].append({"id": i, "username": a1, "password": a2, "name":a3,"sex":a4,"college":a7,"class":a9,"snumber":a6,"academy":a8,"birthdate":a5,"qqnum":a10,"contact": a11})
        with open("hust_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        return "注册成功"

if __name__ =="__main__":
    app.run(debug=True,port=8081, host="0.0.0.0")