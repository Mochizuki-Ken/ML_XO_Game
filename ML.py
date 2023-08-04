

import json
class ML:
    file_path="./ML_XO_Games_PY/data.json"
    def UPDATE_DATA(self,data):
        decoded_data=self.GET_DATA()
        decoded_data['record'].append(data)
        self.WRITE_DATA(decoded_data=decoded_data)


    def UPDATE_FIRST_STEP(self,step):
        decoded_data=self.GET_DATA()
        decoded_data['FirstStep'][step]=decoded_data['FirstStep'][step]+1
        self.WRITE_DATA(decoded_data=decoded_data)

    def GET_DATA(self):
        decoded_data=None
        with open(self.file_path,'r') as dataSet:
            decoded_data=json.loads(dataSet.read()) 
        return(decoded_data) 

    def WRITE_DATA(self,decoded_data):
        with open(self.file_path,'w') as dataSet:
            dataSet.write(json.dumps(decoded_data))

    def FIRSTSTEP(self):
        return self.GET_DATA()["FirstStep"].index(max(self.GET_DATA()["FirstStep"]))

    def NextStep(self,Previous_Step=[]):
        if len(Previous_Step)==0:
            return (self.FIRSTSTEP())
        else:
            data=self.GET_DATA()['record']
            nextStep=False
            for i in data:
                # print(list(zip(i,Previous_Step)))
                nextStep=i
                for j,k in zip(i,Previous_Step):
                    if j['pos']!=k['pos']:
                        nextStep=False
                        continue
                if nextStep!=False:
                    nextStep=i
                    break
            
            if (nextStep!=False and nextStep[len(Previous_Step)]['id']==0 ):
                try:
                    print("防禦")
                    return(nextStep[len(Previous_Step)+1]["pos"])
                except:
                    nextStep=False
            # if (nextStep!=False and nextStep[len(Previous_Step)]['id']==0 )or nextStep==False:
            #     nextStep=False
            #     for i in data:
            #         index=1
            #         for j in i:
            #             if Previous_Step[-1]['pos']==j['pos'] :
            #                 try:

            #                     if(i[index]["id"]==1):return(i[index]["pos"])
            #                     else:
            #                         nextStep=False
            #                 except:
            #                     nextStep=False

            #             index+=1

                    # for j,k in zip(i,Previous_Step):
                    #     if j['pos']==k['pos'] and i[len(Previous_Step)]['id']==1:
                    #         nextStep=i
                    #     else


            if nextStep==False:
                print('隨機')
                return("Random")
            
            # print('---1')
            print("進攻")
            # print(nextStep[len(Previous_Step)]['id'])
            return(nextStep[len(Previous_Step)]["pos"])
            
            
            


                
            



n=[{"pos":0,'id':1},{"pos":7,'id':0},{"pos":1,'id':1},{"pos":5,'id':0},{"pos":2,'id':1}]
    
    
ML=ML()
print(ML.NextStep([{"pos":0,'id':1},{"pos":7,'id':0}]))





# # Open the file in write mode
# file_path = "data.json"
# file = open(file_path, "w")
#  # Write content to the file
# file.write("Hello, World!\n")
# file.write("This is a sample text.")
#  # Close the file
# file.close()