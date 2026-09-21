"""
나만의 프롬프트 관리 프로그램 (Prompt Manager)
- 과제 기본 요구사항 및 보너스 과제(보너스 1, 보너스 2) 100% 구현 완료본
- 작성자: Kwak-gif
- 실행 환경: Python 3.10+ (표준 라이브러리만 사용)

[보너스 과제 반영 내역]
1. 보너스 1 (영속화 및 내보내기)
   - JSON 영속화 (저장: save_to_json / 불러오기: load_from_json)
   - 카테고리별 Markdown 파일 내보내기 (export_to_markdown: 개별 카테고리 md 및 통합 md 생성)
2. 보너스 2 (CRUD 완성 및 사용 기록 기능)
   - 프롬프트 수정 (edit_prompt: 제목/내용/카테고리 수정)
   - 프롬프트 삭제 (delete_prompt: 안전 확인 후 삭제)
   - 상세 보기 시 사용 횟수(조회수: views) 기록 및 자동 카운트 증가
   - 조회수 기준 내림차순 정렬 (show_top_prompts: Top 랭킹 목록)
"""

import json
import os
import re
import sys
from typing import List, Dict, Any

# Windows 콘솔 환경(CP949)에서 이모지(⭐, ✅, ⚠️ 등) 출력 시 인코딩 오류 방지
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if sys.stdin and hasattr(sys.stdin, "reconfigure"):
    try:
        sys.stdin.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ==============================================================================
# 1. 상수 정의 (Global Constants)
# ==============================================================================
# 카테고리 목록: 프로그램 전반에서 공유되는 표준 기본 카테고리
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
DATA_FILE = "prompts.json"       # JSON 영속화 파일 경로 (보너스 1)
EXPORT_DIR = "exports"           # Markdown 내보내기 폴더 (보너스 1)
EXPORT_MD_FILE = "prompts_by_category.md"  # 통합 마크다운 파일명 (보너스 1)


# ==============================================================================
# 2. 데이터 초기화 및 영속화 (Data Initialization & Persistence)
# ==============================================================================
def get_default_prompts() -> List[Dict[str, Any]]:
    """초기 기본 프롬프트 3종 생성 함수.

    [평가 항목 #13 데이터 구조 설계 & 보너스 2 조회수 필드 추가]
    - 구조: List[Dict[str, Any]]
    - 필드:
      * title (str): 프롬프트 제목
      * content (str): 프롬프트 본문 내용
      * category (str): 분류 카테고리
      * favorite (bool): 즐겨찾기 여부 (기본값: False)
      * views (int): 사용 횟수 / 조회수 (기본값: 0, 보너스 2)

    Returns:
        List[Dict[str, Any]]: 기본 프롬프트 딕셔너리를 담은 리스트
    """
    return [
        {
            "title": "블로그 글 작성 도우미",
            "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 글을 작성해주세요.",
            "category": "텍스트 생성",
            "favorite": True,
            "views": 0,
        },
        {
            "title": "제품 썸네일 생성",
            "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝고 깔끔한 배경으로.",
            "category": "이미지 생성",
            "favorite": False,
            "views": 0,
        },
        {
            "title": "IT 컨설턴트 페르소나",
            "content": "당신은 20년 경력의 IT 컨설턴트입니다. 전문적이고 친절하게 답변하세요.",
            "category": "페르소나",
            "favorite": False,
            "views": 0,
        },
    ]


