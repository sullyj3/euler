s = 0
for i in 1:999
	if i%3 == 0 
		s += i
	end
	if i%5 == 0
		s += i
	end
end
print(s)
