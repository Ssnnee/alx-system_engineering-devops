#!/usr/bin/env ruby
# This script implement a regular expression that match School


if ARGV.length != 1
  exit 1
end

input = ARGV[0]

regex = /\d{10}/
matches = input.scan(regex)


if matches.empty?
  puts ""
else
  matches.each do |match|
    puts "#{match}"
  end
end
