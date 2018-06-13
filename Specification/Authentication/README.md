
# Group Authentication

This resource refers to the authentication mechanism for the API. It is still implementation-agnostic but the structure
should be similar across all implementations. To start off, we propose to use a call similar to OAuth2.0 password grant type. However, this is not fully secure, as we have to trust third party applications not to do anything nefarious with the password information. Upgrade to full OAuth2.0 in the future.
To log in, we use a POST call and to log out we use a DELETE call. In order to remain as compliant as possible with OAuth2 ( https://tools.ietf.org/html/rfc6749 , 7.1.  Access Token Types)
the access token should be provided by the client in its HTTP header using the format "Authorization: Bearer {bearer_value}".
When authenticated, all the calls, including the authentication call, should be done through HTTPS in order to keep the token safe.
The token life time is fixed. If additional time is required, a new /token call should be made to obtain a new access token.

**HTTPS** should be enforced everywhere.





## Token [Post /brapi/v1/token]

 

+ Parameters


+ Response 201 (application/json)
```
{
    "access_token": "R6gKDBRxM4HLj6eGi4u5HkQjYoIBTPfvtZzUD8TUzg4",
    "userDisplayName": "John Smith",
    "metadata": {
        "datafiles": [],
        "status": [],
        "pagination": {
            "currentPage": 0,
            "totalCount": 0,
            "pageSize": 0,
            "totalPages": 0
        }
    },
    "expires_in": "The lifetime in seconds of the access token"
}
```

## Token [Delete /brapi/v1/token]

 

+ Parameters


