#!/usr/bin/python3
""" Unique FileStorage instance for the application """
from models.engine.file_storage import FileStorage

''' Variable instance of FileStorage'''
storage = FileStorage()
storage.reload()
