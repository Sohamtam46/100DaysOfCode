# --- list Comprehension ---
# new_list = [new_item for item in old_list]
# Conditional list comprehension -> [new_item for item in old_list if (cond)]
# Python Sequence : list - range - string - tuple
# --- Dict Comprehension ---
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}


student_info = {"Name":["Angela","Dave","Andy","Zack","Jake"],
                "Score":[22,25,28,34,33]}
import pandas as pd

student_info_ds = pd.DataFrame(student_info)

# loop through dataframe using pandas inbuilt function
for (index, data) in student_info_ds.iterrows():
    if data.Name == "Dave":
        print(data.Score)

