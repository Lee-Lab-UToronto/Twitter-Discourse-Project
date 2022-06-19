import csv
from fileinput import filename


def datacreater(filename,targetname,path,ftype):
    filen = path+filename+ftype
    csvfile = open(filen,'r',encoding='utf8')
    spamreader = csv.reader(csvfile, delimiter=',')
    targetflie = open(targetname,"a+",encoding='utf8')
    class_label = {'US_2018':0, 'US_2019':1}
    global index
    csvwriter = csv.writer(targetflie,delimiter=',')
    csvwriter.writerow(['sentence','label','idx'])
    for row in spamreader:
        text = row[1]
        text.replace(',',' ')
        # if len(text)>50:
        #     text = text[0:50]
        csvwriter = csv.writer(targetflie,delimiter=',')
        csvwriter.writerow([text,class_label[filename],index])
        index += 1
    

if __name__ == "__main__":
    year_list = ['2019','2018']
    region_list = ['US_']
    path_list = ['data-generation/data/CNY/']
    ftype = '.csv'
    index = 0
    for path in path_list:
        for region in region_list:
            for year in year_list:
                filen = region+year
                datacreater(filen,'./data-generation/data/modified/mydata.csv',path,ftype) #make the hottest words