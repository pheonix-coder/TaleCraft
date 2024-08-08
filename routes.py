from flask import render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, current_user, login_required
from markdown import markdown
from models import User, Story
from ai import generate_story
from sqlalchemy.exc import IntegrityError


def register_routes(app, db, bcrypt):
    @app.route("/")
    def index():
        return render_template("index.html", user=current_user)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("stories"))
            flash("Invalid username or password")
        return render_template("login.html")

    @app.route("/signup", methods=["GET", "POST"])
    def signup():
        if request.method == "POST":
            username = request.form["username"]
            name = request.form["name"]
            password = request.form["password"]
            email = request.form["email"]
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_user = User(
                name=name, username=username, email=email, password=hashed_password
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("login"))
            except IntegrityError:
                db.session.rollback()
                flash("Username or email already exists")
        return render_template("signup.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("index"))

    @app.route("/stories")
    @login_required
    def stories():
        user_stories = Story.query.filter_by(user_id=current_user.id).all()
        for story in user_stories:
            story.story = markdown(story.story)
        return render_template("stories.html", stories=user_stories)

    @app.route("/create_story", methods=["GET", "POST"])
    @login_required
    def create_story():
        if request.method == "POST":
            title = request.form["title"]
            theme = request.form["theme"]
            place = request.form["place"]
            prompt = request.form["prompt"]
            story_prompt, story_text = generate_story(theme, place, prompt)
            new_story = Story(
                title=title,
                user_id=current_user.id,
                prompt=story_prompt,
                story=story_text,
            )
            db.session.add(new_story)
            db.session.commit()
            return redirect(url_for("stories"))
        return render_template("create_story.html")

    @app.route("/delete_story/<int:story_id>", methods=["DELETE"])
    @login_required
    def delete_story(story_id):
        story = Story.query.get_or_404(story_id)
        db.session.delete(story)
        db.session.commit()
        flash("Story deleted successfully.")
        return "", 204
