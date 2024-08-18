from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Target(Base):
    __tablename__ = "targets"
    
    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, index=True)
    redirect_by = Column(String)
    is_activate = Column(Boolean, default=True)

    logs = relationship("Log", back_populates="target_url")


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    user_agent = Column(String, index=True)
    target_id = Column(Integer, ForeignKey("targets.id"))

    target_url = relationship("Target", back_populates="logs")



from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, primary_key=True)
    is_active = Column(Integer, default=1)

class Target(Base):
    __tablename__ = 'targets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text, unique=True)
    redirect_by = Column(Text)
    is_active = Column(Integer, default=1)
    users_created_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', backref='targets')

class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_agents = Column(Text)
    ip_address = Column(Text)
    target_id = Column(Integer, ForeignKey('targets.id'))

    target = relationship('Target', backref='logs')