import urllib.request
import re

def scrape_threat_intel():
    print("[*] Fetching latest threat intelligence indicators...")
    # Example raw malicious IP indicator feed
    url = "https://raw.githubusercontent.com/stamparm/ipsum/master/levels/1.txt"
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            html_content = response.read().decode('utf-8')
            
            # Extract IP addresses using regex
            ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
            ips = re.findall(ip_pattern, html_content)
            
            print(f"[+] Successfully extracted {len(ips)} threat IP indicators!")
            print("-" * 40)
            print("First 10 Threat IPs found:")
            for ip in ips[:10]:
                print(f" - {ip}")
                
    except Exception as e:
        print(f"[!] Error scraping threat feed: {e}")

if __name__ == "__main__":
    scrape_threat_intel()