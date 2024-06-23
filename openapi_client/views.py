# api/views.py
import os
import ssl
import json
import urllib3
import requests

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view

from openapi_client.models.supermodel_io_logistics_express_create_shipment_request import SupermodelIoLogisticsExpressCreateShipmentRequest

from .api import (
    address_api, identifier_api, invoice_api, pickup_api,
    product_api, rating_api, reference_data_api, servicepoint_api,
    shipment_api, tracking_api
)

from openapi_client import Configuration
from openapi_client import ApiClient

from openapi_client.forms import AddressValidateForm, CreateShipmentForm
from .forms import AddressValidateForm, TrackShipmentForm
from openapi_client.api.address_api import AddressApi
from openapi_client.api.shipment_api import ShipmentApi
from openapi_client.api.tracking_api import TrackingApi

# Disable warnings for SSL verification (for development purposes only)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def track_shipment_view(request):
    result = None
    if request.method == 'POST':
        form = TrackShipmentForm(request.POST)
        if form.is_valid():
            api_instance = TrackingApi()
            try:
                response = api_instance.exp_api_shipments_tracking_multi(
                    shipment_tracking_number=form.cleaned_data.get('shipment_tracking_number'),
                    piece_tracking_number=form.cleaned_data.get('piece_tracking_number'),
                    shipment_reference=form.cleaned_data.get('shipment_reference'),
                    shipment_reference_type=form.cleaned_data.get('shipment_reference_type'),
                    shipper_account_number=form.cleaned_data.get('shipper_account_number'),
                    date_range_from=form.cleaned_data.get('date_range_from'),
                    date_range_to=form.cleaned_data.get('date_range_to'),
                    tracking_view=form.cleaned_data.get('tracking_view'),
                    level_of_detail=form.cleaned_data.get('level_of_detail'),
                    request_controlled_access_data_codes=form.cleaned_data.get('request_controlled_access_data_codes'),
                    message_reference=form.cleaned_data.get('message_reference'),
                    message_reference_date=form.cleaned_data.get('message_reference_date'),
                    plugin_name=form.cleaned_data.get('plugin_name'),
                    plugin_version=form.cleaned_data.get('plugin_version'),
                    shipping_system_platform_name=form.cleaned_data.get('shipping_system_platform_name'),
                    shipping_system_platform_version=form.cleaned_data.get('shipping_system_platform_version'),
                    webstore_platform_name=form.cleaned_data.get('webstore_platform_name'),
                    webstore_platform_version=form.cleaned_data.get('webstore_platform_version')
                )
                result = response.to_dict()
            except Exception as e:
                result = {"error": str(e)}
    else:
        form = TrackShipmentForm()

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'pages/track_shipment.html', context)


