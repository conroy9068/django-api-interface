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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues(BaseModel):
    """
    indicativeCustomsValues contains child nodes importCustomsDutyValue and importTaxesValue.<BR>                  <BR>                  These 2 child elements are only applicable for Commercial Invoice printing purpose in Customs Invoice template*: COMMERCIAL_INVOICE_P_10 and COMMERCIAL_INVOICE_L_10.<BR>                  If any of this child nodes are present, it will only be able to display up to three OtherCharges. <BR>                  <BR>                  Nonetheless, the ShipmentRequest can still contain up to five additionalCharges.<BR>                  If there are more than three additionalCharges, the third additionalCharges onwards will be combined and displayed under one single caption of 'Other Charges'.<BR>                  <BR>                  Note: If either first or second additionalCharges has typeCode of 'other', and there are more than three additionalCharges provided in the request, the additionalCharges with typeCode of 'other' will be consolidated under the combined 'Other Charges' caption as well.
    """ # noqa: E501
    import_customs_duty_value: Optional[Union[Annotated[float, Field(le=999999999999999, strict=True, ge=0)], Annotated[int, Field(le=2147483647, strict=True, ge=0)]]] = Field(default=None, description="Please provide the pre-calculated import customs duties value for the shipment", alias="importCustomsDutyValue")
    import_taxes_value: Optional[Union[Annotated[float, Field(le=999999999999999, strict=True, ge=0)], Annotated[int, Field(le=2147483647, strict=True, ge=0)]]] = Field(default=None, description="Please provide the pre-calculated import taxes (VAT/GST) value for the shipment", alias="importTaxesValue")
    total_with_import_duties_and_taxes: Optional[Union[Annotated[float, Field(le=999999999999999, strict=True, ge=0)], Annotated[int, Field(le=2147483647, strict=True, ge=0)]]] = Field(default=None, description="Please provide pre-calculated total of all line items plus additional charges plus indicativeCustomsValues", alias="totalWithImportDutiesAndTaxes")
    __properties: ClassVar[List[str]] = ["importCustomsDutyValue", "importTaxesValue", "totalWithImportDutiesAndTaxes"]

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
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues from a JSON string"""
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
        """Create an instance of SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoiceIndicativeCustomsValues from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "importCustomsDutyValue": obj.get("importCustomsDutyValue"),
            "importTaxesValue": obj.get("importTaxesValue"),
            "totalWithImportDutiesAndTaxes": obj.get("totalWithImportDutiesAndTaxes")
        })
        return _obj


