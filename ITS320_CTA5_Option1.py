# CTA 5: Taking 3 Strings from the user and return a concatenation of the string values in reverse order
# **There are many ways to reverse strs and this is one option with extended slicing formatting**

def reverse_concatenate(str1, str2, str3):
    # variables with reversed user string methods
    reverse_str1 = str1[::-1]
    reverse_str2 = str2[::-1]
    reverse_str3 = str3[::-1]

    concatenate_strs = reverse_str3 + reverse_str2 + reverse_str1
    return concatenate_strs

def main():
    print('Please enter three strings to be reordered.')
    user_str1 = input('String 1: ')
    user_str2 = input('String 2: ')
    user_str3 = input('String 3: ')

    reverse_strs = reverse_concatenate(user_str1, user_str2, user_str3)
    
    print('The original strings in reverse order and concatenated are without additional spacing are: ')
    print(reverse_strs)

if __name__ == '__main__':
    main()