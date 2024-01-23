# 0x1B. Web stack debugging #4

In this episode of the web stack debugging, we will debug a server that give errors
with a huge amount of failed requests. Then automate the solving process.
To simulate the sending request, we use ApacheBench.

# Usage
The script are written in puppet :
```
puppet apply 0-the_sky_is_the_limit_not.pp
```
To install puppet if you're using apt :
```
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
```
