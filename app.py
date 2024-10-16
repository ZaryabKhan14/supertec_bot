# # import os
# # from openai import OpenAI
# # from flask import Flask, request, jsonify, send_from_directory, render_template
# # import speech_recognition as sr
# # from pydub import AudioSegment
# # from dotenv import load_dotenv

# # load_dotenv()

# # app = Flask(__name__)

# # # Directory where audio files will be saved
# # AUDIO_DIR = os.path.join(os.getcwd(), 'static')
# # if not os.path.exists(AUDIO_DIR):
# #     os.makedirs(AUDIO_DIR)

# # # Set your OpenAI API key here

# # # Set OpenAI API key
# # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # def transcribe_audio(file_path):
# #     recognizer = sr.Recognizer()
    
# #     # Convert to a format that the recognizer supports (WAV)
# #     sound = AudioSegment.from_file(file_path)
    
# #     # Export audio to WAV format for better recognition
# #     wav_file = file_path.replace('.wav', '_transcoded.wav')
# #     sound.export(wav_file, format='wav')

# #     # Load the WAV file for transcription
# #     with sr.AudioFile(wav_file) as source:
# #         audio = recognizer.record(source)

# #         try:
# #             # Transcribe the audio file to text
# #             transcription = recognizer.recognize_google(audio)
# #             return transcription
# #         except sr.UnknownValueError:
# #             return "Speech not recognized"
# #         except sr.RequestError:
# #             return "Could not request results from Google Speech Recognition service"

# # # Function to get a response from OpenAI
# # def get_openai_response(prompt):
# #     completion = client.chat.completions.create(
# #         model="gpt-4o-mini",
# #         messages=[
# #             {"role": "system", "content": "You are a helpful assistant."},
# #             {"role": "user", "content": prompt}
# #         ]
# #     )
# #     return completion.choices[0].message.content

# # # Route to serve the home page (index.html)
# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/upload_audio', methods=['POST'])
# # def upload_audio():
# #     if 'audio' not in request.files:
# #         return jsonify({"error": "No audio file"}), 400

# #     audio_file = request.files['audio']
# #     file_path = os.path.join(AUDIO_DIR, audio_file.filename)

# #     # Check if the file already exists and delete it if it does
# #     if os.path.exists(file_path):
# #         os.remove(file_path)

# #     # Save the new audio file
# #     audio_file.save(file_path)

# #     # Transcribe the audio
# #     transcription = transcribe_audio(file_path)

# #     # Get OpenAI's response based on the transcription
# #     openai_response = get_openai_response(transcription)

# #     # Return the file path and the OpenAI response
# #     return jsonify({
# #         "filepath": f'/static/{audio_file.filename}',
# #         "response": openai_response
# #     })

# # @app.route('/send_text', methods=['POST'])
# # def send_text():
# #     user_input = request.json.get('text')
# #     if not user_input:
# #         return jsonify({'error': 'No text provided'}), 400

# #     response = get_openai_response(user_input)
# #     return jsonify({'response': response})

# # @app.route('/static/<path:filename>')
# # def static_files(filename):
# #     return send_from_directory(AUDIO_DIR, filename)

# # if __name__ == "__main__":
# #     app.run(debug=True)
# import os
# import requests
# from openai import OpenAI
# from flask import Flask, request, jsonify, send_from_directory, render_template
# import speech_recognition as sr
# from pydub import AudioSegment
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# # Directory where audio files will be saved
# AUDIO_DIR = os.path.join(os.getcwd(), 'static')
# if not os.path.exists(AUDIO_DIR):
#     os.makedirs(AUDIO_DIR)

# # Set OpenAI API key
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # API endpoint to fetch user information
# API_ENDPOINT = "https://superteclabs.com/apis2/retrieveallusers.php"
# API_PAYLOAD = {'company_token': 'II@tNfQ70O'}
# API_HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'}

# def fetch_user_by_name_or_email(query):
#     """Fetch user details from the external API by name or email."""
#     response = requests.post(API_ENDPOINT, data=API_PAYLOAD, headers=API_HEADERS)
#     if response.status_code == 200:
#         users = response.json()  # Assuming the response is JSON with a list of users
        
#         # Search by name or email in the users
#         for user in users:
#             if query.lower() in user.get('name', '').lower() or query.lower() in user.get('email', '').lower():
#                 return user
#     return None

# def transcribe_audio(file_path):
#     recognizer = sr.Recognizer()
    
#     # Convert to a format that the recognizer supports (WAV)
#     sound = AudioSegment.from_file(file_path)
    
#     # Export audio to WAV format for better recognition
#     wav_file = file_path.replace('.wav', '_transcoded.wav')
#     sound.export(wav_file, format='wav')

#     # Load the WAV file for transcription
#     with sr.AudioFile(wav_file) as source:
#         audio = recognizer.record(source)

#         try:
#             # Transcribe the audio file to text
#             transcription = recognizer.recognize_google(audio)
#             return transcription
#         except sr.UnknownValueError:
#             return "Speech not recognized"
#         except sr.RequestError:
#             return "Could not request results from Google Speech Recognition service"

# # # Function to get a response from OpenAI
# # def get_openai_response(prompt):
# #     completion = client.chat.completions.create(
# #         model="gpt-4o-mini",
# #         messages=[
# #             {"role": "system", "content": "You are a smart assistant that can understand user queries and respond appropriately. When a user requests information about a person by name or mentions details, you should retrieve the relevant user data from external APIs. If the query is unclear or too broad, provide a general response based on your knowledge."},
# #             {"role": "user", "content": prompt}
# #         ]
# #     )
# #     print(completion.choices[0].message.content)
# #     return completion.choices[0].message.content

# # def process_user_request(query):
# #     """Process user request and fetch data from the API if necessary."""
    
# #     # Checking if the user asks for details by name or email
# #     if "details of" in query.lower():
# #         name_or_email = query.lower().split('details of')[-1].strip()
# #         print(name_or_email)

# #         # Fetch user details from the API by name or email
# #         user_details = fetch_user_by_name_or_email(name_or_email)
# #         print(user_details)
# #         if user_details:
# #             return f"Here is the information I found for {name_or_email}: {user_details}"
# #         else:
# #             return f"Sorry, no information found for {name_or_email}."
    
# #     # If no name or email in query, fallback to OpenAI response
# #     print(get_openai_response(query))
# #     return get_openai_response(query)
# # Function to get a response from OpenAI
# def get_openai_response(prompt):
#     try:
#         completion = client.chat.completions.create(
#             model="gpt-4o-mini",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": "You are a smart assistant that can understand user queries and respond appropriately. When a user requests information about a person by name or mentions details, you should retrieve the relevant user data from external APIs. If the query is unclear or too broad, provide a general response based on your knowledge."
#                 },
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         response_content = completion.choices[0].message.content
#         print("OpenAI Response:", response_content)  # Debug statement
#         return response_content
#     except Exception as e:
#         print(f"Error getting response from OpenAI: {e}")  # Error handling
#         return "An error occurred while retrieving the response."

# def process_user_request(query):
#     """Process user request and fetch data from the API if necessary."""
#     print(f"Received query: {query}")  # Debug statement

#     # Checking if the user asks for details by name or email
#     if "details of" in query.lower():
#         name_or_email = query.lower().split('details of')[-1].strip()
#         print(f"Extracted name or email: {name_or_email}")  # Debug statement

#         # Fetch user details from the API by name or email
#         user_details = fetch_user_by_name_or_email(name_or_email)  # Ensure this function exists
#         print(f"Fetched user details: {user_details}")  # Debug statement

#         if user_details:
#             return f"Here is the information I found for {name_or_email}: {user_details}"
#         else:
#             return f"Sorry, no information found for {name_or_email}."
    
#     # If no name or email in query, fallback to OpenAI response
#     openai_response = get_openai_response(query)
#     print(f"Fallback OpenAI response: {openai_response}")  # Debug statement
#     return openai_response

# # Route to serve the home page (index.html)
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload_audio', methods=['POST'])
# def upload_audio():
#     if 'audio' not in request.files:
#         return jsonify({"error": "No audio file"}), 400

#     audio_file = request.files['audio']
#     file_path = os.path.join(AUDIO_DIR, audio_file.filename)

#     # Check if the file already exists and delete it if it does
#     if os.path.exists(file_path):
#         os.remove(file_path)

#     # Save the new audio file
#     audio_file.save(file_path)

#     # Transcribe the audio
#     transcription = transcribe_audio(file_path)

#     # Process transcription to either fetch API data or use OpenAI response
#     response = process_user_request(transcription)

#     # Return the file path and the response
#     return jsonify({
#         "filepath": f'/static/{audio_file.filename}',
#         "response": response
#     })

# @app.route('/send_text', methods=['POST'])
# def send_text():
#     user_input = request.json.get('text')
#     if not user_input:
#         return jsonify({'error': 'No text provided'}), 400

#     # Process user input to either fetch API data or use OpenAI response
#     response = process_user_request(user_input)
#     return jsonify({'response': response})

