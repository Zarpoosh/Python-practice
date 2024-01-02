import subprocess
import wifiPassword


name=subprocess.getoutput("netsh wlan show rpofile: ").replace("profiles on interface wi-fi: ").replace("group policy profiles (read only)","").replace("------------------------", "").replace("<None>","").replace("\n", "").replace("User profiles", "").replace("-------------------------", "").replace("All user profile", "").replace(":", "")
name2=name.split()
for i in name2:
    a=subprocess.getoutput("wifipassword "+i)
    print(a)