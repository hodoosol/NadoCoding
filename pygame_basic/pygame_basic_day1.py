"""
2021.02.01 월요일
나도 코딩 활용편 _ 1 - 추억의 오락실 게임을 만들어보아요.
"""

### 1. 프레임
### 2. 배경
### 3. 캐릭터
### 4. 키보드 이벤트

import pygame

# 초기화 (반드시 필요)
pygame.init()


# 화면 크기 설정
screen_width = 480    # 가로 크기
screen_height = 640   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("SeulSol Game")   # 게임 이름


"""여기까지 입력하고 실행시키면 게임이 켜졌다가 바로 꺼진다."""
"""pygame에서는 항상 이벤트 루프가 실행되고 있어야 창이 꺼지지 않는다."""


# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/hodoo/PycharmProjects/NadoCoding/pygame_basic/background.png")


# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/hodoo/PycharmProjects/NadoCoding/pygame_basic/character.png")


# 이미지의 크기를 구해옴
character_size = character.get_rect().size
character_width = character_size[0]      # 캐릭터의 가로크기
character_height = character_size[1]     # 캐릭터의 세로크기


# 화면 가로의 절반 크기에 해당하는 곳에 위치(가로 위치)
# 이미지가 좌표의 오른쪽 아래로 그려지므로 x좌표는 화면 width의 절반에서 캐릭터의 width 절반을 뺀 값.
character_x_pos = (screen_width / 2) - (character_width / 2)
# 화면 세로의 가장 아래에 해당하는 곳에 위치(세로 위치)
# 이미지가 좌표의 오른쪽 아래로 그려지므로 y좌표는 전체 height에서 캐릭터의 height를 뺀 값.
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0


#이벤트 루프
running = True    # 게임이 진행 중인가 ? True = 게임 진행 중
while running :
    # 어떤 이벤트가 발생하였는가 ?
    for event in pygame.event.get() :      # pygame에서 무 조 건 적어야하는 부분
        # 창이 닫히는 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT :     # pygame 창을 껐을때 이 이벤트(QUIT)가 발생
            running = False                # 발생되면 게임 종료

        # 키가 눌리는 이벤트가 발생하였는가 ?
        if event.type == pygame.KEYDOWN :        # 방향키가 눌러졌다면
            if event.key == pygame.K_LEFT :      # 캐릭터를 왼쪽으로
                to_x -= 5
            elif event.key == pygame.K_RIGHT :   # 캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP :      # 캐릭터를 위로
                to_y -= 5
            elif event.key == pygame.K_DOWN :    # 캐릭터를 아래로
                to_y += 5

        if event.type == pygame.KEYUP :          # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0


    character_x_pos += to_x
    character_y_pos += to_y

    # 여기까지만 하면 캐릭터가 화면 밖으로 벗어나게 됨. 화면 안에서만 이동할 수 있도록 설정
    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    # 배경 그리기. 좌표는 (0, 0) -> 이것만 하면 적용 안됨. update() 필요
    screen.blit(background, (0, 0))

    # 캐릭터 그리기.
    screen.blit(character, (character_x_pos, character_y_pos))

    # pygame에서는 매번 매 프레임마다 화면을 새로 그려주는 동작 필요
    pygame.display.update()   # 게임화면 다시 그리기 !

    # OR, 직접 RGB값을 입력하여 배경색을 채울 수도 있다. -> 이때도 업데이트 필요
    # screen.fill((0, 0, 255))


#pygame 종료
pygame.quit()




