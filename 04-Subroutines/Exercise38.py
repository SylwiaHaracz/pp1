def f(palindrome):
    for i in range (0,len(palindrome)//2):
        if palindrome[i] != palindrome[len(palindrome)-1-i]:
            return False
            break
    return True
    
if __name__=="__main__":
    print(f("12-1561-21"))