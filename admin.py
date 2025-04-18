from flask import Blueprint, render_template, redirect, url_for

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def admin_dashboard():
    return "Admin dashboard: manage users and finances"
