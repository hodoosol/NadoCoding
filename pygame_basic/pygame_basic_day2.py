"""
2021.02.03 수요일
나도 코딩 활용편 _ 1 - 추억의 오락실 게임을 만들어보아요.
"""

### 1. 프레임
### 2. 배경
### 3. 캐릭터
### 4. 키보드 이벤트
### 5. Frame per Second(FPS)
### 6. 충돌 처리
### 7. 텍스트

import pygame

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480    # 가로 크기
screen_height = 640   # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("SeulSol Game")   # 게임 이름

# FPS
clock = pygame.time.Clock()

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

# 이동 속도
# 원래는 방향키 누를 때 마다 5만큼씩 움직이게 설정되어있었으나
# 게임의 프레임 수가 달라진다고해서 게임 자체의 속도가 달라지면 안되므로
# 프레임 수를 고정해야 한다.
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/hodoo/PycharmProjects/NadoCoding/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]      # 캐릭터의 가로크기
enemy_height = enemy_size[1]     # 캐릭터의 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
# Font(폰트파일, 크기)
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시간 계산을 위해 현재 시간 tick 받아오기
start_ticks = pygame.time.get_ticks()

#이벤트 루프
running = True    # 게임이 진행 중인가 ? True = 게임 진행 중
while running :
    # 게임 화면의 초당 프레임 수를 설정
    dt = clock.tick(60)
    # 현재 프레임수 확인하려면
    # print('fps : ' + str(clock.get_fps()))

    # 예를들어, 캐릭터가 1초 동안에 100만큼 이동해야 한다면
    # 10 fps : 1초 동안에 10번 동작  ->  1번에 몇 만큼 이동 ? 10만큼 !
    # 20 fps : 1초 동안에 20번 동작  ->  1번에 5만큼 이동해야함 !


    # 어떤 이벤트가 발생하였는가 ?
    for event in pygame.event.get() :      # pygame에서 무 조 건 적어야하는 부분
        # 창이 닫히는 이벤트가 발생하였는가 ?
        if event.type == pygame.QUIT :     # pygame 창을 껐을때 이 이벤트(QUIT)가 발생
            running = False                # 발생되면 게임 종료

        # 키가 눌리는 이벤트가 발생하였는가 ?
        if event.type == pygame.KEYDOWN :        # 방향키가 눌러졌다면
            if event.key == pygame.K_LEFT :      # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :   # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP :      # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN :    # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP :          # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0

    # 프레임별로 바뀌는 값 dt를 곱해준다.
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    # 캐릭터의 x,y_pos는 수시로 바뀌지만 캐릭터의 rect 정보는 똑같은 위치를 가리킴
    # 때문에 rect 정보를 x,y_pos로 업데이트 해줘야 함
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect) :
        print("충돌했어요.")
        running = False

    # 배경 그리기. 좌표는 (0, 0) -> 이것만 하면 적용 안됨. update() 필요
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    # 적 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))



    # OR, 직접 RGB값을 입력하여 배경색을 채울 수도 있다. -> 이때도 업데이트 필요
    # screen.fill((0, 0, 255))

    # 타이머 집어넣기
    # 경과 시간 계산 : (총 시간 - 경과 시간)을 1000으로 나눠서 밀리초를 초로 환산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 10 9 8 7 ... 로 표시될 수 있게 (출력한 시간 글자, True, 글자 색상)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0 :
        print('Time Out !')
        running = False


    # pygame에서는 매번 매 프레임마다 화면을 새로 그려주는 동작 필요
    pygame.display.update() # 게임화면 다시 그리기 !

# 잠시 대기
pygame.time.delay(2000)

#pygame 종료
pygame.quit()




