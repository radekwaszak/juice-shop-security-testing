from zapv2 import ZAPv2
import time
from dotenv import load_dotenv
import os

load_dotenv()

zap_api_key = os.getenv("ZAP_API_KEY")

def zap_scan():
    zap = ZAPv2(apikey='zap_api_key') 

    target = 'http://zero.webappsecurity.com'

    print(f"Starting Spider scan for target: {target}")
    zap.urlopen(target) 
    zap.spider.scan(target)
    while int(zap.spider.status()) < 100:
        print(f"Spider progress: {zap.spider.status()}%")
        time.sleep(2)
    print("Spider scan completed.")

    print(f"Starting Active scan for target: {target}")
    zap.ascan.scan(target)
    while int(zap.ascan.status()) < 100:
        print(f"Active scan progress: {zap.ascan.status()}%")
        time.sleep(2)
    print("Active scan completed.")

    report_path = os.path.join('reports', 'security_report.html')
    with open(report_path, 'w') as f:
        f.write(zap.core.htmlreport())
    print(f"Security report saved to {report_path}")

if __name__ == "__main__":
    zap_scan()