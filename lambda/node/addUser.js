const AWS = require("aws-sdk");
const docClient = new AWS.DynamoDB.DocumentClient({region: 'eu-central-1'});

exports.handler = (event, context, callback) => {
    var queryParameters = {
        TableName: "users",
        Key: {
                "Email": event.Email
             },
        "ProjectionExpression": "Email"
        }
    var params = {
        Item: {
            Email: event.Email,
            Password: event.Password,
            Number: event.Number,
            Date: Date.now(),
            UserName: event.Name,
            Sur: event.Sur,
        },
        TableName: 'users'
    }
    docClient.get(queryParameters, function(err, data){
        if(err){
            callback(err, null)
        }else{
            if(data.Item!=null)
            {
                //setUser()
                callback(null, "User already exist")
            }
            else{
                setUser()
            }
        }
    });
    function setUser() {
        docClient.put(params, function(err, data){
        if(err){
            callback(err, null)
        }else{
            callback(null, "Success")
        }
    });
    }
};
