
def name_lenth_counter_function(name1):

  name = name1

  name_without_space_list = name.split()
  print(type(name_without_space_list))
  name_without_space = ""
  for m in name_without_space_list:
      name_without_space += m

  print(name_without_space)
  print(len(name_without_space))

function_data =  input(f"What is your name? : ")
name_lenth_counter_function(function_data)


