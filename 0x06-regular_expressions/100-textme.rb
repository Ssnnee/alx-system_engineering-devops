#!/usr/bin/env ruby
# This script implement a regular expression that match School


if ARGV.length != 1
  exit 1
end

input = ARGV[0]

sender = input.match(/\[from:(.*?)\]/)&.captures
receiver = input.match(/\[to:(.*?)\]/)&.captures
flags = input.match(/\[flags:(.*?)\]/)&.captures

if sender || receiver || flags
  result = [sender, receiver, flags].compact.join(',')
  puts result
else
  puts ""
end
