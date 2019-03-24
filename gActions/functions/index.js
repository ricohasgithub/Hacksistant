// See https://github.com/dialogflow/dialogflow-fulfillment-nodejs
// for Dialogflow fulfillment library docs, samples, and to report issues
'use strict';

// Initialize Firebase
var firebase = require("firebase");
var admin = require('firebase-admin');
var fs = require('fs');
var serviceAccount = require('./secret.json');
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'https://last-second-hack-128ce.firebaseio.com/'
});

// Import the Dialogflow module from the Actions on Google client library.
const {dialogflow} = require('actions-on-google');

// Import the firebase-functions package for deployment.
const functions = require('firebase-functions');

// Instantiate the Dialogflow client.
const app = dialogflow({debug: true});

// Get database reference and create path
const db = admin.database();
//const ref = db.ref('');

// Make some global variables
var lang = "";
var tpc = "";
var plt = "";

var done = false;

// Handle the Dialogflow intents.
// The intents collect parameters.
app.intent('language to use', (conv, {pLanguage}) => {
	lang = pLanguage;
    const luckyNumber = pLanguage.length;
    //conv.add('Did you know the language ' + pLanguage + ' is ' + luckyNumber + ' characters long? Also, Hello World!');
	conv.ask(lang + ' is one of my favourite languages!\n\nNow, name a topic you might be interested in for your hackathon.');
});
app.intent('possible topic', (conv, {topic}) => {
	tpc = topic;
    conv.ask('Alright, I like the topic of ' + topic + ' too!\n\nFinally, what platform would you like to use?');
});
app.intent('platform to use', (conv, {platform}) => {
	plt = platform;
    conv.close('Looking for potential ' + plt + ' projects written in ' + lang + ' and with the topic of ' + tpc + '...');
	db.ref('response/').set({
		done: true,
		gotLang: true,
		gotPlat: true,
		gotTopic: true
	});
});
// Set the DialogflowApp object to handle the HTTPS POST request.
exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);