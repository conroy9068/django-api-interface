# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.shipment_limitations_by_piece import ShipmentLimitationsByPiece

class TestShipmentLimitationsByPiece(unittest.TestCase):
    """ShipmentLimitationsByPiece unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShipmentLimitationsByPiece:
        """Test ShipmentLimitationsByPiece
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShipmentLimitationsByPiece`
        """
        model = ShipmentLimitationsByPiece()
        if include_optional:
            return ShipmentLimitationsByPiece(
                piece_size_limit1 = openapi_client.models.value_unit.ValueUnit(
                    value = 1.337, 
                    uom = '', ),
                piece_size_limit2 = openapi_client.models.value_unit.ValueUnit(
                    value = 1.337, 
                    uom = '', ),
                piece_size_limit3 = openapi_client.models.value_unit.ValueUnit(
                    value = 1.337, 
                    uom = '', ),
                max_piece_weight = openapi_client.models.value_unit.ValueUnit(
                    value = 1.337, 
                    uom = '', ),
                html = ''
            )
        else:
            return ShipmentLimitationsByPiece(
        )
        """

    def testShipmentLimitationsByPiece(self):
        """Test ShipmentLimitationsByPiece"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