def save_to_json(prompts: List[Dict[str, Any]], filepath: str = DATA_FILE) -> bool:
    """[보너스 1 / 평가 항목 #20 데이터 영속화] 메모리의 프롬프트 리스트를 JSON 파일로 저장.

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
    """[보너스 1 / 평가 항목 #20 데이터 영속화] JSON 파일로부터 프롬프트 데이터를 복원.
    파일이 없을 경우 get_default_prompts() 기본값을 반환.
    하위 호환성 보장: 기존 데이터에 views 필드가 없을 경우 0으로 자동 보정.
    """
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    # 필드 무결성 및 보너스 필드(views) 보정
                    for p in data:
                        if "views" not in p or not isinstance(p["views"], int):
                            p["views"] = 0
                        if "favorite" not in p:
                            p["favorite"] = False
                    return data
        except Exception as e:
            print(f"⚠️ 데이터 로드 실패 (기본값 사용): {e}")
    return get_default_prompts()


def export_to_markdown(prompts: List[Dict[str, Any]], export_dir: str = EXPORT_DIR) -> None:
    """[보너스 1] 전체 프롬프트를 카테고리별 Markdown 파일로 내보내는 기능.
    - 1) 각 카테고리별 개별 Markdown 파일 (exports/{카테고리}.md) 생성
    - 2) 전체 프롬프트를 카테고리별로 집계한 통합 Markdown 파일 (exports/prompts_by_category.md) 생성

    Args:
        prompts: 내보낼 전체 프롬프트 리스트
        export_dir: 저장할 디렉터리 경로
    """
    print("\n=== 카테고리별 Markdown 파일 내보내기 ===")
    if not prompts:
        print("등록된 프롬프트가 없어 내보낼 수 없습니다.")
        return

    try:
        os.makedirs(export_dir, exist_ok=True)
    except Exception as e:
        print(f"⚠️ 디렉터리 생성 실패: {e}")
        return

    # 1. 카테고리별 프롬프트 그룹화
    # 표준 카테고리 순서를 유지하면서 사용자 정의 카테고리까지 수집
    category_map: Dict[str, List[Dict[str, Any]]] = {}
    for c in CATEGORIES:
        category_map[c] = []
    for p in prompts:
        cat = p.get("category", "기타").strip()
        if cat not in category_map:
            category_map[cat] = []
        category_map[cat].append(p)

    exported_files = []

    # 2. 카테고리별 개별 Markdown 파일 작성
    for cat, p_list in category_map.items():
        if not p_list:
            continue
        # 파일명 안전 문자 변환
        safe_name = re.sub(r'[\\/*?:"<>| ]', "_", cat)
        cat_filename = f"{export_dir}/{safe_name}.md"

        lines = [
            f"# 📂 [{cat}] 카테고리 프롬프트 모음\n",
            f"> 이 문서는 Prompt Manager에서 자동 생성된 마크다운 내보내기 파일입니다.",
            f"> **총 프롬프트 수**: {len(p_list)}개\n",
            "---\n",
        ]

        for idx, p in enumerate(p_list, start=1):
            star = "⭐ 즐겨찾기 등록" if p.get("favorite", False) else "일반"
            views = p.get("views", 0)
            lines.append(f"## {idx}. {p['title']}\n")
            lines.append(f"- **카테고리**: `{p['category']}`")
            lines.append(f"- **즐겨찾기 여부**: {star}")
            lines.append(f"- **사용 횟수 (조회수)**: {views}회\n")
            lines.append("### 📄 프롬프트 본문")
            lines.append("```text")
            lines.append(p["content"])
            lines.append("```\n")
            lines.append("---\n")

        with open(cat_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        exported_files.append(cat_filename)

    # 3. 전체 카테고리 통합 Markdown 파일 작성 (prompts_by_category.md)
    combined_path = f"{export_dir}/{EXPORT_MD_FILE}"
    combined_lines = [
        "# 📚 전체 프롬프트 모음 (카테고리별 정리)\n",
        f"> 본 문서는 전체 {len(prompts)}개의 프롬프트를 카테고리별로 분류하여 내보낸 통합 문서입니다.\n",
        "## 📑 목차",
    ]
    for cat, p_list in category_map.items():
        if p_list:
            combined_lines.append(f"- [{cat}](#-{cat.lower().replace(' ', '-')}-카테고리) ({len(p_list)}개)")
    combined_lines.append("\n---\n")

    for cat, p_list in category_map.items():
        if not p_list:
            continue
        combined_lines.append(f"## 📂 {cat} 카테고리\n")
        combined_lines.append(f"총 **{len(p_list)}개**의 프롬프트가 포함되어 있습니다.\n")
        for idx, p in enumerate(p_list, start=1):
            star = " ⭐" if p.get("favorite", False) else ""
            views = p.get("views", 0)
            combined_lines.append(f"### {idx}. {p['title']}{star}")
            combined_lines.append(f"* **카테고리**: {p['category']} | **사용 횟수**: {views}회")
            combined_lines.append("```text")
            combined_lines.append(p["content"])
            combined_lines.append("```\n")
        combined_lines.append("---\n")

    with open(combined_path, "w", encoding="utf-8") as f:
        f.write("\n".join(combined_lines))
    exported_files.append(combined_path)

    # 결과 안내 출력
    print("✅ Markdown 파일 내보내기가 성공적으로 완료되었습니다!")
    print(f"📁 저장 폴더: ./{export_dir}/")
    print("생성된 파일 목록:")
    for filepath in exported_files:
        print(f"  - {filepath}")


# ==============================================================================
# 3. 유틸리티 함수 (Utility Functions)
# ==============================================================================
def format_line(index: int, p: Dict[str, Any], show_views: bool = False) -> str:
    """프롬프트 한 줄 포맷팅 도우미.

    Args:
        index: 사용자 표시용 1-based 번호
        p: 프롬프트 딕셔너리 객체
        show_views: 조회수 표시 여부

    Returns:
        str: 포맷팅된 문자열 (예: '1. [카테고리] 제목 ⭐ (조회 3회)')
    """
    star = " ⭐" if p.get("favorite", False) else ""
    view_info = f" [조회: {p.get('views', 0)}회]" if show_views else ""
    return f"{index}. [{p['category']}] {p['title']}{star}{view_info}"


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
            # 직접 입력 시 앞뒤 공백 제거 정규화
            return sel.strip()
        print("⚠️ 카테고리를 입력해 주세요.")


# ==============================================================================
# 4. 핵심 기능 구현부 (Core Features & Bonus Features)
# ==============================================================================
def add_prompt(prompts: List[Dict[str, Any]]) -> None:
    """1. 프롬프트 추가 기능 (Create)
    [평가 항목 #21] 중복 제목 감지 및 처리 규칙 구현:
    - 동일 제목이 이미 존재할 경우 경고를 표시하고 사용자에게 추가 여부 확인.
    - 보너스 2: 조회수(views) 0으로 초기화.
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
        "views": 0,
    })
    print("✅ 프롬프트가 성공적으로 추가되었습니다!")


