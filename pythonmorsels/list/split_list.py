# method - split
def chunk_it(arg_num_list, arg_num_of_chunks):
    if arg_num_of_chunks <= 0:
        raise Exception("The number of chunks should be greater than zero.")

    list_length = len(arg_num_list)
    quotient, remainder = divmod(list_length, arg_num_of_chunks)
    temp_list = []

    i = 0
    while i < list_length:
        if remainder != 0:
            temp_list.append(arg_num_list[i:i + quotient + 1])
            remainder = remainder - 1
            i = i + quotient + 1
        else:
            temp_list.append(arg_num_list[i:i + quotient])
            i = i + quotient

    if arg_num_of_chunks > list_length:
        remaining_items = arg_num_of_chunks - list_length
        for _ in range(remaining_items):
            temp_list.append([])
    return temp_list


# input
list_size = int(input("Enter number of elements in list:\n"))
str_list = input("Enter list elements separated by space:\n")
num_list = str_list.split(" ")
num_of_chunks = int(input("In how many chunks you want to split?\n"))

print(chunk_it(num_list, num_of_chunks))
