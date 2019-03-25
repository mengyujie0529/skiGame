import pygame
import random
pygame.init()
skier_images = ['./pic/skier_crash.png','./pic/skier_down.png','./pic/skier_left1.png','./pic/skier_left2.png','./pic/skier_right1.png','./pic/skier_right2.png']

window=pygame.display.set_mode((600,600))#设置画布大小（x，y）表示宽度，高度
window.fill([255,255,255])#改变背景色


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
        self.rect = self.rect.move(self.speed)
        if self.rect.left<0 or self.rect.right>600:
            self.speed[0]=-self.speed[0]
        elif self.rect.top<0 or self.rect.bottom>600:
            self.speed[1] = -self.speed[1]



#树
class Tree(pygame.sprite.Sprite):
    def __init__(self,image,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top = location

#创建多个小树
treeList=[]
for a in range(0,6):
    x=random.randint(0,window.get_width()-42)
    y=random.randint(0,window.get_height()-48)
    tree=Tree('./pic/skier_tree.png',[x,y])
    treeList.append(tree)
#加载多棵树
for objTree in treeList :
    window.blit(objTree.image,objTree.rect)

#旗子
class Flag(pygame.sprite.Sprite):
    def __init__(self,image,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left=location[0]
        self.rect.top = location[1]
#创建多个旗子
flagList=[]
for n in range(0,10):
    x = random.randint(0, window.get_width() - 12)
    y = random.randint(0, window.get_height() - 24)
    flag = Tree('./pic/skier_flag.png', [x, y])
    flagList.append(flag)
for objFlag in flagList:
    window.blit(objFlag.image,objFlag.rect)





if __name__ == '__main__':
    # 创建1个小人
    ski = SkierClass('./pic/skier_down.png', [300, 10], [20, 20])

    while True:
        for obj in pygame.event.get():
            if obj.type == pygame.QUIT:  # 关闭窗口
                print("退出")
                exit()
        window.fill([255,255,255])
        ski.move()
        window.blit(ski.image, ski.rect)
        pygame.display.update()  # 刷新  *必须要刷新，不然就不会显示