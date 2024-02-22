from flask import Flask, request, render_template

# Flask Constructor
app = Flask(__name__)

# Route Endpoint
@app.route('/', methods=['GET'])
def index():
    ## Display HTML Form that I made
    return render_template('index.html')

# Read Form endpoint
@app.route('/read-form', methods=['POST'])
def read_form():
    # Get the form data as a python dictionary.
    data = request.form
    
    ## Return Information
    return {
        'Character Name': data['name'],
        'Character Age':  data['age'], 
        'Character Sex':  data['sex'],
        'Skin Color':   data['skin-color'],
        'Skin Traits':  data['skin-traits'],
        'Eye Color':    data['eye-color'],
        'Eye Traits':   data['eye-traits'],
        'Hair Color':   data['hair-color'],
        'Hair Traits':  data['hair-traits'],
        'Clothing':     data['clothing'],
        'Clothing Accessories':  data['accessories'],
        'Profession':   data['profession'],
        'Portrait Style':   data['portrait-style'],
        'Character Expression':   data['expression'],
    }

# Main function
if __name__ == '__main__':
    # Run application
    app.run()
