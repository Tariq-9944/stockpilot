from flask import Blueprint, render_template, request, redirect, url_for

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    return "User registration page"

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return "User login page"

@user_bp.route('/dashboard')
def dashboard():
    return "User dashboard"
