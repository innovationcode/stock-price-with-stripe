from flask import Flask, render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.forms import RegistrationForm
import stripe
from config import Config
from flask_dance.contrib.github import make_github_blueprint, github


######################### BASIC ROUTE '/' AND '/INDEX'##############################
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')

########################## REGISTER ###########################
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

######################### LOGIN ###############################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(url_for('herokuapp'))
    return render_template('login.html', title='Sign In', form=form)

######################### LOGOUT ##############################
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


####################### Route for logged-in user to see basic stock-price-info
@login_required
@app.route('/herokuapp')
def herokuapp():
    return render_template('herokuapp.html')

####################### Route for logged-in user to update as premium-user
@login_required
@app.route('/premium')
def premium():
    user = User.query.filter_by(id=current_user.get_id()).first()
    if user.premium_user is True:
        return render_template('premium_already.html', current_user = user.username)
    else:
        return render_template('premium_update_form.html', pub_key = pub_key)

######################### STRIPE-PAYMENT-ACCEPT ROUTE to accept payment to update free-user to premium-user

pub_key = Config.STRIPE_PUB_KEY
secret_key = Config.STRIPE_SECRET_KEY
stripe.api_key = secret_key

@login_required
@app.route('/pay', methods = ['POST'])
def pay():
    if current_user.is_authenticated:
        customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

        charge = stripe.Charge.create(
            customer = customer.id,
            amount= 3999,
            currency ='usd',
            description= 'Premium User'
        )
        
        print(current_user.get_id())
        update_this = User.query.filter_by(id=current_user.get_id()).first()
        if update_this:
            update_this.premium_user = True
            db.session.commit()
            #flash('Congratulations, updated as premium_user!')

        return render_template('premium_response.html', current_user = update_this.username)

############################### Google-Login route ##############################################


################################ Github-Login route ############################################# 
github_blueprint = make_github_blueprint(client_id = Config.GITHUB_CLIENT_ID, client_secret = Config.GITHUB_CLIENT_SECRET)
#app.register_blueprint(github_blueprint, url_prefix = '/github.login')
app.register_blueprint(github_blueprint, url_prefix="/login")


@app.route('/github')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
        
    account_info = github.get('/user')

    if account_info.ok:
        print("YES ........................................DONE")
        account_info_json = account_info.json()

        return '<h1>GITHUB  DONE</h1>'
    return '<h1>Request failed'

################################ Twitter-Login route ############################################
############################### FORGOT-Password route ##############################################
############################### NEW---Password-setting###########################################
 



