# Backdoor
This contains two python programmes
The purpose of these programmes is to send a command to a host system and recieve the output
It works like a backdoor crated my msfvenom
The main purpose is, post-exploitation we can upload this backdoor and remote execute commands on a host system 

The first one is "backdoor"
This is simply the server which will run on our system and recieve the data sent but the backdoor program on the exploited system

The second one is "backdoor(Backdoor)"
This will reside on the exploited system and recieve the commands and run them on the system and will give us the output
