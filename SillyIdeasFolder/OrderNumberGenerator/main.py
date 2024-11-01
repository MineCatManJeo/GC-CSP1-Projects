def silly(ordi): # I want a order number thing generator and i need to use four, fif, six and so on because fifty and fourty also when it is 1,2,3 change it to use first second type stuff cause it always different
    order = input('Give num: ')
    try: order = int(order) - 1
    except: return 'NaN'
    mod = order % 10
    otherMod = order // 10
    if mod == 0:
        end = 'st'
    elif mod == 1:
        end = 'nd'
    elif mod == 2:
        end = 'rd'
    else:
        end = 'th'
    return str(ordi[mod])+end


    
ordin = ['fir','seco','thi','four','fif','six','seven','eigh','nin', 'ten', 'eleven', 'twelf','twenty','thirty','fourty']
print(silly(ordin))