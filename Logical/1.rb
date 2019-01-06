puts("아이디를 입력해주세요.")
input=gets.chomp()
real_har="har"
real_space="space"
if real_har == input or real_space == input
  puts("Hello! " + input)
else
  puts("Who are you?")
end
