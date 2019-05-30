var mqtt= require('mqtt');
var client= mqtt.connect("mqtt:/192.168.0.116",{
clientId:"LampAmjad",
cleam:false,
will:{topic: "offline", payload: "LampAmjad",qos:2}
});

client.on("connect", function(){
    console.log("Hallåå")
    var lampa= setInterval(function(){

        client.publish("lampa/lamp","change",{qos:0, reatain:false})
        
        },30000);
   var messtimer= setInterval(function(){

client.publish("mess","Hallådär",{qos:0, reatain:false})

},30000);
 });

client.on("error", function(error){
    console.log("Cant connect"+error);
    process.exit(1);
})

function End(timers) {
    timers.forEach(timer => {
        clearInterval(timer);
        
    });
    client.end();
    
}