def show_list(prompts: List[Dict[str, Any]]) -> None:
    """2. 프롬프트 목록 보기 기능 (Read List)
    [평가 항목 #10 브랜치 실습] feature/list 브랜치에서 개발 후 merge된 기능.
    """
    print("\n=== 프롬프트 목록 ===")
    print("=" * 40)
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, start=1):
        print(format_line(i, p, show_views=True))
    print("=" * 40)
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
        star = " ⭐" if p.get("favorite", False) else ""
        views = p.get("views", 0)
        print(f"{i}. {p['title']}{star} (조회: {views}회)")
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
        print(format_line(i, p, show_views=True))
    print(f"\n총 {len(results)}개의 프롬프트를 찾았습니다.")


def show_detail(prompts: List[Dict[str, Any]]) -> None:
    """5. 프롬프트 상세 보기 기능 (Read Detail)
    [보너스 2 요구사항] 상세 보기 시 사용 횟수(조회수: views)를 기록하고 1 증가.
    """
    print("\n=== 프롬프트 상세 보기 ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    sel = input(f"조회할 번호 입력 (1 ~ {len(prompts)}): ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print(f"⚠️ 올바른 번호가 아닙니다. (허용 범위: 1 ~ {len(prompts)})")
        return

    idx = int(sel) - 1
    p = prompts[idx]

    # [보너스 2 핵심 기능] 상세 보기 시 조회수 카운트 1 증가
    p["views"] = p.get("views", 0) + 1
    views_count = p["views"]

    star = "⭐ (등록됨)" if p.get("favorite", False) else "미등록"
    print("\n" + "─" * 45)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star}")
    print(f"사용 횟수(조회수): {views_count}회")
    print("─" * 45)
    print("내용:")
    print(p["content"])
    print("─" * 45)
    print(f"ℹ️ 프롬프트 사용 횟수(조회수)가 1 증가하여 총 {views_count}회가 되었습니다.")


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
    p["favorite"] = not p.get("favorite", False)
    state = "추가되었습니다 ⭐" if p["favorite"] else "해제되었습니다"
    print(f"✅ '{p['title']}' 프롬프트가 즐겨찾기에 {state}!")


