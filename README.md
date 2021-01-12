1. GET API to fetch a bank details, given branch IFSC code

curl --location --request GET 'https://limitless-beach-02623.herokuapp.com/api/bank-details/?ifsc=ABHY0065003' \
--header 'Authorization: Bearer e89618db5e9860ff38620783e898e9d44f644203'

2. GET API to fetch all details of branches, given bank name and a city. This API should also
support limit and offset parameters

curl --location --request GET 'https://limitless-beach-02623.herokuapp.com/api/bank-details/filtered/?bank_name=HDFC%20BANK&city=MUMBAI' \
--header 'Authorization: Bearer e89618db5e9860ff38620783e898e9d44f644203'

curl --location --request GET 'https://limitless-beach-02623.herokuapp.com/api/bank-details/filtered/?bank_name=HDFC+BANK&city=MUMBAI&limit=10&offset=10%22' \
--header 'Authorization: Bearer e89618db5e9860ff38620783e898e9d44f644203'