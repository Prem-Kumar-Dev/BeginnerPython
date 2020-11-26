

def binary_search(input_array, value):
    l_add = 0
    u_add = (len(input_array)-1)
    if len(input_array) > 0:
        while True:
            # Mid_address:Start
            if (l_add+u_add) % 2 == 0:
                mid_add = int(((l_add+u_add))/2)
            else:
                mid_add = int(((l_add+u_add)+1)/2)
                # End

            if int(input_array[mid_add]) == value:
                return mid_add
                break
            else:
                if u_add == mid_add:
                    return -1
                    break

                if int(input_array[mid_add]) > value:
                    u_add = mid_add
                else:
                    if int(input_array[mid_add]) < value:
                        l_add = mid_add
    else:
        return -1
