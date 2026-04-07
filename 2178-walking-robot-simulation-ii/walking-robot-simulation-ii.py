class Robot:

    def __init__(self, width: int, height: int):
        self.x, self.y = 0, 0
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.d = 0
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        if num == 0: return
        total = self.width * 2 + (self.height - 2) * 2
        num %= total
        if num == 0: num = total

        for i in range(num):
            nx, ny = self.x + self.dirs[self.d][0], self.y + self.dirs[self.d][1]
            if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                self.d = (self.d + 1) % 4
                nx, ny = self.x + self.dirs[self.d][0], self.y + self.dirs[self.d][1]
            self.x, self.y = nx, ny
        

    def getPos(self) -> List[int]:
        return [self.x, self.y]
        

    def getDir(self) -> str:
        if self.d == 0: return 'East'
        elif self.d == 1: return 'North'
        elif self.d == 2: return 'West'
        else: return 'South'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()