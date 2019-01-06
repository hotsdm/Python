input_id=input("아이디를 입력해주세요. \n")
ids = ['har', 'space', 'SDM']
for id in ids:
    if id == input_id:
        print('Hello!, ' +id)
        import sys
        sys.exit()

print('who are you?')
