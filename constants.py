WEB_URL = "https://food.grab.com/v1/autocomplete"
REQUEST_PARAMS = {
  "component": "country:SG",
  "language": "en",
  "transportType": 0,
  "keyword": "India",
  "Limit":2

}
http_proxy  = "http://159.89.195.14:80"
https_proxy = "https://23.106.122.179:3128"
ftp_proxy = "ftp://10.10.1.10:3128"

REQUEST_PROXY = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }