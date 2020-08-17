def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between 
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    len1 = len(line1)
    len2 = len(line2)
    length = min(len1, len2)
    i = 0
    while i < length:
        if line1[i] == line2[i]:
            i = i+1
        else:
            return i
    if len1 == len2:
        return -1
    else:
        return min(len1, len2)

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.
      
      If either input line contains a newline or carriage return, 
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    list1 = str(object='')
    if idx == -1:
        return list1
    if "\n" not in line1 and "\n" not in line2:
        if "\r" not in line1 and "\r" not in line2:
            if 0 <= idx <= min(len(line1), len(line2)):
                list1 = line1 + "\n" + "=" * idx + "^\n" + line2 + "\n"
                return list1
    else:
        return list1
  

line1 = "abcdefg"
line2 = "abc"
print(singleline_diff_format(line1, line2, 5))

def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    len1 = len(lines1)
    len2 = len(lines2)
    leng = min(len1, len2)
    i = 0
    while i < leng:
        lin1 = lines1[i]
        lin2 = lines2[i]
        diff = singleline_diff(lin1, lin2)
        if diff == -1:
            i = i+1
        else:
            tup1 = (i, diff)
            return tup1
    if len1 == len2:
        tup1 = (-1, -1)
    else:
        tup1 = (max(len1,len2)-1, 0)
    return tup1

# lines1=["abc","deg","ad", "a"]
# lines2=["abc","deg","ad"]
# print(multiline_diff(lines1, lines2))

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or 
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    file = open(filename)
    list1 = []
    for line in file.readlines():
        if "\n" in line:
            line = line.replace("\n", "")
        if "\r" in line:
            line = line.replace("\r", "")
        
        list1.append(line)
    
    file.close()
    
    return list1

def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    tup1 = multiline_diff(lines1, lines2)
    if tup1 == (-1, -1):
        str1 = "No differences\n"
    else:
        linum = tup1[0]
        lin1 = lines1[linum]
        lin2 = lines2[linum]
        ind = singleline_diff(lin1, lin2)
        str2 = singleline_diff_format(lin1, lin2, ind)
        str1 = "Line " + str(tup1[0]) + ":\n" + str2

    return str1

# print(file_diff_format("ds.txt", "ds2.txt"))

# lines1 = get_file_lines("ds.txt")
# lines2 = get_file_lines("ds2.txt")
# tup1 = multiline_diff(lines1, lines2)
# print(tup1[1])