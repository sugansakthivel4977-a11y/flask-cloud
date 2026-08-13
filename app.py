from flask import Flask
app=Flask(_name_)
@app.route('/')
def home():
     return"<h1>Hello from Cloud!</h1><p>Deployed on Render</p>"
@app.route('/status')
def status ():
    return{
       "status":"running",
       "server":"Render"
}
if_name_=="_main_":
app.run(host="0.0.0.0",port=5000)