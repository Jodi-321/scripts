import pandas as pd
import matplotlib.pyplot as plt
import jinja2


'''
This script pulls specific data form Excel
THis data is used to populate base HTML template
New HTML is generated with updated values

                                        Jodi
'''


def pullData():

    excelVars = 'incidents.xlsx'
    column_subset = ["Severity","Source","Policies","Channel","Destination","Action"]
    severityCol = pd.read_excel(excelVars,usecols=['Severity'])#'Source','Policies','Channel','Destination','Severity'])
    sourceCol = pd.read_excel(excelVars, usecols=['Source'])
    policiesCol = pd.read_excel(excelVars, usecols=['Policies'])
    channelCol = pd.read_excel(excelVars, usecols=['Channel'])
    destinationCol = pd.read_excel(excelVars, usecols=['Destination'])
    actionCol = pd.read_excel(excelVars,usecols=["Action"])

    final_des = [destinationCol.Destination.value_counts()]
    final_severity = [severityCol.Severity.value_counts(),severityCol.value_counts().tolist()]
    final_channel = [channelCol.Channel.value_counts()]
    final_source = [sourceCol.Source.value_counts()]
    final_policies = [policiesCol.Policies.value_counts().tolist()]
    final_action = [actionCol.Action.value_counts().tolist()]


    medInc = final_severity[1][0]
    highInc = final_severity[1][2]
    permitActionCount = final_action[0][0]
    inDataStor = [medInc,highInc,permitActionCount]
    return(inDataStor)

'''
    with pd.option_context('display.max_rows',None,
                           'display.max_columns',None,
                           'display.precision',3,
                           ):
'''

        #print(final_des)


def createIncGraph(dataStor):
    #Storing graph data from list
    medIncidents = dataStor[0]
    highIncidents = dataStor[1]

    #create Bar graph
    fix,ax = plt.subplots()
    IncidentSeverity = ['High','Medium']
    finalData = [int(highIncidents),int(medIncidents)]
    bar_labels = ['High','Medium']
    bar_colors = ['tab:red','tab:orange']

    #fill Bar graph with specific data
    ax.bar(IncidentSeverity,finalData,label=bar_labels, color=bar_colors)
    ax.set_ylabel('Incidents')
    ax.set_title('Incident Count')

    #save graph as png
    plt.savefig('test.png')

def createReport(dataStor):
    createIncGraph(dataStor)

    #storing variable values for HTML template
    hightIncidents = dataStor[1]
    medIncidents = dataStor[0]
    IncGraph = 'test.png'
    permitAction = dataStor[2]
    blockedAction = 0

    #dictionary of values to apply to template
    context = {'hightIncidents':hightIncidents,'medIncidents':medIncidents,'IncGraphLoc':IncGraph,'permitInc':permitAction,'blockedInc':blockedAction}


    #loads jinja2 template
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    #configures jinja2 template to point to specific HTML
    template = template_env.get_template('baseTemplate.html')

    #appliest context dictionary to HTML template
    output_text = template.render(context)

    #saves filled out template as another HTML to preserve base HTML template
    html_path = 'simpleReport2.html'
    html_file = open(html_path,'w')
    html_file.write(output_text)
    html_file.close()

def main():
    #function pulls data from Excel
    dataStor = pullData()

    #function creates report from set template
    createReport(dataStor)


if __name__ == "__main__":
    main()