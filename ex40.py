class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
<<<<<<< HEAD
# how did the object goes to lyrics???这参数不同名啊 怎么传递过去的？？？
=======
# 为什么lyrics自动获得了object的内容？？？
>>>>>>> d2b40c08ef50e57e3ca936a8678cd0342667b916
happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
