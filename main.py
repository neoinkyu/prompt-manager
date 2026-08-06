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


def get_non_empty_input(message):
    """빈 문자열이 아닌 값을 입력받는다."""
    while True:
        value = input(message).strip()

        if value:
            return value

        print("입력값은 비워둘 수 없습니다. 다시 입력해주세요.")


def select_category():
    """카테고리 목록을 출력하고 선택한 카테고리를 반환한다."""
    print("\n카테고리 선택:")

    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}) {category}")

    print("0) 직접 입력")

    while True:
        choice = input("선택: ").strip()

        if choice == "0":
            return get_non_empty_input("새 카테고리: ")

        if choice.isdigit():
            category_index = int(choice) - 1

            if 0 <= category_index < len(CATEGORIES):
                return CATEGORIES[category_index]

        print("올바른 카테고리 번호를 입력해주세요.")


def get_available_categories():
    """기본 카테고리와 현재 프롬프트의 카테고리를 반환한다."""
    available_categories = CATEGORIES.copy()

    for prompt in prompts:
        category = prompt["category"]

        if category not in available_categories:
            available_categories.append(category)

    return available_categories


def show_by_category():
    """선택한 카테고리에 해당하는 프롬프트를 출력한다."""
    print("\n=== 카테고리별 조회 ===")

    categories = get_available_categories()

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit():
            category_index = int(choice) - 1

            if 0 <= category_index < len(categories):
                selected_category = categories[category_index]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    filtered_prompts = [
        prompt
        for prompt in prompts
        if prompt["category"] == selected_category
    ]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    if not filtered_prompts:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(filtered_prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""
        print(f"{index}. {prompt['title']}{favorite_mark}")

    print(f"\n총 {len(filtered_prompts)}개의 프롬프트")


def search_prompt():
    """제목 또는 내용에 검색어가 포함된 프롬프트를 출력한다."""
    print("\n=== 프롬프트 검색 ===")

    keyword = get_non_empty_input("검색어: ")
    normalized_keyword = keyword.lower()

    search_results = [
        prompt
        for prompt in prompts
        if normalized_keyword in prompt["title"].lower()
        or normalized_keyword in prompt["content"].lower()
    ]

    print("\n검색 결과:")

    if not search_results:
        print(f"'{keyword}'에 해당하는 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(search_results, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""
        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(f"\n총 {len(search_results)}개의 프롬프트를 찾았습니다.")


def get_prompt_index(message="프롬프트 번호 입력: "):
    """입력받은 프롬프트 번호를 리스트 인덱스로 반환한다."""
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return None

    choice = input(message).strip()

    if not choice.isdigit():
        print("올바른 프롬프트 번호를 입력해주세요.")
        return None

    prompt_index = int(choice) - 1

    if not 0 <= prompt_index < len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return None

    return prompt_index


def show_detail():
    """선택한 프롬프트의 전체 내용과 조회수를 출력한다."""
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    prompt_index = get_prompt_index()

    if prompt_index is None:
        return

    prompt = prompts[prompt_index]
    prompt["view_count"] += 1

    favorite_status = "⭐ 즐겨찾기됨" if prompt["favorite"] else "즐겨찾기 아님"

    print("\n────────────────────────────")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_status}")
    print(f"조회수: {prompt['view_count']}")
    print("────────────────────────────")
    print("내용:")
    print(prompt["content"])
    print("────────────────────────────")


def toggle_favorite():
    """선택한 프롬프트의 즐겨찾기 상태를 변경한다."""
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    prompt_index = get_prompt_index()

    if prompt_index is None:
        return

    prompt = prompts[prompt_index]
    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(
            f"\n'{prompt['title']}' 프롬프트를 "
            "즐겨찾기에 추가했습니다!"
        )
    else:
        print(
            f"\n'{prompt['title']}' 프롬프트를 "
            "즐겨찾기에서 해제했습니다!"
        )


def add_prompt():
    """새로운 프롬프트를 입력받아 목록에 추가한다."""
    print("\n=== 프롬프트 추가 ===")

    title = get_non_empty_input("제목: ")
    content = get_non_empty_input("내용: ")
    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "view_count": 0,
    }

    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")


def main():
    """프로그램의 메인 반복문을 실행한다."""
    while True:
        show_menu()
        choice = input("선택: ").strip()


        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice in {"7", "8", "9", "10"}:
            print("해당 기능은 순차적으로 구현할 예정입니다.")
        else:
            print("올바른 메뉴 번호를 입력해주세요.")




if __name__ == "__main__":
    main()