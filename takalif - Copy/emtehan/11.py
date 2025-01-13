def kamelBodan(n:int)->str:
    """ma yek adad midirim va maghsoom allayh hayash ra dar ham jam mikonim
    va agar jame maghsoom allayh hash bishtar az khodash bod migim yes dar gheir in sorat migim no

    Args:
        n (int): adadi ke migirim baresi mikonim

    Returns:
        str
    """
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n

n=int(input())

if kamelBodan(n):
    print("YES")
else:
    print('NO')