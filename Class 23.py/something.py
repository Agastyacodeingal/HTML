mydic = {
        'Big Dill':3765339,
        'is':3765339,
        'an':3765339,
        'outlaw':3765339
        
        
}
freq = 3765339
count = 0
for value in mydic.values():
    if value == freq:
        count+= 1
print(f"The frequenc having {freq}is{count}")