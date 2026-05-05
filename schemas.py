# schemas.py
from pydantic import BaseModel
from typing import List, Optional

class Profile(BaseModel):
    login_id: str
    api_type: str
    license_key: str
    customer_code: Optional[str] = None
    area: Optional[str] = None
    version: Optional[str] = None
    is_admin: Optional[str] = None

class Consignee(BaseModel):
    name: str
    address_line_1: str
    address_line_2: Optional[str] = ""
    address_line_3: Optional[str] = ""
    pincode: int
    mobile: int
    email: Optional[str] = ""
    telephone: Optional[str] = ""
    address_type: Optional[str] = "R"
    attention: Optional[str] = ""
    gstn_number: Optional[str] = ""
    latitude: Optional[str] = ""
    longitude: Optional[str] = ""
    masked_contact_number: Optional[str] = ""
    city_name: Optional[str] = ""
    state_code: Optional[str] = ""
    country_code: Optional[str] = ""
    address_info: Optional[str] = ""
    id_type: Optional[str] = ""
    id: Optional[str] = ""
    fiscal_id_type: Optional[str] = ""
    fiscal_id: Optional[str] = ""
    federal_tax_id: Optional[str] = ""
    state_tax_id: Optional[str] = ""
    registration_number: Optional[str] = ""
    registration_number_type_code: Optional[str] = ""
    registration_number_issuer_country_code: Optional[str] = ""
    business_party_type_code: Optional[str] = ""
    full_address: Optional[str] = ""
    available_timing: Optional[str] = ""
    available_days: Optional[str] = ""

class ReturnAddress(BaseModel):
    return_address_line_1: str
    return_address_line_2: Optional[str] = ""
    return_address_line_3: Optional[str] = ""
    return_contact: str
    return_mobile: int
    return_pincode: int
    return_email_id: Optional[str] = ""
    return_telephone: Optional[str] = ""
    return_latitude: Optional[str] = ""
    return_longitude: Optional[str] = ""
    return_masked_contact_number: Optional[str] = ""
    manifest_number: Optional[str] = ""
    return_address_info: Optional[str] = ""

class Dimensions(BaseModel):
    length: float
    width: float
    height: float
    count: int

class ItemDetail(BaseModel):
    item_id: str
    item_name: Optional[str] = ""
    product_desc_1: Optional[str] = ""
    product_desc_2: Optional[str] = ""
    item_value: float
    item_quantity: int
    sku_number: Optional[str] = ""
    hs_code: Optional[str] = ""
    taxable_amount: Optional[float] = 0.0
    cgst_amount: Optional[float] = 0.0
    sgst_amount: Optional[float] = 0.0
    igst_amount: Optional[float] = 0.0
    total_value: Optional[float] = 0.0
    return_reason: Optional[str] = ""
    instruction: Optional[str] = ""
    country_of_origin: Optional[str] = "IN"

