from django import forms


class TrackShipmentForm(forms.Form):
    shipment_tracking_number = forms.CharField(required=False, label='Shipment Tracking Number')
    piece_tracking_number = forms.CharField(required=False, label='Piece Tracking Number')
    shipment_reference = forms.CharField(required=False, max_length=50, label='Shipment Reference')
    shipment_reference_type = forms.CharField(required=False, max_length=50, label='Shipment Reference Type')
    shipper_account_number = forms.CharField(required=False, max_length=50, label='Shipper Account Number')
    date_range_from = forms.CharField(required=False, max_length=50, label='Date Range From')
    date_range_to = forms.CharField(required=False, max_length=50, label='Date Range To')
    tracking_view = forms.CharField(required=False, max_length=50, label='Tracking View')
    level_of_detail = forms.CharField(required=False, max_length=50, label='Level Of Detail')
    request_controlled_access_data_codes = forms.BooleanField(required=False, label='Request Controlled Access Data Codes')
    message_reference = forms.CharField(required=False, max_length=50, label='Message Reference')
    message_reference_date = forms.CharField(required=False, max_length=50, label='Message Reference Date')
    plugin_name = forms.CharField(required=False, max_length=50, label='Plugin Name')
    plugin_version = forms.CharField(required=False, max_length=50, label='Plugin Version')
    shipping_system_platform_name = forms.CharField(required=False, max_length=50, label='Shipping System Platform Name')
    shipping_system_platform_version = forms.CharField(required=False, max_length=50, label='Shipping System Platform Version')
    webstore_platform_name = forms.CharField(required=False, max_length=50, label='Webstore Platform Name')
    webstore_platform_version = forms.CharField(required=False, max_length=50, label='Webstore Platform Version')

    def clean_shipment_tracking_number(self):
        data = self.cleaned_data['shipment_tracking_number']
        if data:
            return data.split(',')
        return []

    def clean_piece_tracking_number(self):
        data = self.cleaned_data['piece_tracking_number']
        if data:
            return data.split(',')
        return []

