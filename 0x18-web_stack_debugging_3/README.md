# 0x17. Web stack debugging #3
In this series of project, we then automate it with a
bash script or puppet or whatever.

For this specific project, we use [strace](https://strace.io/) `strace -f -o output.text ...`
and cat error in file to find the problem fix it we use then puppet to automate it.

# Usage
To use the script :
```
puppet apply 0-strace_is_your_friend.pp
```

