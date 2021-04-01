import logging
from storage import *

class FuncCallException(Exception):
    pass

call_stack = 0

def check_call_stack():
    global call_stack
    if call_stack < 1:
        logging.critical('Invalid function call!')
        raise FuncCallException
    call_stack -= 1

def check_number(request):
    if False in list(map(lambda x: x in nums, request[0])): 
        logging.critical('Something went wrong! Probably non-number character found in your request string!')



def check_kirill(request):
    error_list = cons + vowl
    if request[-1] not in error_list and request[-2] not in error_list:
        logging.critical('Something went wrong! Probably nsupported character found in your request string!')



def make_numb(request):
    check_call_stack()
    global call_stack
    call_stack += 1
    check_number(request)
    str_req = request[0]
    stack_num = []
    for i,j in zip( str_req[::-1], list(range(0,len(str_req))) ):
        if j == 0:
            stack_num.append('нөл' if len(str_req) < 2 and int(i) == 0 else numb_dict_list[0][int(i)])
        else:
            stack_num.append(numb_dict_list[j][int(i)])
    stack_num = list(filter(lambda a: a, stack_num[::-1]))
    str_req = ' '.join(stack_num)
    if 'миллиард' in str_req or 'миллион' in str_req and int(request[0][::-1][3:6]) == 0:
        str_req = str_req.replace(' миң','')
    if request[1][-1] == 's':
        pass
    return str_req
    
    

def make_plural(request):
    check_call_stack()
    global call_stack
    call_stack += 1
    check_kirill(request[0])
    plur_str = ''
    for i in plur_dict_list[0]:
        if request[0][-1] in i:
            plur_str += plur_dict_list[0][i]

    for i in plur_dict_list[1]:
        if request[0][-2 if request[0][-1] not in vowl else -1] in i:
            plur_str += plur_dict_list[1][i]
            
    return request[0] + plur_str

def make_case(request):
    check_call_stack()
    global call_stack
    call_stack += 1
    check_kirill(request[0])
    try:
        num_case = int(request[1][3])
        r_1_2 = request[0][-1] in vowl
        if request[0][-1] in 'гГ' and num_case == 2:
            request[0] = request[0][:-1] + 'к'
        need_sog = 'н' if r_1_2 and num_case == 1 else 'г' if request[0][-1] in z_cons + vowl and num_case == 2 else 'к' if request[0][-1] in g_cons and num_case == 2 else 'д' if request[0][-1] in z_cons + vowl else 'т' 
        check_let = request[0][-1] if r_1_2 else request[0][-2]
        for i in case_dict_list[num_case - 1]:
            if check_let in i:
                return request[0] + need_sog + case_dict_list[num_case - 1][i]
    except:
        logging.critical('Something went wrong! Check your request string!')



router = {
    'm-c' : make_case,
    'm-p' : make_plural,
    'm-n' : make_numb
}



def make_format(got_request, route):
    global call_stack
    call_stack += 1
    request = [got_request, route]
    try:
        return router[request[1][:3]](request)
    except:
        logging.critical('Something went wrong! Check your route or func call!')