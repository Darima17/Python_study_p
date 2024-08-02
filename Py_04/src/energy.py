from itertools import zip_longest

def fix_wiring(cables, sockets, plugs):
    filtered_pl = list(filter(lambda obj: type(obj) == str, plugs))
    filtered_sk = list(filter(lambda obj: type(obj) == str, sockets))
    filtered_cb = list(filter(lambda obj: type(obj) == str, cables))   
    full_list =list(zip_longest(filtered_pl, filtered_sk, filtered_cb))   
    result1 = list(filter(lambda obj: obj[1] != None and obj[2] != None, full_list))
    result2 = (map(lambda x: f'plug {x[2]} into {x[1]} using {x[0]}' if x[0] != None else f'weld {x[2]} to {x[1]} without plug', result1))
    return result2

if __name__ == "__main__": 
    ## test1
    print('test 1')
    plugs_1 = ['plug1', 'plug2', 'plug3']
    sockets_1 = [0,'socket1', 'socket2', 'socket3', 'socket4']
    cables_1 = ['cable1', 'cable2', 'cable3', 'cable4']
    for c in fix_wiring(cables_1, sockets_1, plugs_1):
        print(c)

    ## test2
    print('test 2')
    plugs_2 = ['plugZ', None, 'plugY', 'plugX']
    sockets_2 = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables_2 = ['cable2', 'cable1', False]
    for c in fix_wiring(cables_2, sockets_2, plugs_2):
        print(c)


