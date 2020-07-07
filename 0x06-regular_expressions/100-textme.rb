#!/usr/bin/env ruby
s1 =  ARGV[0].scan(/\[(from:.*?)\]/).join().split(":")[1]
s2 =  ARGV[0].scan(/\[(to:.*?)\]/).join().split(":")[1]
s3 =  ARGV[0].scan(/\[(flags:.*?)\]/).join().split(":", 2)[1]
puts [s1, s2, s3].join(",")
