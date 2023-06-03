import pandas as pd
import matplotlib.pyplot as plt
import jinja2
import time

'''
This script pulls IP addresses from excel spreadsheet
Then sorts data based on IP Class
Then graphs number of IPs for each class
                                                Jodi
'''

def getTime():
    current_time = time.ctime()
    return current_time

def get_data():#excelData):
    pulledData = []
    path = 'data/MOCK_DATA.xlsx'
    #listing spreadsheet headers
    fields = ['site names','Networks','Addresses']
    #pulling data from spreadsheet
    data = pd.read_excel(open(path, 'rb'))
    #storing 'Networks' column in variable
    excelNetworksData = (data.Networks)


    pulledData.append(excelNetworksData)
    return pulledData
   #returns data that will be graphed
    #return excelNetworksData


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
    #plt.show()
    imgPath = 'data/graph.png'
    plt.savefig(imgPath)

def createReport(dataStore,genTime):
    print(dataStore)

    classA = dataStore[0]
    classB = dataStore[1]
    classC = dataStore[2]
    classU = dataStore[3]
    DateTime = genTime
    graphPng = 'graph.png'
    companyLogo = 'companyLogo.jpg'

    htmlVars = {'CompanyLogo':companyLogo,'graphImg':graphPng,'DateTime':DateTime,'classA':classA,'classB':classB,'classC':classC,'classU':classU}

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template_path = 'data/simpleTemplate.html'
    template = template_env.get_template(template_path)

    output_text = template.render(htmlVars)

    html_path = 'data/simpleReport.html'#'simpleReport.html'
    html_file = open(html_path,'w')
    html_file.write(output_text)
    html_file.close()

def main():
    genTime = getTime()
    dataArray = [get_data(),genTime]
    #print(dataArray[1])
    networkList = set(dataArray[0][0])
    #print(networkList)
    # store IP with CIDRs in set
    #networkList = set(get_data(networkList))
    #print(networkList)

    # Send to function to sort IPs
    getGraphData = sortNGraph(networkList)


    # send to function to create graph
    createGraph(getGraphData)

    createReport(getGraphData,dataArray[1])

if __name__ == '__main__':
    main()
