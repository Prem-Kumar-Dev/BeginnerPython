if __name__ == '__main__':
    n = int(input())
    
    student_data = [[input(), float(input())] for _ in range(n)]
    scores = [item[1] for item in student_data]
    scores=list(set(scores))
    scores.sort()
    
    student_data.sort(key=lambda x: x[1])
    second=scores[1]
        
    common=[name for name, scores in student_data if scores==second]
    common.sort()

    for i in common:
        
        print(i)
            