import json
# import urllib2
import uuid
import hmac
import hashlib
import requests
import codecs

class Util():
    def momo_payment_excute(amount):
        endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
        partnerCode = "MOMOHOVU20200623"
        accessKey = "2v9LtQc2rqVaAqMw"
        serectkey = '9mDMxZ3O3bLVJY2RdMjSIV13O30Gdqbe'
        orderInfo = "pay with MoMo"
        returnUrl = "https://momo.vn/return"
        notifyurl = "https://dummy.url/notify"
        orderId = str(uuid.uuid4())
        requestId = str(uuid.uuid4())
        requestType = "captureMoMoWallet"
        extraData = "merchantName=;merchantId=" #pass empty value if your merchant does not have stores else merchantName=[storeName]; merchantId=[storeId] to identify a transaction map with a physical store

    
        rawSignature = "partnerCode="+partnerCode+"&accessKey="+accessKey+"&requestId="+requestId+"&amount="+amount+"&orderId="+orderId+"&orderInfo="+orderInfo+"&returnUrl="+returnUrl+"&notifyUrl="+notifyurl+"&extraData="+extraData

        print("--------------------RAW SIGNATURE----------------")
        print(rawSignature)
        #signature
        h = hmac.new( codecs.encode(serectkey), codecs.encode(rawSignature), hashlib.sha256 )
        signature = h.hexdigest()
        print("--------------------SIGNATURE----------------")
        print(signature)

        #json object send to MoMo endpoint

        data = {
                'partnerCode' : partnerCode,
                'accessKey' : accessKey,
                'requestId' : requestId,
                'amount' : amount,
                'orderId' : orderId,
                'orderInfo' : orderInfo,
                'returnUrl' : returnUrl,
                'notifyUrl' : notifyurl,
                'extraData' : extraData,
                'requestType' : requestType,
                'signature' : signature
        }
        data = json.dumps(data)
        res = requests.post(endpoint,data=data,headers={'Content-Type': 'application/json'})
        print(res.content)
        response = json.loads(res.content)
        return response
