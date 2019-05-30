function startConnect() {
    // Generate a random client ID
    clientID = "clientID_" + parseInt(Math.random() * 100);

    // Fetch the hostname/IP address and port number from the form
    host =document.getElementById("host").value;
    port = document.getElementById("port").value;

    // Print output for the user in the messages div
    document.getElementById("messages").innerHTML += '<span>Connecting to: ' + host + ' on port: ' + port + '</span><br/>';
    document.getElementById("messages").innerHTML += '<span>Using the following client value: ' + clientID + '</span><br/>';

    // Initialize new Paho client connection
    client = new Paho.MQTT.Client(host, Number(port), clientID);

    // Set callback handlers
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;

    client.connect({ 
        onSuccess: onConnect,
        onFailure: onFail,
                   });
}
function onFail() {
    document.getElementById("messages").innerHTML += '<span>ERROR: Connection to: ' + host + ' on port: ' + port + ' failed.</span><br/>'

}  
// Called when the client connects
function onConnect() {
    // Fetch the MQTT topic from the form
    topic = document.getElementById("topic").value;

    // Print output for the user in the messages div
    document.getElementById("messages").innerHTML += '<span>Subscribing to: ' + topic + '</span><br/>';

    // Subscribe to the requested topic
     client.subscribe(topic);
      message= new Paho.MQTT.Message("Hello World!");
      message.destinationName = "mess"; 
      client.send(message);
}

// Called when the client loses its connection
function onConnectionLost(responseObject) {
    document.getElementById("messages").innerHTML += '<span>ERROR: Connection lost</span><br/>';
    if (responseObject.errorCode !== 0) {
        document.getElementById("messages").innerHTML += '<span>ERROR: ' + + responseObject.errorMessage + '</span><br/>';
        updateScroll()
    }
}

// Called when a message arrives
function onMessageArrived(message) {
    console.log("onMessageArrived: " + message.payloadString);
    document.getElementById("messages").innerHTML += '<span>Topic: ' + message.destinationName + '  | ' + message.payloadString + '</span><br/>';
    updateScroll()
}

// Called when the disconnection button is pressed
function startDisconnect() {
    client.disconnect();
    document.getElementById("messages").innerHTML += '<span>Disconnected</span><br/>';
    
}

function updateScroll(){
    var element = document.getElementById("messages")
    element.scrollTop = element.scrollHeight;
}