class CreateShipmentForm(forms.Form):
    planned_shipping_date_and_time = forms.DateTimeField()
    pickup_requested = forms.BooleanField(required=False)
    product_code = forms.CharField(max_length=1)
    local_product_code = forms.CharField(max_length=1)
    value_added_service_code = forms.CharField(max_length=2)
    value_added_service_value = forms.DecimalField(max_digits=10, decimal_places=2)
    value_added_service_currency = forms.CharField(max_length=3, min_length=3)
    shipper_postal_code = forms.CharField(max_length=10)
    shipper_city_name = forms.CharField(max_length=50)
    shipper_country_code = forms.CharField(max_length=2)
    shipper_address_line1 = forms.CharField(max_length=100)
    shipper_address_line2 = forms.CharField(max_length=100, required=False)
    shipper_address_line3 = forms.CharField(max_length=100, required=False)
    shipper_county_name = forms.CharField(max_length=50, required=False)
    shipper_country_name = forms.CharField(max_length=50)
    shipper_email = forms.EmailField()
    shipper_phone = forms.CharField(max_length=20)
    shipper_mobile_phone = forms.CharField(max_length=20, required=False)
    shipper_company_name = forms.CharField(max_length=100)
    shipper_full_name = forms.CharField(max_length=100)
    receiver_postal_code = forms.CharField(max_length=10)
    receiver_city_name = forms.CharField(max_length=50)
    receiver_country_code = forms.CharField(max_length=2)
    receiver_address_line1 = forms.CharField(max_length=100)
    receiver_country_name = forms.CharField(max_length=50)
    receiver_email = forms.EmailField()
    receiver_phone = forms.CharField(max_length=20)
    receiver_mobile_phone = forms.CharField(max_length=20, required=False)
    receiver_company_name = forms.CharField(max_length=100)
    receiver_full_name = forms.CharField(max_length=100)
    package_type_code = forms.ChoiceField(choices=[
        ('3BX', '3BX'), ('2BC', '2BC'), ('2BP', '2BP'), ('CE1', 'CE1'),
        ('7BX', '7BX'), ('6BX', '6BX'), ('4BX', '4BX'), ('2BX', '2BX'),
        ('1CE', '1CE'), ('WB1', 'WB1'), ('WB3', 'WB3'), ('XPD', 'XPD'),
        ('8BX', '8BX'), ('5BX', '5BX'), ('WB6', 'WB6'), ('TBL', 'TBL'),
        ('TBS', 'TBS'), ('WB2', 'WB2')
    ])
    package_weight = forms.DecimalField(max_digits=10, decimal_places=3)
    package_length = forms.DecimalField(max_digits=10, decimal_places=3)
    package_width = forms.DecimalField(max_digits=10, decimal_places=3)
    package_height = forms.DecimalField(max_digits=10, decimal_places=3)
    package_customer_reference_value = forms.CharField(max_length=50)
    package_description = forms.CharField(max_length=100)
    is_customs_declarable = forms.BooleanField(required=False)
    declared_value = forms.DecimalField(max_digits=10, decimal_places=2)
    declared_value_currency = forms.CharField(max_length=3, min_length=3)
    description = forms.CharField(max_length=100)
    incoterm = forms.ChoiceField(choices=[
        ('EXW', 'EXW'), ('FCA', 'FCA'), ('CPT', 'CPT'), ('CIP', 'CIP'),
        ('DPU', 'DPU'), ('DAP', 'DAP'), ('DDP', 'DDP'), ('FAS', 'FAS'),
        ('FOB', 'FOB'), ('CFR', 'CFR'), ('CIF', 'CIF'), ('DAF', 'DAF'),
        ('DAT', 'DAT'), ('DDU', 'DDU'), ('DEQ', 'DEQ'), ('DES', 'DES')
    ])
    unit_of_measurement = forms.ChoiceField(choices=[('metric', 'metric'), ('imperial', 'imperial')])
    # Add other necessary fields as per your requirements


class AddressValidateForm(forms.Form):
    type_ = forms.ChoiceField(required=True, choices=[('pickup', 'Pickup'), ('delivery', 'Delivery')])
    country_code = forms.CharField(required=True)
    postal_code = forms.CharField(required=False)
    city_name = forms.CharField(required=False)
    county_name = forms.CharField(required=False)
    strict_validation = forms.BooleanField(required=False)
    message_reference = forms.CharField(required=False)
    message_reference_date = forms.CharField(required=False)
    plugin_name = forms.CharField(required=False)
    plugin_version = forms.CharField(required=False)
    shipping_system_platform_name = forms.CharField(required=False)
    shipping_system_platform_version = forms.CharField(required=False)
    webstore_platform_name = forms.CharField(required=False)
    webstore_platform_version = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Overriding form widgets to add "form-control" class (bootstrap class).
        # This way you can pass html attributes to the form fields.
        for field in self.fields:
            if field not in ['type_', 'strict_validation']:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

        # This field is a "select"
        self.fields['type_'].widget.attrs.update({'class': 'form-select', 'autocomplete': 'off'})

        # This field is a "checkbox"
        self.fields['strict_validation'].widget.attrs.update({'class': 'form-check', 'autocomplete': 'off'})

    def clean_country_code(self):
        # An example of how to "clean" fields.
        # Let's assume the country_code must be one of the following list and if it's not
        # we return an error. You can customize this as you wish
        country_code = self.cleaned_data['country_code']


        # This is just for an example, you can just delete this method or modify it as per your needs.
        if country_code not in ['CZ', 'TR', 'AE', 'IR']:
            self.add_error('country_code', f'"{country_code}" is not a valid country code.')


        return country_code

    def clean_message_reference(self):
        message_reference = self.cleaned_data['message_reference']
        if len(message_reference) <= 28:
            return None
        else:
            return message_reference
