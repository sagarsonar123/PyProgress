from random import randrange
class pet():
    boredom_decrement=4
    hunger_decrement=6
    boredom_threshold=5
    hunger_threshold=5
    sounds=['Brrr']
    def __init__(self,name="My Pet"):
        self.name=name
        self.boredom=randrange(self.boredom_threshold)
        self.hunger=randrange(self.hunger_threshold)
        self.sounds=self.sounds[:]
    def clock_tick(self):
        self.boredom+=1
        self.hunger+=1
    def mood(self):
        if self.boredom<=self.boredom_threshold and self.hunger<=self.hunger_threshold:
            return "Happy!"
        elif self.hunger>self.hunger_threshold:
            return "Hungry"
        else:
            return "Bored"
    def __str__(self):
        state= " I am "+ self.name + "."
        state+="I feel "+self.mood()+"."
        return state
    def feed(self):
        self.reduce_hunger()
    def reduce_hunger(self):
        self.hunger=max(0, self.hunger-self.hunger_decrement)
    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()
    def teach(self,word):
        self.sounds.append(word)
        self.reduce_boredom
    def reduce_boredom(self):
        self.boredom=max(0, self.boredom-self.boredom_decrement)