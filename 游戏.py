import pygame
pygame.init()
skier_images = ['./pic/skier_crash.png','./pic/skier_down.png','./pic/skier_left1.png','./pic/skier_left2.png','./pic/skier_right1.png','./pic/skier_right2.png']


window=pygame.display.set_mode((600,600))#设置画布大小（x，y）表示宽度，高度
pygame.display.set_caption('cool')#设置画布的名字
#image=pygame.image.load('a.jpg').convert()#加载背景

skier = pygame.image.load(skier_images[1]).convert()

pygame.mixer.init()
pygame.mixer.music.load('liangliang.mp3')   #加载音乐
pygame.mixer.music.play()#播放音乐

window.fill([255,255,255])#改变背景色

#让小人动起来
x = 185#小人x坐标
y = 20
window.blit(skier,(x,y))
for i in range(1,100):
    pygame.time.delay(20)
    pygame.draw.rect(window,[255,255,255],[x,y,30,64])
    x+=5
    y+=5
    window.blit(skier,(x,y))
    pygame.display.flip()



while True:
    #window.blit(image,(0,0))#把图片添加到画布
    # window.blit(skier,(x,y))



    for obj in pygame.event.get():
        if obj.type == pygame.QUIT:#关闭窗口
            print("退出")
            exit()
        # elif obj.type == pygame.KEYDOWN:
        #     if obj.key==pygame.K_a or obj.key==pygame.K_LEFT:
        #         print("向左")
        #         x=x-1
        #         #skier=skier_images[2]
        #     elif obj.key==pygame.K_s or obj.key==pygame.K_DOWN:
        #         print("向下")
        #         y=y+1
        #         #skier = skier_images[1]
        #     elif obj.key==pygame.K_d or obj.key==pygame.K_RIGHT:
        #         print("向右")
        #         x=x+1
        #         #skier = skier_images[4]



    pygame.display.update() #刷新  *必须要刷新，不然就不会显示