const AWS = require("aws-sdk");
const docClient = new AWS.DynamoDB.DocumentClient({region: 'eu-central-1'});
var uuid = require('uuid');

exports.handler = (event, context, callback) => {
    var queryParameters = {
        TableName: "users",
        Key: {
            "Email": "enriqueramosmunoz@gmail.com"
        },
        "ProjectionExpression": "UserName, Sur"
    }
    docClient.get(queryParameters, function(err, data){
        if(err){
            callback(err, null)
        }else{
            callback(null, data)
        }
    });
};
