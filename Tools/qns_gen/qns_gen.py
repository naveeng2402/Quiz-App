import json, sys

def read_round_json():
    with open('Json/data.json') as f:
        data = json.load(f)
    rounds_info = {}
    for i in data['Rounds'].keys():
        rounds_info[i] = rounds_info.get(i, data['Rounds'][i]['nos'])
    return rounds_info
    # print(rounds_info)

def create_dict_jsonnet(rounds_info):
    qns={}
    for i in rounds_info.keys():
        for j in range(rounds_info[i]):
            qns['_'.join(i.split(' '))+'_Q'+str(j+1)] = qns.get('_'.join(i.split(' '))+'_Q'+str(j+1),{"content": '''html_template[0]+"Your Text"+html_template[1]''',"options":[],"answer":"","explain":""})
    return qns

        
def create_file_jsonnet(qns):
    with open('Tools/qns_gen/test.jsonnet','w') as f:
        f.writelines(['local qns_size = 30;\n','''local html_template = ["<p style='text-align: center; font-size: "+qns_size+"px;'>","</p>"];\n'''])
        json.dump(qns, f, indent=4)
    with open('Tools/qns_gen/test.jsonnet') as f:
        text = f.readlines()
    for i in range(len(text)):
        if "content" in text[i]:
            text[i] = text[i].replace('"h', 'h')
            text[i] = text[i].replace(']"', ']')
            text[i] = text[i].replace('\\', '')
    with open('Tools/qns_gen/test.jsonnet','w') as f:
        f.writelines(text)
        
def create_dict_json(round_info:dict):
    qns_size = sys.argv[2]
    with open('Tools/qns_gen/data.txt') as f: data = f.readlines()
    qns = {}
    line = 0
    for i in round_info.keys():
        for j in range(round_info[i]):
            qns['_'.join(i.split(' '))+'_Q'+str(j+1)] = qns.get('_'.join(i.split(' '))+'_Q'+str(j+1),{"content": f'''<p style='text-align: center; font-size: {qns_size}px;'>{data[line].strip()}</p>''',"options":[],"answer":"","explain":""})
            line += 1
    return qns
            

def create_file_json(qns):
    with open('Tools/qns_gen/qns.json','w') as f:
        json.dump(qns,f,indent=4)




def main(jsonnet = True):
    
    rounds_info = read_round_json()
    if jsonnet == True: 
        qns = create_dict_jsonnet(rounds_info)
        create_file_jsonnet(qns)
        
    else:
        qns = create_dict_json(rounds_info)
        create_file_json(qns)
    
if __name__ == '__main__':
    
    run = False
    
    if len(sys.argv) == 1 or len(sys.argv) == 3:
        run = True
    
    if run != True:
        print('Invalid Execution...')
        sys.exit()
        
    try :
        main(sys.argv[1])
    except: main()
