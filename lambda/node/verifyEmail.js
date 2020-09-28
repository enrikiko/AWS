const AWS = require("aws-sdk");
const docClient = new AWS.DynamoDB.DocumentClient({region: 'eu-central-1'});

exports.handler = (event, context, callback) => {
    var password = {
        "Password": event.Password
    }
    var queryParameters = {
        TableName: "users",
        Key: {
                "Email": event.Email
             },
        "ProjectionExpression": "Password"
        }
    docClient.get(queryParameters, function(err, data){
        if(err){
            callback(err, null)
        }else{
            if(data.Item!=null)
            {
                if(data.Item.Password==password.Password){
                    callback(null, "Password correct")
                }
                else{
                    callback(null, "Password incorrect")
                }
            }
            else{
                callback(null, "Email correct")
            }
        }
    });
};
