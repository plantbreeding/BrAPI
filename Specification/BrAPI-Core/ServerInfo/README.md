# Group Server Info
The '/serverinfo' call is used to find the available BrAPI calls on a particular server. 





### Get - /serverinfo [GET /brapi/v2/serverinfo{?contentType}{?dataType}]

Implementation Notes

Having a consistent structure for the path string of each call is very 
important for teams to be able to connect and find errors. Read more on Github.

Here are the rules for the path of each call that should be returned

Every word in the call path should match the documentation exactly, both in 
spelling and capitalization. Note that path strings are all lower case, but 
path parameters are camel case.

Each path should start relative to \"/\" and therefore should not include \"/\"

No leading or trailing slashes (\"/\") 

Path parameters are wrapped in curly braces (\"{}\"). The name of the path parameter 
should be spelled exactly as it is specified in the documentation.

Examples 

GOOD   "call": "germplasm/{germplasmDbId}/pedigree" 

BAD    "call": "germplasm/{id}/pedigree"

BAD    "call": "germplasm/{germplasmDBid}/pedigree" 

BAD    "call": "brapi/v2/germplasm/{germplasmDbId}/pedigree" 

BAD    "call": "/germplasm/{germplasmDbId}/pedigree/" 

BAD    "call": "germplasm/<germplasmDbId>/pedigree"



**Response Fields** 

<table>
<tr> <th> Field </th> <th> Type </th> <th> Description </th> </tr> 
<tr><td><span style="font-weight:bold;">calls</span></td><td>array[object]</td><td>Array of available calls on this server</td></tr>
<tr><td>calls<br><span style="font-weight:bold;margin-left:5px">.contentTypes</span></td><td>array[string]</td><td>The possible content types returned by the service endpoint</td></tr>
<tr><td>calls<br><span style="font-weight:bold;margin-left:5px">.dataTypes</span></td><td>array[string]</td><td>**Deprecated in v2.1** Please use `contentTypes`. Github issue number #443  <br/>The possible data formats returned by the available call </td></tr>
<tr><td>calls<br><span style="font-weight:bold;margin-left:5px">.methods</span></td><td>array[string]</td><td>The possible HTTP Methods to be used with the available call</td></tr>
<tr><td>calls<br><span style="font-weight:bold;margin-left:5px">.service</span></td><td>string</td><td>The name of the available call as recorded in the documentation</td></tr>
<tr><td>calls<br><span style="font-weight:bold;margin-left:5px">.versions</span></td><td>array[string]</td><td>The supported versions of a particular call</td></tr>
<tr><td><span style="font-weight:bold;">contactEmail</span></td><td>string</td><td>A contact email address for this server management</td></tr>
<tr><td><span style="font-weight:bold;">documentationURL</span></td><td>string</td><td>A URL to the human readable documentation of this object</td></tr>
<tr><td><span style="font-weight:bold;">location</span></td><td>string</td><td>Physical location of this server (ie. City, Country)</td></tr>
<tr><td><span style="font-weight:bold;">organizationName</span></td><td>string</td><td>The name of the organization that manages this server and data</td></tr>
<tr><td><span style="font-weight:bold;">organizationURL</span></td><td>string</td><td>The URL of the organization that manages this server and data</td></tr>
<tr><td><span style="font-weight:bold;">serverDescription</span></td><td>string</td><td>A description of this server</td></tr>
<tr><td><span style="font-weight:bold;">serverName</span></td><td>string</td><td>The name of this server</td></tr>
</table>


 

+ Parameters
    + contentType (Optional, ) ... Filter the list of endpoints based on the response content type.
    + dataType (Optional, ) ... **Deprecated in v2.1** Please use `contentType`. Github issue number #443<br>The data format supported by the call.
    + Authorization (Optional, ) ... HTTP HEADER - Token used for Authorization <strong> Bearer {token_string} </strong>




+ Response 200 (application/json)
```
{
    "@context": [
        "https://brapi.org/jsonld/context/metadata.jsonld"
    ],
    "metadata": {
        "datafiles": [],
        "pagination": {
            "currentPage": 0,
            "pageSize": 1000,
            "totalCount": 10,
            "totalPages": 1
        },
        "status": [
            {
                "message": "Request accepted, response successful",
                "messageType": "INFO"
            }
        ]
    },
    "result": {
        "calls": [
            {
                "contentTypes": [
                    "application/json"
                ],
                "dataTypes": [
                    "application/json"
                ],
                "methods": [
                    "GET",
                    "POST"
                ],
                "service": "germplasm/{germplasmDbId}/pedigree",
                "versions": [
                    "2.0",
                    "2.1"
                ]
            }
        ],
        "contactEmail": "contact@institute.org",
        "documentationURL": "institute.org/server",
        "location": "USA",
        "organizationName": "The Institute",
        "organizationURL": "institute.org/home",
        "serverDescription": "The BrAPI Test Server\nWeb Server - Apache Tomcat 7.0.32\nDatabase - Postgres 10\nSupported BrAPI Version - V2.0",
        "serverName": "The BrAPI Test Server"
    }
}
```

+ Response 400 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Malformed JSON Request Object\n\nERROR - 2018-10-08T18:15:11Z - Invalid query parameter\n\nERROR - 2018-10-08T18:15:11Z - Required parameter is missing"
```

+ Response 401 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - Missing or expired authorization token"
```

+ Response 403 (application/json)
```
"ERROR - 2018-10-08T18:15:11Z - User does not have permission to perform this action"
```

