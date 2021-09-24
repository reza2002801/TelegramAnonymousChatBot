import pickle
def MessageAccount(id,messages):
    dix={}
    dix["id"]=id
    dix["messages"]=messages
    return dix
def saveMessageAccount(list):
    try:
        with open('SendMessage.txt', 'wb') as fp:
            pickle.dump(list, fp)
    except:
        print("Error in save")
def loadMessageAccount():
    with open("SendMessage.txt", "rb") as input_file:
         e = pickle.load(input_file)
    return e
def addMessage(id,message,text,id2,replyId,dataType,fileId,r2):

    list=loadMessageAccount()

    for i in list:

        if str(i['id'])==str(id):

            dix={}
            dix['message']=message
            dix['text']=text
            dix['id2']=id2
            dix['replyId'] =replyId
            dix['dataType']=dataType
            dix['fileId']=fileId
            dix['r2']=r2
            i['messages'].append(dix)


    saveMessageAccount(list)
def existMessageAccount(id):

    l=loadMessageAccount()
    for i in l:
        if(i["id"]==id):
            return True

    return False
def st_by_id(id):
    list=loadMessageAccount()
    for i in list:
        if i['id']==id:
            return i['messages']

    return None
def clearByid(id):
    list = loadMessageAccount()
    for i in list:
        if i['id']==id:
            i['messages']=[]
    saveMessageAccount(list)
