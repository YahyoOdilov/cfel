def put_comma(num):
    result = str(num)
    lenth =  result.find('.') if result.find('.') != -1 else int(len(result))
    while lenth > 3:
        lenth -= 3
        if not result[lenth -1] == '-':
            result = result[:lenth]+ ',' + result[lenth:]
    return result
 
# put_comma(13345342334514548788.74)