def decode_menu(menu_str: str) -> int:
    """
    menu_str -> org 역연산
    """
    if len(menu_str) != 16:
        raise ValueError("menu_str must be 16 characters long")
    
    res_list = []
    for ch in menu_str:
        if ch == "_":
            # 원래 조건: ~res & 0xf == 0x4
            # 즉, (0xf - res) == 4 → res == 0xb (11)
            res_list.append(0xb)
        elif ch.isdigit():
            res_list.append(int(ch))
        else:
            res_list.append(int(ch, 16))  # hex 처리
    
    # menu_str은 역순으로 저장되어 있었으므로 다시 반대로 정렬
    res_list = res_list[::-1]

    # 4비트씩 합쳐서 org 복원
    org = 0
    for i, val in enumerate(res_list):
        org |= (val & 0xf) << (4 * i)
    
    return org


if __name__ == "__main__":
    menu_str = input("menu_str 입력: ").strip()
    org = decode_menu(menu_str)
    print("복원된 org:", org)
    print("서버에 제출해야 할 값:", str(org))
