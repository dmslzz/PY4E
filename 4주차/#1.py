def make_comma(num) : 
    # 입력받은 숫자를 역순으로 만듦
    reversed_num = num[::-1]
    # 세자리마다 콤마를 찍은 리스트
    comma_num = list()
    # 콤마용 카운터
    len_cnt = 0
    
    for i in list(reversed_num) :
        len_cnt += 1 
        # 끝에서 세자리마다 콤마를 찍음, 맨 윗자리가 세자리 다 차있을 경우에도 콤마를 찍지 않음
        if (len_cnt % 3 == 0) and (len_cnt != len(reversed_num)) : 
            i = ',' + i 
        # 역순으로 숫자를 리스트에 추가함
        comma_num.append(i)
    
    # 순차로 되돌림
    comma_num.reverse()

    # 출력
    print("".join(comma_num))
    


make_comma(input("숫자를 입력해주세요"))
