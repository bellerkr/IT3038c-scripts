from cowinapi_by_ashaan import FetchData
cowin = FetchData()

#view in table format
table = cowin.get_states_table()
print(table)

#view in listed format
lists = cowin.get_states_list()
print(lists)

#view by districts
districts = cowin.get_districts_dict()
print(districts)
