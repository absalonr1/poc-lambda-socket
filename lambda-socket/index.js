'use strict';
var net = require('net');

var host = "192.168.75.145";
var puerto = 9999;

// sam local invoke -e event.json HelloWorld
var client = new net.Socket();
client.setKeepAlive(true);

client.setEncoding('utf8');

    client.connect(puerto, host, function() {

        client.removeAllListeners('data');

        console.log('---------client details -----------------');
        var address = client.address();
        var port = address.port;
        var family = address.family;
        var ipaddr = address.address;
        console.log('Client is listening at port: ' + port);
        console.log('Client ip :' + ipaddr);
        console.log('Client is IP4/IP6 : ' + family);
        client.write("\u0002TINFCTC.Tc_InterfazPos3.ConInfoCuenta3('1','11111','94713102','POS','19','')\u0003",'utf8',

        function(){
            console.log('SEND!!');
        });
        client.end();
    });

    client.on('data', function(data) {
        console.log('Received: ' + data);
        client.destroy(); // kill client after server's response
    });

    client.on('close', function() {
        console.log('Connection closed');
    });


    setTimeout(function(){
        client.end('Bye bye server');
      },5000);
exports.handler = (event, context, callback) => {

    console.log('Nme is: '+event.name);
    callback(null, "Hello " + event.name);

}