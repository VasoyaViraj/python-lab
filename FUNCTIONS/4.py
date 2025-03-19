def total_avg(listt):
    listtt = [i for i in listt]
    return {
        "Total" : sum(listtt),
        "Average" : sum(listtt)/len(listtt)
    }

print(total_avg([1,2,3,4,5]))