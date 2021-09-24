import json
import os

import Message1
import Message2
import pickle
import time
import savingMethods
import User

import telebot
from telebot import types



cccc = []
bot = telebot.TeleBot("token")
id = ""
text = ""

n=[]

piam=[]
replace={}
replace2={}
replace3={}
replace4={}
# this is a change
def read_message_newmsg(list,message):
    for i in list:
        print(i)
        if i['dataType'] == "text":
            if (i['replyId'] != ""):
                bot.send_message(message.chat.id, i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']),
                                 reply_to_message_id=i['replyId'])
                # bot.reply_to(Message1.find_by_text(message.chat.id,i['text']),i['message'],reply_markup=MessageKeyboaed1(i['id2']))
            else:
                bot.send_message(message.chat.id, i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
        elif i['dataType'] =="photo":
            file = bot.get_file(i['fileId'])
            if (i['replyId'] != ""):
                if (i['message'] == "" or i['message'] == None):
                    bot.send_photo(message.chat.id, i['fileId'], reply_to_message_id=i['replyId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_photo(message.chat.id, i['fileId'],
                                   reply_to_message_id=i['replyId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
            else:
                if (i['message'] == "" or i['message'] == None):
                    bot.send_photo(message.chat.id, i['fileId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_photo(message.chat.id, i['fileId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
        elif i['dataType'] == "animation":
            file = bot.get_file(i['fileId'])
            if (i['replyId'] != ""):
                if (i['message'] == "" or i['message'] == None):
                   bot.send_animation(message.chat.id, i['fileId'], reply_to_message_id=i['replyId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_animation(message.chat.id, i['fileId'],
                                   reply_to_message_id=i['replyId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
            else:
                bot.send_animation(message.chat.id, i['fileId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))

        elif i['dataType'] == "voice":
            file = bot.get_file(i['fileId'])
            if (i['replyId'] != ""):
                if (i['message'] == "" or i['message'] == None):
                   bot.send_voice(message.chat.id, i['fileId'], reply_to_message_id=i['replyId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_voice(message.chat.id, i['fileId'],
                                   reply_to_message_id=i['replyId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
            else:
                if (i['message'] == "" or i['message'] == None):
                    bot.send_voice(message.chat.id, i['fileId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_voice(message.chat.id, i['fileId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))

        elif i['dataType'] == "audio":
            file = bot.get_file(i['fileId'])
            if (i['replyId'] != ""):
                if (i['message'] == "" or i['message'] == None):
                   bot.send_audio(message.chat.id, i['fileId'], reply_to_message_id=i['replyId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_audio(message.chat.id, i['fileId'],
                                   reply_to_message_id=i['replyId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
            else:
                if (i['message'] == "" or i['message'] == None):
                    bot.send_audio(message.chat.id, i['fileId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_audio(message.chat.id, i['fileId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))


        elif i['dataType'] =="document":
            file = bot.get_file(i['fileId'])

            if (i['replyId'] != ""):
                if(i['message']=="" or i['message']==None ):
                    bot.send_document(message.chat.id, i['fileId'], reply_to_message_id=i['replyId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_document(message.chat.id, i['fileId'],
                                   reply_to_message_id=i['replyId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))

            else:
                if (i['message'] == "" or i['message'] == None):
                    bot.send_document(message.chat.id, i['fileId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_document(message.chat.id, i['fileId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))

        elif i['dataType'] == "sticker":
            print("ff")
            file = bot.get_file(i['fileId'])
            print(message)
            if (i['replyId'] != ""):

                bot.send_sticker(message.chat.id, i['fileId'], reply_to_message_id=i['replyId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
            else:
                bot.send_sticker(message.chat.id, i['fileId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))

        elif i['dataType'] == "video":
            print("jd")
            file = bot.get_file(i['fileId'])

            if (i['replyId'] != ""):
                if (i['message'] == "" or i['message'] == None):
                    bot.send_video(message.chat.id, i['fileId'], reply_to_message_id=i['replyId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_video(message.chat.id, i['fileId'],
                                   reply_to_message_id=i['replyId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
            else:
                print("this")
                if (i['message'] == "" or i['message'] == None):
                    bot.send_video(message.chat.id, i['fileId'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))
                else:
                    bot.send_video(message.chat.id, i['fileId'],caption=i['message'], reply_markup=MessageKeyboaed1(i['id2'], i['r2']))



    Message2.clearByid(message.chat.id)
def send_message_start(message):
    print(message)
    if message.content_type=="text":
        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], message.text, "", message.chat.id, "", "text", "",
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type=="photo":

        fileID = message.photo[-1].file_id
        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "photo",fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "animation":
        fileID = message.animation.file_id

        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], "", "", message.chat.id, "", "animation", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type== "voice":
        fileID = message.voice.file_id

        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "voice", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type=="audio":
        fileID = message.audio.file_id

        bot.send_message(replace4[str(message.chat.id)],"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "audio", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type=="document":
        fileID = message.document.file_id

        bot.send_message(replace4[str(message.chat.id)],"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "document", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type=="sticker":
        print(message)
        fileID = message.sticker.file_id
        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], "", "", message.chat.id, "", "sticker", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type=="video":
        fileID = message.video.file_id
        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        print("this=", message.id)
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "video", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")

def send_message_contact(message):

    if message.content_type=="text":
        Message2.addMessage(replace4[str(message.chat.id)], message.text, "", message.chat.id, "", "text", "", message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)],"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
    elif message.content_type=="photo":

        fileID = message.photo[-1].file_id
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "photo", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)],"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
    elif message.content_type == "animation":
        fileID = message.animation.file_id
        Message2.addMessage(replace4[str(message.chat.id)], "", "", message.chat.id, "", "animation", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
    elif message.content_type== "voice":
        fileID = message.voice.file_id
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "voice", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
    elif message.content_type=="audio":
        fileID = message.audio.file_id
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "audio", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
    elif message.content_type=="document":
        fileID = message.document.file_id
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "document", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)],"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
    elif message.content_type=="sticker":
        fileID = message.sticker.file_id
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "sticker", fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)],"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
    elif message.content_type == "video":
        fileID = message.video.file_id
        Message2.addMessage(replace4[str(message.chat.id)], message.caption, "", message.chat.id, "", "video",
                            fileID,
                            message.id)
        Message1.addMessage(message.chat.id, message)

        bot.send_message(replace4[str(message.chat.id)], "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        custom = keyboard()
        bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.", reply_markup=custom)
def send_message_reply(message):
    if message.content_type == "text":
        print("ddd")
        b = replace2[str(message.chat.id)].split(" ")
        print(b)
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s,"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.text, replace[str(message.chat.id)], message.chat.id, d, "text", "", message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "photo":

        fileID = message.photo[-1].file_id
        b = replace2[str(message.chat.id)].split(" ")
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s, "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.caption, replace[str(message.chat.id)], message.chat.id, d, "photo", fileID, message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "animation":
        fileID = message.animation.file_id
        b = replace2[str(message.chat.id)].split(" ")
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s, "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.caption, replace[str(message.chat.id)], message.chat.id, d, "animation", fileID, message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "voice":
        fileID = message.voice.file_id
        b = replace2[str(message.chat.id)].split(" ")
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s,"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.caption, replace[str(message.chat.id)], message.chat.id, d, "voice", fileID, message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "audio":
        fileID = message.audio.file_id
        b = replace2[str(message.chat.id)].split(" ")
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s, "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.caption, replace[str(message.chat.id)], message.chat.id, d, "audio", fileID, message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "document":
        fileID = message.document.file_id
        b = replace2[str(message.chat.id)].split(" ")
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s, "\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.caption, replace[str(message.chat.id)], message.chat.id, d, "document", fileID, message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "sticker":
        fileID = message.sticker.file_id
        b = replace2[str(message.chat.id)].split(" ")
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s,"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.caption, replace[str(message.chat.id)], message.chat.id, d, "sticker", fileID, message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    elif message.content_type == "video":
        fileID = message.video.file_id
        b = replace2[str(message.chat.id)].split(" ")
        s = b[0]
        d = b[1]
        print(s, " ", d)
        bot.send_message(s,"\nشما یک پیام مشاهده نشده دارید .\n " + "\n لطفا روی " +"/newmsg"+"  کلیک نمایید .")
        gt = Message2.loadMessageAccount()
        print("first ", gt)
        Message2.addMessage(s, message.caption, replace[str(message.chat.id)], message.chat.id, d, "video", fileID, message.id)
        gt = Message2.loadMessageAccount()
        print("search ", gt)
        # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد.")
    custom = keyboard()
    bot.send_message(message.chat.id,"پیام به مخاطب ارسال شد.", reply_markup=custom)
def check_Acounts(message):
    if (Message1.existMessageAccount(message.chat.id) == False):
        try:
            o = Message1.MessageAccount(message.chat.id, [])
            list = Message1.loadMessageAccount()
            list.append(o)
            Message1.saveMessageAccount(list)
        except:
            print("fedc")
    if (Message2.existMessageAccount(message.chat.id) == False):
        try:
            o = Message2.MessageAccount(message.chat.id, [])
            list = Message2.loadMessageAccount()
            list.append(o)
            Message2.saveMessageAccount(list)
        except:
            print("fedc")
# ----------------------help------------------------------

def processPhotoMessage(message):

    pass


# @bot.message_handler(content_types=['document'])
# def photo(message):
#     try:
#         print(message)
#
#         print(message.caption)
#         # print(message.content_type)
#         # print(message.caption)
#     except:
#         print(message)
#     # print(message)
#     # processPhotoMessage(message)
#     # bot.send_message()
@bot.message_handler(func=lambda m: m.text=='راهنمایی')
def help(message):
    franc=message
    bot.reply_to(message,"\nبا استفاده از این ربات می توانید به مخاطب مورد نظر خود به صورت ناشناس پیام بدهید.\n"+"\nهمچنین می توانید لینک ناشناس خود را از راه های گوناگون در اختیار دیگران قرار داده تا بتوانند به صورت ناشناس به شما پیام دهند.\n")



# ---------------------------------start----------------------------------------


def keyboard123():
    custom=types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('انصراف')


    # custom.row(a)
    custom.add(a)

    return custom


@bot.message_handler(commands=["start"])
def start(message):

    if (message.text == "/start"):

        if(savingMethods.exist_User(message.chat.id)):
            check_Acounts(message)
            newUser = User.User(message.chat.first_name, message.chat.last_name, message.chat.username, message.chat.id, [])

        else:

            newUser=User.User(message.chat.first_name,message.chat.last_name,message.chat.username,message.chat.id,[])

            savingMethods.Add_User(newUser)
            check_Acounts(message)

        custom = keyboard()
        bot.send_message(message.chat.id,"سلام  " +savingMethods.find_by_id(message.chat.id)+" عزیز\n"+"\nممنون از اینکه ربات مارو انتخاب کردی. \n"+"\nمیخوای برات چه کاری انجام بدم؟\n", reply_markup=custom)
    else:
        if (savingMethods.exist_User(message.chat.id)!=True):
            newUser = User.User(message.chat.first_name, message.chat.last_name, message.chat.username, message.chat.id,[])
            savingMethods.Add_User(newUser)
        check_Acounts(message)

        b = str(message.text).split(" ")
        targetId = b[1]
        custom = keyboard123()
        if (savingMethods.can_message(message.chat.id, str(targetId))):
            answer = bot.send_message(message.chat.id, " شما در حال پیام به " + savingMethods.find_by_id(
                str(targetId)) + " هستید پیام خود را وارد نمایید.\n" + "توجه داشته باشید که پیام شما به صورت کاملا ناشناس برای شخص ارسال می شود.",
                                      reply_markup=custom)
            replace4[str(message.chat.id)] = targetId

            cccc.append(targetId)
            bot.register_next_step_handler(answer, next_step3)
        else:
            answer = bot.reply_to(message, "مخاطب شما را بلاک کرده شما نمیتوانید به مخاطب پیام دهید .")





def next_step3(message):
    print("here3")
    try:
        if(message.text!="انصراف"):
            # # bot.send_message(replace3[str(message.chat.id)], message.text,reply_markup=MessageKeyboaed(message))
            # bot.send_message(replace4[str(message.chat.id)], "شما یک پیام مشاهده نشده دارید  " + "/newmsg")
            # print("this=",message.id)
            # Message2.addMessage(replace4[str(message.chat.id)],message.text,"",message.chat.id,"","text","",message.id)
            # Message1.addMessage(message.chat.id,message)
            # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد"  )
            send_message_start(message)
        else:

            custom = keyboard()
            bot.send_message(message.chat.id, "\nاوکی😊\n"+"\n\nچه کاری برات انجام بدم؟", reply_markup=custom)


    except:
        custom = keyboard()
        bot.send_message(message.chat.id, "نفهمیدم", reply_markup=custom)




# --------------------------------link-------------------------------------
@bot.message_handler(func=lambda m: m.text=="دریافت لینک ناشناس من")
def link(message):

    bot.reply_to(message,  "\n لینک ناشناس شما \n"+"http://t.me/AnonymousChatPersian_bot?start=" + str(message.chat.id)+"  \nمی باشد.\n  "+"\nشما میتوانید این لینک را برای دوستان و آشنایان خود ارسال کنید و یا آن را در صفحه اینستاگرام خود در قسمت وب سایت و یا در صفحه توییتر خود به اشتراک بگذارید.\n"+"\nدوستان شما از طریق این لینک می توانند به راحتی و یه صورت ناشناس پیام های خود را برای شما ارسال کنند.\n")
    with open("list_1.txt", "rb") as input_file:
         e = pickle.load(input_file)
    # with open('list_1.txt', 'wb') as fp:
    #     pickle.dump(message, fp)

# ------------------------contact---------------------------------------

#             ------------------------kkmmkds---------------------------
def MessageKeyboaed1(st,ft):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="reply", callback_data="1" + " " + str(st)+" "+str(ft))
    callback_button1 = types.InlineKeyboardButton(text="block", callback_data="2"+ " " + str(st)+" "+str(ft))

    keyboard.add(callback_button)
    keyboard.add(callback_button1)
    return keyboard


@bot.message_handler(commands=["newmsg"])
def find(message):
    check_Acounts(message)

    l=Message2.loadMessageAccount()
    list=Message2.st_by_id(message.chat.id)
    try:
        read_message_newmsg(list, message)
    except:
        print("error eccured in read_message_newmsg")
        Message2.clearByid(message.chat.id)
    # for i in list:
    #     if(i['text']!=""):
    #         bot.send_message(message.chat.id,i['message'],reply_markup=MessageKeyboaed1(i['id2'],i['r2']),reply_to_message_id=i['replyId'])
    #         # bot.reply_to(Message1.find_by_text(message.chat.id,i['text']),i['message'],reply_markup=MessageKeyboaed1(i['id2']))
    #     else:
    #         bot.send_message(message.chat.id,i['message'],reply_markup=MessageKeyboaed1(i['id2'],i['r2']))

    Message2.clearByid(message.chat.id)
@bot.message_handler(func=lambda m: m.text=="به مخاطب خاص وصلم کن")
def find(message):
    answer=bot.send_message(message.from_user.id, "\nبرای پیام دادن به مخاطب خاص به صورت زیر عمل کنید:\n"+"\n🔸اگر شخص مورد نظر دارای آی‌دی می‌باشد، آی‌دی شخص را ارسال کنید." +"\n🔹در غیر این صورت یکی از پیام های شخص را برای ربات فوروارد کنید.\n",reply_markup=keyboard123())

    bot.register_next_step_handler(answer, next_step5)
def next_step5(message):
    if message.text!="انصراف":
        if(message.text[0]=='@'):
            print("d")
            if(savingMethods.exist_User_by_username(message.text[1:])):
                print("c")

                replace4[str(message.chat.id)] = savingMethods.id_by_username(message.text[1:])
                print( replace4[str(message.chat.id)])
                custom = keyboard123()
                if (savingMethods.can_message(message.chat.id, replace4[str(message.chat.id)])):
                    answer = bot.send_message(message.from_user.id, "شما در حال پیام به " + savingMethods.find_by_id(
                        savingMethods.id_by_username(message.text[
                                                     1:])) + " هستید پیام خود را وارد نمایید.\n\n" + "توجه داشته باشید که پیام شما به صورت کاملا ناشناس برای شخص ارسال می شود.",
                                              reply_markup=custom)
                    bot.register_next_step_handler(answer, next_step6)
                else:
                    answer = bot.reply_to(message, "مخاطب شما را بلاک کرده شما نمیتوانید به مخاطب پیام دهید .")


            else:
                bot.send_message(message.chat.id, " کاربر عضو ربات نمیباشد!!")
        else:
            try:

                if(savingMethods.exist_User(message.forward_from.id)):

                    print("cd")
                    replace4[str(message.chat.id)] = message.forward_from.id
                    print("cd")
                    print(replace4[str(message.chat.id)])
                    print("cd")
                    custom=keyboard123()
                    if (savingMethods.can_message(message.chat.id, replace4[str(message.chat.id)])):
                        answer = bot.send_message(message.from_user.id,
                                                  "شما در حال پیام به " + savingMethods.find_by_id(
                                                      savingMethods.id_by_username(message.text[
                                                                                   1:])) + " هستید پیام خود را وارد نمایید.\n\n" + "توجه داشته باشید که پیام شما به صورت کاملا ناشناس برای شخص ارسال می شود.",
                                                  reply_markup=custom)
                        bot.register_next_step_handler(answer, next_step6)
                    else:
                        answer = bot.reply_to(message, "مخاطب شما را بلاک کرده شما نمیتوانید به مخاطب پیام دهید .")
                    # answer = bot.send_message(message.from_user.id, "شما در حال پیام به "+ savingMethods.find_by_id(message.forward_from.id )+ " هستید .پیام خود را وارد نمایید:")
                    # bot.register_next_step_handler(answer, next_step6)
                else:
                    bot.send_message(message.chat.id, "مخاطب مورد نظر در ربات عضو نمیباشد!!")
            except:
                bot.send_message(message.chat.id, "مجددا از ابتدا تلاش نمایید!!")
    else:
        custom = keyboard()
        bot.send_message(message.chat.id, "\nاوکی😊\n" + "\n\nچه کاری برات انجام بدم؟", reply_markup=custom)
def next_step6(message):

    if(message.text!="انصراف"):
        # # bot.send_message(replace4[str(message.chat.id)], message.text,reply_markup=MessageKeyboaed(message))
        # Message2.addMessage(replace4[str(message.chat.id)], message.text, "", message.chat.id, "", "text", "",message.id)
        # Message1.addMessage(message.chat.id,message)
        #
        # bot.send_message(replace4[str(message.chat.id)], "شما یک پیام مشاهده نشده دارید  " + "/newmsg")
        # custom = keyboard()
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد" ,reply_markup=custom)
        send_message_contact(message)
    else:
        custom = keyboard()
        bot.send_message(message.chat.id, "\nاوکی😊\n"+"\n\nچه کاری برات انجام بدم؟", reply_markup=custom)

# -------------------------------query-----------------------------------
@bot.callback_query_handler(func=lambda call:True)
def callback_data(call):
    if call.message:
        if call.data[0] == "1":
            print("kl")
            replace[str(call.message.chat.id)]=call.message.text
            replace2[str(call.message.chat.id)]=call.data[2:]
            piam.append(call.message.text)
            n.append(call.data[2:])
            b=call.data[2:].split(" ")
            a=b[0]
            print(a)
            if(savingMethods.can_message(call.message.chat.id,a)):
                print("yes")
                answer =bot.reply_to(call.message, "شما در حال پاسخ به این پیام هستید:",reply_markup=keyboard123())
                bot.register_next_step_handler(answer, next_step1)
            else:
                answer = bot.reply_to(call.message, "مخاطب شما را بلاک کرده شما نمیتوانید به مخاطب پیام دهید .")
        elif call.data[0] =="2":
            print("s")
            b=call.data[2:].split(" ")

            savingMethods.add_block_id(call.message.chat.id,b[0])
            # msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="TEXT" parse_mode='Markdown')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=call.message.text,
                                  reply_markup=MessageKeyboaed2(call.message,call.data[2:]))
        elif call.data[0] == "3":
            b = call.data[2:].split(" ")
            savingMethods.remove_block_id(call.message.chat.id, b[0])

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=call.message.text,
                                  reply_markup=MessageKeyboaed3(call.message,call.data[2:]))

@bot.message_handler(func=lambda m: m.text=="تست")
def find(message):
    answer = bot.send_message(message.from_user.id, "الان یه پیام متنی از اون شخص به این ربات فوروارد کن تا ببینم عضو هست یا نه!")
    bot.register_next_step_handler(answer, next_step8)



def next_step8(message):

    print(message.forward_from)

def next_step1(message):
    check_Acounts(message)

    print("here1")
    try:
        if(message.text!="انصراف"):
        # b=replace2[str(message.chat.id)].split(" ")
        # s=b[0]
        # d=b[1]
        # print(s," ",d)
        # bot.send_message(s, "شما یک پیام مشاهده نشده دارید  " + "/newmsg")
        # gt = Message2.loadMessageAccount()
        # print("first ",gt)
        # Message2.addMessage(s,message.text,replace[str(message.chat.id)],message.chat.id,d,"text","",message.id)
        # gt=Message2.loadMessageAccount()
        # print("search ",gt)
        # # f=bot.send_message(n[len(n)-1], message.text, reply_markup=MessageKeyboaed(message))
        # Message1.addMessage(message.chat.id, message)
        # bot.send_message(message.chat.id, "پیام به مخاطب ارسال شد")
            try:
                send_message_reply(message)
            except:
                print("d")
        else:
            custom = keyboard()
            bot.send_message(message.chat.id, "\nاوکی😊\n" + "\n\nچه کاری برات انجام بدم؟", reply_markup=custom)
    except:

        bot.send_message(message.chat.id, "نفهمیدم")

#---------------------------------FUNCTIONS-------------------------------
def keyboard():
    custom = types.ReplyKeyboardMarkup()
    a = types.KeyboardButton('راهنمایی')
    b = types.KeyboardButton('دریافت لینک ناشناس من')
    # c = types.KeyboardButton('تست')
    d = types.KeyboardButton('به مخاطب خاص وصلم کن')
    # custom.row(a)

    custom.add(b)
    # custom.add(c)
    custom.add(d)
    custom.add(a)
    return custom
def MessageKeyboaed(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="reply", callback_data="1"+" "+str(message.chat.id))
    callback_button1 = types.InlineKeyboardButton(text="block", callback_data="2"+" "+str(message.chat.id))
    keyboard.add(callback_button)
    keyboard.add(callback_button1)
    return keyboard
def MessageKeyboaed2(message,p):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="reply", callback_data="1" + " " + p)
    callback_button1 = types.InlineKeyboardButton(text="unblock", callback_data="3" + " " + p)
    keyboard.add(callback_button)
    keyboard.add(callback_button1)
    return keyboard
def MessageKeyboaed3(message,p):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="reply", callback_data="1"+" "+p)
    callback_button1 = types.InlineKeyboardButton(text="block", callback_data="2"+" "+p)
    keyboard.add(callback_button)
    keyboard.add(callback_button1)
    return keyboard
# -----------------------------POLLING--------------------------
while True:
    try:
        bot.polling()
    except:
        time.sleep(15)



