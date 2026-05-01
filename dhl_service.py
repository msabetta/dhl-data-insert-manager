# dhl_service.py
import requests
import base64
import json
from config import DHL_API_KEY, BASE_URL, DHL_SECRET

headers = {
    "DHL-API-Key": DHL_API_KEY,
    "DHL-API-Secret": DHL_SECRET,
    "Content-Type": "application/json"
}

def generate_waybill(data):
    url = f"{BASE_URL}/GenerateWayBill"

    payload = json.dumps({
    "Request": {
        "Consignee": {
        "ConsigneeGSTNumber": "string",
        "ConsigneeTelephone": data.receiver.phone,
        "ConsigneeEmailID": data.receiver.email,
        "ConsigneeMobile": data.receiver.phone,
        "ConsigneeLatitude": "string",
        "ConsigneeName": data.receiver.name,
        "ConsigneeAddress2": "string",
        "ConsigneeAddressType": "O",
        "AvailableTiming": data.receiver.available_timing,
        "AvailableDays": data.receiver.available_days,
        "ConsigneeIDType": "st",
        "ConsigneeID": data.receiver.identification_number,
        "ConsigneeFiscalIDType": "st",
        "ConsigneeFiscalID": data.receiver.fiscal_id,
        "ConsingeeFederalTaxId": "string",
        "ConsingeeStateTaxId": "string",
        "ConsingeeRegistrationNumber": data.receiver.registration_number,
        "ConsingeeRegistrationNumberTypeCode": "SDT",
        "ConsingeeRegistrationNumberIssuerCountryCode": "st",
        "ConsigneeBusinessPartyTypeCode": data.receiver.business_type,
        "ConsigneeFullAddress": data.receiver.address,
        "ConsigneeAddress1": data.receiver.address,
        "ConsigneeAddress3": "string",
        "ConsigneePincode": "string",
        "ConsigneeAttention": data.receiver.attention,
        "ConsigneeLongitude": "string",
        "ConsigneeAddressinfo": "string",
        "ConsigneeCountryCode": data.receiver.country,
        "ConsigneeStateCode": data.receiver.state,
        "ConsigneeCityName": data.receiver.city,
        "ConsigneeMaskedContactNumber": "string"
        },
        "Services": {
        "SpecialInstruction": data.special_instruction,
        "DeclaredValue": data.service.declared_value,
        "CollactableAmount": 0,
        "PieceCount": None,
        "PickupTime": "stri",
        "ActualWeight": None,
        "PackType": "s",
        "InvoiceNo": "string",
        "ProductCode": "s",
        "RegisterPickup": True,
        "DeliveryTimeSlot": "string",
        "IsReversePickup": True,
        "IsForcePickup": True,
        "ParcelShopCode": "string",
        "ForwardAWBNo": "string",
        "ForwardLogisticCompName": "string",
        "CreditReferenceNo2": "string",
        "CreditReferenceNo3": "string",
        "PickupMode": data.service.pickup_mode,
        "PickupType": "string",
        "ItemCount": data.service.item_count,
        "IsPartialPickup": True,
        "TotalCashPaytoCustomer": 0,
        "PreferredPickupTimeSlot": "string",
        "DeferredDeliveryDays": 0,
        "Officecutofftime": "string",
        "PDFOutputNotRequired": True,
        "ProductType": 0,
        "Dimensions": [
            {
            "Length": 0,
            "Breadth": 0,
            "Height": 0,
            "Count": 0
            }
        ],
        "ECCN": "string",
        "FreightCharge": 0,
        "InsurenceCharge": 0,
        "CessCharge": 0,
        "ReverseCharge": 0,
        "PayerGSTVAT": 0,
        "AdditionalDeclaration": "string",
        "NotificationMessage": "string",
        "IsCargoShipment": True,
        "ExportReason": "string",
        "BankAccountNumber": "string",
        "GovNongovType": "G",
        "NFEIFlag": True,
        "itemdtl": [
            {
            "ItemID": "string",
            "ItemName": "string",
            "ProductDesc1": "string",
            "ProductDesc2": "string",
            "SubProduct1": "string",
            "SubProduct2": "string",
            "SubProduct3": "string",
            "SubProduct4": "string",
            "ReturnReason": "string",
            "Instruction": "string",
            "ItemValue": 0,
            "SKUNumber": "string",
            "Itemquantity": 0,
            "countryOfOrigin": "st",
            "HSCode": "string",
            "TaxableAmount": 0,
            "CGSTAmount": 0,
            "SGSTAmount": 0,
            "IGSTAmount": 0,
            "TotalValue": 0,
            "PlaceofSupply": "string",
            "InvoiceNumber": "string",
            "InvoiceDate": "string",
            "SellerName": "string",
            "SellerGSTNNumber": "string",
            "cessAmount": 0,
            "eWaybillNumber": 0,
            "eWaybillDate": "string",
            "supplyType": "s",
            "subSupplyType": 0,
            "docType": 1,
            "PerUnitRate": 0,
            "PieceID": "stri",
            "Unit": "str",
            "IGSTRate": 0,
            "Discount": 0,
            "Weight": 0,
            "CommodityCode": "string",
            "LicenseNumber": "string",
            "LicenseExpiryDate": "string",
            "ManufactureCountryCode": "st",
            "ManufactureCountryName": "st",
            "PieceIGSTPercentage": 0
            }
        ],
        "ItemImg": [
            {
            "AWBNo": "string",
            "ItemID": "string",
            "ImageURL": "string"
            }
        ],
        "PDFPrintContent": "string",
        "CustomerEDD": "string",
        "IsDDN": True,
        "IsCommercialShipment": True,
        "IsDutyTaxPaidByShipper": True,
        "ExchangeWaybillNo": "string",
        "PickupDate": "string",
        "noOfDCGiven": 0,
        "AWBNo": "string",
        "OTPCode": "string",
        "Total_IGST_Paid": 0,
        "SupplyOfIGST": "Yes",
        "SupplyOfwoIGST": "Yes",
        "IncotermCode": "strin",
        "IsChequeDD": "Q",
        "InsurancePaidBy": "O",
        "FavouringName": "string",
        "PayableAt": "string",
        "PreferredDeliveryDate": "stringst",
        "PrinterLableSize": "string",
        "DynamicQCDetails": [
            {
            "ItemID": "string",
            "QuestionId": "string",
            "QuestionDescription": "string",
            "QuestionValue": "string",
            "ExpectedAnswers": "Y",
            "IsQCMandate": True
            }
        ],
        "IsIntlEcomCSBUser": True,
        "ExportImportCode": "string",
        "TermsOfTrade": "CIF",
        "IsEcomUser": "1",
        "InsuranceAmount": 0,
        "AuthorizedDealerCode": "string",
        "CurrencyCode": "str",
        "OrderURL": "string",
        "EsellerPlatformName": "string",
        "BillingReference1": "string",
        "BillingReference2": "string",
        "MarketplaceName": "string",
        "MarketplaceURL": "string",
        "BillToCompanyName": "string",
        "BillToContactName": "string",
        "BillToAddressLine1": "string",
        "BillToCity": "string",
        "BillToSuburb": "string",
        "BillToState": "string",
        "BillToCountryName": "string",
        "BillToCountryCode": "st",
        "BillToPhoneNumber": "string",
        "BillToFederalTaxID": "string",
        "ExporterCompanyName": "string",
        "ExporterSuiteDepartmentName": "string",
        "ExporterAddressLine1": "string",
        "ExporterAddressLine2": "string",
        "ExporterAddressLine3": "string",
        "ExporterCity": "string",
        "ExporterDivision": "string",
        "ExporterDivisionCode": "st",
        "ExporterPostalCode": "string",
        "ExporterCountryCode": "st",
        "ExporterCountryName": "string",
        "ExporterPersonName": "string",
        "ExporterPhoneNumber": "string",
        "ExporterFaxNumber": "string",
        "ExporterEmail": "string",
        "ExporterMobilePhoneNumber": "string",
        "ExporterRegistrationNumber": "string",
        "ExporterRegistrationNumberTypeCode": "SDT",
        "ExporterRegistrationNumberIssuerCountryCode": "st",
        "ExporterBusinessPartyTypeCode": "BU",
        "SignatureName": "string",
        "SignatureTitle": "string",
        "Commodity": {
            "CommodityDetail1": "string",
            "CommodityDetail2": "string",
            "CommodityDetail3": "string"
        },
        "OTPBasedDelivery": "string",
        "SubProductCode": "C",
        "CreditReferenceNo": "string"
        },
        "Shipper": {
        "CustomerAddressinfo": "string",
        "CustomerLongitude": "string",
        "CustomerMobile": "stringstri",
        "CustomerGSTNumber": "string",
        "CustomerCode": "string",
        "OriginArea": "str",
        "Sender": "string",
        "CustomerPincode": "string",
        "CustomerTelephone": "string",
        "CustomerEmailID": "string",
        "IsToPayCustomer": True,
        "CustomerAddress3": "string",
        "CustomerAddress2": "string",
        "VendorCode": "string",
        "CustomerName": "string",
        "CustomerAddress1": "string",
        "CustomerMaskedContactNumber": "string",
        "CustomerFiscalIDType": "st",
        "CustomerFiscalID": "string",
        "CustomerRegistrationNumber": "string",
        "CustomerRegistrationNumberTypeCode": "EOR",
        "CustomerRegistrationNumberIssuerCountryCode": "AT",
        "CustomerBusinessPartyTypeCode": "BU",
        "CustomerLatitude": "string"
        },
        "Returnadds": {
        "ManifestNumber": "string",
        "ReturnMobile": "stringstri",
        "ReturnPincode": "string",
        "ReturnEmailID": "string",
        "ReturnContact": "string",
        "ReturnMaskedContactNumber": "string",
        "ReturnTelephone": "string",
        "ReturnAddress3": "string",
        "ReturnAddress2": "string",
        "ReturnAddress1": "string",
        "ReturnLatitude": "string",
        "ReturnLongitude": "string",
        "ReturnAddressinfo": "string"
        }
    },
    "Profile": {
        "LoginID": "string",
        "Api_type": "string",
        "LicenceKey": "string"
    }
    })
    headers = {
    'content-type': 'application/json',
    'JWTToken': 'REPLACE_KEY_VALUE'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code != 200:
        raise Exception(response.text)

    res = response.json()

    return res["GenerateWayBillResult"]



def create_shipment(data):
    url = f"{BASE_URL}/shipments"

    payload = {
        "plannedShippingDateAndTime": "2026-05-01T10:00:00GMT+01:00",
        "productCode": data.service,
        "customerDetails": {
            "shipperDetails": {
                "postalAddress": {
                    "postalCode": data.shipper.postal_code,
                    "cityName": data.shipper.city,
                    "countryCode": data.shipper.country,
                    "addressLine1": data.shipper.address
                },
                "contactInformation": {
                    "fullName": data.shipper.name,
                    "phone": data.shipper.phone
                }
            },
            "receiverDetails": {
                "postalAddress": {
                    "postalCode": data.receiver.postal_code,
                    "cityName": data.receiver.city,
                    "countryCode": data.receiver.country,
                    "addressLine1": data.receiver.address
                },
                "contactInformation": {
                    "fullName": data.receiver.name,
                    "phone": data.receiver.phone
                }
            }
        },
        "content": {
            "packages": [
                {
                    "weight": data.package.weight,
                    "dimensions": {
                        "length": data.package.length,
                        "width": data.package.width,
                        "height": data.package.height
                    }
                }
            ]
        }
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(response.text)

    res = response.json()

    tracking = res["shipmentTrackingNumber"]
    label_base64 = res["documents"][0]["content"]

    label_file = f"label_{tracking}.pdf"

    with open(label_file, "wb") as f:
        f.write(base64.b64decode(label_base64))

    return {
        "tracking": tracking,
        "label_file": label_file
    }


def track_shipment(tracking):
    url = f"{BASE_URL}/track/shipments?trackingNumber={tracking}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(response.text)

    res = response.json()

    return res["shipments"][0]["status"]["statusCode"]