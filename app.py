from flask import Flask, render_template, request, redirect
from backend.db import db_operations
from backend.auth import auth 
from backend.storage import storage
from backend.crypto import cryptomanager

app = Flask(__name__, template_folder='frontend/templates')

backend = db_operations()
backend_auth = auth()
cryptomanager = cryptomanager()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        if username and password and email:
            hashed_password = auth.hash_password(password)
            backend.adduser(username, hashed_password, email)  
            return redirect('/login') 
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = backend.get_user(username)
            return user
        passw = backend_auth.verify_password(password)
        if user and passw:
                # session variable needed
                    print("User logged in")
    return render_template("dashboard.html")

storage_instance = storage()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400  

        file = request.files['file']

        if file.filename == '':
            return "No selected file", 400  

        try:
            file_data = storage_instance.get_file_binary(file) 

            return "File uploaded successfully!", 200  
        except Exception as e:
            return f"Error processing file: {str(e)}", 500
    return render_template('dashboard.html')


   

   


#UPLOAD 
@app.route('/upload', methods=['GET', 'POST'])
def upload(uploaded = False):
    if request.method == 'GET':
         return render_template ('upload.html')
      
    if 'file' not in request.files:
        return 'No file attached', 400
         
    file = request.files['file']
         
    if file:
     storage.save_file(file)
     return redirect(url_for('dashboard'))
    


@app.route('/dashboard')
def dashboard():
<<<<<<< Updated upstream
     return render_template('dashboard.html')
=======
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_data = []
    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        if os.path.isfile(file_path):
            #get in kb
            file_size = round(os.path.getsize(file_path) / 1024, 2)
            last_modified = datetime.utcfromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            
            file_data.append({
                'name': file,
                'size': file_size,
                'last_modified': last_modified
            })

    return render_template('dashboard.html')
         
         
        
      
@app.route('/download/<filename>')
def download_files(filename):
     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
>>>>>>> Stashed changes

if __name__ == '__main__':
    
    app.run(debug=True)
