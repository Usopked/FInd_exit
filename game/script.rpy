﻿# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('???', color="#c8ffc8")

transform fullsize:
    size (1920, 1080)
    zoom 1.0



# 여기에서부터 게임이 시작합니다.
label start:
    play music "audio/뒤뚱뒤뚱.mp3" loop

    e "아주대학교 탈출 게임."

    e "개발 1일차"

    menu:

        "정문으로 간다.":
            jump front_door


label front_door:
    scene black
    with dissolve
    scene 정문 at fullsize

    e "정문이다."

    e "이거 정문 맞... 겠지?"

    menu:
        "운동장으로 간다.":
            jump playground
        "도서관으로 간다.":
            jump library


label playground:
    scene black
    with dissolve
    scene 운동장 at fullsize

    e "운동장이다."

    e "졸업하기 전에 운동장 잔디밭을 밟아본 사람이 얼마나 될까?"

    menu:
        "체육관으로 간다.":
            jump gym
        "가온마당으로 간다.":
            jump gaon_park
        "정문으로 간다.":
            jump front_door


label gym:
    scene black
    with dissolve
    scene 체육관 at fullsize

    e "체육관이다."

    e "농구나 배드민턴 동아리가 아니면 거의 들어올 일 없는 장소같다."

    menu:
        "운동장으로 간다.":
            jump playground
        "남문으로 간다.":
            jump south_door


label south_door:
    scene black
    with dissolve
    scene 남문 at fullsize

    e "남문이다."

    e "무언가 찝찝한 기분이 느껴지지만, 어쨌든 탈출에 성공했다."

    return


label gaon_park:
    scene black
    with dissolve
    scene 가온마당 at fullsize

    e "가온마당이다."

    menu:
        "운동장으로 간다.":
            jump gym
        "노천극장으로 간다.":
            jump open_theater
        "송재관으로 간다.":
            jump songjae_holl


label library:
    scene black
    with dissolve
    scene 도서관 at fullsize

    e "도서관이다."

    e "정말 공대스러운 3,4층과 스터디카페를 모방한 2층이 어우러져 기묘한 분위기를 자아낸다."

    menu:
        "노천극장으로 간다.":
            jump open_theater
        "더테라스로 간다.":
            jump the_terrace


label open_theater:
    scene black
    with dissolve
    scene 노천극장 at fullsize

    e "노천극장이다."

    e "리모델링이 끝난 모습이 기대된다."

    menu:
        "가온마당으로 간다.":
            jump gaon_park
        "도서관으로 간다.":
            jump library
        "율곡관으로 간다.":
            jump yulgok_holl


label yulgok_holl:
    scene black
    with dissolve
    scene 율곡관 at fullsize

    e "율곡관이다."

    menu:
        "연암관으로 간다.":
            jump yeonam_holl
        "노천극장으로 간다.":
            jump open_theater


label yeonam_holl:
    scene black
    with dissolve
    scene 연암관 at fullsize

    e "연암관이다."

    menu:
        "다산관으로 간다.":
            jump dasan_holl
        "홍재관으로 간다.":
            jump hongjae_holl
        "율곡관으로 간다.":
            jump yulgok_holl


label dasan_holl:
    scene black
    with dissolve
    scene 다산관 at fullsize

    e "다산관이다."

    menu:
        "연암관으로 간다.":
            jump yeonam_holl
        "약학관으로 간다.":
            jump pharmacy_holl
    

label songjae_holl:
    scene black
    with dissolve
    scene 송재관 at fullsize

    e "송재관이다."

    menu:
        "가온마당으로 간다.":
            jump gaon_park
        "홍재관으로 간다.":
            jump hongjae_holl
        "병원으로 간다.":
            jump hospital


label hospital:
    scene black
    with dissolve
    scene 병원 at fullsize

    e "병원이다."

    menu:
        "병원 정문으로 간다.":
            jump hospital_front_door
        "송재관으로 간다.":
            jump songjae_holl
        "권역외상센터로 간다.":
            jump trauma_center


label hospital_front_door:
    scene black
    with dissolve
    scene 병원정문 at fullsize

    e "병원 정문이다."

    e "이곳으로 나가는 게 맞나..?"

    e "떨떠름한 마음으로 당신은 발을 옮긴다."

    return


label trauma_center:
    scene black
    with dissolve
    scene 외상센터 at fullsize

    e "외상센터이다."

    e "학교를 너무 많이 벗어난 느낌이 든다."

    menu:
        "병원으로 간다.":
            jump hospital


