# 사용자의 대답을 변수에 저장한다.
stadium = input("경기장은 어디입니까? ")
winner = input("이긴 팀은 어디입니까? ")
loser = input("진 팀은 어디입니까? ")
vip = input("우수선수는 누구입니까? ")
score = input("스코어는 몇대몇입니까? ")

# 사용자의 입력을 바탕으로 기사를 작성한다.
print("")
print("===========================================")
print("오늘", stadium, "에서 야구 경기가 열렸습니다.")
print(winner, "과", loser, "은 치열한 공방전을 펼쳤습니다.")
print(vip, "의 맹활약으로 ", winner,"가", loser,"를 ", score,"로 이겼습니다.")
print("===========================================")