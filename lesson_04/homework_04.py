adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#Task1
print("Task_1")
text_01 = adwentures_of_tom_sawer.replace("\n", " ")
print(text_01, "...")
print()

#Task2
print("Task_2")
text_02 = text_01.replace("....", " ")
print(text_02, "...")
print()

#Task3
print("Task_3")
text_03 = " ".join(text_02.split())
print(text_03, "...")
print()

#Task4
print("Task_4")
count_h = text_03.count("h")
print(count_h)
print()

#Task5
print("Task_5")
words = text_03.split()
count_capital = 0
for w in words:
    if w[0].isupper():
        count_capital += 1
print(count_capital)
print()

#Task6
print("Task_6")
first_index = text_03.find("Tom")
second_index = text_03.find("Tom", first_index + 1)
print(second_index)
print()

#Task7
print("Task_7")
adwentures_of_tom_sawer_sentences = text_03.split(". ")
print(adwentures_of_tom_sawer_sentences)
print()

#Task8
print("Task_8")
if len(adwentures_of_tom_sawer_sentences) >= 4:
    print(adwentures_of_tom_sawer_sentences[3].lower())
    print()

#Task9
print("Task_9")
starts_with = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        starts_with = True
print(starts_with)
print()

#Task10
print("Task_10")
last_sentence = adwentures_of_tom_sawer_sentences[-1]
last_sentence_word_count = len(last_sentence.split())
print(last_sentence_word_count)