def create_shipment_view(request):
    if request.method == 'POST':
        form = CreateShipmentForm(request.POST)
        if form.is_valid():
            payload = {
                "plannedShippingDateAndTime": form.cleaned_data['planned_shipping_date_and_time'].strftime('%Y-%m-%dT%H:%M:%S%z'),
                "pickup": {
                    "isRequested": form.cleaned_data['pickup_requested']
                },
                "productCode": form.cleaned_data['product_code'],
                "localProductCode": form.cleaned_data['local_product_code'],
                "getRateEstimates": False,
                "accounts": [
                    {
                        "typeCode": "shipper",
                        "number": "123456789"
                    }
                ],
                "valueAddedServices": [
                    {
                        "serviceCode": form.cleaned_data['value_added_service_code'],
                        "value": form.cleaned_data['value_added_service_value'],
                        "currency": form.cleaned_data['value_added_service_currency']
                    }
                ],
                "outputImageProperties": {
                    "printerDPI": 300,
                    "encodingFormat": "pdf",
                    "imageOptions": [
                        {
                            "typeCode": "invoice",
                            "templateName": "COMMERCIAL_INVOICE_P_10",
                            "isRequested": True,
                            "invoiceType": "commercial",
                            "languageCode": "eng",
                            "languageCountryCode": "US"
                        },
                        {
                            "typeCode": "waybillDoc",
                            "templateName": "ARCH_8x4",
                            "isRequested": True,
                            "hideAccountNumber": False,
                            "numberOfCopies": 1
                        },
                        {
                            "typeCode": "label",
                            "templateName": "ECOM26_84_001",
                            "renderDHLLogo": True,
                            "fitLabelsToA4": False
                        }
                    ],
                    "splitTransportAndWaybillDocLabels": True,
                    "allDocumentsInOneImage": False,
                    "splitDocumentsByPages": False,
                    "splitInvoiceAndReceipt": True,
                    "receiptAndLabelsInOneImage": False
                },
                "customerDetails": {
                    "shipperDetails": {
                        "postalAddress": {
                            "postalCode": form.cleaned_data['shipper_postal_code'],
                            "cityName": form.cleaned_data['shipper_city_name'],
                            "countryCode": form.cleaned_data['shipper_country_code'],
                            "addressLine1": form.cleaned_data['shipper_address_line1'],
                            "addressLine2": form.cleaned_data['shipper_address_line2'],
                            "addressLine3": form.cleaned_data['shipper_address_line3'],
                            "countyName": form.cleaned_data['shipper_county_name'],
                            "countryName": form.cleaned_data['shipper_country_name']
                        },
                        "contactInformation": {
                            "email": form.cleaned_data['shipper_email'],
                            "phone": form.cleaned_data['shipper_phone'],
                            "mobilePhone": form.cleaned_data['shipper_mobile_phone'],
                            "companyName": form.cleaned_data['shipper_company_name'],
                            "fullName": form.cleaned_data['shipper_full_name']
                        }
                    },
                    "receiverDetails": {
                        "postalAddress": {
                            "postalCode": form.cleaned_data['receiver_postal_code'],
                            "cityName": form.cleaned_data['receiver_city_name'],
                            "countryCode": form.cleaned_data['receiver_country_code'],
                            "addressLine1": form.cleaned_data['receiver_address_line1'],
                            "countryName": form.cleaned_data['receiver_country_name']
                        },
                        "contactInformation": {
                            "email": form.cleaned_data['receiver_email'],
                            "phone": form.cleaned_data['receiver_phone'],
                            "mobilePhone": form.cleaned_data['receiver_mobile_phone'],
                            "companyName": form.cleaned_data['receiver_company_name'],
                            "fullName": form.cleaned_data['receiver_full_name']
                        }
                    }
                },
                "content": {
                    "packages": [
                        {
                            "typeCode": form.cleaned_data['package_type_code'],
                            "weight": form.cleaned_data['package_weight'],
                            "dimensions": {
                                "length": form.cleaned_data['package_length'],
                                "width": form.cleaned_data['package_width'],
                                "height": form.cleaned_data['package_height']
                            },
                            "customerReferences": [
                                {
                                    "value": form.cleaned_data['package_customer_reference_value'],
                                    "typeCode": "CU"
                                }
                            ],
                            "description": form.cleaned_data['package_description']
                        }
                    ],
                    "isCustomsDeclarable": form.cleaned_data['is_customs_declarable'],
                    "declaredValue": form.cleaned_data['declared_value'],
                    "declaredValueCurrency": form.cleaned_data['declared_value_currency'],
                    "description": form.cleaned_data['description'],
                    "incoterm": form.cleaned_data['incoterm'],
                    "unitOfMeasurement": form.cleaned_data['unit_of_measurement']
                },
                "shipmentNotification": [
                    {
                        "typeCode": "email",
                        "receiverId": "shipmentnotification@mydhlapisample.com",
                        "languageCode": "eng",
                        "languageCountryCode": "UK",
                        "bespokeMessage": "message to be included in the notification"
                    }
                ],
                "getTransliteratedResponse": False,
                "estimatedDeliveryDate": {
                    "isRequested": True,
                    "typeCode": "QDDC"
                },
                "getAdditionalInformation": [
                    {
                        "typeCode": "pickupDetails",
                        "isRequested": True
                    }
                ]
            }

            try:
                api_instance = ShipmentApi()
                shipment_request = SupermodelIoLogisticsExpressCreateShipmentRequest(**payload)
                response = api_instance.exp_api_shipments(
                    supermodel_io_logistics_express_create_shipment_request=shipment_request,
                    message_reference="d0e7832e-5c98-11ea-bc55-0242ac13",
                    message_reference_date="2023-10-10T10:10:10",
                    plugin_name="plugin_name",
                    plugin_version="1.0.0",
                    shipping_system_platform_name="platform_name",
                    shipping_system_platform_version="1.0.0",
                    webstore_platform_name="webstore_name",
                    webstore_platform_version="1.0.0",
                )
                result = response.to_dict()
                print(result)
            except Exception as e:
                result = {"error": str(e)}
        else:
            result = {"error": form.errors}
    else:
        form = CreateShipmentForm()
        result = None

    context = {
        'form': form,
        'result': json.dumps(result, indent=4) if result else None
    }
    return render(request, 'pages/create_shipment.html', context)



