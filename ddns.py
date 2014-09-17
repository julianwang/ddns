#!/usr/bin/python
#-*- coding:utf-8 -*-

# ddns.py
# Check current dns - ip mapping, if not match, update dns record.
# Author: Julian Wang
# 2014/09/16

import os
import re
import time
from dnspod.apicn import *

def log(msg):
    log_file = "/home/ubuntu/ddns/ddns.log"
    if os.path.exists(log_file):
        fp = open(log_file,'a')
    else:
        fp = open(log_file,'w')
    log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    fp.write("%s - %s\n" % (log_time,msg))
    fp.close()

def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read().strip('\n')
    r.close()
    return text

def check_my_ip():
    url = "http://members.3322.org/dyndns/getip"
    cmd = "wget --quiet --no-check-certificate --output-document=- %s" % url
    my_ip = execCmd(cmd)
    if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', my_ip) != None:
        return my_ip
    else:
        log("Can't get my external ip. exit")
        exit(-1)

def check_dns(dnsname):
    cmd = "dig -t a %s @f1g1ns1.dnspod.net +short" % dnsname
    dns_ip = execCmd(cmd)
    if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', dns_ip) != None:
        return dns_ip
    else:
        log("Can't resolve my DNS name. exit")
        exit(-1)

def update_dns(domain, sub_domain, newip):
    email = "DNSPOD_User"
    password = "DNSPOD_Pass"

# Get Domain ID
    api = DomainList(email=email, password=password, type="mine")
    domains = api().get("domains")
    for i in domains:
        if i["name"] == domain:
            domain_id = i["id"]
    log("domain id is %s" % domain_id)

# Get Record ID
    api = RecordList(domain_id, email=email, password=password, sub_domain=sub_domain)
    record = api().get("records")
    for i in record:
        if i["type"] == "A":
            record_id = i["id"]
    log("record id is %s" % record_id)

# Update Record IP
    api = RecordModify(record_id, sub_domain, "A", u'默认'.encode("utf8"), newip, 600, domain_id=domain_id, email=email, password=password)
    result = api().get("status")
    log(result)

def main():
    domain = r"YOUR_DOMAIN"
    sub_domain = r"YOUR_SUB_DOMAIN"
    log("================  Start  ================")
    my_ip = check_my_ip()
    dnsname = sub_domain+"."+domain
    dns_ip = check_dns(dnsname)
    log("My external ip is %s, My DNS record is %s" % (my_ip,dns_ip))
    if my_ip != dns_ip:
        log("Not match. Update DNS record now")
        update_dns(domain, sub_domain, my_ip)
    else:
        log("Match. Do nothing")
    log("================   End   ================")

main()
