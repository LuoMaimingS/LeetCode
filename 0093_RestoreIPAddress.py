from copy import deepcopy


def is_valid(ip_list, dot_loc, length):
    if len(ip_list) == 4:
        last_term = ip_list[-1]
        if int(last_term) > 255 or (len(last_term) >= 2 and last_term[0] == '0'):
            return False
        return True
    temp_str = ip_list[-1]
    pos = dot_loc - length
    left_part = temp_str[:pos]
    right_part = temp_str[pos:]
    if len(left_part) >= 2 and left_part[0] == '0':
        return False
    temp_val = int(left_part)
    if temp_val <= 255:
        return True
    return False


def backtrack(current_p, dots_left, current_list, result, s):
    if dots_left == 0 and is_valid(current_list, len(s), len(s)):
        ip_addr = ''
        for k in range(len(current_list)):
            ip_addr = ip_addr + current_list[k] + '.'
        result.append(ip_addr[:-1])
        return

    for i in range(current_p, len(s)):
        if not is_valid(current_list, i, len(s)):
            break

        # Do choice.
        last_term = current_list[-1]
        pos = i - len(s)
        if pos != 0:
            left_str = last_term[:pos]
            right_str = last_term[pos:]
            del current_list[-1]
            current_list.append(left_str)
            current_list.append(right_str)

        backtrack(i+1, dots_left-1, deepcopy(current_list), result, s)

        # Cancel choice.
        if pos != 0:
            left_str = current_list[-2]
            right_str = current_list[-1]
            comb = left_str + right_str
            del current_list[-1]
            del current_list[-1]
            current_list.append(comb)


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        current_list = [s]
        result = []
        backtrack(1, 3, current_list, result, s)
        return result