label hongjae_holl:
    scene black
    with dissolve
    scene 홍재관 at fullsize

    e "홍재관이다."

    menu:
        "연암관으로 간다.":
            jump yeonam_holl
        "송재관으로 간다.":
            jump songjae_holl
        "의생명과학관으로 간다.":
            jump biomedical_center


label biomedical_center:
    scene black
    with dissolve
    scene 의생명과학관 at fullsize

    e "의생명과학관이다."

    menu:
        "임상수기센터로 간다.":
            jump clinical_center
        "홍재관으로 간다.":
            jump hongjae_holl
        "테니스장으로 간다.":
            jump tennis_court


label tennis_court:
    scene black
    with dissolve
    scene 테니스장 at fullsize

    e "테니스장이다."

    e "학교에 이런 곳이..?"

    menu:
        "의생명과학관으로 간다.":
            jump biomedical_center


label clinical_center:
    scene black
    with dissolve
    scene 임상수기센터 at fullsize

    e "임상수기센터이다."

    menu:
        "의생명과학관으로 간다.":
            jump biomedical_center
        "약학관으로 간다.":
            jump pharmacy_holl


label pharmacy_holl:
    scene black
    with dissolve
    scene 약학관 at fullsize

    e "약학관이다."

    menu:
        "임상수기센터로 간다.":
            jump clinical_center
        "혜강관으로 간다.":
            jump hyegang_holl


label hyegang_holl:
    scene black
    with dissolve
    scene 혜강관 at fullsize

    e "혜강관이다."

    menu:
        "약학관으로 간다.":
            jump pharmacy_holl
        "일신관으로 간다.":
            jump ilshin_domitory


label the_terrace:
    scene black
    with dissolve
    scene 더테라스 at fullsize

    e "더테라스이다."

    e "테라스가 아니다. '더 테라스' 다."

    menu:
        "성호관으로 간다.":
            jump seongho_holl
        "원천관으로 간다.":
            jump woncheon_holl
        "도서관으로 간다.":
            jump library
        "선구자상으로 간다.":
            jump pioneer_statue


label pioneer_statue:
    scene black
    with dissolve
    scene 선구자상 at fullsize

    e "선구자상이다."

    menu:
        "더테라스로 간다.":
            jump the_terrace
        "원천관으로 간다.":
            jump woncheon_holl
        "에너지센터로 간다.":
            jump energy_center


label energy_center:
    scene black
    with dissolve
    scene 에너지센터 at fullsize

    e "에너지 센터이다."

    menu:
        "선구자상으로 간다.":
            jump pioneer_statue


        
label woncheon_holl:
    scene black
    with dissolve
    scene 원천관 at fullsize

    e "원천관이다."

    menu:
        "선구자상으로 간다.":
            jump pioneer_statue
        "더테라스로 간다.":
            jump the_terrace
        "원천정보관으로 간다.":
            jump woncheon_information_center
        "화학공학관으로 간다.":
            jump chemical_engineering_holl


label woncheon_information_center:
    scene black
    with dissolve
    scene 원천정보관 at fullsize

    e "원천정보관이다."

    menu:
        "원천관으로 간다.":
            jump woncheon_holl
        "동관으로 간다.":
            jump east_holl


label east_holl:
    scene black
    with dissolve
    scene 동관 at fullsize

    e "동관이다."

    menu:
        "토목공학관으로 간다.":
            jump civil_engineering_holl
        "원천정보관으로 간다.":
            jump woncheon_information_center
        "서관으로 간다.":
            jump west_holl


label chemical_engineering_holl:
    scene black
    with dissolve
    scene 화학공학관 at fullsize

    e "화학공학관이다."

    menu:
        "원천관으로 간다.":
            jump woncheon_holl
        "서관으로 간다.":
            jump west_holl


label west_holl:
    scene black
    with dissolve
    scene 서관 at fullsize

    e "서관이다."

    menu:
        "동관으로 간다.":
            jump east_holl
        "화학공학관으로 간다.":
            jump chemical_engineering_holl
        "종합설계동으로 간다.":
            jump comprehensive_design_hall



label seongho_holl:
    scene black
    with dissolve
    scene 성호관 at fullsize

    e "성호관이다."

    menu:
        "더테라스로 간다.":
            jump the_terrace
        "구학생회관으로 간다.":
            jump student_center
        "신학생회관으로 간다.":
            jump new_student_center


