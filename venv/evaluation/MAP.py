import sys
import p10

def ap(term_startid,term_endid,
       retrievedfile_path,retrievedfile_name,relevantfile_path,relevantfile_name):
    ap_list=[]
    for i in range(term_startid,term_endid+1):
        retrieved_doc=p10.retrieved_file(retrievedfile_path,retrievedfile_name,i)
        relevant_doc=p10.relevant_file(relevantfile_path,relevantfile_name,i)
        num=0
        temp=0
        pre_value=0
        for j in range(0,len(retrieved_doc)):
            if retrieved_doc[j] in relevant_doc:
                num=num+1
                temp_value=num/(j+1)
                temp=temp+temp_value
        if num>0:
            pre_value=temp/len(relevant_doc)
            ap_list.append(pre_value)
        else: ap_list.append('0')
    #print(ap_list)
    return ap_list


