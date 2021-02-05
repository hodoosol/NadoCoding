"""
2021.02.05 금요일
나도 코딩 활용편 _ 1 - 추억의 오락실 게임을 만들어보아요.

"""

# 1. 배경과 캐릭터
# 2. 무기와 키보드 이벤트
# 3. 공 만들기

import os
import pygame

#############################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("SeulSol Pang")   # 게임 이름

# FPS
clock = pygame.time.Clock()
#############################################################################

### 1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 현재 파일 위치 반환
current_path = os.path.dirname(__file__)
# images 폴더 위치 반환
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
# 스테이지의 높이 위에 캐릭터를 두기 위해 사용
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []
# 무기 이동 속도
weapon_speed = 10

# 공 만들기(4개 크기에 대해 따로 처리)
ball_images = [pygame.image.load(os.path.join(image_path, "balloon1.png")),
               pygame.image.load(os.path.join(image_path, "balloon2.png")),
               pygame.image.load(os.path.join(image_path, "balloon3.png")),
               pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드 조정, x는 그대로 y만 조정
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3에 해당하는 값

# 공들의 정보
balls = []

balls.append({
    "pos_x" : 50,      # 공의 x 좌표
    "pos_y" : 50,      # 공의 y 좌표
    "img_idx" : 0,     # 공의 이미지 인덱스
    "to_x" : 3,        # 공의 x축 이동 방향, -3이면 왼쪽으로, 3이면 오른쪽으로 이동
    "to_y" : -6,       # 공의 y축 이동 방향
    "init_speed_y" :  ball_speed_y[0]}) # y의 최초 속도

running = True
while running :
    dt = clock.tick(30)
    ### 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN :
            # 캐릭터를 왼쪽으로
            if event.key == pygame.K_LEFT :
                character_to_x -= character_speed
            # 캐릭터를 오른쪽으로
            elif event.key == pygame.K_RIGHT :
                character_to_x += character_speed
            # 무기 발사
            elif event.key == pygame.K_SPACE :
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0

    ### 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # (100, 200) -> y의 좌표 180, 160, 140 ...
    # (500, 200) -> y의 좌표 180, 160, 140 ...
    # 무기 위치를 위로
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # 천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
    ### 4. 충돌 처리

    ### 5. 화면에 그리기
    screen.blit(background, (0, 0))
    # 무기를 먼저 그리고 그 다음에 스테이지와 캐릭터 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update()

#pygame 종료
pygame.quit()




