import numpy as np
# import gviz_api

def get_total_num_rows():
    csvfile = open(dataset_name, 'rb')
    return sum(1 for line in csv.reader(csvfile))

def get_bitcoint_rows(csv_reader, numrows, elements=None):
    ret = np.zeros((numrows, len(csv_reader.fieldnames)))
    r = None
    # try:
    for i in range(numrows):
        t = csv_reader.__next__()
        r = t
        ret[i,:] = np.fromiter(iter(r.values()), dtype=float)
    # except ValueError:
    ret = ret[:i,:]
    # finally:
    if(r):
        return r.keys(), ret
    else:
        return [], ret
# def create_gplot(keys, data, filename="graph1.json"):
#     data_table_description = [
#         (keys[0], "number"),
#         (keys[1], "number")]
#     data_table = gviz_api.DataTable(data_table_description)    
#     data_table.LoadData(data)
#     json_str = data_table.ToJSon(columns_order=(keys[0], keys[1]), order_by=keys[1])
#     with open(filename,"w") as f:
#         f.write(json_str)