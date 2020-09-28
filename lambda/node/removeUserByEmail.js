const AWS = require("aws-sdk");
const docClient = new AWS.DynamoDB.DocumentClient({region: 'eu-central-1'});

exports.handler = (event, context, callback) => {
    var queryParameters = {
        TableName: "users",
        Key: {
            "Email": event.Email
        }
    }
    docClient.delete(queryParameters, function(err, data){
        if(err){
            callback(err, null)
        }else{
            callback(null, data)
        }
    });
};
