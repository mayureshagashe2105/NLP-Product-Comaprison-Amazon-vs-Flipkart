import numpy as np
import helperfuncs
import MySQL_DB

PLACEHOLDER = '!!!'

def textformat(text):
    formatter = helperfuncs.TextFormatting(text)
    formatter.RemoveTagsAndPunctuations()
    formatter.ToLower()
    formatter.RemoveStopWords()
    return formatter.text


def distance_calc(shape):
    global PLACEHOLDER
    amazon = MySQL_DB.getamazon(shape)
    dist_matrix = np.zeros((shape, shape))
    i = 0
    try:
        for j in amazon:
            words1 = textformat(j)
            words1 = words1.split(" ")
            len1 = len(words1)
            flipkart = MySQL_DB.getflipkart(shape)
            temp_score = []
            for k in flipkart:
                counter = 0
                words2 = textformat(k)
                words2 = words2.split(" ")
                len2 = len(words2)
                for word in words2:
                    if word in words1:
                        counter += 1
                if len1 >= len2:
                    counter /= len2
                else:
                    counter /= len1

                temp_score.append(counter)

            dist_matrix[i] = temp_score
            i += 1
        return dist_matrix
    except ValueError:
        print(f'{shape} record(s) are not available to compare')


matrix = distance_calc(shape=5)
print(matrix)
