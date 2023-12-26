# 0x13-firewall

A firewall is a hardware or software security system that controls incoming
and outgoing network traffic based on predetermined security rules.

In this project, we will try to install and setup ufw firewall one off the server
provided by ALX.
Ufw, or Uncomplicated Firewall, is a simplified firewall management
interface that hides the complexity of lower-level packet filtering technologies
and it's by default install on Ubuntu server. But if it's not for whatever reason,
just `sudo apt install ufw`.
WE configure ufw so that it blocks all incoming traffic, except the following TCP ports:
+ 22 (SSH)
+ 443 (HTTPS SSL)
+ 80 (HTTP)

## Files
| Project directory or file name | Description |
|------------------------|-------------|
| 0-block_all_incoming_traffic_but | is the commands I used to set up the firewall |
| README.md | the root README file off the projects |


### Useful commands
To check if the status of ufw
```shell
sudo ufw status verbose
```

To see rules numbers so that we can delete one as we want or just to see our rules
```shell
sudo ufw status numbered
```
Here is an example of an output
```
Status: active

     To                         Action      From
     --                         ------      ----
[ 1] Nginx HTTP                 ALLOW IN    Anywhere
[ 2] 22/tcp                     ALLOW IN    Anywhere
[ 3] 22                         ALLOW IN    Anywhere
[ 4] 80/tcp                     ALLOW IN    Anywhere
[ 5] 443/tcp                    ALLOW IN    Anywhere
[ 6] Nginx HTTP (v6)            ALLOW IN    Anywhere (v6)
[ 7] 22/tcp (v6)                ALLOW IN    Anywhere (v6)
[ 8] 22 (v6)                    ALLOW IN    Anywhere (v6)
[ 9] 80/tcp (v6)                ALLOW IN    Anywhere (v6)
[10] 443/tcp (v6)               ALLOW IN    Anywhere (v6)
```

So, to delete the rule 2 :
```shell
sudo ufw delete 2
```
