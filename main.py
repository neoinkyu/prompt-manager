def show_menu():
    """프롬프트 관리 프로그램의 메인 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정")
    print("9. 프롬프트 삭제")
    print("10. 인기 프롬프트")
    print("0. 종료")


def main():
    """프로그램의 메인 반복문을 실행한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        if choice in {
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9", "10"
        }:
            print("해당 기능은 순차적으로 구현할 예정입니다.")
        else:
            print("올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    main()