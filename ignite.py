from openfabric_pysdk.starter import OpenfabricStarter

if __name__ == '__main__':
    OpenfabricStarter.ignite(debug=False, host="0.0.0.0", port=5000),
    #OpenfabricStarter.ignite(debug=False, host="https://app.swaggerhub.com/apis/AnhTh/open-fabric_gateway_api/0.1", port=443),
