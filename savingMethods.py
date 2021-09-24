import json
def  saveToJson(dic):
    with open('result.json', 'w') as fp:
        json.dump(dic, fp, indent=4)

def readFromJson():
    with open('result.json', 'r') as fp:
        stdr = json.load(fp)
    return stdr

def Add_User(p):

    dix=readFromJson()
    dix[str(len(dix))]=p

    # print(list)
    saveToJson(dix)
def find_by_id(id):

    dix=readFromJson()
    for i in range(len(dix)):

        if str(dix[str(i)]['number'])==str(id):

            return dix[str(i)]['firstName']+" "

    return "notFound"
def exist_User(id):
    try:
        dix=readFromJson()
        for i in range(len(dix)):
            print(str(dix[str(i)]['number']))
            print(id)
            if str(dix[str(i)]['number'])==str(id):
                print("ff")
                return True
        return False
    except:
        print("user not found")
        return False

def add_message_by_id(id,message,kind):
    dix=readFromJson()
    if(kind=="s"):
        for i in range(len(dix)):
            if dix[str(i)]['number']==id:
                dix[str(i)]['smessage'].append(message)
def exist_User_by_username(username):
    dix = readFromJson()
    for i in range(len(dix)):
        if dix[str(i)]['userName']==username:
            return True
    return False
def id_by_username(username):
    dix = readFromJson()
    for i in range(len(dix)):
        if dix[str(i)]['userName'] == username:
            return dix[str(i)]['number']
    return "notFound"
def add_block_id(id,id2):
    dix = readFromJson()
    for i in range(len(dix)):
        if dix[str(i)]['number'] == id:
            if(id2 not in dix[str(i)]['blockId']):
                dix[str(i)]['blockId'].append(id2)
    saveToJson(dix)
def remove_block_id(id,id2):
    dix = readFromJson()
    for i in range(len(dix)):
        if dix[str(i)]['number'] == id:
            if(str(id2)  in dix[str(i)]['blockId']):
                dix[str(i)]['blockId'].remove(str(id2))
    saveToJson(dix)
def can_message(id,id2):
    dix = readFromJson()
    for i in range(len(dix)):
        if str(dix[str(i)]['number']) == str(id2):
            if(str(id) in dix[str(i)]['blockId']):
                return False
    return True


