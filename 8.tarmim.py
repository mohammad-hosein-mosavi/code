def reverse_numbers():
    """
    dar inja ma aadad vared mikonim ta inke shakhs 0 vared kone dar
    an zaman ma hame aadad ra az paeen be bala chap mikonim
    args:
        num=int vared shode aadad
    return:
        int:baraaks shode
    """
    #baraye toonestan baraks kardan
    numbers = []
    
    while True:
        #az karbar vorody begire
        num = int(input())
        
        #harvaght 0 vared kard dige adad nagire
        if num == 0:
            break
        
        # rikhtan aadad dar list
        numbers.append(num)
    
    #baraks sazi va chap
    for number in reversed(numbers):
        print(number)

# seda kardan
reverse_numbers()