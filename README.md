Import dnspod python package from
https://github.com/DNSPod/dnspod-python

Make sure your domain is managed by DNSPOD
The dns server of your domain should be
f1g1ns1.dnspod.net
f1g1ns2.dnspod.net

Get this script, Modify following lines as you like
    log_file = "/home/ubuntu/ddns/ddns.log"

    email = "DNSPOD_User"
    password = "DNSPOD_Pass"

    domain = r"YOUR_DOMAIN"
    sub_domain = r"YOUR_SUB_DOMAIN"

Put this script into cron job to do regular check.

Reference:
DNSPOD API manual: https://www.dnspod.cn/docs/records.html
