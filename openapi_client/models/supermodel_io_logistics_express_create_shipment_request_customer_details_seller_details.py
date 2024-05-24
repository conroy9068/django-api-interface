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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.supermodel_io_logistics_express_address_create_shipment_request import SupermodelIoLogisticsExpressAddressCreateShipmentRequest
from openapi_client.models.supermodel_io_logistics_express_bank_details_inner import SupermodelIoLogisticsExpressBankDetailsInner
from openapi_client.models.supermodel_io_logistics_express_contact import SupermodelIoLogisticsExpressContact
from openapi_client.models.supermodel_io_logistics_express_registration_numbers import SupermodelIoLogisticsExpressRegistrationNumbers
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsSellerDetails(BaseModel):
    """
    Please enter address and contact details related to seller
    """ # noqa: E501
    postal_address: SupermodelIoLogisticsExpressAddressCreateShipmentRequest = Field(alias="postalAddress")
    contact_information: SupermodelIoLogisticsExpressContact = Field(alias="contactInformation")
    registration_numbers: Optional[Annotated[List[SupermodelIoLogisticsExpressRegistrationNumbers], Field(max_length=50)]] = Field(default=None, alias="registrationNumbers")
    bank_details: Optional[Annotated[List[SupermodelIoLogisticsExpressBankDetailsInner], Field(max_length=1)]] = Field(default=None, alias="bankDetails")
    type_code: Optional[StrictStr] = Field(default=None, description="Please enter the business party role type of the seller", alias="typeCode")
    __properties: ClassVar[List[str]] = ["postalAddress", "contactInformation", "registrationNumbers", "bankDetails", "typeCode"]

    @field_validator('type_code')
    def type_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['business', 'direct_consumer', 'government', 'other', 'private', 'reseller']):
            raise ValueError("must be one of enum values ('business', 'direct_consumer', 'government', 'other', 'private', 'reseller')")
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
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsSellerDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of postal_address
        if self.postal_address:
            _dict['postalAddress'] = self.postal_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_information
        if self.contact_information:
            _dict['contactInformation'] = self.contact_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in registration_numbers (list)
        _items = []
        if self.registration_numbers:
            for _item in self.registration_numbers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['registrationNumbers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bank_details (list)
        _items = []
        if self.bank_details:
            for _item in self.bank_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bankDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsSellerDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "postalAddress": SupermodelIoLogisticsExpressAddressCreateShipmentRequest.from_dict(obj["postalAddress"]) if obj.get("postalAddress") is not None else None,
            "contactInformation": SupermodelIoLogisticsExpressContact.from_dict(obj["contactInformation"]) if obj.get("contactInformation") is not None else None,
            "registrationNumbers": [SupermodelIoLogisticsExpressRegistrationNumbers.from_dict(_item) for _item in obj["registrationNumbers"]] if obj.get("registrationNumbers") is not None else None,
            "bankDetails": [SupermodelIoLogisticsExpressBankDetailsInner.from_dict(_item) for _item in obj["bankDetails"]] if obj.get("bankDetails") is not None else None,
            "typeCode": obj.get("typeCode")
        })
        return _obj

