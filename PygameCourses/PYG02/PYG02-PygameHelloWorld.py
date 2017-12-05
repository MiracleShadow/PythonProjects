import pygame, sys

pygame.init()
size = width, height = 600, 400     # 设置窗体的大小
speed = [1, 1]      # 设置壁球的速度
BLACK = 0, 0, 0     # 设置背景的颜色
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame游戏壁球")
ball = pygame.image.load("PYG02-ball.gif")
# pygame.image.load(filename)
# 将filename路径下的图像载入游戏，支持JPG、PNG、GIF（非动画）等13种常用图片格式
ballrect = ball.get_rect()
# Surface对象  ball.get_rect()
# Pygame使用内部定义的Surface对象表示所有载入的图像，其中.get_rect()方法返回一个覆盖图像的举行Rect对象
# Rect对象
# Rect对象有一些重要的属性，例如：
# top, bottom, left, right 表示上下左右
# width, height表示宽度、高度



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    # ballrect.move(x, y)
    # 矩形移动一个偏移量(x, y)， 即在横轴方向移动x像素， 纵轴方向移动y像素， xy为整数
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]        # 遇到左右两侧， 横向速度取反
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]        # 遇到上下两侧， 纵向速度取反
    screen.fill(BLACK)
    # screen.fill(color)
    # 由于窗口背景为color颜色， 采用RGB色彩体系。由于壁球不断运动，
    # 运动后原有位置将默认填充白色，因此需要不断刷新背景色
    screen.blit(ball, ballrect)
    # screen.blit(src, dest)
    # 将一个图像绘制在另一个图像上， 即将src绘制到dest位置上。通过Rect对象引导壁球的绘制
    pygame.display.update()
