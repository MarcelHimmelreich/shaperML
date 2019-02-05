import os
from flask import Flask, request, redirect, url_for
from flask import Blueprint



UPLOAD_FOLDER = '/path/upload'
AllOWED_EXTENSIONS = set(['csv', 'json', 'jsonl', 'html', 'xls', 'xlsx'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower in AllOWED_EXTENSIONS


