nums = *gets.split(" ").map{|a| a.to_i}

puts(nums.sum - nums.min)