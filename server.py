from flask import Flask, render_template, request, redirect
from user import User
from flask import app
# ...server.py

app = Flask(__name__)




from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)


@app.route('/')
@app.route('/users')
def index():

    users = User.get_all()
    print(users)
    return render_template("Read(All).html", all_users = users)

@app.route('/create_user', methods=["POST"])
def create_user():

    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    id= User.save(data)
    return redirect(f'/users/{id}')

@app.route('/new_page', methods=["POST"])
def new_page():
    return render_template('create.html')

@app.route('/Read(All)')
def all_user():
    return render_template('Read(All).html')

@app.route('/edit/<int:id>')
def edit_user(id):
    user = User.data({'id': id})
    
    return render_template('edit.html', user=user)

@app.route('/update/<int:id>', methods=["POST"])
def update_user(id):
    data = {
        'id': id,
        **request.form
    }
    User.update(data)
    return redirect(f'/users/{id}')

@app.route('/users/<int:id>')
def one_user(id):
    user = User.data({'id': id})
    print (user)
    return render_template('read(one).html', user=user)

@app.route('/show/<int:id>')
def show_user(id):
    user = User.data({'id': id})
    print(user) 
    return redirect(f'/users/{id}')

@app.route('/delete/<int:id>', methods=["POST"])
def delete_user(id):
    User.delete({'id': id})
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)



if __name__ == "__main__":
    app.run(debug=True)
