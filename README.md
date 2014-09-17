Import hacked dnspod python package 
./setup.py install

Make sure your domain is managed by DNSPOD.
The dns server of your domain should be

    f1g1ns1.dnspod.net
    f1g1ns2.dnspod.net

Get this script, Modify following lines

    log_file = r"/home/ubuntu/ddns/ddns.log"

    email = r"DNSPOD_User"
    password = r"DNSPOD_Pass"

    domain = r"YOUR_DOMAIN"
    sub_domain = r"YOUR_SUB_DOMAIN"

Put this script into cron job to do regular check.

Reference: 

    DNSPOD API manual: https://www.dnspod.cn/docs/index.html
    dnspod python package: https://github.com/DNSPod/dnspod-python
