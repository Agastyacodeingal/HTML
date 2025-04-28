#duplicate no-no.

dic1 = {
        "id1" :
            {
              "Name":"Joy",
              "Class":"V",
              "subject":["Maths","Science,","English"]  
            },
        "id2" :
            {
              "Name":"Sigma",
              "Class":"VI",
              "subject":["Maths","Science,","English"]  
            },
         "id3" :
            {
              "Name":"Rizz",
              "Class":"VII",
              "subject":["Maths","Science,","English"]  
            },   
          "id4" :
            {
              "Name":"Joy",
              "Class":"V",
              "subject":["Maths","Science,","English"]  
            } 
}



result = {}
for key, values in dic1.items():
    if values not in result.values():
        result[key] = values
        
        
print(result)