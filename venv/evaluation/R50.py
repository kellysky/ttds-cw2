import sys
import p10
import p10

def recall(top_num,relevant_file,retrieved_file):
    retrieved_doc=[]
    for i in range(0,int(top_num)):
        if retrieved_file[i]:
            retrieved_doc.append(retrieved_file[i])
    common_doc=set(relevant_file).intersection(set(retrieved_doc))
    precision=len(common_doc)/len(relevant_file)
    return precision


def create_recallfile(topnum,term_startid,term_endid,
                      retrievedfile_path,retrievedfile_name,relevantfile_path,relevantfile_name):
    recall_list=[]
    for i in range(term_startid,term_endid+1):
        retrieved_doc=p10.retrieved_file(retrievedfile_path,retrievedfile_name,i)
        relevant_doc=p10.relevant_file(relevantfile_path,relevantfile_name,i)
        pre_value=recall(topnum,relevant_doc,retrieved_doc)
        recall_list.append(pre_value)
    #print(recall_list)
    return recall_list


