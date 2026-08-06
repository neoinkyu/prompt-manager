CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타",
]


prompts = [
    {
        "title": "안전신문고 광고 문구 작성",
        "content": (
            "연구개발특구진흥재단 임직원의 안전신문고 신고 참여를 "
            "유도하는 10초 광고 문구를 작성해주세요. "
            "짧은 내레이션 1문장과 화면 카피를 함께 제안하고, "
            "마지막에는 연구개발특구진흥재단을 표시해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": True,
        "view_count": 0,
    },
    {
        "title": "안전 캠페인 이미지 생성",
        "content": (
            "공공기관 임직원이 생활 속 위험 요소를 발견하고 "
            "스마트폰으로 안전신문고에 신고하는 장면을 표현해주세요. "
            "신뢰감 있고 밝은 공공 캠페인 분위기로 제작해주세요."
        ),
        "category": "이미지 생성",
        "favorite": False,
        "view_count": 0,
    },
    {
        "title": "월간 신고 데이터 자동화 설계",
        "content": (
            "매월 수집되는 안전신문고 데이터를 구글 시트에 정리하고, "
            "새 데이터가 등록되면 담당자에게 이메일을 발송하는 "
            "노코드 자동화 절차를 단계별로 설계해주세요."
        ),
        "category": "자동화",
        "favorite": False,
        "view_count": 0,
    },
]

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

def show_list():
    """저장된 모든 프롬프트를 목록으로 출력한다."""
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""
        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")

def main():
    """프로그램의 메인 반복문을 실행한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "2":
            show_list()
        elif choice in {
            "1", "3", "4", "5",
            "6", "7", "8", "9", "10"
        }:
            print("해당 기능은 순차적으로 구현할 예정입니다.")
        else:
            print("올바른 메뉴 번호를 입력해주세요.")





if __name__ == "__main__":
    main()