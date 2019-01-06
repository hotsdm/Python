def login(_id):
        members = ['har', 'space', 'SDM']
        for member in members:
                if member == _id:
                        return True
        return False

input_id=input("아이디를 입력해주세요. \n")

if login(input_id):
        print('hello!, ' + input_id)
else:
        print('Who are you?')
