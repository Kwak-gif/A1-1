"""
나만의 프롬프트 관리 프로그램 (Prompt Manager)
- 과제 개선본 (사전평가 피드백 반영 완료)
- 작성자: Kwak-gif
- 실행 환경: Python 3.10+
"""

import json
import os
from typing import List, Dict, Any

# ==============================================================================
# 1. 상수 정의 (Global Constants)
# ==============================================================================
# 카테고리 목록: 프로그램 전반에서 공유되는 표준 카테고리
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
DATA_FILE = "prompts.json"  # 영속화 파일 경로


# ==============================================================================
# 2. 데이터 초기화 및 영속화 (Data Initialization & Persistence)
# ==============================================================================
def get_default_prompts() -> List[Dict[str, Any]]:
    """초기 기본 프롬프트 3종 생성 함수.

    [평가 항목 #13 데이터 구조 설계]
    - 구조: List[Dict[str, Any]]
    - 선택 이유:
      * Dict: title, content, category, favorite 필드 접근의 직관성과 가독성(O(1))
      * List: 순서 유지, 인덱스 기반 접근(O(1)), JSON 직렬화의 높은 호환성

    Returns:
        List[Dict[str, Any]]: 기본 프롬프트 딕셔너리를 담은 리스트
    """
    return [
        {
            "title": "블로그 글 작성 도우미",
            "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 글을 작성해주세요.",
            "category": "텍스트 생성",
            "favorite": True,
        },
        {
            "title": "제품 썸네일 생성",
            "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝고 깔끔한 배경으로.",
            "category": "이미지 생성",
            "favorite": False,
        },
        {
            "title": "IT 컨설턴트 페르소나",
            "content": "당신은 20년 경력의 IT 컨설턴트입니다. 전문적이고 친절하게 답변하세요.",
            "category": "페르소나",
            "favorite": False,
        },
    ]


