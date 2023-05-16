import pandas as pd
import matplotlib.pyplot as plt

'''
This script pulls IP addresses from excel spreadsheet
Then sorts data based on IP Class
Then graphs number of IPs for each class
                                                Jodi
'''

def get_data(excelData):
    #listing spreadsheet headers
    fields = ['site names','Networks','Addresses']
    #pulling data from spreadsheet
    data = pd.read_excel(open('MOCK_DATA.xlsx', 'rb'))
    #storing 'Networks' column in variable
    excelData = (data.Networks)

   #returns data that will be graphed
    return excelData


def sortNGraph(sortData):
    classAarray = [1,2,3,4,5,7,8]
    classBarray = [9,10,11,12,13,14,15,16]
    classCarray = [17,18,19,20,21,22,23,24]

    clasA = []
    clasB = []
    clasC = []
    clasU = []


    for x in sortData:
        #Each line is checked to IP Class, and stored in appropriate array
        cidr = x.split('/',1)[1]
        if int(cidr) in classAarray:
            clasA.append(x)
        elif int(cidr) in classBarray:
            clasB.append(x)
        elif int(cidr) in classCarray:
            clasC.append(x)
        else:
            #If addr doesn't match A,B,or C class, thes IPs are stored in a seperate array as 'Unknown'
            clasU.append(x)

    #stores amount of each class in array for graph
    graphData = [len(clasA),len(clasB),len(clasC),len(clasU)]

    return graphData

def createGraph(graphData):
    #function creates graph
    fix,ax = plt.subplots()
    xAxis = ['Class A','Class B', 'Class C','Class U']
    bar_colors = ['tab:purple','tab:purple','tab:purple','tab:purple']

    ax.bar(xAxis,graphData,color=bar_colors)

    ax.set_ylabel("Number of IPs")
    ax.set_title('Site IPs')
    #ax.legend(title='Legend')

    #plt.savefig('foo.pdf')
    plt.show()



if __name__ == '__main__':
    networkList = ()
    #store IP with CIDRs in set
    networkList = set(get_data(networkList))

    #Send to function to sort IPs
    getGraphData = sortNGraph(networkList)

    #send to function to create graph
    createGraph(getGraphData)
