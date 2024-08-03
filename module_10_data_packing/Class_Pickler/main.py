
from module_10_data_packing.data_packing_difficult._02_difficult import LinkedList
from module_10_data_packing.Class_Pickler._03_Pickler import MyPickler, MyUnPickler

my_pickler_5 = MyPickler(protocol=5)
my_pickler_4 = MyPickler(protocol=4)

box_list = LinkedList()
box_list.insert_at_head("Снежок_1")
box_list.insert_at_head("Мурзик_0")
box_list.insert_at_tail("Персик_2")

box_list = my_pickler_5.pickle_data(box_list)
box_list = MyUnPickler.unpickle_data(box_list)
box_list.print_ll_from_head()
print()
my_pickler_5.pickle_file(box_list, 'll_pickle.cats')
box_list = MyUnPickler.unpickle_file('ll_pickle.cats')
box_list.print_ll_from_head()

