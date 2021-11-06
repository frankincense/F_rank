

ABC_country = [
    {
        "Id"        :   "011A",
        "FirstName" :   "Gavin",
        "LastName"  :   "Goved",
        "Age"       :   56,    
        "Hobbies"   :   ["Singing", "Comedy", "Rap"],
        "Spouse"    :   "Shade",
        "Reigned"   :   2000 #[2000, 2001, 2002, 2003, 2004, 2005]
    },

    {
        "Id"        :   "020Z",
        "FirstName" :   "Aminat",
        "LastName"  :   "Mustapha",
        "Age"       :   44,    
        "Hobbies"   :   ["Swimming", "Cycling"],
        "Spouse"    :   "Mustapha",
        "Reigned"   :   2005 #[2005, 2006, 2007, 2008, 2009, 2010]
    },

    {
        "Id"        :   "222F",
        "FirstName" :   "Adeleke",
        "LastName"  :   "Bright",
        "Age"       :   67,    
        "Hobbies"   :   ["Coding", "Cooking", "Sleeping"],
        "Spouse"    :   "Jiri Jiri",
        "Reigned"   :   2011 #[2011, 2012, 2013, 2014, 2015]
    },

    {
        "Id"        :   "876V",
        "FirstName" :   "Bigjara",
        "LastName"  :   "Bonenus",
        "Age"       :   35,    
        "Hobbies"   :   ["Coding", "Teaching", "Talking", "Singing"],
        "Spouse"    :   "Fine Jara",
        "Reigned"   :   2015 #[2015, 2016, 2017, 2018, 2019, 2020]
    }
    
]
print("hello")

print (" Question 1 ")
for k in ABC_country:
    for key in k:
        if k[key] == 2015:
            print("The staff that was elected in the year 2015 was", k["FirstName"], "\nwith ID", k["Id"])


print ("  Question 2  ")
lst=[]
for k in ABC_country:
    y = (len(k["Hobbies"]))
    lst.append(y)
print("The leader with the highest hobbies is", lst)

x = max(lst)
print("The MAX is", x)


if (lst.index(0) == x):
    print("The leader with the highest hobbies is Gavin Goved")
elif (lst.index(1) == x):
    print("The leader with the highest hobbies is Aminat Mustapha")
elif (lst.index(2) == x):
    print("The leader with the highest hobbies is Adeleke Bright")
else:
    print("The leader with the highest hobbies is Bigjara Bonenus")
