# Dimensions

Dimensions of the package

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **float** | Length of the package | 
**width** | **float** | Width of the package | 
**height** | **float** | Height of the package | 

## Example

```python
from openapi_client.models.dimensions import Dimensions

# TODO update the JSON string below
json = "{}"
# create an instance of Dimensions from a JSON string
dimensions_instance = Dimensions.from_json(json)
# print the JSON string representation of the object
print(Dimensions.to_json())

# convert the object into a dict
dimensions_dict = dimensions_instance.to_dict()
# create an instance of Dimensions from a dict
dimensions_from_dict = Dimensions.from_dict(dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