def address_validate_view_EXAMPLE(request):
    if request.method == 'POST':
        form = AddressValidateForm(request.POST)
        if form.is_valid():
            api_instance = AddressApi()
            try:
                response = api_instance.exp_api_address_validate(
                    type=form.cleaned_data.get('type_'),
                    country_code=form.cleaned_data.get('country_code'),
                    postal_code=form.cleaned_data.get('postal_code'),
                    city_name=form.cleaned_data.get('city_name'),
                    county_name=form.cleaned_data.get('county_name'),
                    strict_validation=form.cleaned_data.get('strict_validation'),
                    message_reference=form.cleaned_data.get('message_reference'),
                    message_reference_date=form.cleaned_data.get('message_reference_date'),
                    plugin_name=form.cleaned_data.get('plugin_name'),
                    plugin_version=form.cleaned_data.get('plugin_version'),
                    shipping_system_platform_name=form.cleaned_data.get('shipping_system_platform_name'),
                    shipping_system_platform_version=form.cleaned_data.get('shipping_system_platform_version'),
                    webstore_platform_name=form.cleaned_data.get('webstore_platform_name'),
                    webstore_platform_version=form.cleaned_data.get('webstore_platform_version'),
                )
                result = response.to_dict()
            except Exception as e:
                result = str(e)
        else:
            result = None
    else:
        form = AddressValidateForm()
        result = None

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'address_validate.html', context)



