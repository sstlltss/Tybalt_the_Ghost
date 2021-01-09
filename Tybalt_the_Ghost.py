# coding=utf-8
from time import sleep
from sys import stdout
from os import system
#--------------初始化角色属性--------------#
Tybalt = {
    'name' : 'Tybalt',
    'Mercutio' : 0,
    'known' : 0,
    'want' : 0,
    'rooms':[['去朱丽叶的房间','去卡普莱家主的房间','去酒馆','回自己的房间','留在广场'],[]],
    'talk': []
}
def speak(st,end=1):
    for char in st:
        print(char,end='')
        sleep(0.04)
        stdout.flush()
    if set_enter:
        if end:
            input()
    else:
        if end:
            print('')
        sleep(0.76)
def choose(choices):
    n = len(choices)
    st = "----------\n"
    for i in range(n):
        st = st + str(i+1) + "." + choices[i]+'\n'
    st += '→'
    while(1):
        speak(st,0)
        choose = input()
        try:
            choose = int(choose)
        except ValueError:
            speak("输入有误，请重新输入。\n",0)
        else:
            if (choose >= 1) and (choose <= n):
                speak("----------\n",0)
                return choose
            else:
                speak("输入有误，请重新输入。\n",0)
def wake():
    def wake_1_1():
        speak("你站起身走近，借着月光看才发现是一个被踩坏了的吊坠，打开的小夹层里放着一张朱丽叶的迷你画像——这是你生前的吊坠。你下意识地想把它捡起来，但却没能做到：你知道你伸出了手，但眼前只有一个模糊的、几乎透明的影子，也没能触碰到吊坠。")
        wake_2(1)
    def wake_1_2():
        speak("你发现这个模糊的身影似乎是人形，并且走路的姿势有些熟悉。看见它和看见周围的其他东西不大相同，仿佛是这个它直接告诉你自己的位置，进而映到你眼前，大脑优先于眼睛。")
        wake_2(2)
    def wake_1():
        speak("你快速地左右看了看。广场上的沙尘一如既往——尽管你很少从这个角度、也很少在这个时间看它们——但地上的血迹在月光的衬托下更加张牙舞爪，提醒着任何看到它的人：这里发生过流血事件。风吹着，楼里的灯亮着，但广场上一个人也没有。")
        speak("你注意到，地上有一个闪闪发亮的东西，同时，不远处似乎有一个模糊的身影。")
        choice = choose(["去看看闪闪发亮的东西","仔细盯着模糊的身影看","什么也不做"])
        if choice == 1:
            speak("你决定去看看在地上那个闪光的东西。")
            wake_1_1()
        elif choice == 2:
            speak("你仔细盯着那个模糊的身影看。")
            wake_1_2()
        else:
            speak("你继续躺在地上。")
            wake_2(2)
    def wake_2(root=0):
        if root==1:
            speak('就在这时，你听见了一个声音:“碰不到的哦。”')
            speak('和你之前听到的声音不同，与其说是你听到，不如说是这个声音凭空出现在你大脑里。于是你开口道：“茂丘西奥？”')
            speak('“是我，我英俊的提伯尔特，虽然你看不到自己的脸了。我该说什么？嗯……欢迎光临？怎么样，死后的世界如何？看得到又看不到，听得到又听不到……不过摸是肯定摸不到的。”那团模糊的身影走到你的身边，对着地上的吊坠扬了扬下巴。')
        elif root == 2:
            speak('就在这时，你听见了一个声音:“是在找这个吗？”')
            speak('和你之前听到的声音不同，与其说是你听到，不如说是这个声音凭空出现在你大脑里。于是你开口道：“茂丘西奥？”')
            speak('“是我，我英俊的提伯尔特，虽然你看不到自己的脸了。我该说什么？嗯……欢迎光临？如果你要找的话，你的吊坠在那里。”')
            speak('你看向声音的方向，那里静静躺着一个吊坠。在反应过来之前，你已经迅速朝吊坠扑了过去——当然，它依然躺在地上纹丝不动。这让你稍稍有些发愣。')
            speak('你听到茂丘西奥一阵大笑，随后他说：“需要我提醒你吗？我们死了。”')
            speak('他朝你走过来，接着说：“怎么样，死后的世界如何？看得到又看不到，听得到又听不到……不过摸是肯定摸不到的。”他对着地上的吊坠扬了扬下巴。')
        else:
            speak('就在这时，你听见了一个声音:“是在找这个吗？”')
            speak('和你之前听到的声音不同，与其说是你听到，不如说是这个声音凭空出现在你大脑里。于是你开口道：“茂丘西奥？”')
            speak('“是我，我英俊的提伯尔特，虽然你看不到自己的脸了。我该说什么？嗯……欢迎光临？如果你要找的话，你的吊坠在那里。”')
            speak('你看向声音的方向，那里静静躺着一个吊坠。在反应过来之前，你已经迅速朝吊坠扑了过去——当然，它依然躺在地上纹丝不动。这让你稍稍有些发愣。')
            speak('你听到茂丘西奥一阵大笑，随后他说：“需要我提醒你吗？我们死了。”')
            speak('但你这时突然意识到一件事，于是你说：“茂丘西奥，你能看见我？”')
            speak('“当然，为什么不能？”他回答道。')
            speak('于是你认真地看向茂丘西奥的方向。起初你什么也没看到，直到后来你看见一个透明的东西左右挥舞。这种“看见”和之前也不大相同，仿佛是这个东西直接告诉你它所在自己的位置，进而映到你眼前，大脑优先于眼睛。你顺着看下去，终于从背景里看出整个人影。紧接着对方朝你走过来，盘着腿坐在你面前。')
            speak('“怎么样，死后的世界如何？看得到又看不到，听得到又听不到……不过摸是肯定摸不到的。”他对着地上的吊坠扬了扬下巴。')
        speak('“哦。”你回答道。')
        speak('“别这么冷漠嘛，我的猫王子。你还记得那个关于死后的传说吗？”')
        speak('（于是你想起来，在维罗纳流传着一个关于死后世界的传说，它的内容大概是这样的：通常来说，死后的灵魂会直接前往天堂，或去往地狱。但如果死者有着强烈的愿望，灵魂就会留在人间，并在愿望得以实现之后离开。但由于灵魂离开了躯体，灵魂可能会忘记自己的愿望，并且随着时间的推移，记忆会逐渐变得模糊。当灵魂忘记自己的身份时，就会消散于天地之间，据说此后便再不会有人记得或提起灵魂生前的身份。）')
        speak('“那么我们现在应该……”你问道。')
        speak('他舔了舔嘴唇：“找到愿望，然后实现它。”')
        speak('他抬起头看着月亮，又加了一句：“在我们消失之前？”')
    def do():
        speak("当睁开眼睛的时候，你仍然觉得疼。尽管在过去的十几年里你受过无数次伤，但每一次的感受都是特殊的、独一无二的，谁也没法习惯疼痛。不过这次的要格外特殊一些。")
        choice = choose(["查看四周","坐起来","站起来","继续躺着"])
        if choice == 1:
            speak("你决定查看一下周围的情况。")
            wake_1()
        elif choice == 2:
            speak("你慢慢坐了起来。")
            wake_2()
        elif choice == 3:
            speak("你撑着地面站了起来。")
            wake_2()
        elif choice == 4:
            speak("你决定就这样躺在地上。")
            wake_2()
    do()

