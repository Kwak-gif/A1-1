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
            print("[준비 중] 프롬프트 추가")
        elif choice == "2":
            print("[준비 중] 프롬프트 목록")
        elif choice == "3":
            print("[준비 중] 카테고리별 조회")
        elif choice == "4":
            print("[준비 중] 프롬프트 검색")
        elif choice == "5":
            print("[준비 중] 상세 보기")
        elif choice == "6":
            print("[준비 중] 즐겨찾기 관리")
        elif choice == "7":
            print("[준비 중] 즐겨찾기 목록")
        elif choice == "0":
            print("프로그램을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("⚠️ 잘못된 번호입니다. 다시 선택해 주세요.")


if __name__ == "__main__":
    main()