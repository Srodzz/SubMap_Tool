#!/usr/bin/env python3
import sys
import subprocess
import shutil

# Tool that blend sublist3r with nmap and automatically scans subdomains

# check if user add a domain

if len(sys.argv) < 2:
    print(f"Use: {sys.argv[0]} domain.com")

domain = sys.argv[1]
subli_output = f"subs_{domain}.txt"

def run_sublister():
    print(""" 
        =====================================
        Enumerating subdomains with sublist3r
        =====================================
        """)
    
    #Exceptions
    if shutil.which("sublist3r") is None:
        raise SystemExit("sublist3r not install")
        sys.exit(1)
    
    try:
        subprocess.run(["sublist3r", "-d", domain, "-o", subli_output], check=True)
        print("Done. Results in:", subli_output)
    except subprocess.CalledProcessError as e:
        print("The command Failed with code:", e.returncode)
        print("Exit (stderr):", e.stderr)

def run_nmap():
    print("""
        =============================
        Scanning subdomains with Nmap
        =============================        
        """)
    nmap_output= f"nmap_report_{domain}.txt"

    try:
        subprocess.run(["nmap", "-iL", subli_output, "-sCV", "-Pn", "-n", "oN", nmap_output], check=True)
        print("Done. Results in", nmap_output)
        print(f"""
            ==================================
            Finish!
            Subdomain save in: {subli_output}
            Nmap report in: {nmap_output}
            ==================================
            """)
    except subprocess.CalledProcessError as e:
        print("The command Failed with code:", e.returncode)
        print("Exit (stderr):", e.stderr)

run_sublister()
run_nmap()
