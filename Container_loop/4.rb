puts("아이디를 입력해주세요.")
input_id = gets.chomp()
ids = ['har', 'space', 'SDM']
for id in ids do
    if id == input_id
        puts('Hello!, ' +id)
        exit
    end
end
puts('who are you?')
