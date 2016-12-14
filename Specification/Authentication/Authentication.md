## Authentication [/brapi/v1/token]

Implemented by: Tripal Brapi module, Cassavabase, Germinate

Used by: Flapjack

###### Response data types
Exception: the result is not embeded in a "result" structure in order to be (one day) OAuth2 compliant. It's also why the anwser mixes snake_case and camelCase.
For login, returns a hash with the user name and the token as the value. A metadata key is also present (but usually set to null, unless an error condition occurs).

For logout, returns an empty resource. A token to remove could be provided (amdin interface) but it is not required. By default, current user token will be removed.

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
| userDisplayName| string| the display name of the user | Y |
| access_token | string | the access token for the session | Y |
| expires_in | integer | The lifetime in seconds of the access token | Y | 

### Login [POST]
+ Request (application/json)

        {
            "grant_type" : "password", //(optional, text, `password`) ... The grant type, only allowed value is password, but can be ignored
            "username" : "user38", // (required, text, `thepoweruser`) ... The username
            "password" : "secretpw", // (optional, text, `mylittlesecret`) ... The password
            "client_id" : "blabla" // (optional, text, `blabla`) ... The client id, currently ignored.
        }

+ Response 201 (application/json)

        {
            "metadata": {
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
		},
                "status" : [],
                "datafiles": []
                },
            "userDisplayName": "John Smith",
            "access_token": "R6gKDBRxM4HLj6eGi4u5HkQjYoIBTPfvtZzUD8TUzg4",
            "expires_in": "The lifetime in seconds of the access token"
        }




### Logout [DELETE]

+ Request (application/json)
        
        { 
            "access_token" : "R6gKDBRxM4HLj6eGi4u5HkQjYoIBTPfvtZzUD8TUzg4" // (optional, text, `R6gKDBRxM4HLj6eGi4u5HkQjYoIBTPfvtZzUD8TUzg4`) ... The user access token. Default: current user token.
        }
        
+ Response 201 (application/json)

        {
            "metadata": {
                    "pagination" : null,
                    "status" : [ { "message" : "User has been logged out successfully."} ],
                    "datafiles": []
                }
            "result" : {}
        }

