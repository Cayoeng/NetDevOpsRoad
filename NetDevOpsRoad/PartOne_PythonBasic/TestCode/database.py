
import requests
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

#----------------------------sqlit3------------------------------
engine = create_engine('sqlite:///sqlalchemy_sqlite3.db?check_same_thread=False',
                       # echo=True
                       )

Base = orm.declarative_base()