@api_view(['GET'])
def address_validate_view(request):
    api_instance = address_api.AddressApi()
    try:
        response = api_instance.exp_api_address_validate(
            type=request.GET.get('type'),
            country_code=request.GET.get('countryCode'),
            postal_code=request.GET.get('postalCode'),
            city_name=request.GET.get('cityName'),
            county_name=request.GET.get('countyName'),
            strict_validation=request.GET.get('strictValidation'),
            message_reference=request.GET.get('messageReference'),
            message_reference_date=request.GET.get('messageReferenceDate'),
            plugin_name=request.GET.get('pluginName'),
            plugin_version=request.GET.get('pluginVersion'),
            shipping_system_platform_name=request.GET.get('shippingSystemPlatformName'),
            shipping_system_platform_version=request.GET.get('shippingSystemPlatformVersion'),
            webstore_platform_name=request.GET.get('webstorePlatformName'),
            webstore_platform_version=request.GET.get('webstorePlatformVersion')
        )
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['GET'])
def identifier_view(request):
    api_instance = identifier_api.IdentifierApi()
    try:
        response = api_instance.exp_api_identifier(
            type=request.GET.get('type'),
            message_reference=request.GET.get('message_reference'),
            message_reference_date=request.GET.get('message_reference_date'),
            plugin_name=request.GET.get('plugin_name'),
            plugin_version=request.GET.get('plugin_version'),
            shipping_system_platform_name=request.GET.get('shipping_system_platform_name'),
            shipping_system_platform_version=request.GET.get('shipping_system_platform_version'),
            webstore_platform_name=request.GET.get('webstore_platform_name'),
            webstore_platform_version=request.GET.get('webstore_platform_version')
        )
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['GET'])
def invoice_view(request):
    api_instance = invoice_api.InvoiceApi()
    try:
        response = api_instance.exp_api_invoice(
            message_reference=request.GET.get('message_reference'),
            message_reference_date=request.GET.get('message_reference_date'),
            plugin_name=request.GET.get('plugin_name'),
            plugin_version=request.GET.get('plugin_version'),
            shipping_system_platform_name=request.GET.get('shipping_system_platform_name'),
            shipping_system_platform_version=request.GET.get('shipping_system_platform_version'),
            webstore_platform_name=request.GET.get('webstore_platform_name'),
            webstore_platform_version=request.GET.get('webstore_platform_version')
        )
        return JsonResponse(response.to_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



# @api_view(['GET'])
# def ratings_view(request):
#     url = "https://api-mock.dhl.com/mydhlapi/rates"
#     headers = {
#         'Message-Reference': request.GET.get('message_reference', 'SOME_STRING_VALUE'),
#         'Message-Reference-Date': request.GET.get('message_reference_date', 'SOME_STRING_VALUE'),
#         'Plugin-Name': request.GET.get('plugin_name', 'SOME_STRING_VALUE'),
#         'Plugin-Version': request.GET.get('plugin_version', 'SOME_STRING_VALUE'),
#         'Shipping-System-Platform-Name': request.GET.get('shipping_system_platform_name', 'SOME_STRING_VALUE'),
#         'Shipping-System-Platform-Version': request.GET.get('shipping_system_platform_version', 'SOME_STRING_VALUE'),
#         'Webstore-Platform-Name': request.GET.get('webstore_platform_name', 'SOME_STRING_VALUE'),
#         'Webstore-Platform-Version': request.GET.get('webstore_platform_version', 'SOME_STRING_VALUE'),
#         'Authorization': 'Basic REPLACE_BASIC_AUTH'
#     }
#     params = {
#         'accountNumber': request.GET.get('accountNumber', '123456789'),
#         'originCountryCode': request.GET.get('originCountryCode', 'CZ'),
#         'originCityName': request.GET.get('originCityName', 'Prague'),
#         'destinationCountryCode': request.GET.get('destinationCountryCode', 'CZ'),
#         'destinationCityName': request.GET.get('destinationCityName', 'Prague'),
#         'weight': request.GET.get('weight', '5'),
#         'length': request.GET.get('length', '15'),
#         'width': request.GET.get('width', '10'),
#         'height': request.GET.get('height', '5'),
#         'plannedShippingDate': request.GET.get('plannedShippingDate', '2020-02-26'),
#         'isCustomsDeclarable': request.GET.get('isCustomsDeclarable', 'false').lower() == 'true',
#         'unitOfMeasurement': request.GET.get('unitOfMeasurement', 'metric'),
#         'nextBusinessDay': request.GET.get('nextBusinessDay', 'false').lower() == 'true',
#         'strictValidation': request.GET.get('strictValidation', 'false').lower() == 'true',
#         'getAllValueAddedServices': request.GET.get('getAllValueAddedServices', 'false').lower() == 'true',
#         'requestEstimatedDeliveryDate': request.GET.get('requestEstimatedDeliveryDate', 'true').lower() == 'true',
#         'estimatedDeliveryDateType': request.GET.get('estimatedDeliveryDateType', 'QDDF')
#     }

#     response = requests.get(url, headers=headers, params=params, verify=False)

#     if response.status_code == 200:
#         return JsonResponse(response.json(), safe=False)
#     else:
#         return JsonResponse({'error': response.text}, status=response.status_code)


