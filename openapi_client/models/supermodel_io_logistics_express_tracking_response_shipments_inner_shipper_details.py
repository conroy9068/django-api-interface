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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_postal_address import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsPostalAddress
from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_service_area_inner import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsServiceAreaInner
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails(BaseModel):
    """
    SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Note: This field may be intentionally left empty in accordance with the General Data Protection Regulation (GDPR) requirements.                  ")
    postal_address: Optional[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsPostalAddress] = Field(default=None, alias="postalAddress")
    service_area: Optional[List[SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsServiceAreaInner]] = Field(default=None, alias="serviceArea")
    __properties: ClassVar[List[str]] = ["name", "postalAddress", "serviceArea"]

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
        """Create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in service_area (list)
        _items = []
        if self.service_area:
            for _item in self.service_area:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceArea'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "postalAddress": SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsPostalAddress.from_dict(obj["postalAddress"]) if obj.get("postalAddress") is not None else None,
            "serviceArea": [SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetailsServiceAreaInner.from_dict(_item) for _item in obj["serviceArea"]] if obj.get("serviceArea") is not None else None
        })
        return _obj

