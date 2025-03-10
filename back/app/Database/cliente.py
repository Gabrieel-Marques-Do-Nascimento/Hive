"""Database models for user and contact management.

This module defines SQLAlchemy models for managing users and their contacts
in the application database. It includes:

- Users: Model for storing user account information
- Contacts: Model for storing user contact relationships

The models use SQLAlchemy for object-relational mapping and include 
proper relationships and constraints between tables.
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


data_str = datetime.strftime(datetime.now(),   "%d %m %Y %H:%M")
data_objt = datetime.strptime(data_str,   "%d %m %Y %H:%M")


class Users(db.Model):
    """Database model class for Users table.

    This class represents the Users table in the database and defines
    its schema and relationships.

    Attributes:
        id (int): Primary key for the user
        username (str): Unique username for the user
        password (str): Hashed password for the user
        email (str): Unique email address for the user
        email_verify (bool): Whether email has been verified
        online (datetime): Last online timestamp
        created_at (datetime): Account creation timestamp
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    bio = db.Column(db.String(200), default="")
    update = db.Column(db.DateTime, default=datetime.now())
    email_verify = db.Column(db.Boolean, default=False)
    online = db.Column(db.DateTime, default=datetime.now())
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Users {self.id}>'


class Contacts(db.Model):
    """Database model class for Contacts table.

    This class represents the Contacts table in the database and defines
    its schema and relationships.

    Attributes:
        id (int): Primary key for the contact
        userId (int): Foreign key reference to Users table
        contactId (int): ID of the contact
        created_at (datetime): Contact creation timestamp
        user (relationship): Relationship to Users table
    """
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, db.ForeignKey("users.id"),
                        nullable=False)  # Chave estrangeira para Users
    custom_name = db.Column(db.String(50), nullable=True)
    contact_Id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    # Relacionamento com Users
    user = db.relationship('Users', backref=db.backref('contacts', lazy=True))

    def __repr__(self):
        return f'<Contacts {self.id}>'


class Messages(db.Model):
    """Database model class for Messages table.
    This class represents the Messages table in the database and defines
    its schema and relationships.
    Attributes:
        id (int): Primary key for the message
        userId (int): Foreign key reference to Users table
        to (int): ID of the sender

        other_Id (int): ID of the person
        message (str): Content of the message
        created_at (datetime): Message creation timestamp
        user (relationship): Relationship to Users table
    """
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    user_Id = db.Column(db.Integer, db.ForeignKey("users.id"),
                        nullable=False)  # Chave estrangeira para Users
    to = db.Column(db.Integer, nullable=True)  # para quem vai a mensagem
    other_Id = db.Column(db.Integer)  # id do outro usuario
    message = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    # Relacionamento com Users
    user = db.relationship('Users', backref=db.backref('messages', lazy=True))

    def __repr__(self):
        return f'<Mensagem {self.id}>'


# class Notify(db.Model):
#     """Database model class for Notify table.
#     This class represents the Notify table in the database and defines
#     its schema and relationships.
#     Attributes:
#         id (int): Primary key for the notification
#         user_id (int): Foreign key reference to Users table
#         contact_update (int): Update status for contact
#     """
#     __tablename__ = 'notify'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     contact_update = db.Column(db.Integer, nullable=False)
