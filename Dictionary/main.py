def nested_aggregation(data):
    dept_dict = {}
    for dept, emp, salary in data:
        if dept not in dept_dict:
            dept_dict[dept] = []
        dept_dict[dept].append((emp, salary))
    for dept in dept_dict:
        dept_dict[dept] = sorted(dept_dict[dept], key=lambda x: x[1], reverse=True)
    return dept_dict
data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]
result = nested_aggregation(data)
print("Department-wise sorted employee salaries:")
for dept in result:
    print(f"{dept}: {result[dept]}")





