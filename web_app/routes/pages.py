from flask import Blueprint, render_template

mainpage_bp = Blueprint("mainpage", __name__)


@mainpage_bp.route('/')
def mainpage():
    return render_template("mainpage.html", title="Pizza Main page")


menu_bp = Blueprint("menupage", __name__)


@menu_bp.route('/menu')
def menu():
    return render_template("mainpage.html", title="Pizza Menu page")


services_bp = Blueprint("services", __name__)


@services_bp.route('/services')
def menu():
    return render_template("mainpage.html", title="Pizza Services page")


blog_bp = Blueprint("blog", __name__)


@blog_bp.route('/blog')
def menu():
    return render_template("mainpage.html", title="Pizza Blog page")


about_bp = Blueprint("about", __name__)


@about_bp.route('/about')
def menu():
    return render_template("mainpage.html", title="Pizza About page")


contact_bp = Blueprint("contact", __name__)


@contact_bp.route('/contact')
def menu():
    return render_template("mainpage.html", title="Pizza Contact page")