def visit():
    def end(root):
        if root == 1:
            word1 = '链甲'
        else:
            word1 = '玩偶'
        speak("你和茂丘西奥来到了夫人的房间，她一个人坐在梳妆台前，对着面前的%s发愣。不知道是不是没有刻意打扮的原因，她看起来比以往憔悴得多。她是你的姑姑，是你父亲的姐妹，也是你的情人——尽管直到你死，你们都尚未挑明关系。她对你而言到底是什么呢？姑姑？情人？又或是母亲或朱丽叶的替代品？你自己也不清楚。而直到这次踏进她房间为止，你都以为在她看来你也不过是一位普通情人，或是父亲的替代品。" %(word1))
        speak("卡普莱夫人抚摸着%s，叹了口气：“提伯尔特……先是你的父亲，现在又是你。甚至今天还是他的忌日……第二次了，如果我能早一点赶到。家主说，今天就要把你的东西全都清理干净，说是宴会需要。得了吧，我知道他，不过是看你不顺眼，毕竟你和哥哥的脾气差太多了。他不明白，你们是两个人，而我明白，可我正是太明白了，所以才会看着你们死去两次。”她说着哭了起来。" %(word1))
        speak("你下意识地想为她擦去眼角的泪水。茂丘西奥正要提醒你，却发现你的手并没穿过夫人的脸，而是如你所愿地拦住了那颗眼泪的去路。")
        speak("夫人突然抬起头：“谁？”而后轻轻眯起眼睛，目光聚焦在你身上，犹豫着问道：“提伯尔特？”")
        speak("“是我，姑姑。”你完全忘记了自己已死的事，答道。但就在这时，你发现你的手指尖变得越发模糊，连隐约的轮廓也几乎看不出了，就像是溶化在空气中一样。")
        speak("茂丘西奥也发现了，你转过头去看到了他惊讶的表情。")
        speak("夫人看着你的身影越发模糊，仿佛鼓起勇气一般，探起身子给了你一个吻：“抱歉提伯尔特，这是我欠你的。”")
        if Tybalt['want'] >= 4:
            speak("这一刻你突然明白了，一直以来你的愿望不过是得到一份真正为你的爱。不是因为你的父亲，不是因为你的家族而爱你，只是为了你，提伯尔特这个人而爱你。朱丽叶没有，那不过是你的单相思。而夫人，你从没想过她对你的感情远远超过了普通情人，也绝不是把你当做父亲的替代品。")
        else:
            speak("这一刻你似乎隐约想到了自己的愿望。要是再有一点时间或许就能知道了。你想。")
        speak("“茂丘西奥在那里吗？”夫人朝你刚才转头的方向看去。")
        speak("“是的，他在。”你回答。可夫人并没听到你的声音，从她四下张望的神情来看，恐怕她现在看不见你了。")
        if Tybalt['known'] >= 4:
            speak("你想起了今晚还出现过的类似情况，突然明白了能让活着的人看见或听见你们的方法，于是你告诉茂丘西奥：“当你发自内心地忘记自己已经死了，他们就能看到你，但必须发自内心，我们是灵魂，没法欺骗自己的意志。”茂丘西奥点点头表示明白。")
        speak("你的身影越来越模糊。既然最终的愿望已经完成，你的灵魂就没有留在此地的理由了。但在临走之前还有一件事。")
        speak("“茂丘西奥，你的愿望是什么？”")
        if Tybalt['Mercutio'] >= 1:
            speak("“我想让维罗纳的仇恨消失，无论是他们彼此和解，还是统统灭亡都可以，我想让仇恨消失。”茂丘西奥笑着和你挥手：“一路好走，我亲爱的提伯尔特。”")
            if Tybalt['Mercutio'] >= 2:
                speak("“可如果等到你消失还没有完成呢？”")
                if Tybalt['known'] >= 4:
                    speak("“那我就一直等下去。不过没关系的，我已经知道不会消失的办法了。比起消失来更大的问题可能是没有你陪我了呢，猫王子。”")
                else:
                    speak("“那我就一直等下去，等到我消失为止。”")
        else:
            speak("“不告诉你，就当是你抛下我的惩罚吧，猫王子。再见了。”茂丘西奥笑着和你挥手。")
        speak("在你离开前的最后一刻，你看到卡普莱夫人对着或许是她最后看见你的方向挥了挥手：“再见了，提伯尔特。”")
        speak("----------")
        speak("游戏结束，感谢您的游玩。")
        speak("构思&脚本&代码编写&发布：阿贺")
        speak("特别鸣谢：夏裕 月怀 寥若晨星 黎墨")
        input("按任意键退出。")
        exit()
    def corrider(root):
        if root == 1:
            speak("你们从房间出来，正好撞见女仆长抱着什么东西，匆匆忙忙地跑着。你定睛一看，发现是你生前穿的那件链甲，它曾是你父亲的物品，在他死后就归你所有。仆人跑去的方向并不是楼外，谁会要那件链甲吗？")
            choice = choose(['跟上去','不去管它'])
            if choice == 1:
                speak("你和茂丘西奥跟了上去，可走到门口才发现，那是卡普莱夫人的房间。女仆长把链甲送到就离开了，你决定留下来看看夫人到底要你的链甲做什么。")
                end(1)
            else:
                speak("那件链甲确实很好，毕竟是父亲留下来的，或许是谁想穿吧。你这么想着，和茂丘西奥一起回到了广场。")
                Tybalt['rooms'][1].append('corrider')
                return
        elif 'corrider' in Tybalt['rooms'][1]:
            speak('你们再次离开了房间，没想到又遇到了女仆长，这次也匆匆忙忙地抱着什么跑走——是你藏在柜子里的玩偶。如果说想要链甲还有父亲的原因在里面，那么你一直珍藏的洋娃娃又是谁会想要呢？你和茂丘西奥一路跟上，可走到门口才发现，那是卡普莱夫人的房间。女仆长把玩偶送到就离开了，你决定留下来看看夫人到底要它做什么。')
            end(2)
        else:
            speak("你们从房间出来，正好撞见女仆长抱着什么东西，匆匆忙忙地跑着。你定睛一看，发现是你的玩偶。她跑去的方向并不是楼外，谁会要你的洋娃娃？你和茂丘西奥一路跟上，可走到门口才发现，那是卡普莱夫人的房间。女仆长把玩偶送到就离开了，你决定留下来看看夫人到底要它做什么。")
            end(2)
    def square():
        Tybalt['rooms'][1].append("留在广场")
        Tybalt['Mercutio'] += 1
        speak("茂丘西奥耸了耸肩，一屁股坐在你脚边。你们就这样一站一坐，望望天，看看地。月光一如以往地照在地面，昨天如此，今天如此，日后也将是如此。对维罗纳的其他人来说，今天的月亮和昨天的没有什么不同，但对你们来说不是。直到今天中午，你们都还是维罗纳城内的一部分，是她世代仇恨里漂浮在最上层的气泡，时不时得以窥见下层或浓稠或凝固的部分。但就那么一会儿——十分钟，十秒钟，眨眼之间——生命就破了，掉下去了。如今，维罗纳还活着的东西都与你们无关，生命是，仇恨也是。")
        speak("你们就这样一言不发地待了好一会儿，突然间，茂丘西奥像是想起了什么，开口问你：“提伯尔特，你是怎么死的？”")
        choice = choose(['“嗯，什么？你不知道吗？”','“是罗密欧”','“是亲王下令将我处死”','摇摇头，什么也不说'])
        if choice == 1:
            speak("“嗯，什么？你不知道吗？”你反问道。")
            speak("“我的好提伯尔特，死了又能知道些什么呢？你不也是刚刚才醒吗？”虽然看不清，但你觉得茂丘西奥必然对着你翻了个白眼。")
            speak("“好吧，是……”就在你正准备吐出罗密欧的名字时，你想起眼前的人生前和罗密欧的关系，你犹豫了，是不是不告诉他反而更好？")
            choice = choose(['“罗密欧”','“亲王，他下令将我处死，立即执行”'])
            if choice == 1:
                speak("“罗密欧。”你还是决定说出真相。")
                speak("“什么？”")
                speak("“是罗密欧，就用我杀死你的那把刀。”你狠下心，一字一顿地说。")
                speak("“罗密欧？那他……他会死吗？”")
                speak("“我不知道，抱歉。”你如实回答，而茂丘西奥像是立刻失去了力气，你甚至觉得他的轮廓都模糊了一些。")
            else:
                speak("“亲王，他下令将我处死，立即执行。”你没法说出口。")
                speak("“不对，你在骗我，提伯尔特。”茂丘西奥盯着你看了半天之后，斩钉截铁地说道：“我舅舅下判决决不会立即执行，他肯定会先弄清楚事情来由，而我醒来之后不到10分钟你就醒了。更何况你现在甚至不敢正眼看我，提伯尔特。到底是谁？”")
                speak("你没法再骗他了，只好说出了罗密欧这个名字。")
                speak("“罗密欧？我就说你为什么瞒着我……果然是他……”茂丘西奥像是立刻失去了力气，你甚至觉得他的轮廓都模糊了一些。")
        elif choice == 2:
            speak("“被罗密欧杀的。”你直截了当地说了。")
            speak("“罗密欧？！”茂丘西奥听起来非常激动，甚至惊起了树上一群鸟。")
            speak("“为什么……会是他啊……”他喃喃自语，而你看着那群鸟飞走，突然想起你们已死的事实——为什么茂丘西奥能惊起一群鸟？你感到背后一阵发凉。茂丘西奥显然没心思关注飞天上的鸟，他一门心思都在罗密欧身上。")
            Tybalt['talk'].append("飞鸟")
        elif choice == 3:
            speak("“是亲王，他下令将我处死，立即执行。”你犹犹豫豫地说。")
            speak("“不对，你在骗我，提伯尔特。”茂丘西奥盯着你看了半天之后，斩钉截铁地说道：“我舅舅下判决决不会立即执行，他肯定会先弄清楚事情来由，而我醒来之后不到10分钟你就醒了。更何况你现在甚至不敢正眼看我，提伯尔特。到底是谁？”")
            speak("你没法再骗他了，只好说出了罗密欧这个名字。")
            speak("“罗密欧？我就说你为什么瞒着我……果然是他……”茂丘西奥像是立刻失去了力气，你甚至觉得他的轮廓都模糊了一些。")
        else:
            speak("你摇摇头，什么也没说。茂丘西奥追着你问了半天，你就是不肯回答，他也只好作罢。")
            speak("“好吧，好吧，我的好提伯尔特，你不想说就不说吧。那么下一个问题：我们现在去哪儿呢？总不能就在这儿耗着。”")
            Tybalt['Mercutio'] -= 1
            return "留在广场"
        Tybalt['talk'].append('罗密欧')
        speak("“罗密欧……罗密欧……该死的，我明明告诉过他好好去爱朱丽叶，我的意思是，不要卷进这些仇恨里来……你知道吗，提伯尔特，这些仇恨是……是无知的、无意义的……我没有说你的意思，我只是想……它们是可恨的。你看，卡普莱和蒙太古，明明他们——你们或者我们——说着同样的语言，何必要这样呢？今天卡普莱多伤了蒙太古一人，明天蒙太古多伤了卡普莱两人，最后谁也逃不出。你是自愿卷进来的，而我……我拦在他面前，甚至为他去死，我以为这样至少能把他推出去，可他还是挤到我们中间……”")
        speak("你看看他，又看看旁边的溪流，什么也没说，周围又只剩下蟋蟀的声音。")
        speak("过了一会儿，茂丘西奥似乎恢复了一点精神，他决定打破沉默：“你有什么想去的地方吗，提伯尔特，我随便去哪里都行，我跟着你。”")
        Tybalt['want'] += 2
        if "飞鸟" in Tybalt['talk']:
            speak("“在考虑去哪里之前……我刚才看到一件奇怪的事。”你想起了刚才被惊飞的鸟，决定就在这里告诉他：“你刚才激动的吼声惊起了一群鸟。我发誓我看到了那群鸟，当时也没有别的声音，我的意思是，会吓到它们的那种。”")
            speak("“我？可我们死了。”茂丘西奥显得有些迷惑。")
            speak("“是的，问题就在这里，我们死了。”你也有些不知所措。")
            speak("茂丘西奥环顾四周，你也顺着他的方向到处看看，但周围只有蛐蛐的叫声。他又试着大吼了几声，但没有任何动静。")
            speak("“算了，在这儿也不是个办法，说不定它们就是突然想飞了。不如考虑接下来去哪里吧，提伯尔特。”茂丘西奥停了下来。")
            Tybalt['known'] += 2
        return "留在广场"
    def visit_1(root):
        if root == 0:        
            speak("你们来到朱丽叶的房间门口，你突然有些犹豫。尽管你是出于好意，并且现在除了茂丘西奥没人知道你的存在，半夜进入朱丽叶的房间还是让你有些愧疚。茂丘西奥似乎看出来了你的犹豫：“怎么了，难道我们英勇神武的提伯尔特在朱丽叶房间门口害羞了？在自己房间藏着她的洋娃娃，却不敢来见她本人？行行好，提伯尔特，死都死了，你还在乎这个么？”说着他径直穿过房门走了进去，你只好跟上。")
            speak("穿过物品的感觉有些怪异，你并没能看到物品内部的任何结构，而是眼前一黑一亮，看见的就已经是房间内部的场景了。")
            speak("朱丽叶坐在床边，对着阳台，朝窗外望着，不知道在想些什么。茂丘西奥穿过床走到朱丽叶的面前盯着她看了一会儿，比划着告诉你：“她刚哭过。”会是为我哭的吗？你想道。")
            speak("正在这时，窗外传来了什么动静。你看到朱丽叶晃了晃脑袋回神，接着就向阳台走去，而从阳台外面蹑手蹑脚地爬进来了一个人……")
            speak("“罗密欧！”你听到朱丽叶压着声音叫道。")
            speak("“这真是……”茂丘西奥看看匆忙进屋的两人，又看看你，没把话说完。他没有揶揄你，尽管你已经做好了被他嘲笑的准备。不过不管茂丘西奥如何，看来朱丽叶恐怕并不是为你而哭的，虽然你尚未知道亲王对罗密欧的判决如何。")
            speak("但这个问题的答案很快就揭晓了，就从这房间里仍活着两人的口中：永久流放。说实在的，你倒是更愿意一死了之，至少不用像这两人一样，活着受罪。但很显然，茂丘西奥并不这么想。")
            speak("“流放？”茂丘西奥像是意识到什么一般，把目光从罗密欧和朱丽叶身上转向了你：“是罗密欧杀了你，是吗？”")
            Tybalt['talk'].append('罗密欧流放')
            choice = choose(['点点头：“是的。”','“你不知道吗？”'])
            if choice == 1:
                speak('你点了点头。')
            else:
                speak("“你不知道吗？”你有些疑惑。")
                speak("“我？我当然不知道……我怎么会知道呢？我比你早醒不了多久，我还以为……我还以为和他无关，是亲王下令将你处死。”")
            speak('茂丘西奥突然好像失去了所有力气，你甚至觉得他的轮廓都略微模糊了一些。')
            speak('“我想出去走走，提伯尔特，你先在这儿待着吧，抱歉。”说完就径直向窗外走去。')
            choice = choose(['跟上他','留在朱丽叶的房间'])
            if choice == 1:
                Tybalt['want']+=1
                Tybalt['Mercutio'] += 1
                speak("你紧跟着茂丘西奥的脚步一起跳下了窗台，他没有回头，只是继续走着，自言自语：“我还说要他好好爱朱丽叶，现在他恐怕自身都难保……罗密欧，我从未想过要你帮我复仇，我从未想让你卷入这些仇恨里……”")
                speak("你走到他身边，他看了看你，继续说：“你知道吗，提伯尔特，这些仇恨是……是无知的、无意义的……我没有说你的意思，我只是想……它们是可恨的。你看，卡普莱特和蒙太古，明明他们——你们或者我们——说着同样的语言，何必要这样呢？今天卡普莱特多伤了蒙太古一人，明天蒙太古多伤了卡普莱特两人，最后谁也逃不出。你是自愿卷进来的，而我……我拦在他面前，甚至为他去死，我以为这样至少能把他推出去，可他还是挤到我们中间……”")
                speak("你看看他，又看看旁边的溪流，什么也没说，周围又只剩下蟋蟀的声音。")
                speak("茂丘西奥望了一会儿天，决定打破沉默：“我没事了，走吧。我们去哪儿？”")
            else:
                speak('你目送茂丘西奥跳下阳台，转过头又看着朱丽叶和罗密欧讲些肉麻的情话。朱丽叶望向罗密欧的眼神里全是爱意，你忽然又觉得活着其实也不错——若是能被朱丽叶这样望一次，即使是活着受苦，那也心甘情愿。可是现在，再也不会有人用这种眼神看你了。')
                speak("你也走出阳台，跳了下去，茂丘西奥就在不远处。等你走近，他点了点头，什么也没说，只是问你：“我们接下来去哪儿？”")
                Tybalt['want']+=3
            Tybalt['rooms'][1].append("去朱丽叶的房间")
            return '去朱丽叶的房间'
        elif '去朱丽叶的房间' in Tybalt['rooms'][1]:
            speak("你们再次来到朱丽叶的房间门口，这次你毫不犹豫地穿过房门进入房间。虽然早就猜到罗密欧会在这里留宿，但亲眼看见他睡在朱丽叶旁边还是让你有些气愤。")
            if ('罗密欧流放' in Tybalt['talk'])or('罗密欧' in Tybalt['talk']):
                speak("你瞥了一眼茂丘西奥，他看着罗密欧出神，不知道在想什么。")
            if '朱丽叶结婚' in Tybalt['talk']:
                speak("你转过头去看朱丽叶，她沉沉地睡着，全然不知自己即将被父亲嫁出去的消息。")
            speak("“可惜我们死了。”你轻声说。")
            speak("“现在后悔可没什么用。”茂丘西奥回了你一句：“关于你的愿望，你有什么头绪了吗？”")
            speak("你思索着说：“我总觉得或许与朱丽叶有关，但每当我看见她又觉得，好像不是。”")
            if Tybalt['want'] >=2:
                speak("或许和爱有关。你在心里默念道。")
            speak("茂丘西奥歪了一下头：“那要不要去别的地方看看？在这儿守一宿也不会发生什么。”")
            Tybalt['want'] += 1
            corrider(root)
        else:
            speak("你们来到朱丽叶的房间门口，你突然有些犹豫。尽管你是出于好意，并且现在除了茂丘西奥没人知道你的存在，半夜进入朱丽叶的房间还是让你有些愧疚。茂丘西奥似乎看出来了你的犹豫：“怎么了，难道我们英勇神武的提伯尔特在朱丽叶房间门口害羞了？在自己房间藏着她的洋娃娃，却不敢来见她本人？行行好，提伯尔特，死都死了，你还在乎这个么？”说着他径直穿过房门走了进去，你只好跟上。")
            speak("穿过物品的感觉有些怪异，你并没能看到物品内部的任何结构，而是眼前一黑一亮，看见的就已经是房间内部的场景了。")
            speak("但这房间内部的场景把你着实气得不轻：朱丽叶躺在床上，盖着被子，而她的身边躺着的赫然是……")
            speak("“罗密欧我杀了你！！！”你忘记了一切，朝着床上的人怒吼道。而茂丘西奥只顾捂着嘴笑。")
            speak("但你没想到的是，朱丽叶突然惊醒，环顾四周，小声说了一句：“提伯尔特？”这让你瞬间冷静下来。")
            choice = choose(['朱丽叶，你能看到我？','是我，朱丽叶，是我。'])
            if choice == 1:
                speak("“朱丽叶，你能看到我？”你满怀着期望发问，却看到她自嘲地笑了笑，又摇了摇头躺下睡去。")
            if choice == 2:
                speak("“是我，朱丽叶，是我。提伯尔特。”你的声音有些颤抖，但她却只是自嘲地笑了笑，又摇了摇头躺下睡去。")
            if Tybalt['known'] <2:
                speak("“刚才那是怎么回事？”茂丘西奥看看你，又看看缓缓睡去的朱丽叶。你摇了摇头，表示自己也不知道。")
            elif '酒馆' in Tybalt['talk']:
                speak("你想起之前茂丘西奥说的，玛缇娜似乎听到了你的吼声，总觉得事情有些不对劲。你们确实死了，但要说是巧合，两次又有些过分。茂丘西奥看起来也摸不着头脑，你们只好决定先离开房间。")
            elif '酒馆' in Tybalt['rooms'][1]:
                speak("“啊！我想起来了，刚才在酒馆里也是这样。玛缇娜，你吼了一声，我回头的时候朝你的方向看了一眼，她像是被你的声音吓到了，就像……”茂丘西奥指了指床上的人，“就像刚才她一样。”")
                Tybalt['talk'].append("酒馆")
                speak("“……可我们死了啊？会不会是巧合？”你有些不敢相信。")
                speak("“巧合不会发生两次，提伯尔特，比起来我更好奇的是‘为什么’。”茂丘西奥若有所思，“算了，我们还是先走吧？”你点点头，眼睛一直盯着朱丽叶看，想从中找出什么答案来。")
                Tybalt['known'] += 1
            else:
                speak("你们又盯着睡梦中的两人看了一会儿，两人并没有任何新的动静，于是你们决定先离开，去别处看看。")
            Tybalt['rooms'][1].append("去朱丽叶的房间")
            Tybalt['talk'].append("朱丽叶的房间")
            Tybalt['known'] += 2
            Tybalt['want'] += 1
            corrider(root)
            return '去朱丽叶的房间'
    def visit_2(root):
        if root == 0:
            speak("你独自一人来到卡普莱家主的房间。虽说是家主，可即使是在父亲逝去后，你也并不怕他。他不过是个名义上的家主，胆小怕事忍气吞声，“维罗纳的和平主义者”，哈！生前他碍于你的威名极少和你正面冲突，现在你死了，不知道他又会做出什么事？")
            speak("你进入房间的时候，家主正在和管家吩咐：“……明天他就会来，务必要准备好，不光是吃喝歌舞，下人们的情绪也要注意……”“可大小姐和夫人……”“她知道分寸，朱丽叶让夫人去劝就是了。提伯尔特死了，我们必须尽快找到靠山，帕里斯是最好的选择，一定不能错过了。”“是。”")
            speak("“你疯了？”你朝家主吼道，全然忘记了你已死的事。")
            speak("而家主突然四下张望，又掏了掏耳朵：“你有听到什么声音吗？”管家摇摇头。")
            speak("“我好像听到提伯尔特在吼我。”家主皱紧了眉头。")
            speak("“可……您也知道，提伯尔特下午就死了，是蒙太古家那小子动的手。”管家看起来有些疑惑。家主嘟囔了一句，摆了摆手，让管家离开了。")
            speak("你听着他们的对话突然愣住。家主真的听到你的声音了吗？还是说只是恰巧？可这未免也太巧了。家主戴起眼镜，或许是准备写些什么。而你打算回到广场，和茂丘西奥谈谈刚才发生的事。")
            speak("你在广场上和茂丘西奥汇合，他看起来很失落。他告诉你，他在亲王那里听说你的死是罗密欧所为，而亲王对他下达的判决是永久流放。你则告诉他，卡普莱家主要让朱丽叶和帕里斯结婚，明天就是订婚宴。")
            speak("“还有一件事，”你想了想说：“我还遇到了一件奇怪的事。我听到家主说要让朱丽叶结婚时朝他吼了一句——我当时忘记我死了——本来也没什么，但他好像……听到我的声音了。”")
            speak("“听到你的声音？”")
            speak("“是的，他看了看周围，又问管家有没有听到我说话，管家说他没有。我不知道是不是巧合，但这怎么想都有些……太巧了。”")
            speak("茂丘西奥环顾四周，你也顺着他的方向到处看看，但周围只有蛐蛐的叫声。他又试着大吼了几声，但没有任何动静。")
            speak("“算了，在这儿也不是个办法，说不定就是刚好遇到了。不如考虑接下来去哪里吧，提伯尔特。”茂丘西奥停了下来。")
            Tybalt['talk'].append("罗密欧流放")
            Tybalt['known'] += 1
            Tybalt['want'] += 1
            Tybalt['talk'].append('朱丽叶结婚')
            Tybalt['talk'].append('家主的房间')
            Tybalt['rooms'][1].append('去卡普莱家主的房间')
            return '去卡普莱家主的房间'
        elif root == 1:
            if ('罗密欧流放' in Tybalt['talk'])and('朱丽叶结婚' in Tybalt['talk']):
                speak("你本打算独自一人过来的，但茂丘西奥以自己无事可做为由死活要跟着你，你没法也没那个心情阻止他。家主要让朱丽叶结婚的事令你烦躁不安。但当你们进入房间时，除了卡普莱家主，还看到了他的夫人。")
            else:    
                speak("你和茂丘西奥来到卡普莱家主的房间，令人意外的是，卡普莱夫人也在。")
            speak("“我说了，明天就要举办宴会，他的房间必须收拾干净。”")
            speak("“可他甚至还没下葬！这就收拾提伯尔特的东西不合规矩。”")
            speak("“得了吧，别以为我不知道你们俩之间那点儿勾当。我不管扔到哪里去，他的房间今天晚上必须清空。你要是想要，就趁仆人还没扔干净快去拿吧！”")
            speak("卡普莱夫人听到这句话，瞪了家主许久，转身离开了。她走后，家主又坐回椅子上写东西，似乎是在写他的日记。")
            speak("“哇哦，没想到卡普莱夫人对你这么认真啊。真好，她对我可从没这样过。”茂丘西奥揶揄道。")
            speak("而你走出门外，看到卡普莱夫人对女仆长吩咐了几句，直接回到了她自己的房间。")
            choice = choose(['和茂丘西奥聊天','去卡普莱夫人的房间'])
            Tybalt['talk'].append("夫人收拾东西")
            Tybalt['want'] += 1
            Tybalt['rooms'][1].append('去卡普莱家主的房间')
            if choice == 1:
                speak("“少说两句你也不会死第二次，茂丘西奥。”你回敬他：“我猜夫人不过是想要我的那身链甲，从我父亲那留下来的。”")
                speak("茂丘西奥耸了耸肩：“是是是，我的提伯尔特大人。别那么认真嘛！那么我们现在去哪儿？”")
                return '去卡普莱家主的房间'
            if choice == 2:
                speak("你决定跟上卡普莱夫人，看看她到底想要你的东西做些什么。")
                end(1)
        else:
            if ('罗密欧流放' in Tybalt['talk'])and('朱丽叶结婚' in Tybalt['talk']):
                speak("你本打算独自一人过来的，但茂丘西奥以自己无事可做为由死活要跟着你，你没法也没那个心情阻止他。家主要让朱丽叶结婚的事令你烦躁不安。当你们进入房间时，卡普莱家主正戴着眼镜坐在桌子前写着什么，你仔细看了看，发现那是他的日记。")
            else:    
                speak("你和茂丘西奥来到卡普莱家主的房间。进入房间的时候，他正戴着眼镜坐在桌子前写着什么。你仔细看了看，发现是他的日记。")
            if '去卡普莱家主的房间' in Tybalt['rooms'][1]:
                speak("你上次走的时候他就在写这个，这让你十分好奇日记的内容——显然，茂丘西奥对此更是有着一百分的好奇。于是你们仔细看起了日记。")
            speak("“……我觉得我该对你说抱歉，但死亡本就与我们相伴而行，我没有多余的时间来为他默哀，家族的事务还在等着我。朱丽叶若是个男人，那提伯尔特死后家中至少还有个靠山，但她不是。蒙太古家仍有一子，为此我只有为她寻找靠山这一条出路，帕里斯是最好的选择，实际上他几乎是唯一一个选项。这样一来，艾斯卡勒斯不会让蒙太古做得太越界，至少在朱丽叶还活着的时候。\n……”")
            speak("“……她和你的儿子，我想毫无疑问是有些勾当。抱歉我用这样的词来描述。他活着的时候我从未告诉过你，尽管我早就知道。我没有怕他，只是你也知道的，那份协定。她来找我要求晚些收拾提伯尔特的遗物时，我告诉今晚就是最后期限。她应当是想要从他的遗物里拿走一些作为纪念。起初我以为她只是从提伯尔特的身上看到你的影子，因此想要你的那件链甲，但后来发现她似乎还想要别的什么，或许是‘定情信物’一类的……抱歉，原谅我对你的儿子所知甚少，或许那件物品只有他和她二人才会知道吧。”")
            speak("“是什么‘定情信物’啊？说出来让我听听嘛，提啵~”茂丘西奥的声音让你感到一阵恶寒。")
            choice = choose(['“别想多了茂丘西奥，什么也没有”','“你猜猜看呀，咩库~”'])
            if choice == 1:
                speak("“别想多了茂丘西奥，什么也没有。”你翻了个白眼，虽然并不知道他是否能看到：“我都不知道她还会对我的东西感兴趣，除了那件链甲。”")
                speak("“在意的话不如去看看。”茂丘西奥话里仍有笑意。你点点头，两人一起向卡普莱夫人的房间走去。")
            else:
                speak("“你猜猜看呀，咩库~”你模仿着他的语气，先把自己恶心得够呛，反倒是茂丘西奥对此适应良好，他提议去一趟卡普莱夫人的房间，看看她到底对你的什么东西念念不忘。")
                Tybalt['Mercutio']+=1
            Tybalt['rooms'][1].append('去卡普莱家主的房间')
            Tybalt['want'] += 1
            end(2)
    def visit_3(root):
        if root == 2:
            if '去酒馆' in Tybalt['rooms'][1]:
                speak("你们再次来到了酒馆。和上次来的时候一样，这里比起往常安静地过分。你们站在了一桌卡普莱旁，看看能否了解到什么新的事。")
            else:
                speak("酒馆里人不少，但和以往的喧哗景象不同，这里现在安静得过分。没有互相嘲讽挑事的声音，更没有打闹的身影，每个人都只是喝着自己面前的酒，最多也不过和同座的人小声讲讲话。你们来到一桌卡普莱边上打探消息。")
            speak("“……夫人呢？家主之前找我们几个说了明天宴会的事，可我都没怎么看见她。”")
            speak("“我听仆人说，在收拾提伯尔特的东西，仆人送到她房间，她亲自收拾。”")
            if '夫人收拾东西' in Tybalt['talk']:
                speak("“哇哦提伯尔特，夫人对你还真是上心啊。”茂丘西奥揶揄你。")
                speak("“我听说，她特意叮嘱仆人们，好好对付那件链甲，还有柜子里的洋娃娃。没想到啊，提伯尔特居然喜欢那种东西……不过也说不定，或许是夫人送他的什么定情信物呢。”")
            else:
                speak("“她听说家主今天就要把提伯尔特的房间都收拾干净，气得去找家主理论，最后又让女仆长把提伯尔特的东西全送到她那儿去。我看夫人对提伯尔特可真是念念不忘，说不定是拿了东西回去睹物思人。她还特别强调了，要提伯尔特的链甲，和柜子里的一个不知道什么东西，怕不是他们的什么定情信物”")
                speak("你不出意外地听到茂丘西奥戏谑的声音：“哇哦，没想到卡普莱夫人对你这么认真啊。真好啊，她对我可从没这样过。是什么定情信物啊，能让我知道吗？”")
            speak("你没有向茂丘西奥回嘴，你只是在想，夫人要你的链甲或许情有可原——为了思念她的兄长，你的父亲——但洋娃娃实在没道理。你左想右想，决定去一趟夫人的房间，而茂丘西奥执意要跟来。")
            Tybalt['want'] += 1
            Tybalt['rooms'][1].append('去酒馆')
            end(2)
        elif ('朱丽叶结婚' in Tybalt['talk'])or('罗密欧流放' in Tybalt['talk']):
            if not '罗密欧流放' in Tybalt['talk']:
                Tybalt['Mercutio'] += 1
                speak("当你们来到酒馆的时候，茂丘西奥的注意力几乎是立刻就被吧台吸引了，他在吧台后面逛了一整圈，这里摸摸，那里看看。")
                choice = choose(['“你几岁了？”','“你在干什么？”'])
                if choice == 1:
                    speak("“你几岁了？”你有些无奈。")
                else:
                    speak("“你在干什么？”你看着他跑来跑去，不知道他在干什么。")
                speak("“我对吧台背后的模样好奇很久了！”茂丘西奥听起来异常兴奋。")
                speak("你提醒他别忘了正事，他只是随意应了两声。你摇摇头，在一桌卡普莱桌旁站着，不一会儿茂丘西奥终于闹够了，并肩站在你的旁边，听这几个卡普莱人聊天。")
            else:
                speak("你们来到了酒馆。酒馆里人不少，但和以往的喧哗景象不同，这里现在安静得过分。没有互相嘲讽挑事的声音，更没有打闹的身影，每个人都只是喝着自己面前的酒，最多也不过和同座的人小声讲讲话。茂丘西奥默默地跟着你来到一桌卡普莱边上，他们似乎在聊着什么。")
            speak("“……夫人呢？家主之前找我们几个说了明天宴会的事，可我都没怎么看见她。”")
            speak("“我听仆人说，在收拾提伯尔特的东西，仆人送到她房间，她亲自收拾。”")
            if '夫人收拾东西' in Tybalt['talk']:
                speak("“我听说，她特意叮嘱仆人们，好好对付那件链甲。没想到啊，夫人对他这么上心。”")
                speak("“哇哦提伯尔特，夫人对你还真是上心啊。”茂丘西奥揶揄你。")
            else:
                speak("“她听说家主今天就要把提伯尔特的房间都收拾干净，气得去找家主理论，最后又让女仆长把提伯尔特的东西全送到她那儿去。我看夫人对提伯尔特可真是念念不忘，说不定是拿了东西回去睹物思人。她还特别强调了，要提伯尔特的链甲，怕不是他们的什么定情信物。”")
                speak("你不出意外地听到茂丘西奥戏谑的声音：“哇哦，没想到卡普莱夫人对你这么认真啊。真好啊，她对我可从没这样过。”")
            speak("“如果你知道那件链甲来自我的父亲，或许就不会这么想了。”你瞥了茂丘西奥一眼。")
            speak("话虽这么说，但你对夫人想要自己的链甲这件事还是有些好奇。聊过一轮，几人又开始喝酒。")
            choice = choose(['去夫人的房间看看','离开酒馆'])
            Tybalt['want']+=1
            Tybalt['rooms'][1].append('去酒馆')
            if choice == 1:
                speak("你决定去夫人的房间看看，而茂丘西奥执意要跟来。")
                end(root)
            else:
                speak("“我们现在去哪儿？”茂丘西奥问。")
                return '去酒馆'
        else:
            Tybalt['Mercutio'] += 1
            Tybalt['known'] += 1
            speak("当你们来到酒馆的时候，茂丘西奥的注意力几乎是立刻就被吧台吸引了，他在吧台后面逛了一整圈，这里摸摸，那里看看。")
            choice = choose(['“你几岁了？”','“你在干什么？”'])
            if choice == 1:
                speak("“你几岁了？”你有些无奈。")
            else:
                speak("“你在干什么？”你看着他跑来跑去，不知道他在干什么。")
            speak("“我对吧台背后的模样好奇很久了！”茂丘西奥听起来异常兴奋。")
            speak("你提醒他别忘了正事，他只是随意应了两声。你左右看了看，酒馆里人不少，但和以往的喧哗景象不同，这里现在安静得过分。没有互相嘲讽挑事的声音，更没有打闹的身影，每个人都只是喝着自己面前的酒，最多也不过和同座的人小声讲讲话。茂丘西奥又在吧台转了一圈之后，去了一桌蒙太古旁偷听。你也只好找一桌卡普莱家的人打探消息，看看在你们死后这里都发生了些什么。")
            speak("“……宴会？真是胡闹！……帕里斯？……什么？让朱丽叶结婚？！……”")
            speak("“什么？！”你脱口而出，接着就意识到并向茂丘西奥的方向看去。被你吓到的茂丘西奥看起来有些无辜，但这个无辜的表情几乎是立刻就转变成了惊讶，你有些奇怪，但面前玛缇娜所说的事令你更为在意：卡普莱家明天要举办宴会、帕里斯会参加，以及最重要的——朱丽叶将要嫁给帕里斯。最后这件事确确实实地吓到了你。")
            Tybalt['talk'].append('朱丽叶结婚')
            speak("走出酒馆的时候你和茂丘西奥都没有说话，而你注意到他的神色有些异样。过了一会儿，你转过头去想要用刚才听到的消息打开话题，正巧他也转过头来，似乎想说些什么。")
            topic_v3 = ['告诉他朱丽叶将要结婚的事','询问他在酒馆内奇怪的表情','什么也不说']
            choice = choose(['抢在茂丘西奥之前开口，告诉他朱丽叶将要结婚的事','抢在茂丘西奥之前开口，询问他在酒馆内奇怪的表情','示意他先说'])
            if choice == 1:
                del topic_v3[0]
                speak("“朱丽叶要结婚了。”你表情严肃地说。")
                speak("茂丘西奥嘴边的话显然被吓了回去，他改口道：“朱丽叶结婚？谁说的？和谁？”")
                speak("“我刚才在酒馆听到的，家主安排朱丽叶和帕里斯结婚，订婚的宴会明天就举办。”你回答道。")
                speak("“难怪你刚才那么激动……你还听到什么别的消息了吗？”")
                Tybalt['want'] += 1
            elif choice == 2:
                del topic_v3[1]
                speak("“你刚才的表情是怎么回事？被什么吓到了吗？”你抢在他前面开口。")
                speak("“我？刚才……啊！我想起来了，是玛缇娜。你吼了一声，我回头的时候看到她像是被你的声音吓到了一样，朝你的方向看了一眼，但好像什么都没看见。不过……不过我当时在蒙太古那边，可能是看错了。”茂丘西奥听起来不是那么确定。")
                speak("“听到我？”你有些疑惑：“能听到我的应该只有你吧？”")
                speak("茂丘西奥点了点头，又解释可能是自己看错了。可你们心知肚明，酒馆本就不大，今天还格外安静，不可能有什么东西遮挡视线。你们就这样又陷入沉默。过了一会儿，茂丘西奥试图打开话匣子：“你刚才还听到了什么吗？”")
                Tybalt['known'] += 1
                Tybalt['talk'].append('酒馆')
            else:
                speak("你示意他先说，他表情落寞地轻轻点了点头：“罗密欧……是他杀了你，对不对？”")
                speak("“是，你怎么突然……”你停住了。你这才想起来，你们的苏醒是在傍晚，也就是说，茂丘西奥并不知道知道你的死是罗密欧亲手所为。")
                speak("“那么……罗密欧怎么样了？”你小心翼翼地发问。")
                speak("“他们说，”茂丘西奥顿了顿，“罗密欧被流放了，永远不得再踏入维罗纳。”")
                Tybalt['talk'].append('罗密欧流放')
                choice = choose(['什么也不说','“我很抱歉……”'])
                if choice == 1:
                    speak("你看着他，一言不发。")
                    speak("茂丘西奥没有计较，他只是继续说下去，像是在自言自语：")
                else:
                    speak("“我很抱歉……”你轻轻地说。茂丘西奥脑袋耷拉着，摇了摇头。他没有看你，像是在自言自语：")
                speak("“我还说要他好好爱朱丽叶，现在他恐怕自身都难保……罗密欧，我从未想过要你帮我复仇，我从未想让你卷入这些仇恨里。你知道吗，提伯尔特，这些仇恨是……是无知的、无意义的……我没有说你的意思，我只是想……它们是可恨的。你看，卡普莱和蒙太古，明明他们——你们或者我们——说着同样的语言，何必要这样呢？今天卡普莱多伤了蒙太古一人，明天蒙太古多伤了卡普莱两人，最后谁也逃不出。你是自愿卷进来的，而我……我拦在他面前，甚至为他去死，我以为这样至少能把他推出去，可他还是挤到我们中间……”")
                speak("你看看他，又看看旁边的溪流，什么也没说，周围又只剩下蟋蟀的声音。")
                speak("茂丘西奥望了一会儿天，决定打破沉默：“说说你的吧，提伯尔特，你刚才听到了什么？”")
                Tybalt['want'] += 1
                Tybalt['Mercutio'] += 1
            while len(topic_v3)-1:
                choice = choose(topic_v3)
                if topic_v3[choice-1] == '告诉他朱丽叶将要结婚的事':
                    speak("“家主要让朱丽叶结婚，和帕里斯。”你用尽量简洁的话总结道。")
                    speak("茂丘西奥翘起一边眉毛：“那可真是……够快的，你还没下葬呢……”")
                    Tybalt['want'] += 1
                    del topic_v3[topic_v3.index('告诉他朱丽叶将要结婚的事')]
                elif topic_v3[choice-1] == '询问他在酒馆内奇怪的表情':
                    speak("“你在酒馆的表情是怎么回事？被什么吓到了吗？”你问。")
                    speak("“我？……啊！我想起来了，是玛缇娜。你吼了一声，我回头的时候看到她像是被你的声音吓到了一样，朝你的方向看了一眼，但她好像什么都没看见。不过……不过我当时在蒙太古那边，可能是看错了。”茂丘西奥听起来不是那么确定。")
                    speak("“听到我？”你有些疑惑：“能听到我的应该只有你吧？”")
                    speak("茂丘西奥点了点头，又解释可能是自己看错了。可你们心知肚明，酒馆本就不大，今天还格外安静，不可能有什么东西遮挡视线。你们就这样又陷入沉默。过了一会儿，茂丘西奥试图打开话匣子：“你刚才还听到了什么吗？”")
                    Tybalt['known'] += 1
                    del topic_v3[topic_v3.index('询问他在酒馆内奇怪的表情')]
                else:
                    break
            speak("你摇了摇头。")
            speak("“好吧，那我们现在去哪儿？”茂丘西奥问道。")
            Tybalt['rooms'][1].append('去酒馆')
            return '去酒馆'
    def visit_4(root):
        if '回自己的房间' in Tybalt['rooms']:
            speak("你们再次来到你的房间，仆人们仍在收拾你的遗物，尽管你自己都不知道，自己哪儿来这么多私人物品。")
        else:
            speak("你站在房间里，看着往来的佣人收拾你生前的东西。一般来说，逝者的房间不会这么快就被收拾掉，至少会保留两三天，供他或她生前的朋友们来怀念，或是完成什么嘱托。但也许是因为所有的卡普莱都知道你没有亲近的朋友和亲人，在你死去的当晚，房间里就进了三四个佣人打扫；而佣人们如此，显然是家主点了头的。")
            speak("“想起什么了吗？”茂丘西奥问你。")
            speak("“没有。”你摇头，继续看着往来的佣人手里拿着曾经属于你的东西：卡普莱家的衣服、卡普莱家的甲胄、卡普莱家徽纹样的火漆印章……卡普莱、卡普莱，全都是卡普莱，自从你来到卡普莱，在人前仿佛再没作为提伯尔特生活过。")
        if root == 0:
            speak("茂丘西奥也躺在你的床上翘着腿有一搭没一搭地笑你：“虽然我知道你人缘不好，但这也太差了吧？……嘿，小心点，那可是他的宝贝洋娃娃。”")
            speak("你几乎是立刻循声看去——一位毛手毛脚的佣人差点儿把玩偶掉在地上，看起来还为此吓得不轻。")
            choice = choose(['“给我小心点儿！”','什么也不说'])
            if choice == 1:
                speak("你几乎是立刻吼出声：“给我小心点儿！”话一出口，你才想起来自己是个死人。但令你和茂丘西奥惊讶的是，弄掉了玩偶的佣人的的确确地抖了一下，四下张望，仿佛在寻找什么一样。之后才赶紧把玩偶放回了柜子里。你和茂丘西奥互相对视了一眼，虽然你们看不清对方的表情，但你能猜到他现在和你同样惊讶。")
                speak("“为什么……怎么会……”茂丘西奥首先组织好了语言：“她是听到你的声音了？”")
                speak("“我不知道，”你愣了半天才从嘴里挤出这句话：“我只是吼了一声……”")
                speak("茂丘西奥走到那个佣人面前大吼大叫，挥挥手，从她身前穿到身后——但无事发生，她只是继续收拾着提伯尔特的东西。")
                speak("“会不会是巧合？”你说。")
                speak("“也许是吧……”茂丘西奥听起来仍有些怀疑，“但好像也没什么可做的了，我们走吧？”")
                Tybalt['known'] += 2
                Tybalt['want']+= 2
                Tybalt['talk'].append('提包房间')
            else:
                speak("显然佣人们还没有习惯你再不会到来的斥责。生前脾气暴躁的那个人现在只能站在这儿看着，你知道，你再不能对这世界上的东西干涉哪怕是一丝一毫。")
                speak("“真是余威犹在啊，提伯尔特。”茂丘西奥揶揄道。")
                speak("“你自己的愿望呢？不去找么？”你冲他翻了个白眼。")
                speak("“不急着这一会儿。比起来我还是更好奇你的——我们猫王子的冷面之下到底藏着什么小心思呢？”茂丘西奥双手合十跪在床上，装模作样地说：“哦，上帝啊，请您告诉我，提伯尔特·卡普莱，他最想要的究竟是什么？是他那美若天仙的表妹，还是对他求而不得的玛缇娜？又或是和他父母年龄相仿的、背德又禁忌的——卡普莱夫人呢？”")
                speak("“茂丘西奥！”")
                speak("“诶！我在这儿。”茂丘西奥冲你抛了个媚眼：“别这么凶嘛，你可没法杀我第二次……还是什么想法都没有？”")
                speak("“没有，我们走吧。”你说，但仍盯着那位佣人怀里的洋娃娃。")
                Tybalt['want'] += 2
                Tybalt['Mercutio'] += 1
            Tybalt['rooms'][1].append('回自己的房间')
            return '回自己的房间'
        elif root == 1:
            speak("门突然被打开，进来的是家中的女仆长：“夫人说了，把房间里的东西都打包，送到她那里去。房间今晚还是要清空，但东西都别乱扔。表少爷的链甲现在就拿出来好好刷洗干净，夫人一会儿就要；其他的东西也都好好收拾，别弄坏了。”")
            if '夫人收拾东西' in Tybalt['talk']:
                speak("原来她吩咐的是这个……恐怕是准备留着怀念父亲。你想。")
            else:
                Tybalt['talk'].append('夫人收拾东西')
            speak("“啧啧，不错啊提伯尔特，能让夫人这么上心的男人恐怕全维罗纳只有你一个了。”茂丘西奥戏谑地说。")
            speak("“如果你知道那件链甲来自我的父亲，或许就不会这么想了。”你瞥了茂丘西奥一眼。")
            speak("“是是是，我的提伯尔特大人。”")
            speak("话虽如此，夫人对链甲这么上心这件事还是让你有些好奇。要不要去看看呢？")
            Tybalt['want'] += 1
            Tybalt['rooms'][1].append('回自己的房间')
            choice = choose(['去夫人的房间看看','离开房间去广场'])
            if choice == 1:
                speak("你决定去夫人的房间看看。")
                end(root)
            else:
                speak("你暂时没什么心情，比起来你更想去别处看看。")
                return '回自己的房间'
        else:
            speak("门突然被打开，进来的是家中的女仆长，她在柜子边上翻找了一会儿之后说：“刚才夫人又吩咐了，要我把提伯尔特上锁的柜子里的东西拿给她。你们收拾的时候看见了吗？”")
            if '回自己的房间' in Tybalt['rooms'][1]:
                speak("“我之前看见了，是个玩偶。我放在门口的箱子里了。”一个仆人回答。你发现她就是你上次来的时候把玩偶弄掉的人。")
            else:
                speak("“我之前看见了，是个玩偶。我放在门口的箱子里了。”一个仆人回答。")
            speak("女仆长在房间门口的箱子里翻找玩偶，而茂丘西奥的戏谑声也出现：“卡普莱夫人对你真是好啊，该说真不愧是猫王子呢。”")
            speak("“少说两句你也不会死第二次，茂丘西奥。”你回敬他。但你也的确好奇夫人的这么做的目的，你决定去夫人的房间看个究竟。")
            Tybalt['want'] += 2
            Tybalt['rooms'][1].append('回自己的房间')
            end(root)
    def do():
        choice = choose(Tybalt['rooms'][0])
        if choice == 1:
            speak("你提议去朱丽叶的房间一趟。看看她，也看看能不能找到关于愿望的线索。茂丘西奥思考了一会儿，决定陪你一起去。“反正还有的是时间，比起来我还是更好奇你的愿望。”")
            place = visit_1(0)
        elif choice == 2:
            speak("你提议去卡普莱家主的房间，直觉告诉你，那里会有关于你愿望的线索。茂丘西奥点点头，表示自己打算去一趟舅舅家。你们约好稍后回到这里见。")
            place = visit_2(0)
        elif choice == 3:
            speak("你提议去一趟酒馆，看看在你们醒来之前都发生了些什么，茂丘西奥同意了，他打算和你一起去。")
            place = visit_3(0)
        elif choice == 4:
            speak("你打算去自己的房间，茂丘西奥眼睛突然发亮，连连同意，并且死活都要跟你一起去，你只好答应。")
            place = visit_4(0)
        else:   #留在广场
            speak("你哪儿也不想去，就待在这儿。")
            place = square()
        #----------------第二次选择-------------------#
        room_list = Tybalt['rooms'][0][:-1]
        if place != '留在广场':
            del room_list[room_list.index(place)]
        choice = choose(room_list)
        if room_list[choice-1] == '去朱丽叶的房间':
            if ('罗密欧流放' in Tybalt['talk'])or('罗密欧' in Tybalt['talk']):
                speak("过了一会儿，你有些放心不下，提议去看看朱丽叶。茂丘西奥随意点了点头，表示反正他也没处可去。")
            elif '朱丽叶结婚' in Tybalt['talk']:
                speak("你提议去看看朱丽叶，你对她总是放心不下。茂丘西奥点点头，打算和你一起去。")
            else:
                speak("你提议去看看朱丽叶，说不定你的愿望与她有关。茂丘西奥以“反正还有的是时间，比起来我还是更好奇你的愿望”为由，死活要跟着你。")
            place = visit_1(1)
        elif room_list[choice-1] == '去卡普莱家主的房间':
            if '罗密欧流放' in Tybalt['talk']:
                speak("你想去卡普莱家主那里看看，你对他做出让朱丽叶结婚的决定这件事十分生气。茂丘西奥随意点了点头，表示反正他也没处可去。")
            elif '朱丽叶结婚' in Tybalt['talk']:
                speak("过了一会儿，你说想去卡普莱家主那里看看。茂丘西奥点点头：“我跟你一起。”")
            else:
                speak("你提议去卡普莱家主的房间看看，能不能找到和愿望相关的线索。茂丘西奥说要和你一起去。")
            place = visit_2(1)
        elif room_list[choice-1] == '去酒馆':
            if ('罗密欧流放' in Tybalt['talk'])or('罗密欧' in Tybalt['talk']):
                speak("你提议去一趟酒馆，看看能不能打听到什么新的消息。茂丘西奥随意点了点头，表示反正他也没处可去。")
            else:
                speak("你提议去一趟酒馆，看看能不能从那里打听到什么。茂丘西奥点点头：“我跟你一起。”")
            place = visit_3(1)
        else:   #回自己的房间
            if ('罗密欧流放' in Tybalt['talk'])or('罗密欧' in Tybalt['talk']):
                speak("你想去自己的房间看看。茂丘西奥随意点了点头，说要和你一起：“反正我也没别处可去。”")
            else:
                speak("你想去自己的房间看看。茂丘西奥眼睛突然发亮，连连同意，并且死活都要跟你一起去，你只好答应。")
            place = visit_4(1)
        #----------------第三次选择（如果有）---------------#
        room_list = Tybalt['rooms'][0][:-1]
        del room_list[room_list.index(place)]
        choice = choose(room_list)
        if room_list[choice-1] == '去朱丽叶的房间':
            if ('罗密欧流放' in Tybalt['talk'])or('罗密欧' in Tybalt['talk']):
                speak("过了一会儿，你有些放心不下，提议去看看朱丽叶。茂丘西奥似乎恢复了些精神，他决定和你一起去。")
            elif '朱丽叶结婚' in Tybalt['talk']:
                speak("你提议去看看朱丽叶，你对她总是放心不下。茂丘西奥点点头，打算和你一起去。")
            else:
                speak("你提议去看看朱丽叶，说不定你的愿望与她有关。茂丘西奥以“反正还有的是时间，比起来我还是更好奇你的愿望”为由，死活要跟着你。")
            place = visit_1(2)
        elif room_list[choice-1] == '去卡普莱家主的房间':
            if '罗密欧流放' in Tybalt['talk']:
                speak("你想去卡普莱家主那里看看，你对他做出让朱丽叶结婚的决定这件事十分生气。茂丘西奥似乎恢复了些精神，他决定和你一起去。")
            elif '朱丽叶结婚' in Tybalt['talk']:
                speak("过了一会儿，你说想去卡普莱家主那里看看。茂丘西奥想了想，决定和你一起去。")
            else:
                speak("你提议去卡普莱家主的房间看看，能不能找到和愿望相关的线索。茂丘西奥说要和你一起去。")
            place = visit_2(2)
        elif room_list[choice-1] == '去酒馆':
            if ('罗密欧流放' in Tybalt['talk'])or('罗密欧' in Tybalt['talk']):
                speak("你提议去一趟酒馆，看看能不能打听到什么新的消息。茂丘西奥似乎恢复了些精神，他决定和你一起去。")
            else:
                speak("你提议去一趟酒馆，看看能不能从那里打听到什么。茂丘西奥想了想，决定和你一起去。")
            place = visit_3(2)
        else:   #回自己的房间
            if ('罗密欧流放' in Tybalt['talk'])or('罗密欧' in Tybalt['talk']):
                speak("你想去自己的房间看看。茂丘西奥似乎恢复了些精神，他决定和你一起去。")
            else:
                speak("你想去自己的房间看看。茂丘西奥眼睛突然发亮，连连同意，并且死活都要跟你一起去，你只好答应。")
            place = visit_4(2)
    do()

set_enter = 0
speak("请选择您的阅读喜好：")
set_enter = choose(["停顿一会儿后播放下一小段","手动回车后播放下一小段"]) -1
wake()
visit()