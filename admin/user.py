from . import admin_bp
from flask import render_template


@admin_bp.get("/user")
def user():
    module = 'user'
    return render_template('admin/user/user.html', module=module)


@admin_bp.get("/user/add")
def add_user():
    module = 'user'
    return render_template('admin/user/add.html', module=module)


@admin_bp.get("/user/edit")
def edit_user():
    module = 'user'
    return render_template('admin/user/edit.html', module=module)


@admin_bp.get("/user/confirm-delete")
def confirm_delete():
    module = 'user'
    return render_template('admin/user/confirm_delete.html', module=module)
