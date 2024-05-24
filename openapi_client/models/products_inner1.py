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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.products_inner1_delivery_capabilities import ProductsInner1DeliveryCapabilities
from openapi_client.models.products_inner1_detailed_price_breakdown_inner import ProductsInner1DetailedPriceBreakdownInner
from openapi_client.models.products_inner1_pickup_capabilities import ProductsInner1PickupCapabilities
from openapi_client.models.products_inner1_total_price_breakdown_inner import ProductsInner1TotalPriceBreakdownInner
from openapi_client.models.products_inner1_total_price_inner import ProductsInner1TotalPriceInner
from openapi_client.models.products_inner_service_code_dependency_rule_groups_inner import ProductsInnerServiceCodeDependencyRuleGroupsInner
from openapi_client.models.products_inner_service_code_mutually_exclusive_groups_inner import ProductsInnerServiceCodeMutuallyExclusiveGroupsInner
from openapi_client.models.weight1 import Weight1
from typing import Optional, Set
from typing_extensions import Self

class ProductsInner1(BaseModel):
    """
    ProductsInner1
    """ # noqa: E501
    product_name: Optional[StrictStr] = Field(default=None, description="Name of the DHL Express product", alias="productName")
    product_code: Optional[StrictStr] = Field(default=None, description="This is the global DHL Express product code for which the delivery is feasible respecting the input data from the request.", alias="productCode")
    local_product_code: Optional[StrictStr] = Field(default=None, description="This is the local DHL Express product code for which the delivery is feasible respecting the input data from the request.", alias="localProductCode")
    local_product_country_code: Optional[StrictStr] = Field(default=None, description="The country code for the local service used", alias="localProductCountryCode")
    network_type_code: Optional[StrictStr] = Field(default=None, description="The NetworkTypeCode element indicates the product belongs to the Day Definite (DD) or Time Definite (TD) network.<BR>            Possible Values;<BR>             DD: Day Definite product<BR>             TD: Time Definite product", alias="networkTypeCode")
    is_customer_agreement: Optional[StrictBool] = Field(default=None, description="Indicator that the product only can be offered to customers with prior agreement.", alias="isCustomerAgreement")
    weight: Weight1
    total_price: List[ProductsInner1TotalPriceInner] = Field(alias="totalPrice")
    total_price_breakdown: Optional[List[ProductsInner1TotalPriceBreakdownInner]] = Field(default=None, alias="totalPriceBreakdown")
    detailed_price_breakdown: Optional[List[ProductsInner1DetailedPriceBreakdownInner]] = Field(default=None, alias="detailedPriceBreakdown")
    service_code_mutually_exclusive_groups: Optional[List[ProductsInnerServiceCodeMutuallyExclusiveGroupsInner]] = Field(default=None, description="Group of serviceCodes that are mutually exclusive.  Only one serviceCode among the list must be applied for a shipment", alias="serviceCodeMutuallyExclusiveGroups")
    service_code_dependency_rule_groups: Optional[List[ProductsInnerServiceCodeDependencyRuleGroupsInner]] = Field(default=None, description="Dependency rule groups for a particular serviceCode.", alias="serviceCodeDependencyRuleGroups")
    pickup_capabilities: Optional[ProductsInner1PickupCapabilities] = Field(default=None, alias="pickupCapabilities")
    delivery_capabilities: Optional[ProductsInner1DeliveryCapabilities] = Field(default=None, alias="deliveryCapabilities")
    items: Optional[List[object]] = None
    pricing_date: Optional[StrictStr] = Field(default=None, description="The date when the rates for DHL products and services is provided", alias="pricingDate")
    __properties: ClassVar[List[str]] = ["productName", "productCode", "localProductCode", "localProductCountryCode", "networkTypeCode", "isCustomerAgreement", "weight", "totalPrice", "totalPriceBreakdown", "detailedPriceBreakdown", "serviceCodeMutuallyExclusiveGroups", "serviceCodeDependencyRuleGroups", "pickupCapabilities", "deliveryCapabilities", "items", "pricingDate"]

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
        """Create an instance of ProductsInner1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of weight
        if self.weight:
            _dict['weight'] = self.weight.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in total_price (list)
        _items = []
        if self.total_price:
            for _item in self.total_price:
                if _item:
                    _items.append(_item.to_dict())
            _dict['totalPrice'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in total_price_breakdown (list)
        _items = []
        if self.total_price_breakdown:
            for _item in self.total_price_breakdown:
                if _item:
                    _items.append(_item.to_dict())
            _dict['totalPriceBreakdown'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in detailed_price_breakdown (list)
        _items = []
        if self.detailed_price_breakdown:
            for _item in self.detailed_price_breakdown:
                if _item:
                    _items.append(_item.to_dict())
            _dict['detailedPriceBreakdown'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_code_mutually_exclusive_groups (list)
        _items = []
        if self.service_code_mutually_exclusive_groups:
            for _item in self.service_code_mutually_exclusive_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceCodeMutuallyExclusiveGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_code_dependency_rule_groups (list)
        _items = []
        if self.service_code_dependency_rule_groups:
            for _item in self.service_code_dependency_rule_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceCodeDependencyRuleGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of pickup_capabilities
        if self.pickup_capabilities:
            _dict['pickupCapabilities'] = self.pickup_capabilities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery_capabilities
        if self.delivery_capabilities:
            _dict['deliveryCapabilities'] = self.delivery_capabilities.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductsInner1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "productName": obj.get("productName"),
            "productCode": obj.get("productCode"),
            "localProductCode": obj.get("localProductCode"),
            "localProductCountryCode": obj.get("localProductCountryCode"),
            "networkTypeCode": obj.get("networkTypeCode"),
            "isCustomerAgreement": obj.get("isCustomerAgreement"),
            "weight": Weight1.from_dict(obj["weight"]) if obj.get("weight") is not None else None,
            "totalPrice": [ProductsInner1TotalPriceInner.from_dict(_item) for _item in obj["totalPrice"]] if obj.get("totalPrice") is not None else None,
            "totalPriceBreakdown": [ProductsInner1TotalPriceBreakdownInner.from_dict(_item) for _item in obj["totalPriceBreakdown"]] if obj.get("totalPriceBreakdown") is not None else None,
            "detailedPriceBreakdown": [ProductsInner1DetailedPriceBreakdownInner.from_dict(_item) for _item in obj["detailedPriceBreakdown"]] if obj.get("detailedPriceBreakdown") is not None else None,
            "serviceCodeMutuallyExclusiveGroups": [ProductsInnerServiceCodeMutuallyExclusiveGroupsInner.from_dict(_item) for _item in obj["serviceCodeMutuallyExclusiveGroups"]] if obj.get("serviceCodeMutuallyExclusiveGroups") is not None else None,
            "serviceCodeDependencyRuleGroups": [ProductsInnerServiceCodeDependencyRuleGroupsInner.from_dict(_item) for _item in obj["serviceCodeDependencyRuleGroups"]] if obj.get("serviceCodeDependencyRuleGroups") is not None else None,
            "pickupCapabilities": ProductsInner1PickupCapabilities.from_dict(obj["pickupCapabilities"]) if obj.get("pickupCapabilities") is not None else None,
            "deliveryCapabilities": ProductsInner1DeliveryCapabilities.from_dict(obj["deliveryCapabilities"]) if obj.get("deliveryCapabilities") is not None else None,
            "items": obj.get("items"),
            "pricingDate": obj.get("pricingDate")
        })
        return _obj

