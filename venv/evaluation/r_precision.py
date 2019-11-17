import sys
import p10
import p10

#caculate the precision for one query
def r_precision(relevant_file,retrieved_file):
    retrieved_doc=[]
    rank=len(relevant_file)
    for i in range(0,int(rank)):
        if retrieved_file[i]:
            retrieved_doc.append(retrieved_file[i])
    common_doc=set(relevant_file).intersection(set(retrieved_doc))
    precision=len(common_doc)/len(retrieved_doc)
    return precision

#caculate precisions for all queries and write results into file
def create_r_precisionfile(term_startid,term_endid,
                      retrievedfile_path,retrievedfile_name,relevantfile_path,relevantfile_name):
    recall_list=[]
    for i in range(term_startid,term_endid+1):
        retrieved_doc=p10.retrieved_file(retrievedfile_path,retrievedfile_name,i)
        relevant_doc=p10.relevant_file(relevantfile_path,relevantfile_name,i)
        pre_value=r_precision(relevant_doc,retrieved_doc)
        recall_list.append(pre_value)
    #print(recall_list)
    return recall_list


