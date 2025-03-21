# morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
# afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}
morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

# possible_courses = morning ^ afternoon

possible_courses = set(morning).symmetric_difference(afternoon)
# same result
# possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)
