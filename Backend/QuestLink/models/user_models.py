import sqlalchemy as sa
from QuestLink.models.db_session import Base

class User(Base):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    is_verified = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())


class Account(Base):
    __tablename__ = "accounts"
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"), nullable=False)
    login = sa.Column(sa.String(255), nullable=False)
    password = sa.Column(sa.String(255), nullable=False)
    is_superuser = sa.Column(sa.Boolean, default=False)
