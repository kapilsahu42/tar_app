import os
from flask_restful import Resource 
from flask_jwt import jwt_required
from flask import Flask, request,flash,jsonify, send_from_directory ,redirect
import sqlite3
from resources.constants import UPLOAD_DIRECTORY
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['tar','pdf'])

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

class Item(Resource):

    @classmethod
    def allowed_file(cls,filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @jwt_required()
    def get(self,name):
        """Download a file."""
        file_path=f"{UPLOAD_DIRECTORY}/{name}"
        if os.path.isfile(file_path):
            return send_from_directory(UPLOAD_DIRECTORY, name, as_attachment=True)
        return "file doesnot exist", 201
        
    def post(self,name):
        """Upload a file."""
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_DIRECTORY, name))
                return "file uploaded", 201
            return "wrong file format", 200

class Itemlist(Resource):
    @jwt_required()
    def get(self):
        """Endpoint to list files on the server."""
        files = []
        for filename in os.listdir(UPLOAD_DIRECTORY):
            path = os.path.join(UPLOAD_DIRECTORY, filename)
            if os.path.isfile(path):
                files.append(filename)
        return jsonify(files)
