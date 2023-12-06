# 0x0F. Load balancer

To handle a huge amounts of traffic, we use mutiple servers.In order to achieve
this, web traffic needs to be distributed to these servers, and that is the
role of a load-balancer.

In this project, we configure some thing one the server then write some scripts
that automate the work and we configure.

Here some load-balancing algorithms names :
Round Robin
Weighted Round Robin
Dynamic Round Robin
Fastest
Least Connections

**Useful commands**
nginx -t
haproxy -f /etc/haproxy/haproxy.cfg -c
