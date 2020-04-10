from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login_manager

from app.models.forms import LogonForm
from app.models.forms import LoginForm
from app.models.forms import ReservaForm
from app.models.tables import User
from app.models.tables import Reserva
from app.models.tables import Quarto
from app.models import tables, forms

@login_manager.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/quartos', methods=["POST","GET"])
@app.route('/quartos.html', methods=["POST","GET"])
def quartos():
	form = ReservaForm()
	if request.method == 'POST':
		if "quarto1" in request.form:
			check_room = Quarto.query.filter_by(id=1).first()
			print(check_room)
			if str(check_room)=='True':
				return redirect(url_for('ocupado'))
			elif str(check_room)=='False':
				user_id = current_user.get_id()
				r=Reserva(user_id,1)
				db.session.add(r)
				db.session.commit()
				q=Quarto.query.filter_by(id=1).update(dict(reservado=1))
				db.session.commit()
				flash("Cadastrado com sucesso!")
				return redirect(url_for('reservado'))

		elif "quarto2" in request.form:
			check_room = Quarto.query.filter_by(id=2).first()
			if str(check_room)=='True':
				return redirect(url_for('ocupado'))
			elif str(check_room)=='False':
				user_id = current_user.get_id()
				r=Reserva(user_id,2)
				db.session.add(r)
				db.session.commit()
				q=Quarto.query.filter_by(id=2).update(dict(reservado=1))
				db.session.commit()
				flash("Cadastrado com sucesso!")
				return redirect(url_for('reservado'))

		elif "quarto3" in request.form:
			check_room = Quarto.query.filter_by(id=3).first()
			if str(check_room)=='True':
				return redirect(url_for('ocupado'))
			elif str(check_room)=='False':
				user_id = current_user.get_id()
				r=Reserva(user_id,3)
				db.session.add(r)
				db.session.commit()
				q=Quarto.query.filter_by(id=3).update(dict(reservado=1))
				db.session.commit()
				flash("Cadastrado com sucesso!")
				return redirect(url_for('reservado'))

		elif "quarto4" in request.form:
			check_room = Quarto.query.filter_by(id=4).first()
			if str(check_room)=='True':
				return redirect(url_for('ocupado'))
			elif str(check_room)=='False':
				user_id = current_user.get_id()
				r=Reserva(user_id,4)
				db.session.add(r)
				db.session.commit()
				q=Quarto.query.filter_by(id=4).update(dict(reservado=1))
				db.session.commit()
				flash("Cadastrado com sucesso!")
				return redirect(url_for('reservado'))
	return render_template('quartos.html', form=form)

@app.route('/fotos')
@app.route('/fotos.html')
def fotos():
	return render_template('fotos.html')

@app.route('/login', methods=["POST","GET"])
@app.route('/login.html', methods=["POST", "GET"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == form.password.data:
				login_user(user)
				# flash("Logado com sucesso")
				return redirect(url_for('quartos'))
			else:
				flash("Senha incorreta.")
		else:
			flash("Nome de usuário não encontrado")
	return render_template('login.html', form=form)


@app.route('/logon', methods=["POST","GET"])
@app.route('/logon.html', methods=["POST", "GET"])
def logon():
	form = LogonForm()
	#if request.method=="POST":
	if form.validate_on_submit():
		name=request.form.get("name")
		username=request.form.get("username")
		email=request.form.get("email")
		password=request.form.get("password")

		check_user = User.query.filter_by(username=form.username.data).first()
		check_email = User.query.filter_by(email=form.email.data).first()
		if check_user:
			flash("Nome de usuário já existe")
		elif check_email:
			flash("Email já cadastrado")
		else:
			if name and username and email and password:
				u=User(name,username,email,password)
				db.session.add(u)
				db.session.commit()
				flash("Cadastrado com sucesso!")
				return redirect(url_for('login'))
	return render_template('logon.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/reservado')
@app.route('/reservado.html')
def reservado():
	return render_template('reservado.html')

@app.route('/ocupado')
@app.route('/ocpuado.html')
def ocupado():
	return render_template('ocupado.html')
