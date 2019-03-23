// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
'use strict';

// Import the Dialogflow module from the Actions on Google client library.
const {dialogflow} = require('actions-on-google');

// Import the firebase-functions package for deployment.
const functions = require('firebase-functions');

// Instantiate the Dialogflow client.
const app = dialogflow({debug: true});

// Handle the Dialogflow intents.
// The intents collect parameters.
app.intent('language to use', (conv, {pLanguage}) => {
    const luckyNumber = pLanguage.length;
    // Respond with the user's lucky number and end the conversation.
    //conv.add('Did you know the language ' + pLanguage + ' is ' + luckyNumber + ' characters long? Also, Hello World!');
	conv.ask('Did you know the language ' + pLanguage + ' is ' + luckyNumber + ' characters long? Also, Hello World!\n\nName a topic you might be interested in for your hackathon.');
});
app.intent('possible topic', (conv, {topic}) => {
    conv.close('Alright, i like the topic of ' + topic + ' too!');
});
// Set the DialogflowApp object to handle the HTTPS POST request.
exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);