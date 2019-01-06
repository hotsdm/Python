# ids = ['har', 'space', 'SDM']
# for id in ids do
#     if id == input_id
#         puts('Hello!, ' +id)
#         exit
#     end
# end
# puts('who are you?')

puts("아이디를 입력해주세요.")
input_id = gets.chomp()

def login(id)
    members = ['har', 'space', 'SDM']
    for member in members do
        if member == id
            return true
        end
    end
    return false
end

if login(input_id)
    puts('Hello, ' + input_id)
else
    puts('who are you?')
end