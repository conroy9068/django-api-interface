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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_customer_references_inner import SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceCustomerReferencesInner
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_indicative_customs_values import SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues
from openapi_client.models.supermodel_io_logistics_express_create_shipment_request_content_export_declaration_invoice_pre_calculated_total_values import SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoicePreCalculatedTotalValues
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice(BaseModel):
    """
    Please provide invoice related information
    """ # noqa: E501
    number: Annotated[str, Field(min_length=1, strict=True, max_length=35)] = Field(description="Please enter commercial invoice number")
    var_date: date = Field(description="Please enter commercial invoice date", alias="date")
    signature_name: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="Please enter who has signed the invoce", alias="signatureName")
    signature_title: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="Please provide title of person who has signed the invoice", alias="signatureTitle")
    signature_image: Optional[Annotated[str, Field(strict=True, max_length=1048576)]] = Field(default=None, description="Please provide the signature image", alias="signatureImage")
    instructions: Optional[Annotated[List[Annotated[str, Field(min_length=1, strict=True, max_length=300)]], Field(min_length=1, max_length=1)]] = Field(default=None, description="Shipment instructions for customs invoice printing purposes. Printed only when using Customs Invoice template COMMERCIAL_INVOICE_04. If using Customs Invoice template    COMMERCIAL_INVOICE_04, recommended max length is 120 characters.")
    customer_data_text_entries: Optional[Annotated[List[Annotated[str, Field(min_length=0, strict=True, max_length=45)]], Field(min_length=1, max_length=6)]] = Field(default=None, description="Customer data text to be printed in<BR>                  customs invoice.<BR>                  Printed only when using Customs<BR>                  Invoice template<BR>                  COMMERCIAL_INVOICE_04.", alias="customerDataTextEntries")
    total_net_weight: Optional[Union[Annotated[float, Field(multiple_of=0.001, le=999999999999, strict=True, ge=0)], Annotated[int, Field(le=2147483647, strict=True, ge=0)]]] = Field(default=None, description="Please provide the total net weight", alias="totalNetWeight")
    total_gross_weight: Optional[Union[Annotated[float, Field(multiple_of=0.001, le=999999999999, strict=True, ge=0)], Annotated[int, Field(le=2147483647, strict=True, ge=0)]]] = Field(default=None, description="Please provide the total gross weight", alias="totalGrossWeight")
    customer_references: Optional[Annotated[List[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceCustomerReferencesInner], Field(max_length=100)]] = Field(default=None, description="Please provide the customer references at invoice level. It is recommended to provide less than 20 customer references of 'MRN' type code.", alias="customerReferences")
    terms_of_payment: Optional[StrictStr] = Field(default=None, description="Please provide the terms of payment", alias="termsOfPayment")
    indicative_customs_values: Optional[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues] = Field(default=None, alias="indicativeCustomsValues")
    pre_calculated_total_values: Optional[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoicePreCalculatedTotalValues] = Field(default=None, alias="preCalculatedTotalValues")
    __properties: ClassVar[List[str]] = ["number", "date", "signatureName", "signatureTitle", "signatureImage", "instructions", "customerDataTextEntries", "totalNetWeight", "totalGrossWeight", "customerReferences", "termsOfPayment", "indicativeCustomsValues", "preCalculatedTotalValues"]

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
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in customer_references (list)
        _items = []
        if self.customer_references:
            for _item in self.customer_references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customerReferences'] = _items
        # override the default output from pydantic by calling `to_dict()` of indicative_customs_values
        if self.indicative_customs_values:
            _dict['indicativeCustomsValues'] = self.indicative_customs_values.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pre_calculated_total_values
        if self.pre_calculated_total_values:
            _dict['preCalculatedTotalValues'] = self.pre_calculated_total_values.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "date": obj.get("date"),
            "signatureName": obj.get("signatureName"),
            "signatureTitle": obj.get("signatureTitle"),
            "signatureImage": obj.get("signatureImage"),
            "instructions": obj.get("instructions"),
            "customerDataTextEntries": obj.get("customerDataTextEntries"),
            "totalNetWeight": obj.get("totalNetWeight"),
            "totalGrossWeight": obj.get("totalGrossWeight"),
            "customerReferences": [SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceCustomerReferencesInner.from_dict(_item) for _item in obj["customerReferences"]] if obj.get("customerReferences") is not None else None,
            "termsOfPayment": obj.get("termsOfPayment"),
            "indicativeCustomsValues": SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues.from_dict(obj["indicativeCustomsValues"]) if obj.get("indicativeCustomsValues") is not None else None,
            "preCalculatedTotalValues": SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoicePreCalculatedTotalValues.from_dict(obj["preCalculatedTotalValues"]) if obj.get("preCalculatedTotalValues") is not None else None
        })
        return _obj