label student_center:
    scene black
    with dissolve
    scene 구학생회관 at fullsize

    e "구학생회관이다."

    menu:
        "신학생회관으로 간다.":
            jump new_student_center
        "성호관으로 간다.":
            jump seongho_holl


label new_student_center:
    scene black
    with dissolve
    scene 신학생회관 at fullsize

    e "신학생회관이다."

    menu:
        "구학생회관으로 간다.":
            jump student_center
        "성호관으로 간다.":
            jump seongho_holl
        "남제관으로 간다.":
            jump namje_domitory


label civil_engineering_holl:
    scene black
    with dissolve
    scene 토목공학관 at fullsize

    e "토목공학관이다."

    menu:
        "동관으로 간다.":
            jump east_holl
        "팔달관으로 간다.":
            jump paldal_holl


label namje_domitory:
    scene black
    with dissolve
    scene 남제관 at fullsize

    e "남제관이다."

    menu:
        "신학생회관으로 간다.":
            jump new_student_center
        "기숙사 식당으로 간다.":
            jump domitory_cafeteria


label domitory_cafeteria:
    scene black
    with dissolve
    scene 기숙사식당 at fullsize

    e "기숙사 식당이다."

    menu:
        "남제관으로 간다.":
            jump namje_domitory
        "학군단으로 간다.":
            jump school_team
        "용지관으로 간다.":
            jump yongji_domitory


label yongji_domitory:
    scene black
    with dissolve
    scene 용지관 at fullsize

    e "용지관이다."

    menu:
        "일신관으로 간다.":
            jump ilshin_domitory
        "기숙사 식당으로 간다.":
            jump domitory_cafeteria
        "화홍관으로 간다.":
            jump hwahong_domitory


label hwahong_domitory:
    scene black
    with dissolve
    scene 화홍관 at fullsize

    e "화홍관이다."

    menu:
        "용지관으로 간다.":
            jump yongji_domitory
        "광교관으로 간다.":
            jump gwanggyo_domitory
        "국제학사로 간다.":
            jump international_domitory
        

label gwanggyo_domitory:
    scene black
    with dissolve
    scene 광교관 at fullsize

    e "광교관이다."

    menu:
        "화홍관으로 간다.":
            jump hwahong_domitory
        "국제학사로 간다.":
            jump international_domitory


label ilshin_domitory:
    scene black
    with dissolve
    scene 일신관 at fullsize

    e "일신관이다."

    menu:
        "용지관으로 간다.":
            jump yongji_domitory
        "혜강관으로 간다.":
            jump hyegang_holl
        "국제학사로 간다.":
            jump international_domitory


label international_domitory:
    scene black
    with dissolve
    scene 국제학사 at fullsize

    e "국제학사다."

    menu:
        "화홍관으로 간다.":
            jump hwahong_domitory
        "광교관으로 간다.":
            jump gwanggyo_domitory
        "일신관으로 간다.":
            jump ilshin_domitory
        "광교로 간다.":
            jump gwanggyo


label paldal_holl:
    scene black
    with dissolve
    scene 팔달관 at fullsize

    e "팔달관이다."

    menu:
        "학군단으로 간다.":
            jump school_team
        "토목공학관으로 간다.":
            jump civil_engineering_holl
        "북문으로 간다.":
            jump north_door


label comprehensive_design_hall:
    scene black
    with dissolve
    scene 종합설계동 at fullsize

    e "종합설계동이다."

    menu:
        "서관으로 간다.":
            jump west_holl
        "북문으로 간다.":
            jump north_door
        

label school_team:
    scene black
    with dissolve
    scene 학군단 at fullsize

    e "학군단이다."

    menu:
        "팔달관으로 간다.":
            jump paldal_holl
        "기숙사 식당으로 간다.":
            jump domitory_cafeteria
        "북문으로 간다.":
            jump north_door
        "산학협력원으로 간다.":
            jump industry_academic_cooperation


label north_door:
    scene black
    with dissolve
    scene 북문 at fullsize

    e "북문이다."

    return


label industry_academic_cooperation:
    scene black
    with dissolve
    scene 산학협력원 at fullsize

    e "산학협력원이다."

    menu:
        "광교로 간다.":
            jump gwanggyo


label gwanggyo:
    scene black
    with dissolve
    scene 광교 at fullsize

    e "당신은 진엔딩에 도달하셨습니다."

    e "게임을 종료합니다."

    return