#!/usr/bin/env ruby

if ARGV.length != 1
  exit 1
end

input = ARGV[0]

regex = /hbt{2,5}n/
matches = input.scan(regex)


if matches.empty?
  puts ""
else
  matches.each do |match|
    puts "#{match}"
  end
end
