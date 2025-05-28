from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ..extensions import db
from ..models import Question, Answer
from flask import flash

questions_bp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_bp.route('/')
@login_required
def list_questions():
    questions = Question.query.order_by(Question.date_posted.desc()).all()
    return render_template('questions/list.html', questions=questions)

@questions_bp.route('/ask', methods=['GET', 'POST'])
@login_required
def ask_question():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        subject = request.form['subject']

        new_question = Question(
            title=title,
            content=content,
            subject=subject,
            author=current_user
        )
        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('questions.list_questions'))

    return render_template('questions/ask.html')

@questions_bp.route('/<int:question_id>', methods=['GET'])
@login_required
def question_detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('questions/detail.html', question=question)

@questions_bp.route('/<int:question_id>/answer', methods=['POST'])
@login_required
def answer_question(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']

    new_answer = Answer(
        content=content,
        question=question,
        author=current_user
    )
    db.session.add(new_answer)
    db.session.commit()

    return redirect(url_for('questions.question_detail', question_id=question.id))

@questions_bp.route('/<int:question_id>/delete', methods=['POST'])
@login_required
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    if question.author != current_user:
        flash("No tienes permiso para eliminar esta pregunta.", "danger")
        return redirect(url_for('questions.question_detail', question_id=question.id))
    
    db.session.delete(question)
    db.session.commit()
    flash("Pregunta eliminada correctamente.", "success")
    return redirect(url_for('questions.list_questions'))
