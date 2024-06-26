# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details import SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails

class TestSupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails(unittest.TestCase):
    """SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails:
        """Test SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails`
        """
        model = SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails()
        if include_optional:
            return SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails(
                name = '',
                postal_address = openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_postal_address.supermodelIoLogisticsExpressTrackingResponse_shipments_inner_shipperDetails_postalAddress(
                    city_name = '', 
                    county_name = '', 
                    postal_code = '', 
                    province_code = '', 
                    country_code = 'CZ', ),
                service_area = [
                    openapi_client.models.supermodel_io_logistics_express_tracking_response_shipments_inner_shipper_details_service_area_inner.supermodelIoLogisticsExpressTrackingResponse_shipments_inner_shipperDetails_serviceArea_inner(
                        code = 'ABC', 
                        description = 'Alpha Beta Area', 
                        outbound_sort_code = '', )
                    ]
            )
        else:
            return SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails(
        )
        """

    def testSupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails(self):
        """Test SupermodelIoLogisticsExpressTrackingResponseShipmentsInnerShipperDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
