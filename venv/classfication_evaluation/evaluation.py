
def correct_result(test_file):
    correct=[]
    with open('../classfication_results/'+test_file,'r') as f:
        line=f.readline()
        while line:
            line=line.split()
            correct.append(line[0])
            line=f.readline()
    return  correct

def pre_result(pred_file):
    result = []
    with open('../predict_results/' + pred_file, 'r') as f:
        line = f.readline()
        while line:
            line = line.split()
            result.append(line[0])
            line = f.readline()
    return result



def count_Accurancy(test_file,pred_file):
    correct_result=[]
    real_result=0
    with open("../classfication_results/"+test_file,'r') as f:
        line=f.readline()
        while line:
            line=line.split()
            correct_result.append(line[0])
            line=f.readline()

    doc=0;
    with open("../predict_results/"+pred_file,'r') as f:
        line=f.readline()
        while line:
            line=line.split()
            if int(line[0])== int(correct_result[doc]):
                real_result=real_result+1
            doc=doc+1
            line=f.readline()

    return real_result/len(correct_result)


def count_Precision(test_file,pred_file,class_id):
    class_num=[]
    result=correct_result(test_file)
    class_count=0
    count=0
    doc=0;
    with open('../predict_results/'+pred_file,'r') as f:
        line=f.readline()
        while line:
            line=line.split()
            if int(line[0])==int(class_id):
                class_count=class_count+1
                if line[0] in result[doc]:
                    count=count+1
            doc=doc+1
            line=f.readline()

    return  count/class_count


def count_Recall(test_file,pred_file,class_id):
    result=correct_result(test_file)
    predict_result=pre_result(pred_file)

    class_count=0
    count=0
    for i in range(len(result)):
        if int(result[i])==int(class_id):
            class_count=class_count+1
            if int(result[i])==int(predict_result[i]):
                count=count+1


    return  count/class_count


def count_F1(test_file,pred_file,class_id):
    precision=count_Precision(test_file,pred_file,class_id)
    recall=count_Recall(test_file,pred_file,class_id)

    F1=(2*precision*recall)/(precision+recall)
    return F1

def count_macro_f1(test_file,pred_file):
    macro_f1=0
    for i in  range(1,15):
        macro_f1=macro_f1+count_F1(test_file,pred_file,i)
    return  macro_f1/14

if __name__=="__main__":
    #print(count_macro_f1('feats.test','pred.out'))
    test_file='feats.test4'
    pred_file='pred.out4'
    filename='Eval4.txt'
    with open('../classfication_evaluation_results/'+filename,'w') as f:
        f.write('Accurancy = '+str(round(count_Accurancy(test_file,pred_file),3))+'\n')
        f.write('Macro-F1 = '+str(round(count_macro_f1(test_file,pred_file),3))+"\n")
        for i in range(1,15):
            f.write(str(i)+': '+'P='+str(round(count_Precision(test_file,pred_file,i),3))+' '+'R='+str(round(count_Recall(test_file,pred_file,i),3))+' '+
                    "F="+str(round(count_F1(test_file,pred_file,i),3))+'\n')