class Service(BaseModel):
    actual_weight: float
    piece_count: int
    product_code: str
    product_type: int
    pickup_date: str
    pickup_time: str
    declared_value: float
    pack_type: str
    dimensions: Dimensions
    itemdtl: ItemDetail
    special_instruction: Optional[str] = ""
    register_pickup: bool = True
    pdf_output_not_required: bool = True
    is_reverse_pickup: bool = False
    is_force_pickup: bool = False
    collactable_amount: Optional[float] = 0.0
    pickup_mode: Optional[str] = "P"
    pickup_type: Optional[str] = "O"
    item_count: Optional[int] = 1
    is_partial_pickup: Optional[bool] = False
    total_cash_pay_to_customer: Optional[float] = 0.0
    preferred_pickup_time_slot: Optional[str] = ""
    delivery_time_slot: Optional[str] = ""
    forward_awb_no: Optional[str] = ""
    forward_logistic_comp_name: Optional[str] = ""
    credit_reference_no_2: Optional[str] = ""
    credit_reference_no_3: Optional[str] = ""
    deferred_delivery_days: Optional[int] = 0
    office_cutoff_time: Optional[str] = ""
    eccn: Optional[str] = ""
    freight_charge: Optional[float] = 0.0
    insurence_charge: Optional[float] = 0.0
    cess_charge: Optional[float] = 0.0
    reverse_charge: Optional[float] = 0.0
    payer_gst_vat: Optional[int] = 0
    additional_declaration: Optional[str] = ""
    notification_message: Optional[str] = ""
    is_cargo_shipment: Optional[bool] = False
    export_reason: Optional[str] = ""
    bank_account_number: Optional[str] = ""
    gov_non_gov_type: Optional[str] = ""
    nfei_flag: Optional[bool] = False
    pdf_print_content: Optional[str] = ""
    customer_edd: Optional[str] = ""
    is_ddn: Optional[bool] = False
    is_commercial_shipment: Optional[bool] = False
    is_duty_tax_paid_by_shipper: Optional[bool] = False
    exchange_waybill_no: Optional[str] = ""
    no_of_dc_given: Optional[int] = 0
    awb_no: Optional[str] = ""
    otp_code: Optional[int] = 0
    total_igst_paid: Optional[float] = 0.0
    supply_of_igst: Optional[str] = ""
    supply_of_wo_igst: Optional[str] = ""
    incoterm_code: Optional[str] = ""
    is_cheque_dd: Optional[str] = ""
    insurance_paid_by: Optional[str] = ""
    favouring_name: Optional[str] = ""
    payable_at: Optional[str] = ""
    preferred_delivery_date: Optional[str] = ""
    printer_lable_size: Optional[str] = ""
    is_intl_ecom_csb_user: Optional[bool] = False
    export_import_code: Optional[str] = ""
    terms_of_trade: Optional[str] = ""
    is_ecom_user: Optional[str] = ""
    insurance_amount: Optional[float] = 0.0
    authorized_dealer_code: Optional[str] = ""
    currency_code: Optional[str] = ""
    order_url: Optional[str] = ""
    eseller_platform_name: Optional[str] = ""
    billing_reference_1: Optional[str] = ""
    billing_reference_2: Optional[str] = ""
    marketplace_name: Optional[str] = ""
    marketplace_url: Optional[str] = ""
    bill_to_company_name: Optional[str] = ""
    bill_to_contact_name: Optional[str] = ""
    bill_to_address_line_1: Optional[str] = ""
    bill_to_city: Optional[str] = ""
    bill_to_suburb: Optional[str] = ""
    bill_to_state: Optional[str] = ""
    bill_to_country_name: Optional[str] = ""
    bill_to_country_code: Optional[str] = ""
    bill_to_phone_number: Optional[str] = ""
    bill_to_federal_tax_id: Optional[str] = ""
    exporter_company_name: Optional[str] = ""
    exporter_suite_department_name: Optional[str] = ""
    exporter_address_line_1: Optional[str] = ""
    exporter_address_line_2: Optional[str] = ""
    exporter_address_line_3: Optional[str] = ""
    exporter_city: Optional[str] = ""
    exporter_division: Optional[str] = ""
    exporter_division_code: Optional[str] = ""
    exporter_postal_code: Optional[str] = ""
    exporter_country_code: Optional[str] = ""
    exporter_country_name: Optional[str] = ""
    exporter_person_name: Optional[str] = ""
    exporter_phone_number: Optional[str] = ""
    exporter_fax_number: Optional[str] = ""
    exporter_email: Optional[str] = ""
    exporter_mobile_phone_number: Optional[str] = ""
    exporter_registration_number: Optional[str] = ""
    exporter_registration_number_type_code: Optional[str] = ""
    exporter_registration_number_issuer_country_code: Optional[str] = ""
    exporter_business_party_type_code: Optional[str] = ""
    signature_name: Optional[str] = ""
    signature_title: Optional[str] = ""
    commodity_detail_1: Optional[str] = ""
    commodity_detail_2: Optional[str] = ""
    commodity_detail_3: Optional[str] = ""
    otp_based_delivery: Optional[str] = ""
    sub_product_code: Optional[str] = ""
    credit_reference_no: Optional[str] = ""

class Shipper(BaseModel):
    customer_name: str
    customer_address_line_1: str
    customer_address_line_2: Optional[str] = ""
    customer_address_line_3: Optional[str] = ""
    customer_pincode: int
    customer_mobile: int
    customer_code: str
    origin_area: str
    sender: str
    vendor_code: str
    customer_email_id: Optional[str] = ""
    customer_gst_number: Optional[str] = ""
    customer_telephone: Optional[str] = ""
    is_to_pay_customer: Optional[str] = "N"
    customer_latitude: Optional[str] = ""
    customer_longitude: Optional[str] = ""
    customer_masked_contact_number: Optional[str] = ""
    customer_address_info: Optional[str] = ""
    customer_fiscal_id_type: Optional[str] = ""
    customer_fiscal_id: Optional[str] = ""
    customer_registration_number: Optional[str] = ""
    customer_registration_number_type_code: Optional[str] = ""
    customer_registration_number_issuer_country_code: Optional[str] = ""
    customer_business_party_type_code: Optional[str] = ""

class WaybillRequest(BaseModel):
    consignee: Consignee
    service: Service
    shipper: Shipper
    return_address: ReturnAddress
    invoice_number: Optional[str] = ""
    seller_gst_number: Optional[str] = ""
    waybill_number: Optional[int] = 0

class ERequest(BaseModel):
    profile: Profile
    request: WaybillRequest
    invoice_number: Optional[str] = ""
    invoice_date: Optional[str] = ""
    seller_gstn_number: Optional[str] = ""
    ewaybill_date: Optional[str] = ""
    ewaybill_number: Optional[int] = 0
    waybill_number: Optional[int] = 0

class ShipmentRequest(BaseModel):
    request: ERequest

class UpdateWaybillRequest(BaseModel):
    request: ERequest

class CancelWaybillRequest(BaseModel):
    request: ERequest

class ImportDataRequest(BaseModel):
    request: ERequest

class LoginRequest(BaseModel):
    api_client_id: str
    api_client_secret: str
    token: Optional[str] = None
