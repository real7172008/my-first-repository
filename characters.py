# -*- coding:utf-8 -*-
"""
次元语音伙伴 · 第2课：好感上锁、三种性格、自建伙伴。
Character 是第1课写好的。这一课在它上面接着改：
    先给好感上锁，好感只能看、只能通过 add_love 改；
    再写三个子类 Tsundere、Genki、Senpai，三位伙伴各有各的招呼和回话；
    挑战题写 check_name 和 from_dict，页面上就能自建伙伴。
写的顺序：先做两段基础（好感上锁、三个子类），再做进阶，最后做挑战。
挑战的两个方法要写在 Character 里面，所以那一段排在三个子类的上面。
每一段代码写在这一段「# --- 以上 ---」的下面。方法名和参数照每一段写，网页才找得到它们。
这个文件只写类。不要在下面造伙伴或 print；想试一试写得对不对，右键运行 自查.py。
写完保存，重新运行 app.py，浏览器打开 http://127.0.0.1:5000 。试回话时不要勾 ✨AI。
"""


class Character:
    """一位语音伙伴。名字、声线、口癖、好感、聊过的话，都记在这一位自己身上。"""

    count = 0

    def __init__(self, name, voice, catchphrase):
        self.name = name
        self.voice = voice
        self.catchphrase = catchphrase
        self.__love = 0
        self.history = []
        Character.count = Character.count + 1

    # --- 请完成 ---
    # TODO[第2课-基础] 好感上锁：self.__love、只读属性 love、add_love(self, n)
    #
    # 页面上：♥ 旁边有一个「直接改成 999」按钮，它在类外面写 role.love = 999。
    #         现在一点，♥ 真的变成 999，这个数就不可信了。上锁以后再点，页面提示「好感已上锁」，♥ 不变。
    #         说的话里有「讨厌」时好感减 20，但不会减到 0 以下。
    #
    # 要做的事：
    #     1. 上面 __init__ 里标着「上锁时」的那一行，改成 self.__love = 0。
    #        名字前面两个下划线，类外面就读不到、改不了它。
    #     2. 在这里写只读属性 love：上一行写 @property，下面写 def love(self):，return self.__love。
    #        页面和星火读的都是 role.love，有了它才读得到好感。
    #     3. 在这里写 add_love(self, n)：self.__love 加上 n；大于 100 改回 100；小于 0 改回 0；
    #        最后 return 现在的好感。以后改好感都走这一个方法，检查只写这一份。
    #     4. 下面 respond 里标着「上锁时」的三行，改成一句 self.add_love(10)。
    #     5. 在 respond 里「夸夸」那个分支的 return 下面、「难过」那个 if 的上面，加一个「讨厌」分支：
    #            if "讨厌" in msg:
    #                self.add_love(-20)
    #                return "哼，那我先不理你了……" + self.catchphrase
    #
    # 用得上的写法：
    #     @property            写在 def love(self): 的上一行。外面读 role.love 不加括号。
    #     self.__love          只在类里面的方法里这样写。类外面写 role.__love 会报 AttributeError。
    #
    # 写对时：
    #     夸 3 次，♥ 是 30；说一次「讨厌」，♥ 是 10；再说一次「讨厌」，♥ 是 0，不会是 -10。
    #     点「直接改成 999」，提示「好感已上锁，只能靠聊天慢慢涨」，♥ 不变。
    # --- 以上 ---
    @property
    def love(self):
        return self.__love
    def add_love(self, n):
        self.__love=self.__love + n
        if self.__love>100:
            self.__love = 100
        if self.__love<0:
            self.__love = 0
    def greet(self):
        return "我是" + self.name + "，" + self.catchphrase

    def respond(self, msg):
        self.history.append(msg)
        if "夸夸" in msg:
            self.add_love(10)
            return "被夸啦，好开心！" + self.catchphrase
        if "讨厌" in msg:
            self.add_love(-20)
            return "哼，那我先不理你了……" + self.catchphrase
        if "难过" in msg:
            return "别难过，有我陪着你呢。" + self.catchphrase
        if "再见" in msg:
            return "拜拜～记得想我。" + self.catchphrase
        return "嗯嗯，" + self.catchphrase

    def __str__(self):
        return self.name + " / " + self.catchphrase

    def recall(self):
        if len(self.history) == 0:
            return "我们还没聊过天呢。"
        return ("我们聊了 " + str(len(self.history)) + " 句。"
                + "你最后说的是：" + self.history[-1])

    # --- 请完成 ---
    # TODO[第2课-挑战] 自建伙伴：静态方法 check_name(name)、类方法 from_dict(cls, data)
    #
    # 页面上：左边「＋ 自建伙伴」。填名字、选声线、写口癖，点「造出来！」，左边多一张卡片，顶上的登记数加 1。
    #         关掉 app.py 再运行，自建的伙伴还在：页面把它存进 data/custom_roles.json，下次启动用 from_dict 再造出来。
    #         这两个方法写在 Character 里面，接在 recall 的下面，缩进 4 格。
    #
    # 要做的事：
    #     1. check_name(name)，上一行写 @staticmethod，括号里没有 self：
    #            名字去掉两边空格以后是空的：return False, "名字不能是空的"
    #            超过 8 个字：return False, "名字最多 8 个字"
    #            其他：return True, ""
    #        检查名字只看名字本身，跟是哪一位伙伴没有关系，所以写成静态方法。
    #        return 两个值时用逗号隔开，页面先看第一个是不是 True，不是就把第二个显示出来。
    #     2. from_dict(cls, data)，上一行写 @classmethod：
    #            data 是一个字典，例如 {"name": "小狐", "voice": "x4_yezi", "catchphrase": "嘿嘿"}。
    #            return cls(名字, 声线, 口癖)，三样用 data.get 取，没有时分别用「新伙伴」「x4_yezi」「请多指教」。
    #        cls 就是 Character 这个类。cls(...) 就是调用构造方法，造出一位新伙伴。
    #
    # 用得上的写法：
    #     name.strip()                        去掉两边的空格。
    #     data.get("name", "新伙伴")          字典里有 name 就拿它，没有就用「新伙伴」。
    #
    # 写对时：
    #     名字空着点「造出来！」，表单下面出现「名字不能是空的」。
    #     名字写「小狐」、口癖写「嘿嘿」，左边多一张「小狐」，顶上变成「已登记 4 位伙伴」。
    # --- 以上 ---


