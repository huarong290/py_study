def calc_base_salary(total_salary, performance_rate):
    """
    根据总工资和绩效比例计算基本工资
    :param total_salary: 总工资（包含基本工资 + 绩效 + 年终奖 + 加班费）
    :param performance_rate: 绩效比例（例如 0.1, 0.2, 0.3）
    :return: 基本工资
    """
    base_salary = total_salary / (2.25 + performance_rate)
    return base_salary


# 示例：总工资是 92000，绩效比例 30% 基本7008
total_salary = 19642.000000 -300 -70
performance_rate = 0.5
base = calc_base_salary(total_salary, performance_rate)
print(f"基本工资0为: {base:.2f} 元")

# 示例：总工资是 92000，绩效比例 30% 基本6218
total_salary1 = 15604.000000 -300 -70
performance_rate1 = 0.2
base1 = calc_base_salary(total_salary1, performance_rate1)
print(f"基本工资1为: {base1:.2f} 元")

# 示例：总工资是 92000，绩效比例 30% 基本6218
total_salary3 = 17036.000000 -300-400
performance_rate3 = 0.2
base3 = calc_base_salary(total_salary3, performance_rate3)
print(f"基本工资1为: {base3:.2f} 元")

def calc_total_salary(base_salary, performance_rate):
    """
    根据基本工资和绩效比例计算总工资
    :param base_salary: 基本工资
    :param performance_rate: 绩效比例（例如 0.1, 0.2, 0.3）
    :return: 总工资
    """
    total_salary = (2.25 + performance_rate) * base_salary
    return total_salary


# 示例：基本工资是 40000，绩效比例 30%
base_salary_test = 6668
performance_rate_test  = 0.2
total = calc_total_salary(base_salary_test, performance_rate_test)+300+400
print(f"总工资为: {total:.2f} 元")


def calc_total_salary_no_bonus(base_salary, performance_rate):
    """
    根据基本工资和绩效比例计算总工资（无年终奖）
    :param base_salary: 基本工资
    :param performance_rate: 绩效比例 (例如 0.1, 0.2, 0.3)
    :return: 总工资
    """
    total_salary = (1.25 + performance_rate) * base_salary
    return total_salary
# 示例：基本工资是 40000，绩效比例 30%
base_salary_test2 = 6668
performance_rate_test2  = 0.2
total2 = calc_total_salary_no_bonus(base_salary_test2, performance_rate_test2)+300+400
print(f"总工资为: {total2:.2f} 元")



