# dhl_service.py
import requests
import json
from config import DHL_API_KEY, BASE_URL, DHL_SECRET

def get_jwt_token():
    url = BASE_URL + "in/transportation/token/v1/login"
    headers = {
        'ClientID': DHL_API_KEY,
        'clientSecret': DHL_SECRET
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        return response.json()["JWTToken"]
    raise Exception(f"Token generation failed: {response.text}")

def generate_waybill(data):
    url = BASE_URL + "in/transportation/waybill/v1/GenerateWayBill"
    
    # Mapping manuale dai nomi "puliti" ai nomi "nativi" di Blue Dart
    payload = json.dumps({
        "Request": {
            "Consignee": {
                "ConsigneeName": data.request.request.consignee.name,
                "ConsigneeAddress1": data.request.request.consignee.address_line_1,
                "ConsigneeAddress2": data.request.request.consignee.address_line_2,
                "ConsigneeAddress3": data.request.request.consignee.address_line_3,
                "ConsigneePincode": data.request.request.consignee.pincode,
                "ConsigneeMobile": data.request.request.consignee.mobile,
                "ConsigneeEmailID": data.request.request.consignee.email,
                "ConsigneeTelephone": data.request.request.consignee.telephone,
                "ConsigneeAddressType": data.request.request.consignee.address_type,
                "ConsigneeAttention": data.request.request.consignee.attention,
                "ConsigneeGSTNumber": data.request.request.consignee.gstn_number,
                "ConsigneeLatitude": data.request.request.consignee.latitude,
                "ConsigneeLongitude": data.request.request.consignee.longitude,
                "ConsigneeMaskedContactNumber": data.request.request.consignee.masked_contact_number,
            },
            "Services": {
                "ActualWeight": data.request.request.service.actual_weight,
                "PieceCount": data.request.request.service.piece_count,
                "ProductCode": data.request.request.service.product_code,
                "ProductType": data.request.request.service.product_type,
                "PickupDate": data.request.request.service.pickup_date,
                "PickupTime": data.request.request.service.pickup_time,
                "DeclaredValue": data.request.request.service.declared_value,
                "PackType": data.request.request.service.pack_type,
                "Dimensions": [{
                    "Length": data.request.request.service.dimensions.length,
                    "Breadth": data.request.request.service.dimensions.width,
                    "Height": data.request.request.service.dimensions.height,
                    "Count": data.request.request.service.dimensions.count
                }],
                "itemdtl": [{
                    "ItemID": data.request.request.service.itemdtl.item_id,
                    "ItemName": data.request.request.service.itemdtl.item_name,
                    "ItemValue": data.request.request.service.itemdtl.item_value,
                    "Itemquantity": data.request.request.service.itemdtl.item_quantity,
                    "HSCode": data.request.request.service.itemdtl.hs_code
                }],
                "SpecialInstruction": data.request.request.service.special_instruction,
                "RegisterPickup": data.request.request.service.register_pickup,
                "PDFOutputNotRequired": data.request.request.service.pdf_output_not_required,
            },
            "Shipper": {
                "CustomerName": data.request.request.shipper.customer_name,
                "CustomerAddress1": data.request.request.shipper.customer_address_line_1,
                "CustomerAddress2": data.request.request.shipper.customer_address_line_2,
                "CustomerAddress3": data.request.request.shipper.customer_address_line_3,
                "CustomerPincode": data.request.request.shipper.customer_pincode,
                "CustomerMobile": data.request.request.shipper.customer_mobile,
                "CustomerCode": data.request.request.shipper.customer_code,
                "OriginArea": data.request.request.shipper.origin_area,
                "Sender": data.request.request.shipper.sender,
                "VendorCode": data.request.request.shipper.vendor_code,
                "CustomerGSTNumber": data.request.request.shipper.customer_gst_number,
            },
            "Returnadds": {
                "ReturnAddress1": data.request.request.return_address.return_address_line_1,
                "ReturnAddress2": data.request.request.return_address.return_address_line_2,
                "ReturnAddress3": data.request.request.return_address.return_address_line_3,
                "ReturnContact": data.request.request.return_address.return_contact,
                "ReturnMobile": data.request.request.return_address.return_mobile,
                "ReturnPincode": data.request.request.return_address.return_pincode,
            }
        },
        "Profile": {
            "LoginID": data.request.profile.login_id,
            "LicenceKey": data.request.profile.license_key,
            "Api_type": data.request.profile.api_type
        }
    })

    headers = {
        'content-type': 'application/json',
        'JWTToken': get_jwt_token()
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def cancel_waybill(data):
    url = BASE_URL + "in/transportation/waybill/v1/CancelWaybill"
    payload = json.dumps({
        "Request": {"AWBNo": data.request.waybill_number},
        "Profile": {
            "LoginID": data.request.profile.login_id,
            "LicenceKey": data.request.profile.license_key,
            "Api_type": data.request.profile.api_type
        }
    })
    headers = {'content-type': 'application/json', 'JWTToken': get_jwt_token()}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def update_waybill(data):
    url = BASE_URL + "in/transportation/waybill/v1/UpdateEwayBill"
    payload = json.dumps({
        "ERequest": {
            "Waybillnumber": data.request.waybill_number,
            "eWaybillNumber": data.request.ewaybill_number,
            "eWaybillDate": data.request.ewaybill_date
        },
        "Profile": {
            "LoginID": data.request.profile.login_id,
            "LicenceKey": data.request.profile.license_key,
            "Api_type": data.request.profile.api_type
        }
    })
    headers = {'content-type': 'application/json', 'JWTToken': get_jwt_token()}
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

def import_data(data):
    # Logica simile a generate_waybill ma per ImportData (che accetta liste)
    url = BASE_URL + "in/transportation/waybill/v1/ImportData"
    # ... (implementazione omessa per brevità, ma segue lo stesso schema di mapping)
    return {"message": "ImportData not fully implemented in this restore point"}
