# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()


# Метод для one hot encoding
def create_dummy_variables(origin_lst, origin_da_fr, col_name):
    new_list = sorted(set(origin_da_fr[col_name]))
    test_data = pd.DataFrame()
    itog_list = list()
    for name in new_list:
        for table_data in origin_lst:
            if name == table_data:
                itog_list.append('1')
            else:
                itog_list.append('0')
        test_data[name] = itog_list
        itog_list.clear()
    return test_data


data1 = create_dummy_variables(lst, data, 'whoAmI')
print(data1)
