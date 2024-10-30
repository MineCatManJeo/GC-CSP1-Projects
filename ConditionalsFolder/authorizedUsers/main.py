# Gabriel Crozier, Authorized users

def conditionals(name): # Function that checks for all types of users
    for values in users:
        if name in users[values]:
            if values != 'banned' and values != 'vip':
                print(f'Hello, {name}! You belong in the {values} category!') # basic print return
            elif values == 'vip':
                print(f'Hello our esteemed, {name}!!! Welcome to the VIP version!') # VIP print return
            else:
                print(f'Hello {name}..... You shouldn\'t be here BE GONE!') # Banned print return
            return True # Returns true so that I know that the user is in one of these catergories or not
users = {'admin':'GabeTheGamer', # DICTIONARIES ! ! ! ! ! ! !
         'user':['JogleWessel123','Minecrafter45','BookW0rm1','fdsgoivfdsl','UCASRules1243','XxWataDogDoinxX',
                 'GamerBoy1984','FireCat5853','HenrySm1th','MarshmallowCat666','IamaUser','JoenCena123',
                 'ISatOnMyFatCatCat1'],
         'vip':['ShadowWizardMoneyGang','DefNotGabesAltAccount','MoneyA1B3C4'],
         'banned':['JimmyNeutron34','MyFatCat12356']}

name = input('What is your username?: (Case sensitive)\n')
if not conditionals(name): # if the user is in one of the categories
    print(f'Hello {name}... You are not authorized!')