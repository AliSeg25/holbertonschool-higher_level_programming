#!/usr/bin/python3
"""Defines the State class and links to the states t
able in the database"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""Base = declarative_base() crée une instance de la
classe declarative_base de SQLAlchemy qui est utilisée pour
définir des classes de modèles en tant que classe de base.
Cette classe fournit une variété de fonctionnalités utiles
pour définir et interagiravec des objets de base de données."""
Base = declarative_base()


class State(Base):

    """La ligne de code __tablename__ = 'states'
    est utilisée pour lier la classe Python à la table MySQL"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