# ============ 第2课要写的三个子类 ============

# --- 请完成 ---
# TODO[第2课-基础] 三个子类 Tsundere、Genki、Senpai：super().__init__ 和重写 greet
#
# 页面上：点三位伙伴，招呼各是各的味道，不再都是「我是……」。
#         还要把 services.py 里的 ROLES 换成这三个子类造出来的伙伴，页面才用得上它们。
#
# 要做的事：
#     1. 写 class Tsundere(Character):。括号里写父类 Character，Tsundere 就有了 Character 的全部属性和方法。
#     2. 它的 __init__ 只有 self 一个参数。里面只写一句：
#            super().__init__("傲娇酱", "x4_yezi", "哼，才不是特意来陪你呢！")
#        名字、声线、口癖交给父类的构造方法去存，好感、history、登记数也一起有了。
#     3. 重写 greet：return "哼！我是" + self.name + "……" + self.catchphrase
#     4. Genki 照着写：super().__init__("元气酱", "x4_xiaoyan", "哈喽哈喽～元气满满！")，
#        greet 是 return "哈喽！！" + self.name + "登场！" + self.catchphrase
#     5. Senpai 照着写：super().__init__("学长", "x4_jingjing", "要好好学习哦")，
#        greet 是 return "你好呀，我是" + self.name + "。" + self.catchphrase
#
# 写对时：
#     Tsundere() 不用传参数，name 就是「傲娇酱」。
#     Tsundere().greet() 是「哼！我是傲娇酱……哼，才不是特意来陪你呢！」。
#     recall、love、add_love 都不用再写，三个子类从 Character 继承下来就能用。
#     respond 基础题也不用写，进阶题再重写。
# --- 以上 ---
class Tsundere(Character):
    def __init__(self):
        super().__init__("傲娇酱", "x4_yezi", "哼，才不是特意来陪你呢！")
    def greet(self):
        return "哼！我是" + self.name + "……" + self.catchphrase
class Genki(Character):
    def __init__(self):
        super().__init__("元气酱", "x4_xiaoyan", "哈喽哈喽～元气满满！")
    def greet(self):
        return "哈喽！！" + self.name + "登场！" + self.catchphrase
class Senpai(Character):
    def __init__(self):
        super().__init__("学长", "x4_jingjing", "要好好学习哦")
    def greet(self):
        return "你好呀，我是" + self.name + "。" + self.catchphrase
# --- 请完成 ---
# TODO[第2课-进阶] 三个子类各自重写 respond：同一句「夸夸」，三种回法
#
# 页面上：分别对三位说「夸夸我」，回话是三种味道，♥ 都加 10。说别的话，还是 Character 里的回法。
#
# 要做的事：
#     在每个子类里写一个 respond(self, msg)，放在这个子类的 greet 下面，缩进和 greet 一样：
#     1. msg 里有「夸夸」：先 self.history.append(msg)，再 self.add_love(10)，然后 return 这一位自己的一句：
#            傲娇酱    "谁、谁要你夸了！……不过，还挺开心的。" + self.catchphrase
#            元气酱    "哇！！谢谢！能量充满 1000%！" + self.catchphrase
#            学长      "谢谢，你也很优秀。继续保持。" + self.catchphrase
#     2. 不是「夸夸」：return super().respond(msg)，交给父类按原来的回法回，history 也由父类存。
#     子类里不要写 self.__love：两个下划线的名字只在 Character 自己的方法里能用。改好感只用 self.add_love。
#
# 写对时：
#     同一句「夸夸我」，三位回的三句话各不相同，♥ 都加 10。
#     说「难过」，三位回的都是「别难过，有我陪着你呢。」再接各自的口癖。
# --- 以上 ---
def respond(self, msg):
    if "夸夸" in msg:
        self.history.append(msg)
        self.add_love(10)
        return "谁、谁要你夸了！……不过，还挺开心的。" + self.catchphrase
    return super().respond(msg)
def respond(self, msg):
    if "夸夸" in msg:
        self.history.append(msg)
        self.add_love(10)
        return "哇！！谢谢！能量充满 1000%！" + self.catchphrase
    return super().respond(msg)
def respond(self, msg):
    if "夸夸" in msg:
        self.history.append(msg)
        self.add_love(10)
        return "谢谢，你也很优秀。继续保持。" + self.catchphrase
    return super().respond(msg)