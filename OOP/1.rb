name1 = String.new('객체(class)안에는 여러 함수(method)가 소속 되어있음. 해당 객체(class)와 함수(method)를 통해 각각의 다른 변수값을 지정한 것을 instance라고 함') # <- 이 글자가 String 라는 class의 변수 name1 라는 instance에 담김
puts(name1.upcase()) # <- string 라는 class의 reverse라는 함수를 호출하여 name1라는 변수를 puts함
puts(name1.size())
names = Array.new() # <- array 라는 class가 담긴 names 라는 instance 
names.push('SDM')
names.push('Seoul')
puts(names)
puts(names.join('와 '))