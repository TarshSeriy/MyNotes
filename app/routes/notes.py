from flask import Blueprint, render_template, redirect, url_for, flash
from app.models import db, Note, Category
from app.forms import NoteForm
from datetime import datetime

note_bp = Blueprint('notes', __name__)


@note_bp.route('/notes', methods=['GET'])
@note_bp.route('/', methods=['GET'])
def index():
    notes = Note.query.all()
    current_time = datetime.now().strftime('%H:%M')
    return render_template('index.html', notes=notes, current_time=current_time)


@note_bp.route('/notes/create', methods=['GET', 'POST'])
def create_note():
    form = NoteForm()
    if form.validate_on_submit():
        new_note = Note(
            title=form.title.data,
            content=form.content.data,
            category_id=form.category.data
        )
        db.session.add(new_note)
        db.session.commit()
        flash('Note created successfully!', 'success')
        return redirect(url_for('notes.index'))
    if not form.validate_on_submit():
        return render_template('create_note.html', form=form)


@note_bp.route('/<int:id>', methods=['GET'])
def view_note(id):
    note = Note.query.get_or_404(id)
    return render_template('view_note.html', note=note)


@note_bp.route('/notes/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.content = form.content.data
        note.category_id = form.category.data
        db.session.commit()
        flash('Note updated successfully!', 'success')
        return redirect(url_for('notes.index'))

    form.title.data = note.title
    form.content.data = note.content
    form.category.data = note.category_id
    return render_template('edit_note.html', form=form, note=note, submit_text="Update Note")


@note_bp.route('/notes/delete/<int:id>', methods=['POST'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted successfully!', 'success')
    return redirect(url_for('notes.index'))
