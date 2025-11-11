# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text(text):
    """
    分析文本中字符频率并按频率降序排列
    
    参数:
    text - 输入的字符串
    
    返回:
    list - 按字符频率降序排列的字符列表
    """
    # 在此处增加代码
def analyze_text(text):
    """
    分析字符串，打印按频率降序排列的字母
    """
    # 1. 将文本转换为小写，并只保留字母字符
    text_lower = text.lower()
    letters = [char for char in text_lower if char.isalpha()]

    # 2. 统计频率
    from collections import Counter
    freq_dict = Counter(letters)

    # 3. 排序: 主要按频率降序，次要按字母顺序升序 (a-z)
    # sorted_items 是一个由 (字母, 频率) 元组组成的列表
    sorted_items = sorted(freq_dict.items(), key=lambda item: (-item[1], item[0]))

    # 4. 输出结果
    for letter, count in sorted_items:
        print(f"{letter}: {count}")

# 主程序，接收用户输入
if __name__ == "__main__":
    user_input = input("请输入一个字符串: ")
    analyze_text(user_input)
# 测试
text = input("请输入字符串：")
text_analysis(text)
    

# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("====================")
    print("请输入一段文本（输入空行结束）：")
    
    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    # 合并输入文本
    text = "\n".join(lines)
    
    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)
        
        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))
        
        # 提示用户比较不同语言
        print("\n提示: 尝试输入中英文文章片段，比较不同语言之间字符频率的差别")
