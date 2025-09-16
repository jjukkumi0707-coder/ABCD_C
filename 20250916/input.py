# -*- coding: utf-8 -*-
def print_multiplication_table(num):
    """특정 단의 구구단을 출력하는 함수"""
    print(f"\n{num}단:")
    print("-" * 15)
    for i in range(1, 10):
        print(f"{num} x {i} = {num * i}")
    print("-" * 15)

def main():
    """메인 함수 - 사용자 입력을 받아 구구단 출력"""
    print("=" * 30)
    print("      구구단 프로그램")
    print("=" * 30)
    
    while True:
        try:
            # 사용자 입력 받기
            num = int(input("\n출력하고 싶은 단을 입력하세요 (1-9, 0은 종료): "))
            
            # 종료 조건
            if num == 0:
                print("프로그램을 종료합니다.")
                break
            
            # 유효한 범위 체크
            if 1 <= num <= 9:
                print_multiplication_table(num)
                
                # 계속 진행할지 묻기
                continue_choice = input("\n다른 단도 보시겠습니까? (y/n): ").lower()
                if continue_choice != 'y':
                    print("프로그램을 종료합니다.")
                    break
            else:
                print("❌ 1부터 9까지의 숫자를 입력해주세요.")
                
        except ValueError:
            print("❌ 올바른 숫자를 입력해주세요.")
        except KeyboardInterrupt:
            print("\n\n프로그램을 종료합니다.")
            break

# 추가 기능: 여러 단을 한번에 출력
def print_multiple_tables():
    """여러 단을 한번에 출력하는 함수"""
    try:
        start = int(input("시작 단을 입력하세요: "))
        end = int(input("끝 단을 입력하세요: "))
        
        if 1 <= start <= 9 and 1 <= end <= 9 and start <= end:
            print(f"\n{start}단부터 {end}단까지 출력:")
            print("=" * 50)
            for i in range(start, end + 1):
                print_multiplication_table(i)
        else:
            print("❌ 유효한 범위를 입력해주세요.")
    except ValueError:
        print("❌ 올바른 숫자를 입력해주세요.")

def advanced_menu():
    """고급 메뉴 시스템"""
    while True:
        print("\n" + "=" * 40)
        print("        구구단 프로그램 메뉴")
        print("=" * 40)
        print("1. 특정 단 출력")
        print("2. 여러 단 한번에 출력")
        print("3. 전체 구구단 출력 (2-9단)")
        print("0. 프로그램 종료")
        print("=" * 40)
        
        choice = input("메뉴를 선택하세요: ")
        
        if choice == '1':
            try:
                num = int(input("출력할 단을 입력하세요 (1-9): "))
                if 1 <= num <= 9:
                    print_multiplication_table(num)
                else:
                    print("❌ 1부터 9까지의 숫자를 입력해주세요.")
            except ValueError:
                print("❌ 올바른 숫자를 입력해주세요.")
                
        elif choice == '2':
            print_multiple_tables()
            
        elif choice == '3':
            print("\n전체 구구단 (2단 ~ 9단):")
            print("=" * 60)
            for i in range(2, 10):
                print_multiplication_table(i)
                
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("❌ 올바른 메뉴 번호를 입력해주세요.")

if __name__ == "__main__":
    # 간단한 버전 실행
    # main()
    
    # 고급 메뉴 버전 실행
    advanced_menu()