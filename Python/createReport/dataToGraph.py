import pandas as pd
import matplotlib.pyplot as plt
import jinja2
import time
import random

'''
This script pulls IP addresses from excel spreadsheet(FAKE DATA)
Then sorts data based on IP Class
Then graphs number of IPs for each class
five sites are picked at random each time the report is ran
the details ofr hte sites display in a table in the generated report

                                                Jodi
'''

#pull time report is generated
def getTime():
    current_time = time.ctime()
    return current_time

#pulls data stored in Excel spreadsheet for report
def get_data(dataStor):#excelData):
    pulledData = []
    path = 'data/MOCK_DATA.xlsx'

    #listing spreadsheet headers
    fields = ['site names','Networks','Addresses']

    #pulling data from spreadsheet
    data = pd.read_excel(open(path, 'rb'))

    #storing excel columns in variable
    excelNetworksData = (data.Networks)
    excelSiteNamesData = (data.SiteNames)
    excelAddrData = (data.Addresses)

    #appending excel data to data array
    pulledData.append(excelNetworksData)
    pulledData.append(excelSiteNamesData)
    pulledData.append(excelAddrData)

    # returns data that will be graphed
    return pulledData

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

    #plt.show()
    imgPath = 'data/graph.png'
    plt.savefig(imgPath)

def createReport(dataStore,genTime,pickedSites):
    classA = dataStore[0]
    classB = dataStore[1]
    classC = dataStore[2]
    classU = dataStore[3]
    DateTime = genTime
    graphPng = 'graph.png'
    companyLogo = 'companyLogo.jpg'

    #print(pickedSites[1])
    siteNumOne = pickedSites[1]
    siteNumTwo = pickedSites[2]
    siteNumThree = pickedSites[3]
    siteNumFour = pickedSites[4]
    siteNumFive = pickedSites[5]

    #Storing values in html tags
    htmlVars = {
                'CompanyLogo':companyLogo,'graphImg':graphPng,'DateTime':DateTime,
                'classA':classA,'classB':classB,'classC':classC,'classU':classU,
                'siteNumOne':siteNumOne[3],'siteNameOne':siteNumOne[0],'siteNetworkOne':siteNumOne[1],'siteAddrOne':siteNumOne[2],
                'siteNumTwo':siteNumTwo[3],'siteNameTwo':siteNumTwo[0],'siteNetworkTwo':siteNumTwo[1],'siteAddrTwo':siteNumTwo[2],
                'siteNumThree':siteNumThree[3],'siteNameThree':siteNumThree[0],'siteNetworkThree':siteNumThree[1],'siteAddrThree':siteNumThree[2],
                'siteNumFour':siteNumFour[3],'siteNameFour':siteNumFour[0],'siteNetworkFour':siteNumFour[1],'siteAddrFour':siteNumFour[2],
                'siteNumFive':siteNumFive[3],'siteNameFive':siteNumFive[0],'siteNetworkFive':siteNumFive[1],'siteAddrFive':siteNumFive[2],
                }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template_path = 'data/simpleTemplate.html'
    template = template_env.get_template(template_path)

    output_text = template.render(htmlVars)

    html_path = 'data/simpleReport.html'
    html_file = open(html_path,'w')
    html_file.write(output_text)
    html_file.close()

def sitePicker(dataStor,allExcelData):

    count = 0
    siteNames = list(allExcelData[1])
    topFive = list(random.sample(dataStor,5))
    finalSiteDict = {}

    #print(topFive)
    for x in siteNames:#topFive:

        if x in topFive:
            addPad = siteNames.index(x)
            xSiteName = allExcelData[1][addPad]
            xNetwork = allExcelData[0][addPad]
            xAddress = allExcelData[2][addPad]
            xSiteNum = addPad +2

            topFiveDetails = (xSiteName,xNetwork,xAddress,xSiteNum)

            count += 1
            finalSiteDict.update({count:topFiveDetails})

    return(finalSiteDict)

def main():
    genTime = getTime()
    dataArray = []
    dataArray.append(get_data(dataArray))

    dataArray = [dataArray, genTime]

    siteList = list(dataArray[0][0][1])
    pickedSites = sitePicker(siteList,dataArray[0][0])

    #store IP with CIDRs in set
    networkList = set(dataArray[0][0][0])

    #Send to function to sort IPs
    getGraphData = sortNGraph(networkList)

    #send to function to create graph
    createGraph(getGraphData)

    dataArray.append(pickedSites)

    #create report with graphdata, and current time being sent to function
    createReport(getGraphData,dataArray[1],dataArray[2])

if __name__ == '__main__':
    main()
    print("Script Complete!")
