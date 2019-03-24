from firebase import firebase

# Firebase GET and POST info
firebase = firebase.FirebaseApplication('https://last-second-hack-128ce.firebaseio.com/', None)

result = firebase.post('/response', response,{'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print(result)
