from taskmanager import db


class Category(db.Model):
    # schema for the category model
    id = db.Column(db.Integer, primary_key=True)
    Category_name = db.Column(db.string(25), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='category', cascade="all, delete", lazy=True) # noqa

    def __repr__(self):
        # __repr__ to represent itself in thre form of a string
        return self.Category_name


class Task(db.Model):
    # schema for the task model
    id = db.Column(db.Integer, primary_key=True)
    Task_name = db.Column(db.String(50), unique=True, nullable=False)
    Task_description = db.Column(db.text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', onedelete="CASCADE"), nullable=False) # noqa

    def __repr__(self):
        return "#{0} - Task {1} | Urgent: {2}".format(
            self.id, self.Task_name, self.is_urgent
        )
