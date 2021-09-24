import pickle
def MessageAccount(id,messages):
    dix={}
    dix["id"]=id
    dix["messages"]=messages
    return dix
def saveMessageAccount(list):
    try:
        with open('OrdMessage.txt', 'wb') as fp:
            pickle.dump(list, fp)
    except:
        print("Error in save")
def loadMessageAccount():
    with open("OrdMessage.txt", "rb") as input_file:
         e = pickle.load(input_file)
    return e
def addMessage(id,message):
    list=loadMessageAccount()
    for i in list:
        if i['id']==id:
            i['messages'].append(message)
    saveMessageAccount(list)
def existMessageAccount(id):

    l=loadMessageAccount()
    for i in l:
        if(str(i["id"])==str(id)):
            return True

    return False
def find_by_text(id,text):
    list=loadMessageAccount()
    for i in list:
        if str(i['id'])==str(id):

            for j in i['messages']:

                if j.text==text:
                    return j
    return None






