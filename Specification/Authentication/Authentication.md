## Authentication [/brapi/v2/token]

Implemented by: IRRI

Used by: IRRI

In order to use the API, a client must have a valid access token. This is retrieved by exchanging the authorization code retrieved from the API and a valid Google ID token for an access token.

###### Response data types
Exception: the result is not embeded in a "result" structure in order to be OAuth2 compliant.

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
            "grant_type" : "authorization_code", //(required, text, `password`) ... The grant type, only allowed value is authorization_code
            "redirect_uri" : "user38", // (required, text, `http://brapi.org`) ... The username
            "google_id_token" : "xxxxx", // (required, text, `xxxxx`) ... retrieved by authenticating with Google API
            "client_id" : "blabla" // (required, text, `blabla`) ... The client id.
            "client_secret" : "xxx" // (required, text, `xxxx`) ... The client password.
            "code" : "xxxx" // authorization code
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
                "pagination" : { 
                    "pageSize":0, 
                    "currentPage":0, 
                    "totalCount":0, 
                    "totalPages":0 
                },
                "status" : [ { "message" : "User has been logged out successfully."} ],
                "datafiles": []
             }
            "result" : {}
        }

