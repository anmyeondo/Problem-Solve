def solution(id_list, reports, k):
    dic = {}

    for id in id_list:
        dic[id] = {
            "report": [],
            "reported": [],
            "mail": 0
        }

    for report in set(reports):
        src, dst = report.split()
        dic[src]["report"].append(dst)
        dic[dst]["reported"].append(src)
    
    for id in dic:
        if len(dic[id]["reported"]) >= k:
            for report_id in dic[id]["reported"]:
                dic[report_id]["mail"] += 1
    
    ans = []
    for id in dic:
        ans.append(dic[id]["mail"])\
    
    return ans