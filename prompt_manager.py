# prompt_manager.py

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def get_default_prompts():
    """이전 미션에서 만든 기본 프롬프트 3개 이상."""
    return [
        {"title": "블로그 글 작성 도우미",
         "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 글을 작성해주세요.",
         "category": "텍스트 생성", "favorite": True},
        {"title": "제품 썸네일 생성",
         "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝고 깔끔한 배경으로.",
         "category": "이미지 생성", "favorite": False},
        {"title": "IT 컨설턴트 페르소나",
         "content": "당신은 20년 경력의 IT 컨설턴트입니다. 전문적이고 친절하게 답변하세요.",
         "category": "페르소나", "favorite": False},
    ]

def format_line(index, p):
    star = " ⭐" if p["favorite"] else ""
    return f"{index}. [{p['category']}] {p['title']}{star}"

def show_list(prompts):
    """등록된 모든 프롬프트 목록을 출력."""
    print("\n=== 프롬프트 목록 ===")
    print("=" * 30)
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(prompts)}개의 프롬프트")

def ask_nonempty(label):
    """빈 값이면 다시 물어보는 입력 도우미."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("⚠️ 값을 비워둘 수 없습니다. 다시 입력해 주세요.")

def choose_category():
    """카테고리 번호를 선택하거나 직접 입력받는 도우미."""
    print("\n카테고리 선택:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    while True:
        sel = input("선택(번호, 없으면 직접 입력): ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(CATEGORIES):
            return CATEGORIES[int(sel) - 1]
        if sel:  # 목록에 없는 새로운 카테고리는 직접 입력값 사용
            return sel
        print("⚠️ 카테고리를 입력해 주세요.")

def add_prompt(prompts):
    """새로운 프롬프트를 입력받아 리스트에 추가."""
    print("\n=== 프롬프트 추가 ===")
    title = ask_nonempty("제목: ")
    content = ask_nonempty("내용: ")
    category = choose_category()
    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print("✅ 프롬프트가 추가되었습니다!")

def show_by_category(prompts):
    """선택한 카테고리에 속한 프롬프트만 필터링하여 출력."""
    print("\n=== 카테고리별 조회 ===")
    category = choose_category()
    matched = [p for p in prompts if p["category"] == category]
    if not matched:
        print(f"[{category}] 카테고리에 프롬프트가 없습니다.")
        return
    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, p in enumerate(matched, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")
    print(f"\n총 {len(matched)}개의 프롬프트")

def search_prompt(prompts):
    """키워드가 제목 또는 내용에 포함된 프롬프트를 검색."""
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어: ").strip()
    if not keyword:
        print("⚠️ 검색어를 입력해 주세요.")
        return
    results = [p for p in prompts
               if keyword in p["title"] or keyword in p["content"]]
    if not results:
        print("검색 결과가 없습니다.")
        return
    print("\n검색 결과:")
    for i, p in enumerate(results, start=1):
        print(format_line(i, p))
    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail(prompts):
    """번호를 선택받아 해당 프롬프트의 전체 내용을 상세 출력."""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    sel = input("번호 입력: ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print("⚠️ 올바른 번호가 아닙니다.")
        return
    p = prompts[int(sel) - 1]
    star = "⭐" if p["favorite"] else "없음"
    print("\n" + "─" * 30)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 30)
    print("내용:")
    print(p["content"])
    print("─" * 30)

def toggle_favorite(prompts):
    """번호를 받아 즐겨찾기 상태를 토글(참↔거짓 반전)."""
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    sel = input("프롬프트 번호 입력: ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print("⚠️ 올바른 번호가 아닙니다.")
        return
    p = prompts[int(sel) - 1]
    p["favorite"] = not p["favorite"]
    state = "추가했습니다" if p["favorite"] else "해제했습니다"
    print(f"'{p['title']}' 프롬프트를 즐겨찾기에 {state}!")

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    prompts = get_default_prompts()
    while True:
        show_menu()
        choice = input("선택: ").strip()
        if choice == "1":
            add_prompt(prompts)
        elif choice == "2":
            show_list(prompts)
        elif choice == "3":
            show_by_category(prompts)
        elif choice == "4":
            search_prompt(prompts)
        elif choice == "5":
            show_detail(prompts)
        elif choice == "6":
            toggle_favorite(prompts)
        elif choice == "7":
            print("[준비 중] 즐겨찾기 목록")
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("⚠️ 잘못된 번호입니다. 다시 선택해 주세요.")


if __name__ == "__main__":
    main()