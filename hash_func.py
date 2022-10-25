def get_hash(value):
    def dex_in_any(cod_ord,number): # перевод из десятичной в другую (тут 7,8,9) длиной 6
        str_value = []
        while cod_ord > 0:
            str_value.append(str(cod_ord % number))
            cod_ord = cod_ord // number
        str_value = "".join(str_value[::-1])
        str_value = '0'*(6-len(str_value))+str_value
        return str_value
    hash_value=[]
    ind=0
    for each in value:
        index=ind%3
        cod_value = ord(str(each))
        hash_value.append(dex_in_any(cod_value,7+index))
        ind +=1
    hash_value = int("".join(hash_value))

    h1 = []
    ii=0
    while hash_value>0:
        h1.append(str(hash_value%max(len(value),15)))
        hash_value = hash_value // (ii+len(value))**ii
        ii+=1
    hash_value = int("".join(h1))
    return hash_value
list_data=["привет, lovi 5","привет, lovi 5","a","b","c","cc","ccc","abc"]
for each in list_data:
    print(each,"-->",get_hash(each))

