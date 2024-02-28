from flask import Flask, request, render_template
from datetime import datetime
import json

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

  current_timestamp = datetime.now()
  timestamp_string = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

  print(data)

  ## Return Information
  raw_character_json = {
      'Character': {
          'Character Name': data['name'],
          'Character Age': data['age'],
          'Character Sex': data['sex'],
          'Character Expression': data['expression'],
          'Character Profession': data['profession'],
      },
      'Appearance': {
          'Skin': {
              'Skin Color': data['skin-color'],
              'Skin Traits': data['skin-traits']
          },
          'Eyes': {
              'Eye Color': data['eye-color'],
              'Eye Traits': data['eye-traits']
          },
          'Hair': {
              'Hair Color': data['hair-color'],
              'Hair Traits': data['hair-traits']
          }
      },
      'Clothing': {
          'Worn Attire': data['attire'],
          'Worn Accessories': data['accessories']
      },
      'Style': {
          'Portrait Style': data['portrait-style'],
      },
      'Backend': {
          'Owner': data['username'],
          'Recieved': f'{timestamp_string}',
          'Version': data['form-version']
      }
  }

  new_character = raw_character_json

  print(new_character)

  return (raw_character_json)


# Main function
if __name__ == '__main__':
  # Run application
  app.run(host='0.0.0.0', port=81)
