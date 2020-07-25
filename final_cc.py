import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
import re
URL = ['http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3187',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3192',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3188',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3189',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3202',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3206',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3219',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3220',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3222',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3224',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3445',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3449',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3014',
       
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3040',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2008',
      
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2522',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2008',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2516',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2292',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2289',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2250',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2224',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2178',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2185',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2192',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2132',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2133',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2130',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2129',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=2128',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6005',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6007',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6143',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6141',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6138',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6133',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6156',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6155',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6182',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6195',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6206',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6207',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6226',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6206',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6207',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6220',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6222',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6225',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6250',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6270',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6272',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6276',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6278',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6281',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6283',
    
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6302',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6307',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6310',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6318',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6323',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6325',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6405',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6430',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6454',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6437',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6476',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=6405',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=63040',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3154',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3142',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3183',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3188',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=3189',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5105',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5106',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5107',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5139',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5151',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5160',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5167',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5161',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5168',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5170',
       'http://www.dtemaharashtra.gov.in/frmInstituteSummary.aspx?InstituteCode=5171',
        ]
filename="dte_records.csv"
f= open(filename,"w")
headers ="Code,College_name,College_region,Address,Email_Address,Web_Address,Registrar_name,Personal_no,Office_no,Status,Autonomy_status"
f.write(headers)
for url in URL:
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    res=soup.find("table",{'class':'AppFormTable'})
    institute=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblInstituteCode"})
    c_institute=institute.text
    name=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblInstituteNameEnglish"})
    c_name=name.text.replace(',','')
    region=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblRegion"})
    c_region=region.text.replace(',','')
    address=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblAddressEnglish"})
    c_Address=address.text.replace(',','')
    email_address=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblEMailAddress"})
    c_email_Address=email_address.text
    web_address=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblWebAddress"})
    c_web_Address=web_address.text
    registrar_name=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish"})
    c_registrar_name=registrar_name.text
    personal_no=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblPersonalPhoneNo"})
    c_personal_no=personal_no.text
    office_no=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblOfficePhoneNo"})
    c_Office_no=office_no.text
    status=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblStatus1"})
    c_Status=status.text
    autonomy_status=res.find("span",{"id":"ctl00_ContentPlaceHolder1_lblStatus2"})
    c_Autonomy_status=autonomy_status.text
    #print(c_name+","+c_region+","+c_Address+","+c_email_Address+","+c_web_Address+","+c_Office_no+","+c_Status+","+c_Autonomy_status+"\n")
    f.write("\n"+c_institute+","+c_name+","+c_region+","+c_Address+","+c_email_Address+","+c_web_Address+","+c_registrar_name+","+c_personal_no+","+c_Office_no+","+c_Status+","+c_Autonomy_status+"\n")
    
    
f.close()

data=pd.read_csv('dte_records.csv' ,encoding='LATIN-1')
x=data['Autonomy_status'].iloc[0:100].values
y=data['College_region'].iloc[0:100].values
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title("Graph of colllege region VS Autonomy status")
plt.xlabel('Autonomy_status')
plt.ylabel('College Region')
ax.plot(x,y)
#Graph for college Region
a=data['College_region'].iloc[0:100].values
fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title("Graph of colllege region VS Autonomy status")
plt.xlabel('Colleges')
plt.ylabel('College Region')
ax.plot(a)


    
    