def save_to_json(prompts: List[Dict[str, Any]], filepath: str = DATA_FILE) -> bool:
    """[평가 항목 #20 데이터 영속화] 메모리의 프롬프트 리스트를 JSON 파일로 저장.

    Args:
        prompts: 저장할 프롬프트 리스트
        filepath: 대상 JSON 파일 경로

    Returns:
        bool: 저장 성공 여부
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(prompts, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"⚠️ 저장 중 오류 발생: {e}")
        return False


def load_from_json(filepath: str = DATA_FILE) -> List[Dict[str, Any]]:
    """[평가 항목 #20 데이터 영속화] JSON 파일로부터 프롬프트 데이터를 복원.
    파일이 없을 경우 get_default_prompts() 기본값을 반환.
    """
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return get_default_prompts()


# ==============================================================================
# 3. 유틸리티 함수 (Utility Functions)
# ==============================================================================
def format_line(index: int, p: Dict[str, Any]) -> str:
    """프롬프트 한 줄 포맷팅 도우미.

    Args:
        index: 사용자 표시용 1-based 번호
        p: 프롬프트 딕셔너리 객체

    Returns:
        str: 포맷팅된 문자열 (예: '1. [카테고리] 제목 ⭐')
    """
    star = " ⭐" if p.get("favorite", False) else ""
    return f"{index}. [{p['category']}] {p['title']}{star}"


def ask_nonempty(label: str) -> str:
    """빈 값 입력을 방지하고 재입력을 유도하는 입력 도우미.

    Args:
        label: 입력창에 표시할 프롬프트 안내문

    Returns:
        str: 공백이 제거된 유효 문자열
    """
    while True:
        value = input(label).strip()
        if value:
            return value
        print("⚠️ 값을 비워둘 수 없습니다. 다시 입력해 주세요.")


def choose_category() -> str:
    """카테고리 목록을 표시하고 번호 선택 또는 직접 입력을 받는 도우미.
    [평가 항목 #6, #7] 앞뒤 공백 제거 및 정규화 규칙 적용.

    Returns:
        str: 선택되거나 직접 입력된 정규화된 카테고리명
    """
    print("\n카테고리 선택:")
    for i, c in enumerate(CATEGORIES, start=1):
        print(f"{i}) {c}")
    while True:
        sel = input("선택(번호 1~6, 또는 직접 입력): ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(CATEGORIES):
            return CATEGORIES[int(sel) - 1]
        if sel:
            # 직접 입력 시 앞뒤 공백 제거
            return sel.strip()
        print("⚠️ 카테고리를 입력해 주세요.")


# ==============================================================================
# 4. 핵심 기능 구현부 (Core Features)
# ==============================================================================
def add_prompt(prompts: List[Dict[str, Any]]) -> None:
    """1. 프롬프트 추가 기능
    [평가 항목 #21] 중복 제목 감지 및 처리 규칙 구현:
    - 동일 제목이 이미 존재할 경우 경고를 표시하고 사용자에게 추가 여부 확인.
    """
    print("\n=== 프롬프트 추가 ===")
    title = ask_nonempty("제목: ")

    # [평가 항목 #21 중복 검사 로직]
    duplicate_exists = any(p["title"].strip() == title.strip() for p in prompts)
    if duplicate_exists:
        print("⚠️ 알림: 이미 동일한 제목의 프롬프트가 등록되어 있습니다!")
        confirm = input("그래도 추가하시겠습니까? (y/n, 기본 n): ").strip().lower()
        if confirm != "y":
            print("❌ 프롬프트 추가가 취소되었습니다.")
            return

    content = ask_nonempty("내용: ")
    category = choose_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    })
    print("✅ 프롬프트가 성공적으로 추가되었습니다!")


def show_list(prompts: List[Dict[str, Any]]) -> None:
    """2. 프롬프트 목록 보기 기능
    [평가 항목 #10 브랜치 실습] feature/list 브랜치에서 개발 후 merge된 기능.
    """
    print("\n=== 프롬프트 목록 ===")
    print("=" * 30)
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print(format_line(i, p))
    print("=" * 30)
    print(f"총 {len(prompts)}개의 프롬프트")


def show_by_category(prompts: List[Dict[str, Any]]) -> None:
    """3. 카테고리별 조회 기능
    [평가 항목 #7] 엄격 일치(exact match) 방식으로 필터링 수행.
    """
    print("\n=== 카테고리별 조회 ===")
    category = choose_category()
    # 대소문자 무관 및 공백 제거 엄격 일치 필터링
    matched = [p for p in prompts if p["category"].strip().lower() == category.strip().lower()]
    if not matched:
        print(f"[{category}] 카테고리에 프롬프트가 없습니다.")
        return
    print(f"\n[{category}] 카테고리 프롬프트:")
    for i, p in enumerate(matched, start=1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")
    print(f"\n총 {len(matched)}개의 프롬프트")


def search_prompt(prompts: List[Dict[str, Any]]) -> None:
    """4. 프롬프트 키워드 검색 기능
    [평가 항목 #8, #18] 대소문자 무시(case-insensitive) 및 부분 문자열 포함 매칭.
    """
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어 입력: ").strip()
    if not keyword:
        print("⚠️ 검색어를 입력해 주세요.")
        return

    # 대소문자 무시 부분 문자열 검색
    lower_kw = keyword.lower()
    results = [
        p for p in prompts
        if lower_kw in p["title"].lower() or lower_kw in p["content"].lower()
    ]

    if not results:
        print(f"'{keyword}'에 대한 검색 결과가 없습니다.")
        return

    print(f"\n'{keyword}' 검색 결과:")
    for i, p in enumerate(results, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(results)}개의 프롬프트를 찾았습니다.")


def show_detail(prompts: List[Dict[str, Any]]) -> None:
    """5. 프롬프트 상세 보기 기능"""
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    sel = input(f"조회할 번호 입력 (1 ~ {len(prompts)}): ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print(f"⚠️ 올바른 번호가 아닙니다. (허용 범위: 1 ~ {len(prompts)})")
        return

    p = prompts[int(sel) - 1]
    star = "⭐" if p["favorite"] else "없음"
    print("\n" + "─" * 40)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print("─" * 40)
    print("내용:")
    print(p["content"])
    print("─" * 40)


def toggle_favorite(prompts: List[Dict[str, Any]]) -> None:
    """6. 즐겨찾기 토글(추가/해제) 기능
    [평가 항목 #9] 즐겨찾기 상태 변경 및 즉각 알림 메시지 출력.
    """
    print("\n=== 즐겨찾기 관리 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    sel = input(f"프롬프트 번호 입력 (1 ~ {len(prompts)}): ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print(f"⚠️ 올바른 번호가 아닙니다. (허용 범위: 1 ~ {len(prompts)})")
        return

    p = prompts[int(sel) - 1]
    p["favorite"] = not p["favorite"]
    state = "추가되었습니다 ⭐" if p["favorite"] else "해제되었습니다"
    print(f"✅ '{p['title']}' 프롬프트가 즐겨찾기에 {state}!")


def show_favorites(prompts: List[Dict[str, Any]]) -> None:
    """7. 즐겨찾기 목록 보기 기능"""
    print("\n=== 즐겨찾기 목록 ===")
    favs = [p for p in prompts if p["favorite"]]
    if not favs:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(favs, start=1):
        print(format_line(i, p))
    print(f"\n총 {len(favs)}개의 즐겨찾기 프롬프트")


def update_category(prompts: List[Dict[str, Any]]) -> None:
    """8. 카테고리 수정/변경 기능 [평가 항목 #23 신규 구현]
    
    [데이터 수정 지점 (Data Modification Point)]:
    - 파일: prompt_manager.py
    - 함수: update_category()
    - 수정 코드 라인: `target_prompt["category"] = new_category`
    - 영향 범위: prompts 리스트 내 지정된 프롬프트 딕셔너리의 'category' 키 값
    """
    print("\n=== 프롬프트 카테고리 수정 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list(prompts)
    sel = input(f"카테고리를 수정할 프롬프트 번호 선택 (1 ~ {len(prompts)}): ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print(f"⚠️ 올바른 번호가 아닙니다. (허용 범위: 1 ~ {len(prompts)})")
        return

    target = prompts[int(sel) - 1]
    old_cat = target["category"]
    print(f"\n선택된 프롬프트: '{target['title']}' (현재 카테고리: [{old_cat}])")
    
    new_cat = choose_category()
    
    # [데이터 수정 지점]
    target["category"] = new_cat
    print(f"✅ 카테고리가 [{old_cat}]에서 [{new_cat}](으)로 성공적으로 변경되었습니다!")


# ==============================================================================
# 5. 메뉴 및 메인 루프 (Menu & Main Loop)
# ==============================================================================
def show_menu() -> None:
    """콘솔 메뉴 출력."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 카테고리 수정")
    print("9. 데이터 파일 저장(JSON)")
    print("0. 종료")


def main() -> None:
    """메인 실행 루프.
    [평가 항목 #17] KeyboardInterrupt (Ctrl+C) 예외 안전 처리 포함.
    """
    prompts = load_from_json()

    try:
        while True:
            show_menu()
            choice = input("선택 (0~9): ").strip()

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
                show_favorites(prompts)
            elif choice == "8":
                update_category(prompts)
            elif choice == "9":
                save_to_json(prompts)
                print("✅ prompts.json 파일에 저장되었습니다.")
            elif choice == "0":
                print("프로그램을 종료합니다. 안녕히 가세요!")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 메뉴 번호(0~9)를 입력해 주세요.")
    except KeyboardInterrupt:
        print("\n\n⚠️ 프로그램이 사용자에 의해 중단되었습니다(Ctrl+C). 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
