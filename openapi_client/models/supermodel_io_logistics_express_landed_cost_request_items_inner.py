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
from openapi_client.models.supermodel_io_logistics_express_landed_cost_request_items_inner_additional_quantity_definitions_inner import SupermodelIoLogisticsExpressLandedCostRequestItemsInnerAdditionalQuantityDefinitionsInner
from openapi_client.models.supermodel_io_logistics_express_landed_cost_request_items_inner_goods_characteristics_inner import SupermodelIoLogisticsExpressLandedCostRequestItemsInnerGoodsCharacteristicsInner
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressLandedCostRequestItemsInner(BaseModel):
    """
    SupermodelIoLogisticsExpressLandedCostRequestItemsInner
    """ # noqa: E501
    number: Union[Annotated[float, Field(multiple_of=1, le=1000, strict=True, ge=1)], Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(description="Line item number")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=512)]] = Field(default=None, description="Name of the item")
    description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = Field(default=None, description="Item full description")
    manufacturer_country: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=2)]] = Field(default=None, description="ISO Country code of the goods manufacturer", alias="manufacturerCountry")
    part_number: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=35)]] = Field(default=None, description="SKU number", alias="partNumber")
    quantity: Union[Annotated[float, Field(multiple_of=0.001, le=999999999999, strict=True)], Annotated[int, Field(le=2147483647, strict=True)]] = Field(description="Total quantity of the item(s) to be shipped.")
    quantity_type: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=20)]] = Field(default=None, description="Please provide quantitiy type. prt - part, box - box", alias="quantityType")
    unit_price: Union[Annotated[float, Field(multiple_of=0.000010, le=999999999999999, strict=True)], Annotated[int, Field(le=2147483647, strict=True)]] = Field(description="Product Unit price", alias="unitPrice")
    unit_price_currency_code: Annotated[str, Field(min_length=3, strict=True, max_length=3)] = Field(description="Currency code of the Unit Price", alias="unitPriceCurrencyCode")
    customs_value: Optional[Union[Annotated[float, Field(multiple_of=0.001, le=999999999999999, strict=True)], Annotated[int, Field(le=2147483647, strict=True)]]] = Field(default=None, description="not used", alias="customsValue")
    customs_value_currency_code: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="not used", alias="customsValueCurrencyCode")
    commodity_code: Optional[Annotated[str, Field(strict=True, max_length=18)]] = Field(default=None, description="commodityCode is mandatory if estimatedTariffRateType ('derived_rate' or 'highest_rate' or 'lowest_rate' or 'center_rate') not provided in the request otherwise it is considered as Optional.<BR>                              'highest_rate' or 'lowest_rate' or 'center_rate') not provided in the request otherwise it is considered as Optional.<BR>            Can be provided with or without dots", alias="commodityCode")
    weight: Optional[Union[Annotated[float, Field(multiple_of=0.001, le=999999999999, strict=True)], Annotated[int, Field(le=2147483647, strict=True)]]] = Field(default=None, description="Weight of the item")
    weight_unit_of_measurement: Optional[StrictStr] = Field(default=None, description="Unit of measurement", alias="weightUnitOfMeasurement")
    category: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="commodityCode category can be retrieved via referenceData API/ commodityCategory dataset.<BR> Category code of the Item.<BR>            101 - Coats & Jacket<BR>            102 - Blazers<BR>            103 - Suits<BR>            104 - Ensembles<BR>            105 - Trousers<BR>            106 - Shirts & Blouses<BR>            107 - Dresses<BR>            108 - Skirts<BR>            109 - Jerseys, Sweatshirts & Pullovers<BR>            110 - Sports & Swimwear<BR>            111 - Night & Underwear<BR>            112 - T-Shirts<BR>            113 - Tights & Leggings<BR>            114 - Socks <BR>            115 - Baby Clothes<BR>            116 - Clothing Accessories<BR>            201 - Sneakers<BR>            202 - Athletic Footwear<BR>            203 - Leather Footwear<BR>            204 - Textile & Other Footwear<BR>            301 - Spectacle Lenses<BR>            302 - Sunglasses<BR>            303 - Eyewear Frames<BR>            304 - Contact Lenses<BR>            401 - Watches<BR>            402 - Jewelry<BR>            403 - Suitcases & Briefcases<BR>            404 - Handbags<BR>            405 - Wallets & Little Cases<BR>            406 - Bags & Containers<BR>            501 - Beer<BR>            502 - Spirits<BR>            503 - Wine<BR>            504 - Cider, Perry & Rice Wine<BR>            601 - Bottled Water<BR>            602 - Soft Drinks<BR>            603 - Juices<BR>            604 - Coffee<BR>            605 - Tea<BR>            606 - Cocoa<BR>            701 - Dairy Products & Eggs<BR>            702 - Meat<BR>            703 - Fish & Seafood<BR>            704 - Fruits & Nuts<BR>            705 - Vegetables<BR>            706 - Bread & Cereal Products<BR>            707 - Oils & Fats<BR>            708 - Sauces & Spices<BR>            709 - Convenience Food<BR>            710 - Spreads & Sweeteners<BR>            711 - Baby Food<BR>            712 - Pet Food<BR>            801 - Cigarettes<BR>            802 - Smoking Tobacco<BR>            803 - Cigars<BR>            804 - E-Cigarettes<BR>            901 - Household Cleaners<BR>            902 - Dishwashing Detergents<BR>            903 - Polishes<BR>            904 - Room Scents<BR>            905 - Insecticides<BR>            1001 - Cosmetics<BR>            1002 - Skin Care<BR>            1003 - Personal Care<BR>            1004 - Fragrances<BR>            1101 - Toilet Paper<BR>            1102 - Paper Tissues<BR>            1103 - Household Paper<BR>            1104 - Feminine Hygiene<BR>            1105 - Baby Diapers<BR>            1106 - Incontinence<BR>            1202 - TV, Radio & Multimedia<BR>            1203 - TV Peripheral Devices<BR>            1204 - Telephony<BR>            1205 - Computing<BR>            1206 - Drones<BR>            1301 - Refrigerators<BR>            1302 - Freezers<BR>            1303 - Dishwashing Machines<BR>            1304 - Washing Machines<BR>            1305 - Cookers & Oven<BR>            1306 - Vacuum Cleaners<BR>            1307 - Small Kitchen Appliances<BR>            1308 - Hair Clippers<BR>            1309 - Irons<BR>            1310 - Toasters<BR>            1311 - Grills & Roasters<BR>            1312 - Hair Dryers<BR>            1313 - Coffee Machines<BR>            1314 - Microwave Ovens<BR>            1315 - Electric Kettles<BR>            1401 - Seats & Sofas<BR>            1402 - Beds<BR>            1403 - Mattresses<BR>            1404 - Closets, Nightstands & Dressers<BR>            1405 - Lamps & Lighting<BR>            1406 - Floor Covering<BR>            1407 - Kitchen Furniture<BR>            1408 - Plastic & Other Furniture<BR>            1501 - Analgesics<BR>            1502 - Cold & Cough Remedies<BR>            1503 - Digestives & Intestinal Remedies<BR>            1504 - Skin Treatment<BR>            1505 - Vitamins & Minerals<BR>            1506 - Hand Sanitizer <BR>            1601 - Toys & Games<BR>            1602 - Musical Instruments<BR>            1603 - Sports Equipment")
    brand: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Item's brand")
    goods_characteristics: Optional[Annotated[List[SupermodelIoLogisticsExpressLandedCostRequestItemsInnerGoodsCharacteristicsInner], Field(max_length=999)]] = Field(default=None, alias="goodsCharacteristics")
    additional_quantity_definitions: Optional[Annotated[List[SupermodelIoLogisticsExpressLandedCostRequestItemsInnerAdditionalQuantityDefinitionsInner], Field(max_length=100)]] = Field(default=None, alias="additionalQuantityDefinitions")
    estimated_tariff_rate_type: Optional[StrictStr] = Field(default=None, description="Please enter Tariff Rate Type - default_rate,derived_rate,highest_rate,center_rate,lowest_rate", alias="estimatedTariffRateType")
    __properties: ClassVar[List[str]] = ["number", "name", "description", "manufacturerCountry", "partNumber", "quantity", "quantityType", "unitPrice", "unitPriceCurrencyCode", "customsValue", "customsValueCurrencyCode", "commodityCode", "weight", "weightUnitOfMeasurement", "category", "brand", "goodsCharacteristics", "additionalQuantityDefinitions", "estimatedTariffRateType"]

    @field_validator('quantity_type')
    def quantity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['prt', 'box']):
            raise ValueError("must be one of enum values ('prt', 'box')")
        return value

    @field_validator('weight_unit_of_measurement')
    def weight_unit_of_measurement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['metric', 'imperial']):
            raise ValueError("must be one of enum values ('metric', 'imperial')")
        return value

    @field_validator('estimated_tariff_rate_type')
    def estimated_tariff_rate_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default_rate', 'derived_rate', 'highest_rate', 'center_rate', 'lowest_rate']):
            raise ValueError("must be one of enum values ('default_rate', 'derived_rate', 'highest_rate', 'center_rate', 'lowest_rate')")
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
        """Create an instance of SupermodelIoLogisticsExpressLandedCostRequestItemsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in goods_characteristics (list)
        _items = []
        if self.goods_characteristics:
            for _item in self.goods_characteristics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['goodsCharacteristics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_quantity_definitions (list)
        _items = []
        if self.additional_quantity_definitions:
            for _item in self.additional_quantity_definitions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalQuantityDefinitions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupermodelIoLogisticsExpressLandedCostRequestItemsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "manufacturerCountry": obj.get("manufacturerCountry"),
            "partNumber": obj.get("partNumber"),
            "quantity": obj.get("quantity"),
            "quantityType": obj.get("quantityType"),
            "unitPrice": obj.get("unitPrice"),
            "unitPriceCurrencyCode": obj.get("unitPriceCurrencyCode"),
            "customsValue": obj.get("customsValue"),
            "customsValueCurrencyCode": obj.get("customsValueCurrencyCode"),
            "commodityCode": obj.get("commodityCode"),
            "weight": obj.get("weight"),
            "weightUnitOfMeasurement": obj.get("weightUnitOfMeasurement"),
            "category": obj.get("category"),
            "brand": obj.get("brand"),
            "goodsCharacteristics": [SupermodelIoLogisticsExpressLandedCostRequestItemsInnerGoodsCharacteristicsInner.from_dict(_item) for _item in obj["goodsCharacteristics"]] if obj.get("goodsCharacteristics") is not None else None,
            "additionalQuantityDefinitions": [SupermodelIoLogisticsExpressLandedCostRequestItemsInnerAdditionalQuantityDefinitionsInner.from_dict(_item) for _item in obj["additionalQuantityDefinitions"]] if obj.get("additionalQuantityDefinitions") is not None else None,
            "estimatedTariffRateType": obj.get("estimatedTariffRateType")
        })
        return _obj


