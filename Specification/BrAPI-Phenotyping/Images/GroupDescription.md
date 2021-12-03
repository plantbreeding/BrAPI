# Group Images

Calls for retrieving, storing, and updating images and image metadata

Implementation Notes:

The Images endpoints support a GeoJSON object structure for describing their location. The BrAPI spec for GeoJSON only supports two of the possible geometries: Points and Polygons. 
 + With most images, the Point geometry should be used, and it should indicate the longitude and latitude of the camera. 
 + For top down images (ie from drones, cranes, etc), the Point geometry may be used to indicate the longitude and latitude of the centroid of the image content, and the Polygon geometry may be used to indicate the border of the image content. 

An example use case is available on the BrAPI Wiki -> https://wiki.brapi.org/index.php/Image_Upload