const AWS = require("aws-sdk");
const docClient = new AWS.DynamoDB.DocumentClient({region: 'eu-central-1'});
var uuid = require('uuid');

exports.handler = (event, context, callback) => {
    let scanningParameters = {
        TableName: 'users'
    };
    docClient.scan(scanningParameters, function(err, data){
        if(err){
            callback(err, null)
        }else{
            callback(null, data)
        }
    });
};
