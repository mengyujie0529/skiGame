import pygame
import random

pygame.init()
window = pygame.display.set_mode((600, 600))  # 设置画布大小（x，y）表示宽度，高度
window.fill([255, 255, 255])  # 改变背景色
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


#树和旗子
class TreeFlag(pygame.sprite.Sprite):
    def __init__(self,image,location,speed,type):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed=speed
        self.type=type

    def update(self):
        self.rect = self.rect.move(self.speed)
        self.speed[1] = -1
        if self.rect.top < -48:
            self.kill()
def create_ski():
    window.fill([255, 255, 255])
    window.blit(ski.image, ski.rect)

def create_obstacle():
    global  group
    llist = []
    for a in range(0, 10):

        type = random.choice(['tree', 'flag'])
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        location = [x * 60, y * 60 + 600]
        if location not in llist:
            llist.append(location)
        if type == 'tree':
            image = './pic/skier_tree.png'
        else:
            image = './pic/skier_flag.png'
        obj = TreeFlag(image, location, [0, 1], type)
        group.add(obj)
def draw_win():
    '''绘制屏幕，除去之前的痕迹'''
    global window
    global group
    global  ski
    window.fill([255, 255, 255])

    group.draw(window)
    window.blit(ski.image, ski.rect)
    window.blit(text,(10,10))
    pygame.display.flip()

def collide_check():
    # 检测人和树是否碰撞
    global  ski
    global score
    global group
    for obj in group:
        if obj.type == 'tree':
            if pygame.sprite.collide_rect(ski , obj) :
                ski.image = imageCrash
                score -= 100
                print(score)
        else:
            if pygame.sprite.collide_rect(ski , obj) :
                ski.image = imageDown
                group.remove(obj)
                score += 10
                print(score)

#显示文字
# def ShowFont():
#     global  score
#     myFont = pygame.font.Font("./abc.TTF",60)
#     red=(255,0,0)
#     text=myFont.render('Score:%d'%score,False,red)
#     window.blit(text,(10,10))

if __name__ == '__main__':
    #设置帧,创建了一个时间对象
    clock = pygame.time.Clock()

    position = 0
    score = 0
    # 创建1个小人
    ski = SkierClass('./pic/skier_down.png', [300, 10], [0, 0])
    #创建多棵树和旗子
    group=pygame.sprite.Group()


    create_obstacle()

    while True:
        clock.tick(400)
        for obj in pygame.event.get():
            if obj.type == pygame.QUIT:  # 关闭窗口
                exit()


        position += 1
        if position >= 600:
            create_obstacle()
            position=0

        # 加载分数
        # ShowFont()
        myFont = pygame.font.Font("./abc.TTF", 60)
        red = (255, 0, 0)
        text = myFont.render('Score:%d' % score, False, red)
        window.blit(text, (10, 10))


        create_ski()
        ski.move()
        group.update()#树旗移动
        collide_check()

        draw_win()
        pygame.display.update()  # 刷新  *必须要刷新，不然就不会显示