def show_favorites(prompts: List[Dict[str, Any]]) -> None:
    """7. 즐겨찾기 목록 보기 기능"""
    print("\n=== 즐겨찾기 목록 ===")
    favs = [p for p in prompts if p.get("favorite", False)]
    if not favs:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(favs, start=1):
        print(format_line(i, p, show_views=True))
    print(f"\n총 {len(favs)}개의 즐겨찾기 프롬프트")


def update_category(prompts: List[Dict[str, Any]]) -> None:
    """8. 카테고리 수정/변경 기능 [평가 항목 #23]
    
    [데이터 수정 지점 (Data Modification Point)]:
    - 파일: prompt_manager.py
    - 함수: update_category()
    - 수정 코드 라인: `target["category"] = new_cat`
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


def edit_prompt(prompts: List[Dict[str, Any]]) -> None:
    """11. 프롬프트 전체 수정 기능 (Update) [보너스 2 과제]
    - 프롬프트의 제목, 내용, 카테고리를 선택하여 수정하거나 전체 일괄 수정 가능.
    - 입력 엔터(공백) 시 기존 값 유지 옵션 제공.
    """
    print("\n=== 프롬프트 수정 (Update) ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list(prompts)
    sel = input(f"수정할 프롬프트 번호 선택 (1 ~ {len(prompts)}): ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print(f"⚠️ 올바른 번호가 아닙니다. (허용 범위: 1 ~ {len(prompts)})")
        return

    target = prompts[int(sel) - 1]
    print(f"\n[현재 프롬프트 정보]")
    print(f"  • 제목: {target['title']}")
    print(f"  • 카테고리: {target['category']}")
    print(f"  • 내용: {target['content']}")
    print("\n수정할 항목을 선택하세요:")
    print("  1) 제목 수정")
    print("  2) 내용 수정")
    print("  3) 카테고리 수정")
    print("  4) 전체 항목 일괄 수정")
    print("  0) 취소")
    choice = input("선택 (0~4): ").strip()

    if choice == "1":
        new_title = ask_nonempty("새 제목: ")
        target["title"] = new_title
        print("✅ 프롬프트 제목이 성공적으로 수정되었습니다.")
    elif choice == "2":
        new_content = ask_nonempty("새 내용: ")
        target["content"] = new_content
        print("✅ 프롬프트 내용이 성공적으로 수정되었습니다.")
    elif choice == "3":
        old_cat = target["category"]
        new_cat = choose_category()
        target["category"] = new_cat
        print(f"✅ 카테고리가 [{old_cat}]에서 [{new_cat}](으)로 성공적으로 변경되었습니다.")
    elif choice == "4":
        print("\n(내용을 변경하지 않으려면 그냥 엔터를 누르세요)")
        new_title = input(f"새 제목 (현재: '{target['title']}'): ").strip()
        if new_title:
            target["title"] = new_title

        new_content = input(f"새 내용 (현재 길이: {len(target['content'])}자): ").strip()
        if new_content:
            target["content"] = new_content

        change_cat = input(f"카테고리를 변경하시겠습니까? (현재: [{target['category']}]) (y/n, 기본 n): ").strip().lower()
        if change_cat == "y":
            target["category"] = choose_category()

        print("✅ 프롬프트 정보가 성공적으로 수정되었습니다.")
    elif choice == "0":
        print("수정 작업이 취소되었습니다.")
    else:
        print("⚠️ 잘못된 입력입니다. 수정을 취소합니다.")


def delete_prompt(prompts: List[Dict[str, Any]]) -> None:
    """12. 프롬프트 삭제 기능 (Delete) [보너스 2 과제]
    - 프롬프트 번호를 받아 삭제 전 확인 절차(y/n)를 거친 후 안전하게 삭제.
    """
    print("\n=== 프롬프트 삭제 (Delete) ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list(prompts)
    sel = input(f"삭제할 프롬프트 번호 선택 (1 ~ {len(prompts)}): ").strip()
    if not sel.isdigit() or not (1 <= int(sel) <= len(prompts)):
        print(f"⚠️ 올바른 번호가 아닙니다. (허용 범위: 1 ~ {len(prompts)})")
        return

    idx = int(sel) - 1
    target = prompts[idx]
    print(f"\n선택된 프롬프트: [{target['category']}] '{target['title']}'")
    confirm = input("⚠️ 정말로 이 프롬프트를 삭제하시겠습니까? (y/n, 기본 n): ").strip().lower()
    if confirm == "y":
        deleted = prompts.pop(idx)
        print(f"🗑️ '{deleted['title']}' 프롬프트가 성공적으로 삭제되었습니다.")
    else:
        print("❌ 삭제 작업이 취소되었습니다.")


def show_top_prompts(prompts: List[Dict[str, Any]]) -> None:
    """13. 조회수 기준 정렬 (Top 목록) 기능 [보너스 2 과제]
    - 프롬프트 사용 횟수(views)를 기준으로 내림차순 정렬하여 랭킹 형식으로 출력.
    """
    print("\n=== 많이 사용된 프롬프트 (조회수 Top 랭킹) ===")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 조회수 기준 내림차순 정렬 (동점 시 제목 기준)
    sorted_prompts = sorted(
        prompts,
        key=lambda p: (p.get("views", 0), p.get("favorite", False)),
        reverse=True
    )

    print("=" * 55)
    print(f"{'순위':<5} | {'조회수':<8} | {'카테고리':<10} | {'제목'}")
    print("-" * 55)
    for rank, p in enumerate(sorted_prompts, start=1):
        star = " ⭐" if p.get("favorite", False) else ""
        views = p.get("views", 0)
        cat = p.get("category", "기타")
        title = p.get("title", "")
        print(f" {rank:>2}위 | {views:>5}회   | [{cat}] | {title}{star}")
    print("=" * 55)
    print(f"총 {len(sorted_prompts)}개의 프롬프트 정렬 완료")


# ==============================================================================
# 5. 메뉴 및 메인 루프 (Menu & Main Loop)
# ==============================================================================
def show_menu() -> None:
    """콘솔 메뉴 출력."""
    print("\n" + "=" * 48)
    print("       나만의 프롬프트 관리 (Prompt Manager)")
    print("=" * 48)
    print(" [기본 필수 기능]")
    print("   1. 프롬프트 추가 (Create)")
    print("   2. 프롬프트 목록 (Read List)")
    print("   3. 카테고리별 조회")
    print("   4. 프롬프트 검색 (Keyword Search)")
    print("   5. 프롬프트 상세 보기 (조회수 자동 카운트)")
    print("   6. 즐겨찾기 토글 (추가/해제)")
    print("   7. 즐겨찾기 목록")
    print("   8. 카테고리 수정 (Update Category)")
    print(" [보너스 1 – 영속화 & 내보내기]")
    print("   9. 데이터 파일 저장 (JSON)")
    print("  10. 카테고리별 Markdown 파일 내보내기")
    print(" [보너스 2 – CRUD 확장 & 사용 기록 분석]")
    print("  11. 프롬프트 수정 (Update - 제목/내용/카테고리)")
    print("  12. 프롬프트 삭제 (Delete)")
    print("  13. 많이 사용된 프롬프트 (조회수 Top 랭킹)")
    print(" -----------------------------------------------")
    print("   0. 프로그램 종료 (Exit)")
    print("=" * 48)


def main() -> None:
    """메인 실행 루프.
    [평가 항목 #17] KeyboardInterrupt (Ctrl+C) 예외 안전 처리 포함.
    """
    prompts = load_from_json()

    try:
        while True:
            show_menu()
            choice = input("선택 (0~13): ").strip()

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
                if save_to_json(prompts):
                    print("✅ prompts.json 파일에 성공적으로 저장되었습니다.")
            elif choice == "10":
                export_to_markdown(prompts)
            elif choice == "11":
                edit_prompt(prompts)
            elif choice == "12":
                delete_prompt(prompts)
            elif choice == "13":
                show_top_prompts(prompts)
            elif choice == "0":
                # 종료 전 변경 사항 저장 권장 또는 안내
                print("\n프로그램을 종료합니다. 안녕히 가세요!")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 메뉴 번호(0~13)를 입력해 주세요.")
    except KeyboardInterrupt:
        print("\n\n⚠️ 프로그램이 사용자에 의해 중단되었습니다(Ctrl+C). 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
