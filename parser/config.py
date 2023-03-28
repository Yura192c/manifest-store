import requests
from fake_useragent import UserAgent

ua = UserAgent()
import requests

cookies = {
    '_schn': '_cich3u',
    'geo_ip': '83.171.250.12',
    'adidas_country': 'us',
    'geo_country': 'US',
    'geo_state': 'CA',
    'onesite_country': 'US',
    'gl-feat-enable': 'CHECKOUT_PAGES_ENABLED',
    'badab': 'true',
    'akacd_phased_PDP': '3857303664~rv=36~id=5dda38619f73acb3f760fdcb5a62fe39',
    '_abck': '28E8BC81DA1E8F8DFDA5EA1D4905C2C6~-1~YAAQJqbcF+R0EBaHAQAAfgfrHgkPUP3zuJo0xCN+Ri6ZrEKfin2jz360T8u5qTb40khO1AhYvE8EpLgV1siNyydFchtcbJDO3t9+Tk2zN2jKlfyI9pujdMFo5PCxQNPtJtn05agy+5rbg0BT4R9uz5mxw7wPKvgrq/tnauyf+sAzFhxheC68QJ37Qm5NfH8ubxCRMGpkNRAdhlHKH+/SPVurwlAwd9aEZ2yedbuC3zne0WfennP9k6dSyzMtI/130FSDAO3sMuV1xQ/AUKK3l2ewewytapi2vzRUpuU7/rEX9S3B/9fkcjgtx6JU9n/3UCvcY0pm6IDzrEqrjNnwRboIJQDikCsCz6IViQK+B8KSO+LSgrMHifHoyA719EousyHHFV71bconeyMuiM8EDp24ivONYy9mShqzjrHqcL8+IJ6Ks6EhvhfeQcbpbOA7eLL9D2kp4BI=~-1~-1~1679854417',
    'akacd_Phased_www_adidas_com_Generic': '3857303666~rv=90~id=7ccac71816219a5f5694588ceee97d52',
    'UserSignUpAndSave': '2',
    'persistentBasketCount': '0',
    'userBasketCount': '0',
    'newsletterShownOnVisit': 'true',
    'dwac_bcl5MiaaieF4EaaadeoW6TIGjI': 'LuXUsJpFJ9VybpbGPWM8I_QGesDFA7G94HI%3D|dw-only|||USD|false|US%2FPacific|true',
    'sid': 'LuXUsJpFJ9VybpbGPWM8I_QGesDFA7G94HI',
    'dwanonymous_e23325cdedf446c9a41915343e601cde': 'cfjQRbn6E5zdd90PiMPHcJax8i',
    'pagecontext_secure_cookies': '',
    'pagecontext_cookies': '',
    'dwsid': 'fcCmqlqkHIku_FIgtcb8KYKbe9dkAJaCo-H2EK71SQwxUb7lhg7gzyTk3sRla2k-r17fjPSHuZrXWBsU5rsGrA==',
    'fallback_dwsid': 'fcCmqlqkHIku_FIgtcb8KYKbe9dkAJaCo-H2EK71SQwxUb7lhg7gzyTk3sRla2k-r17fjPSHuZrXWBsU5rsGrA==',
    'mt.v': '5.1593700607.1679850874863',
    'RT': '"z=1&dm=adidas.com&si=89ac045d-a0e6-4ee1-98e8-e910c1f374ba&ss=lfpnutbu&sl=0&tt=0&bcn=%2F%2F17de4c1c.akstat.io%2F"',
    'utag_main': 'v_id:01871eea497100202c957bb9eee405046003b00900bd0$_sn:1$_se:12$_ss:0$_st:1679852731535$ses_id:1679850883442%3Bexp-session$_pn:2%3Bexp-session$_vpn:3%3Bexp-session$ab_dc:CONTROL%3Bexp-1685034917890$_prevpage:PRODUCT%7CADISTAR%20RUNNING%20SHOES%20(GY1685)%3Bexp-1679854526109$ttdsyncran:1%3Bexp-session$dcsyncran:1%3Bexp-session$dc_visit:1$dc_event:2%3Bexp-session',
    'ab_qm': 'b',
    'AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19443%7CMCMID%7C46024977807491213115857636864428035193%7CMCAID%7CNONE%7CMCOPTOUT-1679858099s%7CNONE%7CMCAAMLH-1680455699%7C7%7CMCAAMB-1680455699%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y',
    'ab_inp': 'b',
    'AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg': '1',
    's_pers': '%20s_vnum%3D1680296400598%2526vn%253D1%7C1680296400598%3B%20s_invisit%3Dtrue%7C1679852731622%3B',
    's_cc': 'true',
    '_rdt_uuid': '1679850888781.da962603-91b0-4517-b3f4-ec8bd0c1da8f',
    '_scid': 'a5beb816-8659-49d3-b442-85927ff18b3d',
    'BVBRANDID': '1feccbef-c2e1-4c07-9e34-74eca2b76109',
    '_gcl_au': '1.1.365792524.1679850892',
    '_ga_4DGGV4HV95': 'GS1.1.1679850891.1.1.1679850927.0.0.0',
    '_ga': 'GA1.2.1407509617.1679850892',
    '_pin_unauth': 'dWlkPVlXWTFNelV4TUdRdE9HTXpNQzAwTm1FM0xUa3hOR010TTJKbU16WXdOalk1WlRWbA',
    'IR_gbd': 'adidas.com',
    'IR_PI': 'b9f045ed-cbf9-11ed-ba87-cfcc91173249%7C1679937291591',
    'QuantumMetricUserID': '3aec0a61fc1475c5eafaf4415f33c4a5',
    '_fbp': 'fb.1.1679850901932.737886536',
    '_sctr': '1|1679778000000',
    '_uetvid': 'b70c66a0cbf911ed880ebf8b1d62ca43',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru,en-US;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
    # 'Cookie': '_schn=_cich3u; geo_ip=83.171.250.12; adidas_country=us; geo_country=US; geo_state=CA; onesite_country=US; gl-feat-enable=CHECKOUT_PAGES_ENABLED; badab=true; akacd_phased_PDP=3857303664~rv=36~id=5dda38619f73acb3f760fdcb5a62fe39; _abck=28E8BC81DA1E8F8DFDA5EA1D4905C2C6~-1~YAAQJqbcF+R0EBaHAQAAfgfrHgkPUP3zuJo0xCN+Ri6ZrEKfin2jz360T8u5qTb40khO1AhYvE8EpLgV1siNyydFchtcbJDO3t9+Tk2zN2jKlfyI9pujdMFo5PCxQNPtJtn05agy+5rbg0BT4R9uz5mxw7wPKvgrq/tnauyf+sAzFhxheC68QJ37Qm5NfH8ubxCRMGpkNRAdhlHKH+/SPVurwlAwd9aEZ2yedbuC3zne0WfennP9k6dSyzMtI/130FSDAO3sMuV1xQ/AUKK3l2ewewytapi2vzRUpuU7/rEX9S3B/9fkcjgtx6JU9n/3UCvcY0pm6IDzrEqrjNnwRboIJQDikCsCz6IViQK+B8KSO+LSgrMHifHoyA719EousyHHFV71bconeyMuiM8EDp24ivONYy9mShqzjrHqcL8+IJ6Ks6EhvhfeQcbpbOA7eLL9D2kp4BI=~-1~-1~1679854417; akacd_Phased_www_adidas_com_Generic=3857303666~rv=90~id=7ccac71816219a5f5694588ceee97d52; UserSignUpAndSave=2; persistentBasketCount=0; userBasketCount=0; newsletterShownOnVisit=true; dwac_bcl5MiaaieF4EaaadeoW6TIGjI=LuXUsJpFJ9VybpbGPWM8I_QGesDFA7G94HI%3D|dw-only|||USD|false|US%2FPacific|true; sid=LuXUsJpFJ9VybpbGPWM8I_QGesDFA7G94HI; dwanonymous_e23325cdedf446c9a41915343e601cde=cfjQRbn6E5zdd90PiMPHcJax8i; pagecontext_secure_cookies=; pagecontext_cookies=; dwsid=fcCmqlqkHIku_FIgtcb8KYKbe9dkAJaCo-H2EK71SQwxUb7lhg7gzyTk3sRla2k-r17fjPSHuZrXWBsU5rsGrA==; fallback_dwsid=fcCmqlqkHIku_FIgtcb8KYKbe9dkAJaCo-H2EK71SQwxUb7lhg7gzyTk3sRla2k-r17fjPSHuZrXWBsU5rsGrA==; mt.v=5.1593700607.1679850874863; RT="z=1&dm=adidas.com&si=89ac045d-a0e6-4ee1-98e8-e910c1f374ba&ss=lfpnutbu&sl=0&tt=0&bcn=%2F%2F17de4c1c.akstat.io%2F"; utag_main=v_id:01871eea497100202c957bb9eee405046003b00900bd0$_sn:1$_se:12$_ss:0$_st:1679852731535$ses_id:1679850883442%3Bexp-session$_pn:2%3Bexp-session$_vpn:3%3Bexp-session$ab_dc:CONTROL%3Bexp-1685034917890$_prevpage:PRODUCT%7CADISTAR%20RUNNING%20SHOES%20(GY1685)%3Bexp-1679854526109$ttdsyncran:1%3Bexp-session$dcsyncran:1%3Bexp-session$dc_visit:1$dc_event:2%3Bexp-session; ab_qm=b; AMCV_7ADA401053CCF9130A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19443%7CMCMID%7C46024977807491213115857636864428035193%7CMCAID%7CNONE%7CMCOPTOUT-1679858099s%7CNONE%7CMCAAMLH-1680455699%7C7%7CMCAAMB-1680455699%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y; ab_inp=b; AMCVS_7ADA401053CCF9130A490D4C%40AdobeOrg=1; s_pers=%20s_vnum%3D1680296400598%2526vn%253D1%7C1680296400598%3B%20s_invisit%3Dtrue%7C1679852731622%3B; s_cc=true; _rdt_uuid=1679850888781.da962603-91b0-4517-b3f4-ec8bd0c1da8f; _scid=a5beb816-8659-49d3-b442-85927ff18b3d; BVBRANDID=1feccbef-c2e1-4c07-9e34-74eca2b76109; _gcl_au=1.1.365792524.1679850892; _ga_4DGGV4HV95=GS1.1.1679850891.1.1.1679850927.0.0.0; _ga=GA1.2.1407509617.1679850892; _pin_unauth=dWlkPVlXWTFNelV4TUdRdE9HTXpNQzAwTm1FM0xUa3hOR010TTJKbU16WXdOalk1WlRWbA; IR_gbd=adidas.com; IR_PI=b9f045ed-cbf9-11ed-ba87-cfcc91173249%7C1679937291591; QuantumMetricUserID=3aec0a61fc1475c5eafaf4415f33c4a5; _fbp=fb.1.1679850901932.737886536; _sctr=1|1679778000000; _uetvid=b70c66a0cbf911ed880ebf8b1d62ca43',
}

# DRIVER_PATH = '../parser/chromedriver'