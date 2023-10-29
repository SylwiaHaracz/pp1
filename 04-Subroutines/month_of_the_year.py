def month (n):
    if n == 1: 
        return "styczen"
    if n == 2: 
        return "luty"
    if n == 3: 
        return "marzec"
    if n == 4: 
        return "kwiecien"
    if n == 5: 
        return "maj"
    if n == 6: 
        return "czerwiec"
    if n == 7: 
        return "lipiec"
    if n == 8: 
        return "sierpien"
    if n == 9: 
        return "wrzesien"
    if n == 10: 
        return "pazdziernik"
    if n == 11: 
        return "listopad"
    if n == 12: 
        return "grudzien"
    
    
if __name__=="__main__":
   print( month(4))