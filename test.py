import os

import Message1
import Message2

l=[]
l=Message1.loadMessageAccount()
print(l)



# @bot.message_handler(commands=["contact"])
# def searching(search):
#     answer = bot.send_message(search.from_user.id, "لینک مخاطب خود را وارد نمایید:")
#     bot.register_next_step_handler(answer, searchanswer)
#
#
#
# def searchanswer(search):
#     answer = search.text
#     custom = keyboard123()
#     answer1 = bot.send_message(search.from_user.id,"پیام خود را وارد نمایید:" ,reply_markup=custom)
#     text = answer
#     t = str(text).replace("http://t.me/AnonymousChatPersian_bot?start=", "")
#     replace4[str(search.chat.id)]=t
#     cccc.append(t)
#     a = True
#     bot.register_next_step_handler(answer1, next_step4)
#
#
# def next_step4(message):
#     try:
#         if(message.text!="/cancel"):
#             # bot.send_message(replace4[str(message.chat.id)], message.text,reply_markup=MessageKeyboaed(message))
#             Message2.addMessage(replace4[str(message.chat.id)], message.text, "", message.chat.id)
#             Message1.addMessage(message.chat.id,message)
#             bot.send_message(replace4[str(message.chat.id)], "شما یک پیام مشاهده نشده دارید  " + "/newmsg")
#             custom = keyboard()
#             bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد" ,reply_markup=custom)
#         else:
#             custom = keyboard()
#             bot.send_message(message.chat.id, "/cancel", reply_markup=custom)
#
#
#
#     except:
#
#         bot.send_message(message.chat.id, "نفهمیدم")
#         custom = keyboard()
#         bot.send_message(message.chat.id, "/cancel", reply_markup=custom)
#




