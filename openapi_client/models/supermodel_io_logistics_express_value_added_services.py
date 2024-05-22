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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.supermodel_io_logistics_express_value_added_services_dangerous_goods_inner import SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressValueAddedServices(BaseModel):
    """
    SupermodelIoLogisticsExpressValueAddedServices
    """ # noqa: E501
    service_code: Annotated[str, Field(min_length=1, strict=True, max_length=6)] = Field(description="Please enter DHL Express value added service code. For detailed list of all available service codes for your prospect shipment please invoke GET /products or GET /rates", alias="serviceCode")
    value: Optional[Union[Annotated[float, Field(multiple_of=0.001, le=999999999999999, strict=True, ge=0)], Annotated[int, Field(le=2147483647, strict=True, ge=0)]]] = Field(default=None, description="Please enter monetary value of service (e.g. Insured Value)")
    currency: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="Please enter currency code (e.g. Insured Value currency code)")
    method: Optional[StrictStr] = Field(default=None, description="Payment method code (e.g. Cash)")
    dangerous_goods: Optional[Annotated[List[Optional[SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner]], Field(max_length=1)]] = Field(default=None, description="The DangerousGoods section indicates if there is dangerous good content within the shipment. <BR> The ContentID node contains the Content ID for Dangerous Good classification. <BR> It is required to provide the dangerous good Content ID for every dangerous good special service provided, and vice versa. <BR> For the complete list of dangerous goods Content IDs and dangerous goods special services combinations, refer to Reference Data Guide section 5. valueAddedServicesDefinition\\\\dangerousGoods. <BR> Note: Please contact your DHL Express IT representative if additional assistance is required.<BR><BR> For dangerous goods shipment with Dry Ice example: UN1845 (Content ID: 901), additional node must be populated 'dryIceTotalNetWeight.'<BR> For dangerous goods shipment with 'Excepted Quantities', additional node must be populated 'unCodes'. Few scenarios guideline to prepare a Dangerous Goods shipment for:<BR><BR> A) Dry Ice: <BR> 1.'serviceCode' element must contain value of 'HC'<BR> 2.'contentID' element consists of '901'<BR> 3.'dryIceTotalNetWeight' element consists of the total net weight of the dry ice in 'unitofMeasurement' <BR><BR> B) Lithium Battery: <BR> 1.'serviceType' element must contain value of 'HD', 'HM', 'HV' or 'HW'<BR> 2.'contentID' element consists of '966', '969', '967', '970' respectively<BR><BR> C) Excepted Quantities:<BR> 1.'serviceCode' element must contain value of 'HH'<BR> 2.'contentID' element consists of 'E01<BR> 3.'unCodes' element consists of the UN code associate with it.<BR>", alias="dangerousGoods")
    __properties: ClassVar[List[str]] = ["serviceCode", "value", "currency", "method", "dangerousGoods"]

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
        """Create an instance of SupermodelIoLogisticsExpressValueAddedServices from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dangerous_goods (list)
        _items = []
        if self.dangerous_goods:
            for _item in self.dangerous_goods:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dangerousGoods'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupermodelIoLogisticsExpressValueAddedServices from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serviceCode": obj.get("serviceCode"),
            "value": obj.get("value"),
            "currency": obj.get("currency"),
            "method": obj.get("method"),
            "dangerousGoods": [SupermodelIoLogisticsExpressValueAddedServicesDangerousGoodsInner.from_dict(_item) for _item in obj["dangerousGoods"]] if obj.get("dangerousGoods") is not None else None
        })
        return _obj


