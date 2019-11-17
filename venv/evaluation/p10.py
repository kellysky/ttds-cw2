import re

#create a list of retrieved documents
def retrieved_file(path,filename,term_id):
    document_list=[]
    with open(path+filename,'r') as f:
        line = f.readline()
        while line:
            line=line.split()
            if line[0]==str(term_id):
                document_list.append(line[2])
            line=f.readline()
    return document_list

#create a list of relevant documents
def relevant_file(path,filename,term_id):
    document_list=[]
    with open(path+filename,'r') as f:
        line=f.readline()
        while line:
            line=re.sub('[:]',' ',line)
            line=line.split()
            if line[0]==str(term_id):
                for i in range(1,len(line)):
                    element = line[i]
                    element=re.sub('[( ) ,]',' ',element)
                    element=element.split()
                    document_list.append(element[0])
            line=f.readline()
    return document_list

#caculate the precision by using p@k
def precision(top_num,relevant_file,retrieved_file):
    retrieved_doc=[]
    for i in range(0,int(top_num)):
        if retrieved_file[i]:
            retrieved_doc.append(retrieved_file[i])
    common_doc=set(relevant_file).intersection(set(retrieved_doc))
    precision=len(common_doc)/len(retrieved_doc)
    return precision

#caculate precisions of all queries and write results into file
def create_precisionfile(top_num,term_startid,term_endid,
                retrievedfile_path,retrievedfile_name,relevantfile_path,relevantfile_name):
    precision_list=[]
    for i in range(term_startid,term_endid+1):
        retrieved_doc=retrieved_file(retrievedfile_path,retrievedfile_name,i)
        relevant_doc=relevant_file(relevantfile_path,relevantfile_name,i)
        pre_value=precision(top_num,relevant_doc,retrieved_doc)
        precision_list.append(pre_value) 
    #print(precision_list)
    return precision_list





