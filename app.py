from flask import Flask,request

app=Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}"
@app.route("/")
def home():
    return """
<body>
<a href="/hello/robin">name</a>
</body>
"""

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "Logging in..."+request.args.get("username")
    return """
    
    <form method="POST">
        <input type="text" name="username"/>

        <input type="SUBMIT"/>
    </form>
"""

if __name__ == '__main__':
    app.run(debug=True)