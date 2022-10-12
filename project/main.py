from flask import Blueprint, render_template
from flask_login import login_required, current_user
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route('/base2')
def base2():    
    return render_template('base2.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')



@main.route('/special-dishes')
def specialdishes():
    return render_template('special-dishes.html')

@main.route('/team')
def teams():
    return render_template('team.html')

@main .route('/eror')
def eror():
    return render_template('error-404.html')

@main.route('/icons') 
def icons():
    return render_template('icon-material.html')

@main.route('/admin/home')
@login_required
def adminhome():
    return render_template('adminhome.html', name=current_user.name, email=current_user.email)

@main.route('/admin/reservation')
def adminprofile():
    return render_template('pages-profile.html') 
