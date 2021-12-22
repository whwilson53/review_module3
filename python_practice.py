voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson","registered_voters": 432438}]

for county_dict in voting_data:
   cnty_name = county_dict['county']
   cnty_votes = str(county_dict['registered_voters'])
   
   print(f" {cnty_name} county has {cnty_votes} registered voters")
        

