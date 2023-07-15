#Login Credentials
import pyotp
from api_helper import ShoonyaApiPy
import logging
#import pandas as pd
user    = 'FAXXXX0'
pwd     = 'password'
factor2 = '32K62XREXXXX----------------Y'
vc      = 'FAXXXX0_U'
app_key = 'cxxxxxxxxxxxxxxxxxxxxxxxx1'
imei    = 'abc1234'

### Generating TOTP(factor2) thru system automatically

token   = pyotp.TOTP(factor2).now()
