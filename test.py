from firebase import firebase

 
firebase = firebase.FirebaseApplication('https://senior-project-iot-7c771.firebaseio.com', None)

# Fetch the service account key JSON file contents
data = firebase.get('status','')

# Initialize the app with a service accoun
print(data)

 