import requests
from bs4 import BeautifulSoup
import pprint
import re
import csv

def get_district_viewstate(url,post_data):
    req = requests.get(url)
    data = req.text

    bs = BeautifulSoup(data, "html.parser")
    values = bs.findAll("select", attrs={'name': 'drpDist_cd'})[0].findAll("option")
    districts = filter(None, [tag.attrs['value'] for tag in values])
    post_data['__VIEWSTATE'] = bs.find("input", {"id": "__VIEWSTATE"}).attrs['value']
    post_data['__EVENTVALIDATION'] = bs.find("input", {"id": "__EVENTVALIDATION"}).attrs['value']
    post_data['__VIEWSTATEGENERATOR'] = bs.find("input", {"id": "__VIEWSTATEGENERATOR"}).attrs['value']
    return districts


url = "http://bloodbanks.guj.nic.in/xln_blood_bank_dtls.aspx?ST=GJ"

post_data = {'__EVENTARGUMENT': '',
 '__EVENTTARGET': 'drpDist_cd',
 '__EVENTVALIDATION': '',
 '__LASTFOCUS': '',
 '__VIEWSTATE': '',
 '__VIEWSTATEENCRYPTED': '',
 '__VIEWSTATEGENERATOR': '4DF4E823',
 'ddlComp': 'ALL',
 'drpBloodGrp': 'ALL',
 'drpDist_cd': '',
 'hdStrMod': '',
 'hidU_Name': '',
 'hidflag': ''}

districts = get_district_viewstate(url,post_data)
address_pattern = r'(^.*Tip\(\'Address : )(.*)(\'\))'
data = []
for district in districts:
    post_data['drpDist_cd'] = district
    print "Getting data for district %s" % district
    req = requests.post(url,post_data)
    dist_data = BeautifulSoup(req.text, "html.parser")
    table = dist_data.find('table', id="dgbmw")
    if table:
        rows = table.findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            if cols[0] == "Dist":
                continue
            if int(cols[9]) > 0:
                temp_postdata = post_data
                temp_postdata['__EVENTTARGET'] = str(row.find('a')).split("'")[1]
                temp_postdata['__VIEWSTATE'] = dist_data.find("input", {"id": "__VIEWSTATE"}).attrs['value']
                temp_postdata['__EVENTVALIDATION'] = dist_data.find("input", {"id": "__EVENTVALIDATION"}).attrs['value']
                temp_postdata['__VIEWSTATEGENERATOR'] = dist_data.find("input", {"id": "__VIEWSTATEGENERATOR"}).attrs['value']
                temp_req = requests.post(url, temp_postdata)
                breakdown_data = BeautifulSoup(temp_req.text, "html.parser")
                #print breakdown_data
                b_table = breakdown_data.find('table', id="dgbags")
                b_row = b_table.find('tr', { "class" : "TransGridData" })
                b_td = b_row.findAll('td')
                text_td = [ele.text.strip() for ele in b_td]
                cols.extend(text_td)
                matches = re.match(address_pattern, str(row))
                if matches:
                    address = matches.group(2)
                    cols.append(address)
                #print [ele for ele in cols if ele]
                data.append([ele for ele in cols if ele])


csvfile = "data.txt"
# using | as delimter since data contains comma
data_delimiter = "|"
fileout = open(csvfile,'wb')
csvwriter = csv.writer(fileout, delimiter=data_delimiter)
for row in data:
    csvwriter.writerow(row)






