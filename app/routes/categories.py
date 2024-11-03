from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request
from app import db
from app.models import Category
from app.forms import CategoryForm

category_bp = Blueprint('categories', __name__)

@category_bp.route('/categories', methods=['GET', 'POST'])
def list_categories():
    categories = Category.query.all()
    form = CategoryForm()
    return render_template('categories/list.html', categories=categories, form=form)

@category_bp.route('/categories/create', methods=['GET', 'POST'])
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        new_category = Category(name=form.name.data)
        db.session.add(new_category)
        db.session.commit()
        flash('Category created successfully!', 'success')
        return redirect(url_for('categories.list_categories'))
    return render_template('categories/create_category.html', form=form)

@category_bp.route('/categories/edit/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        category.name = form.name.data
        db.session.commit()
        flash('Category updated successfully!', 'success')
        return redirect(url_for('categories.list_categories'))
    return render_template('categories/edit.html', form=form, category=category)

@category_bp.route('/categories/delete/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted successfully!', 'success')
    return redirect(url_for('categories.list_categories'))



