    def update(self, word):
        

        flag=True

        for count in word:
            if self.hand.get(count, 0)!=0:
                self.hand[count]-=1
            else:
                flag=False

        return flag
