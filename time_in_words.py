h = int(input().strip())
m = int(input().strip())
hr_dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve"}
min_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine'}
if m==0:
    print(dict[h] + " o' clock")
else:
    if m == 30:
        m_text = "half past "
    elif m<30:
        if m==15:
            m_text = "quarter past "
        else:
            m_text = min_dict[m] + " minutes past "
    else:
        if m==45:
            m_text = "quarter to "
        else:
            m_text = min_dict[60-m] + " minutes to "
    if m<=30:
        h_text = hr_dict[h]
    elif h == 12:
        h_text = hr_dict[1]
    else:
        h_text = hr_dict[h+1]
    print(m_text+h_text)

# time in words
# https://www.hackerrank.com/challenges/the-time-in-words?h_r=next-challenge&h_v=zen