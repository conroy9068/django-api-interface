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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItemsInnerCustomerReferencesInner(BaseModel):
    """
    SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItemsInnerCustomerReferencesInner
    """ # noqa: E501
    type_code: Annotated[str, Field(min_length=1, strict=True, max_length=3)] = Field(description="Please provide the line item reference type code. Please refer to the YAML Reference Data Guide PDF file for valid enumeration values.", alias="typeCode")
    value: Annotated[str, Field(min_length=1, strict=True, max_length=35)] = Field(description="Please provide the line item reference")
    __properties: ClassVar[List[str]] = ["typeCode", "value"]

    @field_validator('type_code')
    def type_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['AFE', 'BRD', 'DGC', 'AAJ', 'INB', 'MAK', 'ALX', 'PAN', 'PON', 'ABW', 'SE', 'SON', 'OID', 'DTC', 'DTM', 'DTQ', 'DTR', 'ITR', 'MID', 'OED', 'OET', 'OOR', 'SME', 'USM', 'AAM', 'CFR', 'DOM', 'FOR', 'USG', 'MAT', 'NLR']):
            raise ValueError("must be one of enum values ('AFE', 'BRD', 'DGC', 'AAJ', 'INB', 'MAK', 'ALX', 'PAN', 'PON', 'ABW', 'SE', 'SON', 'OID', 'DTC', 'DTM', 'DTQ', 'DTR', 'ITR', 'MID', 'OED', 'OET', 'OOR', 'SME', 'USM', 'AAM', 'CFR', 'DOM', 'FOR', 'USG', 'MAT', 'NLR')")
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
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItemsInnerCustomerReferencesInner from a JSON string"""
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
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItemsInnerCustomerReferencesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "typeCode": obj.get("typeCode"),
            "value": obj.get("value")
        })
        return _obj