# @app.route('/static/<path:filename>')
# def static_files(filename):
#     return send_from_directory(AUDIO_DIR, filename)

# if __name__ == "__main__":
#     app.run(debug=True)
import os
import requests
from openai import OpenAI
from flask import Flask, request, jsonify, send_from_directory, render_template
import speech_recognition as sr
from pydub import AudioSegment
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Directory where audio files will be saved
AUDIO_DIR = os.path.join(os.getcwd(), 'static')
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

# Set OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# API endpoint to fetch user information
API_ENDPOINT = "https://superteclabs.com/apis2/retrieveallusers.php"
API_PAYLOAD = {'company_token': 'II@tNfQ70O'}
API_HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0'}

def fetch_user_by_name_or_email(query):
    """Fetch user details from the external API by name or email."""
    response = requests.post(API_ENDPOINT, data=API_PAYLOAD, headers=API_HEADERS)
    if response.status_code == 200:
        users = response.json()  # Assuming the response is JSON with a list of users
        
        # Search by name or email in the users
        matched_users = []
        for user in users:
            if query.lower() in user.get('name', '').lower() or query.lower() in user.get('email', '').lower():
                matched_users.append(user)
        return matched_users
    return None

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    # Convert to a format that the recognizer supports (WAV)
    sound = AudioSegment.from_file(file_path)
    
    # Export audio to WAV format for better recognition
    wav_file = file_path.replace('.wav', '_transcoded.wav')
    sound.export(wav_file, format='wav')

    # Load the WAV file for transcription
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)

        try:
            # Transcribe the audio file to text
            transcription = recognizer.recognize_google(audio)
            return transcription
        except sr.UnknownValueError:
            return "Speech not recognized"
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service"

def get_openai_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a smart assistant that can understand user queries and respond appropriately."
                },
                {"role": "user", "content": prompt}
            ]
        )
        response_content = completion.choices[0].message.content
        print("OpenAI Response:", response_content)  # Debug statement
        return response_content
    except Exception as e:
        print(f"Error getting response from OpenAI: {e}")  # Error handling
        return "An error occurred while retrieving the response."

def process_user_request(query):
    """Process user request and fetch data from the API if necessary."""
    print(f"Received query: {query}")  # Debug statement

    # Checking if the user asks for details by name or email
    if "details of" in query.lower():
        name_or_email = query.lower().split('details of')[-1].strip()
        print(f"Extracted name or email: {name_or_email}")  # Debug statement

        # Fetch user details from the API by name or email
        user_details = fetch_user_by_name_or_email(name_or_email)
        print(f"Fetched user details: {user_details}")  # Debug statement

        if user_details:
            if len(user_details) > 1:
                # Agar multiple users hain, to options do
                options = ", ".join(user['name'] for user in user_details)
                return f"Multiple users found: {options}. Please specify which user you mean."
            else:
                # Return the details of the single user found
                user = user_details[0]
                return f"Here are the details for {user['name']}: Email: {user['email']}, Phone: {user['phone']}, Office: {user['office']}, Status: {user['status']}"
        else:
            return f"Sorry, no information found for {name_or_email}."

    # Check for specific user request directly (like "Waleed Ahmed")
    user_details = fetch_user_by_name_or_email(query)
    if user_details:
        if len(user_details) > 1:
            options = ", ".join(user['name'] for user in user_details)
            return f"Multiple users found: {options}. Please specify which user you mean."
        else:
            user = user_details[0]
            return f"Here is the information I found for {user}"

    # Return a message indicating that the request is invalid
    return "I'm sorry, I can only provide user details when specifically requested."


# Route to serve the home page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file"}), 400

    audio_file = request.files['audio']
    file_path = os.path.join(AUDIO_DIR, audio_file.filename)

    # Check if the file already exists and delete it if it does
    if os.path.exists(file_path):
        os.remove(file_path)

    # Save the new audio file
    audio_file.save(file_path)

    # Transcribe the audio
    transcription = transcribe_audio(file_path)

    # Process transcription to either fetch API data or use OpenAI response
    response = process_user_request(transcription)

    # Return the file path and the response
    return jsonify({
        "filepath": f'/static/{audio_file.filename}',
        "response": response
    })

@app.route('/send_text', methods=['POST'])
def send_text():
    user_input = request.json.get('text')
    if not user_input:
        return jsonify({'error': 'No text provided'}), 400

    # Process user input to either fetch API data or use OpenAI response
    response = process_user_request(user_input)
    return jsonify({'response': response})

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
