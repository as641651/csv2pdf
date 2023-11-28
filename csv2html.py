import csv

with open('generated_csv.csv', encoding="utf8", errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    
    #csv_writer = csv.writer(csv_w)

    line_count = 1
    data = []
    total = []
    for row in csv_reader:
        if row[0] == "":
            continue
        #print(row)
        content = "<strong>" + row[0].strip() + '<br>' + row[1].strip() + '<br>' + row[2] + " - " + row[3] + '<br></strong>'
        data.append(content)
        if line_count%3 == 0: 
          #csv_writer.writerow(data)
          total.append(data)
          data = []
        line_count += 1

    if data:
   #        csv_writer.writerow(data)
       total.append(data)  

    #print('Processed {line_count} lines.')
    #csv_w.close()


html_pretext = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">\n\n"
html_pretext += "<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\"/>\n\n"

html_pretext += "<title></title><meta name=\"generator\" content=\"LibreOffice 6.0.7.3 (Linux)\"/><meta name=\"created\" content=\"00:00:00\"/><meta name=\"changed\" content=\"2019-06-15T22:52:04.211853858\"/>\n\n"

#html_pretext += "<link href=\"https://fonts.googleapis.com/css?family=Archivo+Black&display=swap\" rel=\"stylesheet\">\n"
#html_pretext += "<link href=\"https://fonts.googleapis.com/css?family=Francois+One&display=swap\" rel=\"stylesheet\">\n"
html_pretext += "<link href=\"https://fonts.googleapis.com/css?family=Roboto:900&display=swap\" rel=\"stylesheet\">\n"

html_pretext+= "<style type=\"text/css\">body,div,table,thead,tbody,tfoot,tr,th,td,p { font-family:'Roboto', sans-serif; }a.comment-indicator:hover + comment { background:#ffd; position:absolute; display:block; border:1px solid black; padding:0.5em;  } a.comment-indicator { background:red; display:inline-block; border:1px solid black; width:0.5em; height:0.5em;  } comment { display:none;  }\n\n"
html_pretext+= "table{ page-break-inside:auto } tr{ page-break-inside:avoid; page-break-after:auto } </style>\n\n"

html_pretext+= "</head><body><table cellspacing=\"0\" border=\"0\"><colgroup span=\"3\" width=\"396\"></colgroup>"



html_posttext = "</table><!-- ************************************************************************** --></body></html>"


html_contents=""
#pgb_count = 0

for x in total:
    html_contents += "<tr>\n"
    for y in x:
        html_contents += "<td style=\"padding-left: 20px; padding-right: 5px;  border-top: 1px solid #000000; border-bottom: 1px solid #000000; border-left: 1px solid #000000; border-right: 1px solid #000000\" height=\"160\" align=\"left\" valign=middle><font size=4.5>{}</font></td>\n".format(y)

    html_contents += "</tr>\n"

    #if pgb_count == 6:
    #    html_contents += "<div class=\"pagebreak\"></div>\n\n\n"
    #    pgb_count = 0

    #pgb_count+=1


final = html_pretext + html_contents + html_posttext


csv_w = open('write_h.html','w')
csv_w.write(final)
csv_w.close()
