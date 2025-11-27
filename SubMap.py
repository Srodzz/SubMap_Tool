#!/usr/bin/env python3
import sys
import subprocess
import shutil

# Tool that blend subfinder with nmap and automatically scans subdomains

# check if user add a domain

if len(sys.argv) < 2:
    print(f"Use: {sys.argv[0]} domain.com")
    sys.exit(1)

domain = sys.argv[1]
subfinder_output = f"subs_{domain}.txt"

def run_subfinder():
    print(""" 
        =====================================
        Enumerating subdomains with subfinder
        =====================================
        """)
    
    #Exceptions
    if shutil.which("subfinder") is None:
        raise SystemExit("subfinder not install")
        sys.exit(1)
    
    try:
        subprocess.run(["subfinder", "-d", domain, "-silent", "-o", subfinder_output], check=True)
        print("Done. Results in:", subfinder_output)
    except subprocess.CalledProcessError as e:
        print("The command Failed with code:", e.returncode)
        print("Exit (stderr):", e.stderr)

# def run_httx():
#     print("""
#         ================================
#         Searching only active subdomains 
#         ================================
#     """)

#     if shutil.which("httpx")


def run_nmap():
    print("""
        =============================
        Scanning subdomains with Nmap
        =============================        
        """)
    nmap_output= f"nmap_report_{domain}.txt"

    try:

        print("Done. Results in", nmap_output)
        print(f"""
            ==================================
            Finish!
            Subdomain save in: {subfinder_output}
            Nmap report in: {nmap_output}
            ==================================
            """)
    except subprocess.CalledProcessError as e:
        print("The command Failed with code:", e.returncode)
        print("Exit (stderr):", e.stderr)

run_subfinder()
run_nmap()
