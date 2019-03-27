import pygame
import random
pygame.init()

window=pygame.display.set_mode((600,600))#设置画布大小（x，y）表示宽度，高度
window.fill([255,255,255])#改变背景色


imageDown=pygame.image.load('./pic/skier_down.png').convert()
imageCrash=pygame.image.load('./pic/skier_crash.png').convert()
imageLeft1=pygame.image.load('./pic/skier_left1.png').convert()
imageLeft2=pygame.image.load('./pic/skier_left2.png').convert()
imageRight1=pygame.image.load('./pic/skier_right1.png').convert()
imageRight2=pygame.image.load('./pic/skier_right2.png').convert()
imageTree=pygame.image.load('./pic/skier_tree.png').convert()
imageFlag=pygame.image.load('./pic/skier_flag.png').convert()


#动画精灵
class SkierClass(pygame.sprite.Sprite):
    '''
    image:图片路径
    location：列表类型的属性[x横轴坐标，y纵轴坐标]
    speed：[横轴速度，纵轴速度]

    '''
    def __init__(self,image,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()#<rect(0, 0, 30, 64)>
        self.rect.left=location[0]
        self.rect.top = location[1]#设置图像的初始位置
        self.speed=speed
    def move(self):
        # self.rect = self.rect.move(self.speed)
        isPress = pygame.key.get_pressed()  # bool :True
        if isPress[pygame.K_a] == True or isPress[pygame.K_LEFT] == True:
            if self.rect.left>0:
                self.rect.left -= 1
                self.image = imageLeft1
        elif isPress[pygame.K_s] == True or isPress[pygame.K_DOWN] == True:
            if self.rect.bottom < window.get_height() - 64:
                self.rect.bottom += 1
                self.image = imageDown
        elif isPress[pygame.K_d] == True or isPress[pygame.K_RIGHT] == True:
            if  self.rect.right < window.get_width() - 30:
                self.rect.left += 1
                self.image = imageRight1


#树
class Tree(pygame.sprite.Sprite):
    def __init__(self,image,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed=speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top>0 :
            self.speed[1] = -1



#旗子
class Flag(pygame.sprite.Sprite):
    def __init__(self,image,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left=location[0]
        self.rect.top = location[1]
        self.speed=speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top>0 or self.rect.bottom<600:
            self.speed[1] = -1





if __name__ == '__main__':

    # 创建1个小人
    ski = SkierClass('./pic/skier_down.png', [300, 10], [0, 0])
    #创建多棵树
    treeGroup=pygame.sprite.Group()
    for a in range(0, 6):
        x = random.randint(0, window.get_width() - 42)
        y = random.randint(0, window.get_height() - 48)
        tree = Tree('./pic/skier_tree.png', [x, y],[0,1])
        treeGroup.add(tree)


    # 创建多个旗子
    flagGroup=pygame.sprite.Group()#创建精灵组
    for n in range(0, 10):
        x = random.randint(0, window.get_width() - 12)
        y = random.randint(0, window.get_height() - 24)
        flag = Flag('./pic/skier_flag.png', [x, y],[0,1])
        flagGroup.add(flag)
    while True:
        pygame.time.delay(2)
        for obj in pygame.event.get():
            if obj.type == pygame.QUIT:  # 关闭窗口
                print("退出")
                exit()
        #加载人物
        window.fill([255,255,255])
        ski.move()
        window.blit(ski.image, ski.rect)

        # 加载多棵树
        for objTree in treeGroup:
            objTree.move()
            window.blit(objTree.image, objTree.rect)
            # 判断树是否超出范围
            if objTree.rect.bottom < 0:
                treeGroup.remove(objTree)
                print('1.,',treeGroup)
                x2 = random.randint(0, 600)
                y2 = random.randint(0, 1200)
                tree2=Tree('./pic/skier_tree.png', [x2, y2],[0,1])
                treeGroup.add(tree2)
                print("2.",treeGroup)
                window.blit(objTree.image, objTree.rect)
        #加载多个旗子
        for objFlag in flagGroup:
            objFlag.move()
            window.blit(objFlag.image, objFlag.rect)

    #检测人和树是否碰撞
        if pygame.sprite.spritecollide(ski,treeGroup,True):
            ski.image = imageCrash
        #检测人和旗子是否碰撞
        if pygame.sprite.spritecollide(ski,flagGroup,True):
            pass

        pygame.display.update()  # 刷新  *必须要刷新，不然就不会显示