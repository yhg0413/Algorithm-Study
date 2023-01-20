"""
2023 카카오 블라인드 채용
2023-01-21
https://school.programmers.co.kr/learn/courses/30/lessons/150370
"""

def solution(today, terms, privacies):
    t_year, t_month, t_day = today.split('.')
    terms_dict = dict()
    answer = []

    for term in terms:
        term_kind, due_date = term.split(" ")
        terms_dict[term_kind] = due_date

    for i, privac in enumerate(privacies):
        u_year = privac[0:4]
        u_month = privac[5:7]
        u_day = privac[8:10]
        term_kind = privac[-1]

        year = int(t_year) - int(u_year)
        month = int(t_month) - int(u_month)
        day = -1 if (int(t_day) - int(u_day)) < 0 else 0
        dead_date = int(terms_dict[term_kind])
        if (year * 12) + month + (day) >= dead_date:
            answer.append(i + 1)

    return answer