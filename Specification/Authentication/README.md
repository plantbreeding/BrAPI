
# Group Authentication

This resource refers to the authentication mechanism for the API. It is still implementation-agnostic but the structure
should be similar across all implementations. To start off, we propose to use a call similar to OAuth2.0 password grant type. However, this is not fully secure, as we have to trust third party applications not to do anything nefarious with the password information. Upgrade to full OAuth2.0 in the future.
To log in, we use a POST call and to log out we use a DELETE call. In order to remain as compliant as possible with OAuth2 ( https://tools.ietf.org/html/rfc6749 , 7.1.  Access Token Types)
the access token should be provided by the client in its HTTP header using the format "Authorization: Bearer {bearer_value}".
When authenticated, all the calls, including the authentication call, should be done through HTTPS in order to keep the token safe.
The token life time is fixed. If additional time is required, a new /token call should be made to obtain a new access token.

**HTTPS** should be enforced everywhere.





## Post Login  [POST /brapi/v1/login]

Implemented by: Tripal Brapi module, Cassavabase, Germinate, BMS

Used by: Flapjack, BMS

Response data types
Exception: the result is not embeded in a "result" structure in order to be (one day) OAuth2 compliant. It's also why the anwser mixes snake_case and camelCase.
For login, returns a hash with the user name and the token as the value. A metadata key is also present (but usually set to null, unless an error condition occurs).

For logout, returns an empty resource. A token to remove could be provided (amdin interface) but it is not required. By default, current user token will be removed.

|Variable|Datatype|Description|Required|  
|------|------|------|:-----:|
| userDisplayName| string| the display name of the user | Y |
| access_token | string | the access token for the session | Y |
| expires_in | integer | The lifetime in seconds of the access token | Y |  

+ Parameters
 
+ Request (application/json)
```
{
    "properties": {
        "client_id": {
            "type": "string"
        },
        "grant_type": {
            "type": "string"
        },
        "password": {
            "type": "string"
        },
        "username": {
            "type": "string"
        }
    },
    "type": "object"
}
```



+ Response 201 (application/json)
```
{
    "access_token": "R6gKDBRxM4HLj6eGi4u5HkQjYoIBTPfvtZzUD8TUzg4",
    "expires_in": "The lifetime in seconds of the access token",
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 0,
            "totalCount": 0,
            "totalPages": 0
        },
        "status": []
    },
    "userDisplayName": "John Smith"
}
```



## Delete Logout  [DELETE /brapi/v1/logout]

Implemented by: Tripal Brapi module, Cassavabase, Germinate, BMS

Used by: Flapjack, BMS

For logout, returns an empty resource. A token to remove could be provided (amdin interface) but it is not required. By default, current user token will be removed. 

+ Parameters
 
+ Request (application/json)
```
{
    "properties": {
        "access_token": {
            "type": "string"
        }
    },
    "type": "object"
}
```



