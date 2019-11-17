import sys
import p10
import math
import re
import MAP
import R50
import r_precision


#generate the graded score for relevant file
def graded_doc(path,filename,term_id):
    score={}
    with open(path + filename, 'r') as f:
        line = f.readline()
        while line:
            line = re.sub('[:]', ' ', line)
            line = line.split()
            if line[0] == str(term_id):
                for i in range(1, len(line)):
                    element = line[i]
                    element = re.sub('[( ) ,]', ' ', element)
                    element = element.split()
                    score[element[0]]=element[1]
            line = f.readline()
    return score

#caculate nDCG scores for all queries and write it into file
def nDCG(top_num,term_startid,term_endid,
       retrievedfile_path,retrievedfile_name,relevantfile_path,relevantfile_name):
    nDCG_list=[]
    iDCG_list=[]
    DCG_list=[]


    for i in range(term_startid,term_endid+1):
        retrieved_doc=p10.retrieved_file(retrievedfile_path,retrievedfile_name,i)
        relevant_doc=p10.relevant_file(relevantfile_path,relevantfile_name,i)
        relevant_grades=graded_doc(relevantfile_path,relevantfile_name,i)
        temp=0
        score=0
        idcg=0
        iDCG_list=[]
        for j in range(0,top_num):
            if retrieved_doc[j] in relevant_doc:
                score=float(relevant_grades[retrieved_doc[j]])
            else:
                score=0
            if j == 0:
                temp = float(temp) + float(score)
            else:
                temp = float(temp) + float(float(score)/math.log2(j + 1))
        DCG_list.append(temp)


        #find all the relevant score for idcg
        for i in range(len(relevant_doc)):
            iDCG_list.append(relevant_grades[relevant_doc[i]])
        iDCG_list=sorted(iDCG_list,reverse=True)
        for i in range(top_num-len(iDCG_list)):
            iDCG_list.append(0)

        #caculate the value of idcg
        for j in range(top_num):
            if j==0:
                idcg=float(idcg)+float(iDCG_list[j])
            else:
                idcg=float(idcg)+float(float(float(iDCG_list[j])/math.log2(j+1)))
        nDCG_list.append(idcg)

    #caculatet the value of ndcg
    for i in range(len(nDCG_list)):
        nDCG_list[i]=DCG_list[i]/nDCG_list[i]
    #print(nDCG_list)
    return nDCG_list


if __name__=="__main__":
    path='../systems/'
    path1='../evaluation_result/'
    filename='S6.eval'
    filename1='S6.results'
    filename2='qrels.txt'
    with open(path1+'ALL.eval','w') as f:
        f.write("\t" + "P@10" + "\t" + "R@50" + "\t" + "r-precision" + "\t" + "AP" + "\t" + "nDCG@10" + "\t" + "nDCG@20" + "\n")
        for i in range(1,7):
            with open(path1+'S'+str(i)+'.eval','r') as g:
                line=g.readline()
                content=''
                while line:
                    content=line
                    line=g.readline()
                content=content.split()
                f.write('S'+str(i)+'\t')
                for i in range(1,len(content)):
                    content[i]=content[i].strip()
                    f.write(content[i]+'\t')
                f.write('\n')
    p10_list=p10.create_precisionfile(10,1,10,path,filename1,path,filename2)
    r50_list=R50.create_recallfile(50,1,10,path,filename1,path,filename2)
    r_precision_lsit=r_precision.create_r_precisionfile(1,10,path,filename1,path,filename2)
    map_list=MAP.ap(1,10,path,filename1,path,filename2)
    nDCG10_list=nDCG(10,1,10,path,filename1,path,filename2)
    nDCG20_list=nDCG(20,1,10,path,filename1,path,filename2)

    with open(path1+filename,'w') as f:
        f.write("\t"+"P@10"+"\t"+"R@50"+"\t"+"r-precision"+"\t"+"AP"+"\t"+"nDCG@10"+"\t"+"nDCG@20"+"\n")
        p10=0
        r50=0
        r_precision=0
        map=0
        nDCG10=0
        nDCG20=0
        for i in range(0,10):
            p10=p10+p10_list[i]
            r50=r50+r50_list[i]
            r_precision=r_precision+r_precision_lsit[i]
            map=map+float(map_list[i])
            nDCG10=nDCG10+nDCG10_list[i]
            nDCG20=nDCG20+nDCG20_list[i]
            f.write(str(i+1)+"\t"+str(round(p10_list[i],3))+"\t"+str(round(r50_list[i],3))+"\t"+str(round(r_precision_lsit[i],3))+"\t"+
                    str(round(float(map_list[i]),3))+"\t"+str(round(nDCG10_list[i],3))+"\t"+str(round(nDCG20_list[i],3)))
            f.write('\n')
        p10=p10/10
        r50=r50/10
        r_precision=r_precision/10
        map=map/10
        nDCG10=nDCG10/10
        nDCG20=nDCG20/10
        f.write('mean'+"\t"+str(round(p10,3))+"\t"+str(round(r50,3))+"\t"
                +str(round(r_precision,3))+"\t"+str(round(map,3))+"\t"+str(round(nDCG10,3))+"\t"+str(round(nDCG20,3))+"\n")




