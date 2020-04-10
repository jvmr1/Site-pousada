from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

# class Post(db.Model):
#     __tablename__ = "posts"
#
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     user = db.relationship('User', foreign_keys=user_id)
#
#     def __init__(self, content, user_id):
#         self.content = content
#         self.user_id = user_id
#
#     def __repr__(self):
#         return "<Post %r>" % self.id
#
#
# class Follow(db.Model):
#     __tablename__ = "follow"
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     user = db.relationship('User', foreign_keys=user_id)
#     follower = db.relationship('User', foreign_keys=follower_id)

class Quarto(db.Model):
    __tablename__ = "quartos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    #descricao = db.Column(db.String)
    reservado = db.Column(db.Boolean)

    def get_reservado(self):
        return str(self.reservado)

    def __init__(self, id, name, descricao, reservado):
        self.id = id
        self.name = name
        #self.descricao = descricao
        self.reservado = reservado

    def __repr__(self):
        return "%r" % self.reservado


class Reserva(db.Model):
    __tablename__ = "reserva"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quarto_id = db.Column(db.Integer, db.ForeignKey('quartos.id'))

    user = db.relationship('User', foreign_keys=user_id)
    quarto = db.relationship('Quarto', foreign_keys=quarto_id)

    def __init__(self, user_id, quarto_id):
        self.user_id = user_id
        self.quarto_id = quarto_id
