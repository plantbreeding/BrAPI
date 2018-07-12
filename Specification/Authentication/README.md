
# Group Authentication

This resource refers to the authentication mechanism for the API. It is still implementation-agnostic but the structure
should be similar across all implementations. To start off, we propose to use a call similar to OAuth2.0 password grant type. However, this is not fully secure, as we have to trust third party applications not to do anything nefarious with the password information. Upgrade to full OAuth2.0 in the future.
To log in, we use a POST call and to log out we use a DELETE call. In order to remain as compliant as possible with OAuth2 ( https://tools.ietf.org/html/rfc6749 , 7.1.  Access Token Types)
the access token should be provided by the client in its HTTP header using the format "Authorization: Bearer {bearer_value}".
When authenticated, all the calls, including the authentication call, should be done through HTTPS in order to keep the token safe.
The token life time is fixed. If additional time is required, a new /token call should be made to obtain a new access token.

**HTTPS** should be enforced everywhere.





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



