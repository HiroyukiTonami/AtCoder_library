# Pを使うと定数扱いになって再代入すんな！ってwarning出るし、pは予約語
pp = gets.to_i
coins = [1]
for i in 2..10 do
    coins.push coins[i - 2] * i
end

answer = 0

9.downto(0) do |coin|
    count = pp.div coins[coin]
    if count < 101
        pp = pp - (coins[coin] * count)
    else
        pp = pp - (coins[coin] * 100)
        count = 100
    end
    answer += count
    
    break if pp == 0
end

puts answer