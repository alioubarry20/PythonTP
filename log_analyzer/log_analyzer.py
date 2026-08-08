from collections import defaultdict
import re

log_file= "auth.log"

#dictionnaire pour compter les IP

ip_attempts = defaultdict(int)

with open(log_file,"r") as file:
    for line in file:
        if "failed password" in line:
            # extraire l'ip avec regex
            match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if match:
                ip = match.group()
                ip_attempts[ip] +=1


print("Une adresse Ip suspecte a etait detecter\n")
for ip,attempts in ip_attempts.items():
    if attempts>=3:
        print(f"Alert : {ip}has {attempts} failed attempts!")
    else:
        print(f"{ip}->{attempts}failed attemps")