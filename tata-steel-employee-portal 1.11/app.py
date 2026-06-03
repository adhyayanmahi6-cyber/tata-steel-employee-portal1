from flask import Flask,render_template,request,redirect,session
import sqlite3
app=Flask(__name__); app.secret_key='secret'; DB='employees.db'
def db():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
@app.route('/')
def home(): return render_template('home.html')
@app.route('/login',methods=['GET','POST'])
def login():
    m=''
    if request.method=='POST':
        c=db(); u=c.execute('select * from employees where employee_id=? and password=?',(request.form['employee_id'],request.form['password'])).fetchone(); c.close()
        if u: session['employee_id']=u['employee_id']; return redirect('/dashboard')
        m='Invalid Employee ID or Password'
    return render_template('login.html',message=m)
@app.route('/signup',methods=['GET','POST'])
def signup():
    m=''
    if request.method=='POST':
        c=db()
        try:
            c.execute('insert into employees(employee_name,employee_id,department_name,password) values(?,?,?,?)',(request.form['name'],request.form['employee_id'],request.form['department'],request.form['password']))
            c.commit(); c.close(); return redirect('/login')
        except: m='Employee ID already exists'; c.close()
    return render_template('signup.html',message=m)
@app.route('/dashboard')
def dashboard():
    if 'employee_id' not in session: return redirect('/login')
    c=db(); u=c.execute('select * from employees where employee_id=?',(session['employee_id'],)).fetchone(); c.close()
    return render_template('dashboard.html',user=u)
@app.route('/logout')
def logout(): session.clear(); return redirect('/')
if __name__=='__main__': app.run(host="0.0.0.0", port=8000, debug=True)
