# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner(BaseModel):
    """
    SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner
    """ # noqa: E501
    value: Union[Annotated[float, Field(multiple_of=0.001, le=999999999999999, strict=True, ge=0.001)], Annotated[int, Field(le=2147483647, strict=True, ge=1)]] = Field(description="Please provide the charge value")
    caption: Optional[StrictStr] = Field(default=None, description="Please enter charge caption")
    type_code: StrictStr = Field(description="Please enter charge type", alias="typeCode")
    __properties: ClassVar[List[str]] = ["value", "caption", "typeCode"]

    @field_validator('type_code')
    def type_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['admin', 'delivery', 'documentation', 'expedite', 'export', 'freight', 'fuel_surcharge', 'logistic', 'other', 'packaging', 'pickup', 'handling', 'vat', 'insurance', 'reverse_charge']):
            raise ValueError("must be one of enum values ('admin', 'delivery', 'documentation', 'expedite', 'export', 'freight', 'fuel_surcharge', 'logistic', 'other', 'packaging', 'pickup', 'handling', 'vat', 'insurance', 'reverse_charge')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalChargesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "value": obj.get("value"),
            "caption": obj.get("caption"),
            "typeCode": obj.get("typeCode")
        })
        return _obj


