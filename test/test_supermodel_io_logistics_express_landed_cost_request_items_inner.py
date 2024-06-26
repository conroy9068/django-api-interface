# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments) 

    The version of the OpenAPI document: 2.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.supermodel_io_logistics_express_landed_cost_request_items_inner import SupermodelIoLogisticsExpressLandedCostRequestItemsInner

class TestSupermodelIoLogisticsExpressLandedCostRequestItemsInner(unittest.TestCase):
    """SupermodelIoLogisticsExpressLandedCostRequestItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupermodelIoLogisticsExpressLandedCostRequestItemsInner:
        """Test SupermodelIoLogisticsExpressLandedCostRequestItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupermodelIoLogisticsExpressLandedCostRequestItemsInner`
        """
        model = SupermodelIoLogisticsExpressLandedCostRequestItemsInner()
        if include_optional:
            return SupermodelIoLogisticsExpressLandedCostRequestItemsInner(
                number = 1,
                name = 'KNITWEAR COTTON',
                description = 'KNITWEAR 100% COTTON REDUCTION PRICE FALL COLLECTION',
                manufacturer_country = 'CN',
                part_number = '12345555',
                quantity = 2,
                quantity_type = 'prt',
                unit_price = 120,
                unit_price_currency_code = 'EUR',
                customs_value = 120,
                customs_value_currency_code = 'EUR',
                commodity_code = '851713',
                weight = 5,
                weight_unit_of_measurement = 'metric',
                category = '204',
                brand = 'SHOE 1',
                goods_characteristics = [
                    openapi_client.models.supermodel_io_logistics_express_landed_cost_request_items_inner_goods_characteristics_inner.supermodelIoLogisticsExpressLandedCostRequest_items_inner_goodsCharacteristics_inner(
                        type_code = 'IMPORTER', 
                        value = 'Registered', )
                    ],
                additional_quantity_definitions = [
                    openapi_client.models.supermodel_io_logistics_express_landed_cost_request_items_inner_additional_quantity_definitions_inner.supermodelIoLogisticsExpressLandedCostRequest_items_inner_additionalQuantityDefinitions_inner(
                        type_code = 'DPR', 
                        amount = 2, )
                    ],
                estimated_tariff_rate_type = 'default_rate'
            )
        else:
            return SupermodelIoLogisticsExpressLandedCostRequestItemsInner(
                number = 1,
                quantity = 2,
                unit_price = 120,
                unit_price_currency_code = 'EUR',
        )
        """

    def testSupermodelIoLogisticsExpressLandedCostRequestItemsInner(self):
        """Test SupermodelIoLogisticsExpressLandedCostRequestItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
